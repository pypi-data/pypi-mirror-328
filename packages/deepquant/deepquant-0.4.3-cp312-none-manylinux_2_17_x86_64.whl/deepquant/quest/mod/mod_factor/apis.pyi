from rqfactor import *
from deepquant.quest.mod.mod_factor.factor_api import *
from typing import Callable, List, Optional, Union


def reg_indicator(name, factor, freq='1d', win_size=None):
    # type: (str, Callable, Optional[str], int) -> None
    """
    注册指标
    :param name: str	定义的指标名称
    :param factor:function 或 actor	函数对象
    :param freq:str	指标计算的周期。支持日级别与分钟级别，'1d'代表每日，'5m'代表5分钟
    :param win_size:int	获取数据回溯窗口。该指标用于在注册指标时让系统获取回溯获取数据的最大窗口，便于数据的加载与预计算
    :return:无
    """
    ...


def get_indicator(market_code, name):
    # type: (Union[str, List[str]], str) -> int
    """
    获取指标
    :param market_code:str	合约代码
    :param name:str	定义的指标名称
    :return: 定义指标返回值
    """
    ...
