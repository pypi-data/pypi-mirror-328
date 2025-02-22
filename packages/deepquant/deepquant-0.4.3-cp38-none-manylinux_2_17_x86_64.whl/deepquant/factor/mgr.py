"""
因子管理相关接口
1. 因子上传
2. 因子元数据获取用于计算
"""
import pandas as pd

def post_factor_metadata(
    token: str, 
    formula: str, 
    period: str="d",
    frange: list[str]=["hs300"], 
    time_range: str="3m",
    options: dict={},
    ) -> dict:
    """
    通过SDK上传用户需要跟踪的因子,实现和网页上编辑上传的功能;
    通过接口上传便于用户在juypter中调试

    :param token: 用户登录sdk的token
    :type token: str
    :param formula: 因子表达式
    :type formula: str
    :param period: 因子周期, 默认为日，'d': 日 'm':分钟 's':秒
    :type period: str
    :param frange: 股票池范围 
    :type frange: list[str]
    :param time_range: 首次需要计算的历史
    :type time_range: str
    :param options: 其他参数
    :type options: dict
    :return: 因子管理服务返回的json结果, 正确返回结果包含facotr_id
    :rtype: dict
    """
    pass

def get_factor_list(
    token: str,
    ) -> pd.DataFrame:
    """
    获得用户权限下的因子列表

    :param token: 用户登录sdk的token
    :type token: str
    :return: 返回因子列表，包含factor_id
    :rtype: pd.DataFrame
    """

def get_factor_metadata(
    token: str,
    factor_id: str
    ) -> pd.DataFrame:
    """
    获取用户的因子元数据，用于开始每日离线计算因子值和绩效，用于因子跟踪

    :param token: 用户登录sdk的token
    :type token: str
    :param factor_id: 因子id
    :type factor_id: str
    :return: 返回因子列表，包含factor_id
    :rtype: pd.DataFrame
    """
    pass
