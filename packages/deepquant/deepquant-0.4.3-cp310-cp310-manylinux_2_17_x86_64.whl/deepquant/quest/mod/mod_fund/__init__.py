# -*- coding: utf-8 -*-
"""

在策略中  设置config['mod']["fund"]控制基金mod配置

.. code-block:: python

    __config__ = {
        "fee_ratio": 0.015,
        # 基金份额到账时间
        "subscription_receiving_days": 1,
        # 赎回金回款时间
        "redemption_receiving_days": 3,
        # 申赎金额上下限检查限制
        "subscription_limit": True,
        # 申购状态检查限制
        "status_limit": True,
        # 载入mod优先级
        "priority": 220,
    }
"""
import os

import click
from deepquant.quest import cli

from deepquant.quest.mod.mod_fund._version import get_versions

__version__ = get_versions()['version']
del get_versions

__config__ = {
    "fee_ratio": 0.015,
    # 基金份额到账时间
    "subscription_receiving_days": 1,
    # 赎回金回款时间
    "redemption_receiving_days": 3,
    # 申赎金额上下限检查限制
    "subscription_limit": True,
    # 申购状态检查限制
    "status_limit": True,
    # 载入mod优先级
    "priority": 220,
    # 非货币基金净值类型 unit(单位净值) / adjusted(复权净值)
    "fund_nav_type": "unit",
}

cli_prefix = "mod__fund__"

cli.commands["run"].params.append(
    click.Option(
        ("--fund-fee-ratio", cli_prefix + "fee_funds"),
        type=click.FLOAT, help="[mod_fund] 设置基金的前端收费费率",
    )
)


cli.commands["run"].params.append(
    click.Option(
        ('--fund-subscription-receiving-days', cli_prefix + "subscription_receiving_days"),
        type=click.INT, help="[yhalpha_mod_fund] 设置基金申购到账的时间，默认为 1"
    )
)

cli.commands["run"].params.append(
    click.Option(
        ('--fund-redemption-receiving-days', cli_prefix + "redemption_receiving_days",),
        type=click.INT, help="[yhalpha_mod_fund] 设置基金赎回到账的时间，默认为 3"
    )
)

cli.commands["run"].params.append(
    click.Option(
        ('--fund-status-limit/--fund-no-status-limit', cli_prefix + "status_limit"),
        default=None, help="[rqalph-mod-fund] 设置基金申赎是否收到基金申赎状态的限制，默认开启"
    )
)


def load_mod():
    from deepquant.quest.mod.mod_fund.mod import FundMod

    return FundMod()


def update_bundle_base(bundle_path=os.path.join(os.path.expanduser('~/.yhalpha'), 'bundle'),
                       workers_num=None, funds: list = None):
    """
    更新基金回测数据
    :param bundle_path: bundle地址 默认用户目录下 .yhalpha/bundle
    :param workers_num: 线程数
    :param funds: 跟新部分基金时，输入基金列表
    """
    # FIXME: 增加到 rqlpha_plus 中
    gen_bundle(bundle_path, workers_num, funds)


# __doc__ = """"""

__doc__ += "cmd启动时,使用以下命令设置fund mod  参数"
for command in cli.commands['run'].params:
    if not command.name.startswith(cli_prefix):
        continue
    input = "\\".join(command.opts)
    help_str = command.help.replace("\n", "\n\n.. code-block:: bash\n\n    ")
    out_put = "{} : {}".format(input, help_str)
    __doc__ += out_put + "\n\n"
