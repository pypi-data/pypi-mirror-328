import errno
import os
import shutil
import sys

import click
from deepquant.quest.cmds.mod import mod
from deepquant.quest.cmds.run import run
from deepquant.quest.mod.utils import inject_mod_commands
from deepquant.quest.utils import config
from deepquant.quest.utils import init_yhdatac_env

from deepquant.quest.alpha.bundle import TAG_MAP, download_simple_bundle, update_bundle_from_exist_file
from deepquant.quest.alpha.bundle import update_bundle_from_yhdatac
from deepquant.quest.alpha.bundle import check_min_bar_data
from deepquant.quest.alpha.utils.scripts import check_tick

config.yhalpha_path = os.path.join(os.path.expanduser('~'), ".quest")
config.default_config_path = os.path.join(os.path.dirname(__file__), 'config.yml')
config.default_mod_config_path = os.path.join(os.path.dirname(__file__), 'mod_config.yml')


@click.group()
@click.help_option("-h", "--help")
def cli():
    """
    \b
    输入 yhalpha_plus <COMMAND> --help 查看命令详情
    例如：yhalpha_plus update-bundle --help
    """
    pass


@cli.command()
@click.option(
    '-d', '--data-bundle-path', default=config.yhalpha_path, type=click.Path(file_okay=False),
    help="bundle 目录，默认为 {}".format(config.yhalpha_path)
)
@click.option(
    "yhdatac_uri", '--yhdatac/--yhdatac-uri', default=None,
    help='yhdatac uri, eg user:password or tcp://user:password@ip:port'
)
@click.option(
    "--base", default=False, is_flag=True,
    help="更新基础数据及日线，注意：任何回测都需要依赖基础数据"
)
@click.option(
    "--minbar", multiple=True, type=click.STRING,
    help="更新分钟线数据，可选的参数值有 [{}] 或 underlying_symbol 或 market_code".format(", ".join(TAG_MAP.keys()))
)
@click.option(
    "--tick", multiple=True, type=click.STRING,
    help="更新tick数据，可选的参数值有 [{}] 或 underlying_symbol 或 market_code".format(", ".join(TAG_MAP.keys()))
)
@click.option("--with-derivatives", is_flag=True, default=False, help="更新分钟线和 tick 时同时更新选择的合约的衍生品数据")
@click.option("-c", "--concurrency", type=click.INT, default=3, help="并行的线程数量，需要低于 datac 的最大可用连接数")
@click.option("--smart", default=False, is_flag=True, help="检索本地已经存在的分钟线和 tick 数据，增量更新对应品种的数据和日线数据")
@click.option("--rebuild", default=False, is_flag=True, help="将指定的合约 h5 文件从头进行更新，仅对--minbar、--tick生效")
def update_bundle(data_bundle_path, yhdatac_uri, base, minbar, tick, with_derivatives, concurrency, smart, rebuild):
    """
    更新运行回测所需的历史数据

    \b
    例如：
    * 更新日线数据： yhalpha_plus update-bundle --base
    * 更新股票、期权分钟数据： yhalpha_plus update-bundle --minbar stock --minbar option
    * 更新鸡蛋期货合约tick数据： yhalpha_plus update-bundle --tick JD
    * 更新豆粕1905及其合约的衍生品tick数据： yhalpha_plus update-bundle --tick M1905 --with-derivatives
    * 更新已下载的分钟线和tick数据： yhalpha_plus update-bundle --smart
    """
    path = os.path.join(data_bundle_path, 'bundle')
    if os.path.exists(path):
        check_tick(path)

    if base is False and not minbar and not tick and smart is False:
        from click import Context
        ctx = Context(update_bundle)
        click.echo(update_bundle.get_help(ctx))
        return 1
    try:
        import deepquant.quest.datac
    except ImportError:
        click.echo('deepquant.quest.datac is required to create bundle')
        return 1

    try:
        init_yhdatac_env(yhdatac_uri)
        deepquant.quest.datac.init()
    except ValueError as e:
        click.echo('yhdatac init failed with error: {}'.format(e))
        return 1
    succeed = update_bundle_from_yhdatac(concurrency, data_bundle_path, base, minbar, tick, with_derivatives, rebuild)

    if smart:
        succeed = update_bundle_from_exist_file(concurrency, data_bundle_path) and succeed
    if not succeed:
        sys.exit(1)


@cli.command()
@click.option(
    '-d', '--data-bundle-path', default=config.yhalpha_path, type=click.Path(file_okay=False),
    help="bundle 目录，默认为 {}".format(config.yhalpha_path)
)
@click.option("--sample", is_flag=True, help="下载数据样例")
@click.option('-f', '--file-path', default=None, help="指定的压缩文件包")
def download_bundle(data_bundle_path, sample=True, file_path=None):
    """
    下载样例回测数据。
    下载样例数据不使用yhdatac流量。
    """
    return download_simple_bundle(data_bundle_path, sample=sample, file_path=file_path)


@cli.command()
@click.option(
    '-d', '--data-bundle-path', default=config.yhalpha_path, type=click.Path(file_okay=False),
    help="bundle 目录，默认为 {}".format(config.yhalpha_path)
)
@click.option('--minbar', help="检查分钟数据是否异常", default=False, is_flag=True)
def check_bundle(data_bundle_path, minbar):
    """
    检查bundle中的数据是否正确
    """
    if not all([minbar]):
        print("请选择品种:[--minbar]")
    elif minbar:
        check_min_bar_data(data_bundle_path)


@cli.command()
@click.option('-v', '--verbose', is_flag=True)
def version(**kwargs):
    """
    Output yhalpha_plus Version Info
    """
    if kwargs['verbose']:
        from deepquant.quest import __version__
        print("yhalpha Current Version: ", __version__)

    from deepquant.quest.alpha import __version__

    print("yhalpha-Plus Current Version: ", __version__)


@cli.command()
@click.option('-d', '--directory', default="./", type=click.Path(), required=True)
def examples(directory):
    """
    Generate example strategies to target folder
    """
    source_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")

    try:
        print(source_dir, os.path.abspath(os.path.join(directory, "examples")))
        shutil.copytree(source_dir, os.path.join(directory, "examples"))
    except OSError as e:
        if e.errno == errno.EEXIST:
            print("Folder examples exists.")


@cli.command()
@click.option('-d', '--directory', default="./", type=click.Path(), required=True)
def generate_config(directory):
    """
    Generate default config file
    """
    default_config = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.yml")
    target_config_path = os.path.abspath(os.path.join(directory, 'config.yml'))
    shutil.copy(default_config, target_config_path)
    print("Config file has been generated in", target_config_path)


inject_mod_commands()
cli.commands["run"] = run
cli.commands["mod"] = mod
