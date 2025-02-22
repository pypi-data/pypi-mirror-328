# -*- coding: utf-8 -*-
# 版权所有 2020 深圳米筐科技有限公司（下称“米筐科技”）
#
# 除非遵守当前许可，否则不得使用本软件。
#
#     * 非商业用途（非商业用途指个人出于非商业目的使用本软件，或者高校、研究所等非营利机构出于教育、科研等目的使用本软件）：
#         遵守 Apache License 2.0（下称“Apache 2.0 许可”），
#         您可以在以下位置获得 Apache 2.0 许可的副本：http://www.apache.org/licenses/LICENSE-2.0。
#         除非法律有要求或以书面形式达成协议，否则本软件分发时需保持当前许可“原样”不变，且不得附加任何条件。
#
#     * 商业用途（商业用途指个人出于任何商业目的使用本软件，或者法人或其他组织出于任何目的使用本软件）：
#         未经米筐科技授权，任何个人不得出于任何商业目的使用本软件（包括但不限于向第三方提供、销售、出租、出借、转让本软件、
#         本软件的衍生产品、引用或借鉴了本软件功能或源代码的产品或服务），任何法人或其他组织不得出于任何目的使用本软件，
#         否则米筐科技有权追究相应的知识产权侵权责任。
#         在此前提下，对本软件的使用同样需要遵守 Apache 2.0 许可，Apache 2.0 许可与本许可冲突之处，以本许可为准。
#         详细的授权流程，请联系 public@ricequant.com 获取。
import warnings
from functools import wraps

from deepquant.quest.api import export_as_api
from deepquant.quest.environment import Environment
from deepquant.quest.utils.exception import RQInvalidArgument, RQUserError
from deepquant.quest.utils.logger import user_system_log
from rqoptimizer import CovModel, InvalidArgument, MinVariance, OptimizationFailed, portfolio_optimize as optimize


class RQOptimizationFailed(RQUserError):
    pass


DEFAULT_OBJECTIVE = MinVariance()


@export_as_api
def portfolio_optimize(
        market_code, objective=DEFAULT_OBJECTIVE, bnds=None, cons=None, benchmark=None,
        cov_model=CovModel.FACTOR_MODEL_DAILY, factor_risk_aversion=1.0, specific_risk_aversion=1.0
):
    """
    组合优化，根据给定的约束及目标函数计算最优组合权重。

    :param market_code: 候选合约
    :param objective: 目标函数，默认为MinVariance（风险最小化）。支持的目标函数见下表

    :param bnds: {market_code | "*": (lower_limit, upper_limit)} 个股权重上下界
                 字典，key 为 market_code, value 为 (lower_limit, upper_limit) 组成的 tuple。lower_limit/upper_limit
                 取值可以是 [0, 1] 的数或 None。 当取值为 None 时，表示对应的界不做限制。
                 当 key 为 '*' 时，表示所有未在此字典中明确指定的其他合约。
                 所有合约默认上下界为 [0, 1]。
    :param cons: [OptimizationConstraint] 约束列表。支持的约束类型见下表
    :param benchmark: 基准，目前仅支持指数基准
    :param cov_model: 协方差模型，支持 daily/monthly/quarterly
    :param factor_risk_aversion: 因子风险厌恶系数，默认为1
    :param specific_risk_aversion: 特异风险厌恶系数，默认为1

    :return: pd.Series 组合最优化权重

    =========================   ===================================================
    目标函数                     说明
    =========================   ===================================================
    MinVariance                 风险最小化
    MeanVariance                均值（收益）方差（风险）模型
    RiskParity                  风险平价
    MinTrackingError            最小追踪误差
    MaxInformationRatio         最大信息比率
    MaxSharpeRatio              最大夏普率
    MaxIndicator                指标值最大化
    MinStyleDeviation           风格偏离最小化
    =========================   ===================================================

    =============================   ===================================================
    约束类型                         说明
    =============================   ===================================================
    TrackingErrorLimit              跟踪误差约束
    TurnoverLimit                   换手率约束
    BenchmarkComponentWeightLimit   成分股权重约束，即要求优化结果中，基准成分股的权重之和的下限
    IndustryConstraint              行业权重约束，默认行业分类为申万一级。可选中信一级及申万一级(拆分非银金融行业)
    WildcardIndustryConstraint
    StyleConstraint                 风格约束
    WildcardStyleConstraint
    =============================   ===================================================



    """
    date = Environment.get_instance().calendar_dt
    try:
        with warnings.catch_warnings(record=True) as w:
            result = optimize(market_code, date, objective=objective, bnds=bnds,
                              cons=cons, benchmark=benchmark, cov_model=cov_model,
                              factor_risk_aversion=factor_risk_aversion, specific_risk_aversion=specific_risk_aversion)
        for warn in w:
            user_system_log.warn(str(warn.message))
        return result
    except InvalidArgument as e:
        raise RQInvalidArgument(str(e))
    except OptimizationFailed as e:
        raise RQOptimizationFailed(str(e))


def catch_exception_and_warnings(func):
    @wraps(func)
    def dec(*args, **kwargs):
        try:
            with warnings.catch_warnings(record=True) as w:
                result = func(*args, **kwargs)
            for warn in w:
                user_system_log.warn(str(warn.message))
            return result
        except InvalidArgument as e:
            raise RQInvalidArgument(str(e))

    return dec


def __register_api():
    from typing import Callable
    import rqoptimizer

    for name in rqoptimizer.__all__:
        if name in ('portfolio_optimize', 'InvalidArgument', 'OptimizationFailed'):
            continue

        value = getattr(rqoptimizer, name)
        if isinstance(value, Callable):
            value = catch_exception_and_warnings(value)
        export_as_api(value, name=name)


__register_api()
