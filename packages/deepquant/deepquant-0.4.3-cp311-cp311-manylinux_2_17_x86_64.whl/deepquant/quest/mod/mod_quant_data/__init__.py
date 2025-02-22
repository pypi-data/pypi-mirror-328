# -*- coding: utf-8 -*-

import click
from deepquant.quest import cli

from . import api_fund

from ._version import get_versions
__version__ = get_versions()['version']

from .mod import RicequantDataMod

del get_versions


def load_mod():
    return RicequantDataMod()


__config__ = {
    "redis_url": "redis://paladin/2",
    "rqdata_client_addr": "rqdatad.ricequant.com",
    "rqdata_client_port": 16003,
    "rqdata_client_username": "username",
    "rqdata_client_password": "password",
    "rqdata_client_retry_cnt": 30,
    "night_trading": False,
    "h5_tick_path": None,
    "h5_minbar_path": None,
    "tick_type": "rqdata",
    "priority": 110,
}

cli_prefix = "mod__ricequant_data__"

cli.commands['run'].params.append(
    click.Option(
        ('-rdu', '--rqdatad-username', cli_prefix + 'rqdata_client_username'),
        type=click.STRING,
        help="[ricequant_data] rqdatad username",
    )
)
cli.commands['run'].params.append(
    click.Option(
        ('-rdpw', '--rqdatad-password', cli_prefix + 'rqdata_client_password'),
        type=click.STRING,
        help="[ricequant_data] rqdatad password",
    )
)
cli.commands['run'].params.append(
    click.Option(
        ('-rda', '--rqdatad-addr', cli_prefix + 'rqdata_client_addr'),
        type=click.STRING,
        help="[ricequant_data] rqdatad server address",
    )
)
cli.commands['run'].params.append(
    click.Option(
        ('-rdpt', '--rqdatad-port', cli_prefix + 'rqdata_client_port'),
        type=click.INT,
        help="[ricequant_data] rqdatad server port",
    )
)
cli.commands['run'].params.append(
    click.Option(
        ('--night-trading', cli_prefix + 'night_trading'),
        is_flag=True,
        help="[ricequant_data] night trading",
    )
)
cli.commands['run'].params.append(
    click.Option(
        ('--redis-url', cli_prefix + 'redis_url'),
        type=click.STRING,
        help="[ricequant_data] bar & event redis url",
    )
)

cli.commands['run'].params = [param for param in cli.commands['run'].params if param.name != 'base__data_bundle_path']
cli.commands['run'].params.append(
    click.Option(
        ('-d', '--data-bundle-path', 'base__data_bundle_path'),
        type=click.Path(exists=True),
        help="[ricequant_data] data bundle path",
    )
)

cli.commands["run"].params.append(
    click.Option(
        ('--h5-tick-path', cli_prefix + "h5_tick_path"),
        type=click.STRING,
        help="[ricequant_data] path of hdf5 tick bundle",
    )
)

cli.commands["run"].params.append(
    click.Option(
        ('--h5-minbar-path', cli_prefix + "h5_minbar_path"),
        type=click.STRING,
        help="[ricequant_data] path of hdf5 minute bar bundle"
    )
)

cli.commands["run"].params.append(
    click.Option(
        ('--tick-type', cli_prefix + "tick_type"),
        type=click.STRING,
        help="[ricequant_data] data sourc of bt on tick frequency. choose in [h5, rqdata]"
    )
)
