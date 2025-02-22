"""
因子值的计算和因子绩效计算存储
"""
import pandas as pd

def calc_factor_value(
    ) -> pd.DataFrame:
    """
    计算因子值主逻辑, 返回因子值Dataframe主要包括如下流程，若某流程失败返回对应流程

    * 1. 公式解析
    * 2. 数据格式校验
    * 3. 股票池过滤
    * 4. 数据预处理
    * 5. 因子计算
    * 6. 因子值存储
    """
    pass

def calc_factor_perf(
        fval: pd.DataFrame,
        price: pd.DataFrame,
    ) -> pd.DataFrame:
    """
    因子绩效数据计算

    * 1. 因子数据读取
    * 2. 行情数据读取
    * 3. 个股前向收益率计算
    * 4. 因子分组收益统计
    * 5. 因子IC和收益率统计
    """
    pass

def save_factor_value(fval_df: pd.DataFrame, save_to:str='http') -> int:
    """
    保存因子值到数据存储ddb，通过http接口或者直接写数据库

    :param fval_df: 因子值的矩阵
    :type fval_df: pd.DataFrame
    :param save_to: 保存方式, http: 写接口 sql: 写数据库
    :type save_to: str
    :return: 成功返回写入行数，失败返回-1
    :rtype: int
    """
    pass
