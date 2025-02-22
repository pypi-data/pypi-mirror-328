from typing import Callable

from ._swordfishcpp._function import _abs, _add, _And, _any, _array, _arrayVector, _at, _atan, _avg
from ._swordfishcpp._function import _bitAnd, _bitOr, _bitXor, _byRow
from ._swordfishcpp._function import _cast, _cdfNormal, _clip, _cols, _contextby, _cos, _count, \
    _cumcount
from ._swordfishcpp._function import _deltas, _dema, _div, _dot, _double, _dropColumns_, _dropna
from ._swordfishcpp._function import _each, _ema, _eq, _eqFloat, _eqObj, _ewmMean, _exp
from ._swordfishcpp._function import _fill_
from ._swordfishcpp._function import _ge, _groupby, _gt
from ._swordfishcpp._function import _head
from ._swordfishcpp._function import _ifirstNot, _iif, _In, _isNull, _isortTop
from ._swordfishcpp._function import _join, _join_
from ._swordfishcpp._function import _kama, _keys, _last, _le, _linearTimeTrend, _loadText, _log, _lshift, _lt
from ._swordfishcpp._function import _ma, _mavg, _max, _mcorr, _mcovar, _mimax, _mimaxLast, _mimin, _miminLast, _min, \
    _mkurtosis, _mmad, _mmax, _mmed, _mmin, _mod, _move, _moving, _mrank, _mskew, _mstd, _mstdp, _msum, _msum2, \
    _msumTopN, _mul, _mvar
from ._swordfishcpp._function import _ne, _neg, _Not, _nullCompare
from ._swordfishcpp._function import _ols, _Or
from ._swordfishcpp._function import _pair, _panel, _partial, _percentChange, _pivot, _pow, _prev, _prod
from ._swordfishcpp._function import _quantile
from ._swordfishcpp._function import _rad2deg, _rand, _ratio, _ratios, _reciprocal, _rename_, _reshape, _residual, \
    _rowRank, _rows, _rshift
from ._swordfishcpp._function import _schema, _seq, _signum, _sin, _size, _sma, _sortBy_, _spearmanr, _square, _std, \
    _sub, _sum
from ._swordfishcpp._function import _tail, _take, _talib, _talibNull, _trueRange
from ._swordfishcpp._function import _values
from ._swordfishcpp._function import _wavg, _wilder, _wma
from ._swordfishcpp._function import _xor

from ._swordfishcpp import Constant
from ._swordfishcpp import Void, FunctionDef
from ._swordfishcpp._exception import SwordfishError
from ._translator import _translate_wrapper
from ._helper import _ParamAlias, Alias
from typing import Literal, Union, TypeVar, get_args
import copy as m_copy

import inspect


T = TypeVar('T', bound=Callable[..., Constant])


DFLT = Void.DFLT_VALUE
VOID = Void.VOID_VALUE


def __check_sig(func):
    params = inspect.signature(func).parameters
    for name, param in params.items():
        if param.kind != inspect._ParameterKind.POSITIONAL_OR_KEYWORD:
            raise SwordfishError("udf only support POSITIONAL_OR_KEYWORD param.")


def __create_udf_from_func(func, is_aggregation, mode: Literal["default", "translate"], frame=None):
    __check_sig(func)
    if mode == "default":
        return FunctionDef(func, name=func.__name__, aggregation=is_aggregation)
    elif mode == "translate":
        return _translate_wrapper(func, frame=frame, is_aggregation=is_aggregation)
    else:
        raise ValueError("Invalid mode: " + str(mode))


def __set_meta(func, newdef: FunctionDef):
    signature = inspect.signature(func)
    params = signature.parameters
    alias_dict = dict()
    for v in params.values():
        main_name = v.name
        annotation = v.annotation
        alias = []
        if annotation != inspect._empty and annotation != Constant:
            types = get_args(annotation)
            for t in types:
                if issubclass(t, _ParamAlias):
                    alias.append(t.name)
        if alias:
            for a in alias:
                alias_dict[a] = main_name
    if alias_dict:
        newdef.set_meta(signature, alias_dict)
    else:
        newdef.set_meta(signature, None)


def swordfish_udf(func=None, *, is_aggregation: bool = False, mode: Literal["default", "translate"] = "default"):
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1].frame
    if func is not None:
        return __create_udf_from_func(func, is_aggregation, mode, frame)

    def __inner(_func):
        return __create_udf_from_func(_func, is_aggregation, mode, frame)
    return __inner


def builtin_function(functionDef: FunctionDef) -> Callable[[Union[T, FunctionDef]], Union[T, FunctionDef]]:
    def decorator(func: Union[T, FunctionDef]) -> Union[T, FunctionDef]:
        newDef = m_copy.copy(functionDef)
        __set_meta(func, newDef)
        return newDef
    return decorator


@builtin_function(_abs)
def abs(X: Constant) -> Constant:
    ...


# @builtin_function(_accumulate)
# def accumulate(func: Constant, X: Constant, init: Constant = DFLT, consistent: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_acf)
# def acf(X: Constant, maxLag: Constant) -> Constant:
#     ...


# @builtin_function(_acos)
# def acos(X: Constant) -> Constant:
#     ...


# @builtin_function(_acosh)
# def acosh(X: Constant) -> Constant:
#     ...


# @builtin_function(_adaBoostClassifier)
# def adaBoostClassifier(ds: Constant, yColName: Constant, xColNames: Constant, numClasses: Constant, maxFeatures: Constant = DFLT, numTrees: Constant = DFLT, numBins: Constant = DFLT, maxDepth: Constant = DFLT, minImpurityDecrease: Constant = DFLT, learningRate: Constant = DFLT, algorithm: Constant = DFLT, randomSeed: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_adaBoostRegressor)
# def adaBoostRegressor(ds: Constant, yColName: Constant, xColNames: Constant, maxFeatures: Constant = DFLT, numTrees: Constant = DFLT, numBins: Constant = DFLT, maxDepth: Constant = DFLT, minImpurityDecrease: Constant = DFLT, learningRate: Constant = DFLT, loss: Constant = DFLT, randomSeed: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_add)
def add(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_addColumn)
# def addColumn(table: Constant, colNames: Constant, colTypes: Constant) -> Constant:
#     ...


# @builtin_function(_adfuller)
# def adfuller(X: Constant, maxLag: Constant = DFLT, regression: Constant = DFLT, autoLag: Constant = DFLT, store: Constant = DFLT, regResults: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_aggrTopN)
# def aggrTopN(func: Constant, funcArgs: Constant, sortingCol: Constant, top: Constant, ascending: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_aj)
# def aj(leftTable: Constant, rightTable: Constant, matchingCols: Constant, rightMatchingCols: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_align)
# def align(left: Constant, right: Constant, how: Constant = DFLT, byRow: Constant = DFLT, view: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_all)
# def all(obj: Union[Alias[Literal["func"]], Constant], *args) -> Constant:
#     ...


@builtin_function(_And)
def And(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_anova)
# def anova(X: Constant) -> Constant:
#     ...


@builtin_function(_any)
def any(obj: Union[Alias[Literal["func"]], Constant], *args) -> Constant:
    ...


# @builtin_function(_append_)
# def append_(obj: Constant, newData: Constant) -> Constant:
#     ...


# @builtin_function(_appendTuple_)
# def appendTuple_(X: Constant, Y: Constant, wholistic: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_array)
def array(dataType: Union[Alias[Literal["template"]], Constant], initialSize: Constant = DFLT, capacity: Constant = DFLT, defaultValue: Constant = DFLT) -> Constant:
    ...


@builtin_function(_arrayVector)
def arrayVector(index: Constant, value: Constant) -> Constant:
    ...


# @builtin_function(_asFreq)
# def asFreq(X: Constant, rule: Constant, closed: Constant = DFLT, label: Constant = DFLT, origin: Constant = DFLT, fill: Constant = DFLT, limit: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_asin)
# def asin(X: Constant) -> Constant:
#     ...


# @builtin_function(_asinh)
# def asinh(X: Constant) -> Constant:
#     ...


# @builtin_function(_asis)
# def asis(obj: Constant) -> Constant:
#     ...


# @builtin_function(_asof)
# def asof(X: Constant, Y: Constant) -> Constant:
#     ...


@builtin_function(_at)
def at(X: Constant, index: Constant = DFLT) -> Constant:
    ...


@builtin_function(_atan)
def atan(X: Constant) -> Constant:
    ...


# @builtin_function(_atanh)
# def atanh(X: Constant) -> Constant:
#     ...


# @builtin_function(_atImax)
# def atImax(location: Constant, value: Constant) -> Constant:
#     ...


# @builtin_function(_atImin)
# def atImin(location: Constant, value: Constant) -> Constant:
#     ...


# @builtin_function(_autocorr)
# def autocorr(X: Constant, lag: Constant) -> Constant:
#     ...


@builtin_function(_avg)
def avg(X: Constant) -> Constant:
    ...


# @builtin_function(_bar)
# def bar(X: Constant, interval: Constant, closed: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_base64Decode)
# def base64Decode(X: Constant) -> Constant:
#     ...


# @builtin_function(_base64Encode)
# def base64Encode(X: Constant) -> Constant:
#     ...


# @builtin_function(_beta)
# def beta(Y: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_between)
# def between(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_bfill_)
# def bfill_(obj: Constant, limit: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_binaryExpr)
# def binaryExpr(X: Constant, Y: Constant, optr: Constant) -> Constant:
#     ...


# @builtin_function(_binsrch)
# def binsrch(X: Constant, Y: Constant) -> Constant:
#     ...


@builtin_function(_bitAnd)
def bitAnd(X: Constant, Y: Constant) -> Constant:
    ...


@builtin_function(_bitOr)
def bitOr(X: Constant, Y: Constant) -> Constant:
    ...


@builtin_function(_bitXor)
def bitXor(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_bondAccrInt)
# def bondAccrInt(settlement: Constant, maturity: Constant, coupon: Constant, frequency: Constant, par: Constant = DFLT, basis: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_bondConvexity)
# def bondConvexity(settlement: Constant, maturity: Constant, coupon: Constant, _yield: Constant, frequency: Constant = DFLT, basis: Constant = DFLT, bondType: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_bondDirtyPrice)
# def bondDirtyPrice(settlement: Constant, maturity: Constant, coupon: Constant, _yield: Constant, frequency: Constant = DFLT, basis: Constant = DFLT, bondType: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_bondDuration)
# def bondDuration(settlement: Constant, maturity: Constant, coupon: Constant, _yield: Constant, frequency: Constant = DFLT, basis: Constant = DFLT, bondType: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_brentq)
# def brentq(f: Constant, a: Constant, b: Constant, xtol: Constant = DFLT, rtol: Constant = DFLT, maxIter: Constant = DFLT, funcDataPara: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_brute)
# def brute(func: Constant, ranges: Constant, ns: Constant = DFLT, finish: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_bucket)
# def bucket(vector: Constant, dataRange: Constant, bucketNum: Constant, includeOutbound: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_bucketCount)
# def bucketCount(vector: Constant, dataRange: Constant, bucketNum: Constant, includeOutbound: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_businessDay)
# def businessDay(X: Constant, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_businessMonthBegin)
# def businessMonthBegin(X: Constant, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_businessMonthEnd)
# def businessMonthEnd(X: Constant, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_businessQuarterBegin)
# def businessQuarterBegin(X: Constant, startingMonth: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_businessQuarterEnd)
# def businessQuarterEnd(X: Constant, endingMonth: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_businessYearBegin)
# def businessYearBegin(X: Constant, startingMonth: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_businessYearEnd)
# def businessYearEnd(X: Constant, endingMonth: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_byColumn)
# def byColumn(func: Constant, X: Constant, Y: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_byRow)
def byRow(func: Constant, X: Constant, Y: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_call)
# def call(func: Constant, *args) -> Constant:
#     ...


@builtin_function(_cast)
def cast(obj: Constant, type: Constant) -> Constant:
    ...


# @builtin_function(_cbrt)
# def cbrt(X: Constant) -> Constant:
#     ...


# @builtin_function(_cdfBeta)
# def cdfBeta(alpha: Constant, beta: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_cdfBinomial)
# def cdfBinomial(trials: Constant, prob: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_cdfChiSquare)
# def cdfChiSquare(df: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_cdfExp)
# def cdfExp(mean: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_cdfF)
# def cdfF(numeratorDF: Constant, denominatorDF: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_cdfGamma)
# def cdfGamma(shape: Constant, scale: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_cdfKolmogorov)
# def cdfKolmogorov(X: Constant) -> Constant:
#     ...


# @builtin_function(_cdfLogistic)
# def cdfLogistic(mean: Constant, s: Constant, X: Constant) -> Constant:
#     ...


@builtin_function(_cdfNormal)
def cdfNormal(mean: Constant, stdev: Constant, X: Constant) -> Constant:
    ...


# @builtin_function(_cdfPoisson)
# def cdfPoisson(mean: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_cdfStudent)
# def cdfStudent(df: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_cdfUniform)
# def cdfUniform(lower: Constant, upper: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_cdfWeibull)
# def cdfWeibull(alpha: Constant, beta: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_cdfZipf)
# def cdfZipf(num: Constant, exponent: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_ceil)
# def ceil(X: Constant) -> Constant:
#     ...


# @builtin_function(_cell)
# def cell(obj: Constant, row: Constant, col: Constant) -> Constant:
#     ...


# @builtin_function(_cells)
# def cells(obj: Constant, row: Constant, col: Constant) -> Constant:
#     ...


# @builtin_function(_charAt)
# def charAt(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_chiSquareTest)
# def chiSquareTest(X: Constant, Y: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_cholesky)
# def cholesky(obj: Constant, lower: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_cj)
# def cj(leftTable: Constant, rightTable: Constant) -> Constant:
#     ...


# @builtin_function(_clear_)
# def clear_(obj: Constant) -> Constant:
#     ...


# @builtin_function(_clearAllCache)
# def clearAllCache() -> Constant:
#     ...


@builtin_function(_clip)
def clip(X: Constant, Y: Constant, Z: Constant) -> Constant:
    ...


# @builtin_function(_clip_)
# def clip_(X: Constant, Y: Constant, Z: Constant) -> Constant:
#     ...


# @builtin_function(_coalesce)
# def coalesce(X1: Constant, X2: Constant, *args) -> Constant:
#     ...


# @builtin_function(_coevent)
# def coevent(event: Constant, eventTime: Constant, window: Constant, orderSensitive: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_coint)
# def coint(Y0: Constant, Y1: Constant, trend: Constant = DFLT, method: Constant = DFLT, maxLag: Constant = DFLT, autoLag: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_col)
# def col(obj: Constant, index: Constant) -> Constant:
#     ...


@builtin_function(_cols)
def cols(obj: Constant) -> Constant:
    ...


# @builtin_function(_compress)
# def compress(X: Constant, method: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_concat)
# def concat(str1: Union[Alias[Literal["X"]], Constant], str2: Union[Alias[Literal["separator"]], Constant]) -> Constant:
#     ...


# @builtin_function(_concatDateTime)
# def concatDateTime(date: Constant, time: Constant) -> Constant:
#     ...


# @builtin_function(_concatMatrix)
# def concatMatrix(X: Constant, horizontal: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_conditionalFilter)
# def conditionalFilter(X: Constant, condition: Constant, filterMap: Constant) -> Constant:
#     ...


@builtin_function(_contextby)
def contextby(func: Constant, funcArgs: Constant, groupingCol: Constant, sortingCol: Constant = DFLT, semanticFilter: Constant = DFLT, asc: Constant = DFLT, nullsOrder: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_contextCount)
# def contextCount(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_contextSum)
# def contextSum(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_contextSum2)
# def contextSum2(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_convertEncode)
# def convertEncode(str: Constant, srcEncode: Constant, destEncode: Constant) -> Constant:
#     ...


# @builtin_function(_convertExcelFormula)
# def convertExcelFormula(formula: Constant, colStart: Constant, colEnd: Constant, rowStart: Constant, rowEnd: Constant) -> Constant:
#     ...


# @builtin_function(_convertTZ)
# def convertTZ(obj: Constant, srcTZ: Constant, destTZ: Constant) -> Constant:
#     ...


# @builtin_function(_copy)
# def copy(obj: Constant) -> Constant:
#     ...


# @builtin_function(_corr)
# def corr(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_corrMatrix)
# def corrMatrix(X: Constant) -> Constant:
#     ...


@builtin_function(_cos)
def cos(X: Constant) -> Constant:
    ...


# @builtin_function(_cosh)
# def cosh(X: Constant) -> Constant:
#     ...


@builtin_function(_count)
def count(obj: Constant) -> Constant:
    ...


# @builtin_function(_countNanInf)
# def countNanInf(X: Constant, includeNull: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_covar)
# def covar(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_covarMatrix)
# def covarMatrix(X: Constant) -> Constant:
#     ...


# @builtin_function(_crc32)
# def crc32(str: Constant, cksum: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_cross)
# def cross(func: Constant, X: Constant, Y: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_crossStat)
# def crossStat(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_cubicSpline)
# def cubicSpline(X: Constant, Y: Constant, bc_type: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_cubicSplinePredict)
# def cubicSplinePredict(model: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_cumavg)
# def cumavg(X: Constant) -> Constant:
#     ...


# @builtin_function(_cumbeta)
# def cumbeta(Y: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_cumcorr)
# def cumcorr(X: Constant, Y: Constant) -> Constant:
#     ...


@builtin_function(_cumcount)
def cumcount(X: Constant) -> Constant:
    ...


# @builtin_function(_cumcovar)
# def cumcovar(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_cumfirstNot)
# def cumfirstNot(X: Constant, k: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_cumlastNot)
# def cumlastNot(X: Constant, k: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_cummax)
# def cummax(X: Constant) -> Constant:
#     ...


# @builtin_function(_cummed)
# def cummed(X: Constant) -> Constant:
#     ...


# @builtin_function(_cummin)
# def cummin(X: Constant) -> Constant:
#     ...


# @builtin_function(_cumnunique)
# def cumnunique(X: Constant, ignoreNull: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_cumpercentile)
# def cumpercentile(X: Constant, percent: Constant, interpolation: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_cumPositiveStreak)
# def cumPositiveStreak(X: Constant) -> Constant:
#     ...


# @builtin_function(_cumprod)
# def cumprod(X: Constant) -> Constant:
#     ...


# @builtin_function(_cumrank)
# def cumrank(X: Constant, ascending: Constant = DFLT, ignoreNA: Constant = DFLT, tiesMethod: Constant = DFLT, percent: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_cumstd)
# def cumstd(X: Constant) -> Constant:
#     ...


# @builtin_function(_cumstdp)
# def cumstdp(X: Constant) -> Constant:
#     ...


# @builtin_function(_cumsum)
# def cumsum(X: Constant) -> Constant:
#     ...


# @builtin_function(_cumsum2)
# def cumsum2(X: Constant) -> Constant:
#     ...


# @builtin_function(_cumsum3)
# def cumsum3(X: Constant) -> Constant:
#     ...


# @builtin_function(_cumsum4)
# def cumsum4(X: Constant) -> Constant:
#     ...


# @builtin_function(_cumvar)
# def cumvar(X: Constant) -> Constant:
#     ...


# @builtin_function(_cumvarp)
# def cumvarp(X: Constant) -> Constant:
#     ...


# @builtin_function(_cumwavg)
# def cumwavg(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_cumwsum)
# def cumwsum(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_cut)
# def cut(X: Constant, size: Union[Alias[Literal["cutPositions"]], Constant]) -> Constant:
#     ...


# @builtin_function(_cutPoints)
# def cutPoints(X: Constant, binNum: Constant, freq: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_CVaR)
# def CVaR(returns: Constant, method: Constant, confidenceLevel: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_dailyAlignedBar)
# def dailyAlignedBar(X: Constant, timeOffset: Constant, n: Constant, timeEnd: Constant = DFLT, mergeSessionEnd: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_date)
# def date(X: Constant) -> Constant:
#     ...


# @builtin_function(_dayOfMonth)
# def dayOfMonth(X: Constant) -> Constant:
#     ...


# @builtin_function(_dayOfWeek)
# def dayOfWeek(X: Constant) -> Constant:
#     ...


# @builtin_function(_dayOfYear)
# def dayOfYear(X: Constant) -> Constant:
#     ...


# @builtin_function(_daysInMonth)
# def daysInMonth(X: Constant) -> Constant:
#     ...


# @builtin_function(_decimalMultiply)
# def decimalMultiply(X: Constant, Y: Constant, scale: Constant) -> Constant:
#     ...


# @builtin_function(_decodeShortGenomeSeq)
# def decodeShortGenomeSeq(X: Constant) -> Constant:
#     ...


# @builtin_function(_decompress)
# def decompress(X: Constant) -> Constant:
#     ...


# @builtin_function(_defined)
# def defined(names: Constant, type: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_defs)
# def defs(pattern: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_deg2rad)
# def deg2rad(X: Constant) -> Constant:
#     ...


@builtin_function(_deltas)
def deltas(X: Constant, n: Constant = DFLT) -> Constant:
    ...


@builtin_function(_dema)
def dema(X: Constant, window: Constant) -> Constant:
    ...


# @builtin_function(_demean)
# def demean(X: Constant) -> Constant:
#     ...


# @builtin_function(_denseRank)
# def denseRank(X: Constant, ascending: Constant = DFLT, ignoreNA: Constant = DFLT, percent: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_derivative)
# def derivative(func: Constant, X: Constant, dx: Constant = DFLT, n: Constant = DFLT, order: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_det)
# def det(obj: Constant) -> Constant:
#     ...


# @builtin_function(_diag)
# def diag(X: Constant) -> Constant:
#     ...


# @builtin_function(_dictUpdate_)
# def dictUpdate_(dictionary: Constant, function: Constant, keys: Constant, parameters: Constant, initFunc: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_difference)
# def difference(X: Constant) -> Constant:
#     ...


# @builtin_function(_digitize)
# def digitize(x: Constant, bins: Constant, right: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_distance)
# def distance(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_distinct)
# def distinct(X: Constant) -> Constant:
#     ...


@builtin_function(_div)
def div(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_dividedDifference)
# def dividedDifference(X: Constant, Y: Constant, resampleRule: Constant, closed: Constant = DFLT, origin: Constant = DFLT, outputX: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_dot)
def dot(X: Constant, Y: Constant) -> Constant:
    ...


@builtin_function(_double)
def double(X: Constant) -> Constant:
    ...


# @builtin_function(_drop)
# def drop(obj: Constant, count: Constant) -> Constant:
#     ...


@builtin_function(_dropColumns_)
def dropColumns_(table: Constant, colNames: Constant) -> Constant:
    ...


@builtin_function(_dropna)
def dropna(X: Constant, byRow: Constant = DFLT, thresh: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_dynamicGroupCumcount)
# def dynamicGroupCumcount(membership: Constant, prevMembership: Constant, groupCount: Constant) -> Constant:
#     ...


# @builtin_function(_dynamicGroupCumsum)
# def dynamicGroupCumsum(cumValue: Constant, prevCumValue: Constant, membership: Constant, prevMembership: Constant, groupCount: Constant) -> Constant:
#     ...


@builtin_function(_each)
def each(func: Constant, *args) -> Constant:
    ...


# @builtin_function(_eachAt)
# def eachAt(X: Constant, index: Constant) -> Constant:
#     ...


# @builtin_function(_eachLeft)
# def eachLeft(func: Constant, X: Constant, Y: Constant, consistent: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_eachPost)
# def eachPost(func: Constant, X: Constant, post: Constant = DFLT, consistent: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_eachPre)
# def eachPre(func: Constant, X: Constant, pre: Constant = DFLT, consistent: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_eachRight)
# def eachRight(func: Constant, X: Constant, Y: Constant, consistent: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_eig)
# def eig(A: Constant) -> Constant:
#     ...


# @builtin_function(_ej)
# def ej(leftTable: Constant, rightTable: Constant, matchingCols: Constant, rightMatchingCols: Constant = DFLT, leftFilter: Constant = DFLT, rightFilter: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_elasticNet)
# def elasticNet(ds: Constant, yColName: Constant, xColNames: Constant, alpha: Constant = DFLT, l1Ratio: Constant = DFLT, intercept: Constant = DFLT, normalize: Constant = DFLT, maxIter: Constant = DFLT, tolerance: Constant = DFLT, positive: Constant = DFLT, swColName: Constant = DFLT, checkInput: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_elasticNetCV)
# def elasticNetCV(ds: Constant, yColName: Constant, xColNames: Constant, alphas: Constant = DFLT, l1Ratio: Constant = DFLT, intercept: Constant = DFLT, normalize: Constant = DFLT, maxIter: Constant = DFLT, tolerance: Constant = DFLT, positive: Constant = DFLT, swColName: Constant = DFLT, checkInput: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_ema)
def ema(X: Constant, window: Constant, warmup: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_encodeShortGenomeSeq)
# def encodeShortGenomeSeq(X: Constant) -> Constant:
#     ...


# @builtin_function(_endsWith)
# def endsWith(X: Constant, str: Constant) -> Constant:
#     ...


# @builtin_function(_enlist)
# def enlist(X: Constant) -> Constant:
#     ...


@builtin_function(_eq)
def eq(X: Constant, Y: Constant) -> Constant:
    ...


@builtin_function(_eqFloat)
def eqFloat(X: Constant, Y: Constant, precision: Constant = DFLT) -> Constant:
    ...


@builtin_function(_eqObj)
def eqObj(obj1: Constant, obj2: Constant, precision: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_eqPercent)
# def eqPercent(X: Constant, Y: Constant, toleranceLevel: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_erase_)
# def erase_(obj: Constant, key: Union[Alias[Literal["filter"]], Constant]) -> Constant:
#     ...


# @builtin_function(_esd)
# def esd(data: Constant, hybrid: Constant = DFLT, maxAnomalies: Constant = DFLT, alpha: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_euclidean)
# def euclidean(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_eval)
# def eval(expr: Constant) -> Constant:
#     ...


# @builtin_function(_ewmCorr)
# def ewmCorr(X: Constant, com: Constant = DFLT, span: Constant = DFLT, halfLife: Constant = DFLT, alpha: Constant = DFLT, minPeriods: Constant = DFLT, adjust: Constant = DFLT, ignoreNA: Constant = DFLT, other: Constant = DFLT, bias: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_ewmCov)
# def ewmCov(X: Constant, com: Constant = DFLT, span: Constant = DFLT, halfLife: Constant = DFLT, alpha: Constant = DFLT, minPeriods: Constant = DFLT, adjust: Constant = DFLT, ignoreNA: Constant = DFLT, other: Constant = DFLT, bias: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_ewmMean)
def ewmMean(X: Constant, com: Constant = DFLT, span: Constant = DFLT, halfLife: Constant = DFLT, alpha: Constant = DFLT, minPeriods: Constant = DFLT, adjust: Constant = DFLT, ignoreNA: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_ewmStd)
# def ewmStd(X: Constant, com: Constant = DFLT, span: Constant = DFLT, halfLife: Constant = DFLT, alpha: Constant = DFLT, minPeriods: Constant = DFLT, adjust: Constant = DFLT, ignoreNA: Constant = DFLT, bias: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_ewmVar)
# def ewmVar(X: Constant, com: Constant = DFLT, span: Constant = DFLT, halfLife: Constant = DFLT, alpha: Constant = DFLT, minPeriods: Constant = DFLT, adjust: Constant = DFLT, ignoreNA: Constant = DFLT, bias: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_exists)
# def exists(paths: Constant) -> Constant:
#     ...


@builtin_function(_exp)
def exp(X: Constant) -> Constant:
    ...


# @builtin_function(_exp2)
# def exp2(X: Constant) -> Constant:
#     ...


# @builtin_function(_expm1)
# def expm1(X: Constant) -> Constant:
#     ...


# @builtin_function(_expr)
# def expr(*args) -> Constant:
#     ...


# @builtin_function(_eye)
# def eye(n: Constant) -> Constant:
#     ...


# @builtin_function(_ffill)
# def ffill(obj: Constant, limit: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_ffill_)
# def ffill_(obj: Constant, limit: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_fill_)
def fill_(obj: Constant, index: Constant, value: Constant) -> Constant:
    ...


# @builtin_function(_find)
# def find(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_first)
# def first(X: Constant) -> Constant:
#     ...


# @builtin_function(_firstHit)
# def firstHit(func: Constant, X: Constant, target: Constant) -> Constant:
#     ...


# @builtin_function(_firstNot)
# def firstNot(X: Constant, k: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_fj)
# def fj(leftTable: Constant, rightTable: Constant, matchingCols: Constant, rightMatchingCols: Constant = DFLT, leftFilter: Constant = DFLT, rightFilter: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_flatten)
# def flatten(X: Constant) -> Constant:
#     ...


# @builtin_function(_flip)
# def flip(obj: Constant) -> Constant:
#     ...


# @builtin_function(_floor)
# def floor(X: Constant) -> Constant:
#     ...


# @builtin_function(_fmin)
# def fmin(func: Constant, X0: Constant, xtol: Constant = DFLT, ftol: Constant = DFLT, maxIter: Constant = DFLT, maxFun: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_fminBFGS)
# def fminBFGS(func: Constant, X0: Constant, fprime: Constant = DFLT, gtol: Constant = DFLT, norm: Constant = DFLT, epsilon: Constant = DFLT, maxIter: Constant = DFLT, xrtol: Constant = DFLT, c1: Constant = DFLT, c2: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_fminLBFGSB)
# def fminLBFGSB(func: Constant, X0: Constant, fprime: Constant = DFLT, bounds: Constant = DFLT, m: Constant = DFLT, factr: Constant = DFLT, pgtol: Constant = DFLT, epsilon: Constant = DFLT, maxIter: Constant = DFLT, maxFun: Constant = DFLT, maxLS: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_fminNCG)
# def fminNCG(func: Constant, X0: Constant, fprime: Constant, fhess: Constant, xtol: Constant = DFLT, maxIter: Constant = DFLT, c1: Constant = DFLT, c2: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_fminSLSQP)
# def fminSLSQP(func: Constant, X0: Constant, fprime: Constant = DFLT, constraints: Constant = DFLT, bounds: Constant = DFLT, ftol: Constant = DFLT, epsilon: Constant = DFLT, maxIter: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_form)
# def form(X: Constant) -> Constant:
#     ...


# @builtin_function(_format)
# def format(X: Constant, format: Constant) -> Constant:
#     ...


# @builtin_function(_fromJson)
# def fromJson(jsonStr: Constant) -> Constant:
#     ...


# @builtin_function(_fromStdJson)
# def fromStdJson(jsonStr: Constant) -> Constant:
#     ...


# @builtin_function(_fromUTF8)
# def fromUTF8(str: Constant, encode: Constant) -> Constant:
#     ...


# @builtin_function(_fTest)
# def fTest(X: Constant, Y: Constant, ratio: Constant = DFLT, confLevel: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_funcByName)
# def funcByName(name: Constant) -> Constant:
#     ...


# @builtin_function(_fy5253)
# def fy5253(X: Constant, weekday: Constant = DFLT, startingMonth: Constant = DFLT, nearest: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_fy5253Quarter)
# def fy5253Quarter(X: Constant, weekday: Constant = DFLT, startingMonth: Constant = DFLT, qtrWithExtraWeek: Constant = DFLT, nearest: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_gaussianKde)
# def gaussianKde(X: Constant, weights: Constant = DFLT, bwMethod: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_gaussianKdePredict)
# def gaussianKdePredict(model: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_gaussianNB)
# def gaussianNB(Y: Constant, X: Constant, varSmoothing: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_ge)
def ge(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_gema)
# def gema(X: Constant, window: Constant, alpha: Constant) -> Constant:
#     ...


# @builtin_function(_genShortGenomeSeq)
# def genShortGenomeSeq(X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_getLicenseExpiration)
# def getLicenseExpiration() -> Constant:
#     ...


# @builtin_function(_getLicenseServerResourceInfo)
# def getLicenseServerResourceInfo() -> Constant:
#     ...


# @builtin_function(_glm)
# def glm(ds: Constant, yColName: Constant, xColNames: Constant, family: Constant = DFLT, link: Constant = DFLT, tolerance: Constant = DFLT, maxIter: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_gmm)
# def gmm(X: Constant, k: Constant, maxIter: Constant = DFLT, tolerance: Constant = DFLT, randomSeed: Constant = DFLT, mean: Constant = DFLT, sigma: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_gmtime)
# def gmtime(X: Constant) -> Constant:
#     ...


# @builtin_function(_gram)
# def gram(ds: Constant, colNames: Constant = DFLT, subMean: Constant = DFLT, normalize: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_gramSchmidt)
# def gramSchmidt(X: Constant, normalize : Constant = DFLT) -> Constant:
#     ...


@builtin_function(_groupby)
def groupby(func: Constant, funcArgs: Constant, groupingCol: Constant) -> Constant:
    ...


# @builtin_function(_groups)
# def groups(X: Constant, mode: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_gt)
def gt(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_hashBucket)
# def hashBucket(X: Constant, buckets: Constant) -> Constant:
#     ...


# @builtin_function(_hasNull)
# def hasNull(obj: Constant) -> Constant:
#     ...


@builtin_function(_head)
def head(obj: Constant, n: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_hex)
# def hex(X: Constant, reverse: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_hour)
# def hour(X: Constant) -> Constant:
#     ...


# @builtin_function(_hourOfDay)
# def hourOfDay(X: Constant) -> Constant:
#     ...


# @builtin_function(_ifirstHit)
# def ifirstHit(func: Constant, X: Constant, target: Constant) -> Constant:
#     ...


@builtin_function(_ifirstNot)
def ifirstNot(X: Constant) -> Constant:
    ...


# @builtin_function(_ifNull)
# def ifNull(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_ifValid)
# def ifValid(X: Constant, Y: Constant) -> Constant:
#     ...


@builtin_function(_iif)
def iif(cond: Constant, trueResult: Constant, falseResult: Constant) -> Constant:
    ...


# @builtin_function(_ilastNot)
# def ilastNot(X: Constant) -> Constant:
#     ...


# @builtin_function(_ilike)
# def ilike(X: Constant, pattern: Constant) -> Constant:
#     ...


# @builtin_function(_imax)
# def imax(X: Constant) -> Constant:
#     ...


# @builtin_function(_imaxLast)
# def imaxLast(X: Constant) -> Constant:
#     ...


# @builtin_function(_imin)
# def imin(X: Constant) -> Constant:
#     ...


# @builtin_function(_iminLast)
# def iminLast(X: Constant) -> Constant:
#     ...


@builtin_function(_In)
def In(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_initcap)
# def initcap(X: Constant) -> Constant:
#     ...


# @builtin_function(_integral)
# def integral(func: Constant, start: Constant, end: Constant, start2: Constant = DFLT, end2: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_interpolate)
# def interpolate(X: Constant, method: Constant = DFLT, limit: Constant = DFLT, inplace: Constant = DFLT, limitDirection: Constant = DFLT, limitArea: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_intersection)
# def intersection(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_interval)
# def interval(X: Constant, duration: Constant, fill: Constant, step: Constant = DFLT, explicitOffset: Constant = DFLT, closed: Constant = DFLT, label: Constant = DFLT, origin: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_invBeta)
# def invBeta(alpha: Constant, beta: Constant, p: Constant) -> Constant:
#     ...


# @builtin_function(_invBinomial)
# def invBinomial(trials: Constant, prob: Constant, p: Constant) -> Constant:
#     ...


# @builtin_function(_invChiSquare)
# def invChiSquare(df: Constant, p: Constant) -> Constant:
#     ...


# @builtin_function(_inverse)
# def inverse(obj: Constant) -> Constant:
#     ...


# @builtin_function(_invExp)
# def invExp(mean: Constant, p: Constant) -> Constant:
#     ...


# @builtin_function(_invF)
# def invF(numeratorDF: Constant, denominatorDF: Constant, p: Constant) -> Constant:
#     ...


# @builtin_function(_invGamma)
# def invGamma(shape: Constant, scale: Constant, p: Constant) -> Constant:
#     ...


# @builtin_function(_invLogistic)
# def invLogistic(mean: Constant, s: Constant, p: Constant) -> Constant:
#     ...


# @builtin_function(_invNormal)
# def invNormal(mean: Constant, stdev: Constant, p: Constant) -> Constant:
#     ...


# @builtin_function(_invPoisson)
# def invPoisson(mean: Constant, p: Constant) -> Constant:
#     ...


# @builtin_function(_invStudent)
# def invStudent(df: Constant, p: Constant) -> Constant:
#     ...


# @builtin_function(_invUniform)
# def invUniform(lower: Constant, upper: Constant, p: Constant) -> Constant:
#     ...


# @builtin_function(_invWeibull)
# def invWeibull(alpha: Constant, beta: Constant, p: Constant) -> Constant:
#     ...


# @builtin_function(_isAlNum)
# def isAlNum(X: Constant) -> Constant:
#     ...


# @builtin_function(_isAlpha)
# def isAlpha(X: Constant) -> Constant:
#     ...


# @builtin_function(_isDigit)
# def isDigit(X: Constant) -> Constant:
#     ...


# @builtin_function(_isDuplicated)
# def isDuplicated(X: Constant, keep: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_isLeapYear)
# def isLeapYear(X: Constant) -> Constant:
#     ...


# @builtin_function(_isLower)
# def isLower(X: Constant) -> Constant:
#     ...


# @builtin_function(_isMonotonic)
# def isMonotonic(X: Constant) -> Constant:
#     ...


# @builtin_function(_isMonotonicDecreasing)
# def isMonotonicDecreasing(X: Constant) -> Constant:
#     ...


# @builtin_function(_isMonotonicIncreasing)
# def isMonotonicIncreasing(X: Constant) -> Constant:
#     ...


# @builtin_function(_isMonthEnd)
# def isMonthEnd(X: Constant) -> Constant:
#     ...


# @builtin_function(_isMonthStart)
# def isMonthStart(X: Constant) -> Constant:
#     ...


# @builtin_function(_isNanInf)
# def isNanInf(X: Constant, includeNull: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_isNothing)
# def isNothing(obj: Constant) -> Constant:
#     ...


@builtin_function(_isNull)
def isNull(X: Constant) -> Constant:
    ...


# @builtin_function(_isNumeric)
# def isNumeric(X: Constant) -> Constant:
#     ...


# @builtin_function(_isort)
# def isort(X: Constant, ascending: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_isort_)
# def isort_(X: Constant, ascending: Constant = DFLT, indices = DFLT) -> Constant:
#     ...


@builtin_function(_isortTop)
def isortTop(X: Constant, top: Constant, ascending: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_isPeak)
# def isPeak(X: Constant, strict: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_isQuarterEnd)
# def isQuarterEnd(X: Constant) -> Constant:
#     ...


# @builtin_function(_isQuarterStart)
# def isQuarterStart(X: Constant) -> Constant:
#     ...


# @builtin_function(_isSorted)
# def isSorted(X: Constant, ascending: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_isSpace)
# def isSpace(X: Constant) -> Constant:
#     ...


# @builtin_function(_isTitle)
# def isTitle(X: Constant) -> Constant:
#     ...


# @builtin_function(_isUpper)
# def isUpper(X: Constant) -> Constant:
#     ...


# @builtin_function(_isValid)
# def isValid(X: Constant) -> Constant:
#     ...


# @builtin_function(_isValley)
# def isValley(X: Constant, strict: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_isVoid)
# def isVoid(obj: Constant) -> Constant:
#     ...


# @builtin_function(_isYearEnd)
# def isYearEnd(X: Constant) -> Constant:
#     ...


# @builtin_function(_isYearStart)
# def isYearStart(X: Constant) -> Constant:
#     ...


# @builtin_function(_iterate)
# def iterate(init: Constant, coeffs: Constant, input: Constant) -> Constant:
#     ...


@builtin_function(_join)
def join(obj1: Constant, obj2: Constant) -> Constant:
    ...


@builtin_function(_join_)
def join_(obj: Constant, newData: Constant) -> Constant:
    ...


@builtin_function(_kama)
def kama(X: Constant, window: Constant) -> Constant:
    ...


# @builtin_function(_kendall)
# def kendall(X: Constant, Y: Constant) -> Constant:
#     ...


@builtin_function(_keys)
def keys(obj: Constant) -> Constant:
    ...


# @builtin_function(_kmeans)
# def kmeans(X: Constant, k: Constant, maxIter: Constant = DFLT, randomSeed: Constant = DFLT, init: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_knn)
# def knn(Y: Constant, X: Constant, type: Constant, nNeighbor: Constant, power: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_kroghInterpolate)
# def kroghInterpolate(Xi: Constant, Yi: Constant, X: Constant, der: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_ksTest)
# def ksTest(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_kurtosis)
# def kurtosis(X: Constant, biased: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_lasso)
# def lasso(ds: Constant, yColName: Constant, xColNames: Constant, alpha: Constant = DFLT, intercept: Constant = DFLT, normalize: Constant = DFLT, maxIter: Constant = DFLT, tolerance: Constant = DFLT, positive: Constant = DFLT, swColName: Constant = DFLT, checkInput: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_lassoBasic)
# def lassoBasic(Y: Constant, X: Constant, mode: Constant = DFLT, alpha: Constant = DFLT, intercept: Constant = DFLT, normalize: Constant = DFLT, maxIter: Constant = DFLT, tolerance: Constant = DFLT, positive: Constant = DFLT, swColName: Constant = DFLT, checkInput: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_lassoCV)
# def lassoCV(ds: Constant, yColName: Constant, xColNames: Constant, alphas: Constant = DFLT, intercept: Constant = DFLT, normalize: Constant = DFLT, maxIter: Constant = DFLT, tolerance: Constant = DFLT, positive: Constant = DFLT, swColName: Constant = DFLT, checkInput: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_last)
def last(X: Constant) -> Constant:
    ...


# @builtin_function(_lastNot)
# def lastNot(X: Constant, k: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_lastWeekOfMonth)
# def lastWeekOfMonth(X: Constant, weekday: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_le)
def le(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_left)
# def left(X: Constant, n: Constant) -> Constant:
#     ...


# @builtin_function(_lfill)
# def lfill(obj: Constant) -> Constant:
#     ...


# @builtin_function(_lfill_)
# def lfill_(obj: Constant) -> Constant:
#     ...


# @builtin_function(_license)
# def license(fileName: Constant = DFLT, pubKeyFile: Constant = DFLT, read: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_like)
# def like(X: Constant, pattern: Constant) -> Constant:
#     ...


@builtin_function(_linearTimeTrend)
def linearTimeTrend(X: Constant, window: Constant) -> Constant:
    ...


# @builtin_function(_linprog)
# def linprog(f: Constant, A: Constant = DFLT, b: Constant = DFLT, Aeq: Constant = DFLT, beq: Constant = DFLT, lb: Constant = DFLT, ub: Constant = DFLT, method: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_lj)
# def lj(leftTable: Constant, rightTable: Constant, matchingCols: Constant, rightMatchingCols: Constant = DFLT, leftFilter: Constant = DFLT, rightFilter: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_loadNpy)
# def loadNpy(fileName: Constant) -> Constant:
#     ...


# @builtin_function(_loadNpz)
# def loadNpz(fileName: Constant) -> Constant:
#     ...


# @builtin_function(_loadRecord)
# def loadRecord(filename: Constant, schema: Constant, skipBytes: Constant = DFLT, count: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_loadTable)
# def loadTable(database: Constant, tableName: Constant, partitions: Constant = DFLT, memoryMode: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_loadText)
def loadText(filename: Constant, delimiter: Constant = DFLT, schema: Constant = DFLT, skipRows: Constant = DFLT, arrayDelimiter: Constant = DFLT, containHeader: Constant = DFLT, arrayMarker: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_loadTextEx)
# def loadTextEx(dbHandle: Constant, tableName: Constant, partitionColumns: Constant, filename: Constant, delimiter: Constant = DFLT, schema: Constant = DFLT, skipRows: Constant = DFLT, transform: Constant = DFLT, sortColumns: Constant = DFLT, atomic: Constant = DFLT, arrayDelimiter: Constant = DFLT, containHeader: Constant = DFLT, arrayMarker: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_loc)
# def loc(obj: Constant, rowFilter: Constant, colFilter: Constant = DFLT, view: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_localtime)
# def localtime(X: Constant) -> Constant:
#     ...


# @builtin_function(_loess)
# def loess(X: Constant, Y: Constant, resampleRule: Constant, closed: Constant = DFLT, origin: Constant = DFLT, outputX: Constant = DFLT, bandwidth: Constant = DFLT, robustnessIter: Constant = DFLT, accuracy: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_log)
def log(X: Constant) -> Constant:
    ...


# @builtin_function(_log10)
# def log10(X: Constant) -> Constant:
#     ...


# @builtin_function(_log1p)
# def log1p(X: Constant) -> Constant:
#     ...


# @builtin_function(_log2)
# def log2(X: Constant) -> Constant:
#     ...


# @builtin_function(_logisticRegression)
# def logisticRegression(ds: Constant, yColName: Constant, xColNames: Constant, intercept: Constant = DFLT, initTheta: Constant = DFLT, tolerance: Constant = DFLT, maxIter: Constant = DFLT, regularizationCoeff: Constant = DFLT, numClasses: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_loop)
# def loop(func: Constant, *args) -> Constant:
#     ...


# @builtin_function(_lower)
# def lower(X: Constant) -> Constant:
#     ...


# @builtin_function(_lowerBound)
# def lowerBound(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_lowRange)
# def lowRange(X: Constant) -> Constant:
#     ...


# @builtin_function(_lpad)
# def lpad(str: Constant, length: Constant, pattern: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_lshift)
def lshift(X: Constant, bits: Constant) -> Constant:
    ...


# @builtin_function(_lsj)
# def lsj(leftTable: Constant, rightTable: Constant, matchingCols: Constant, rightMatchingCols: Constant = DFLT, leftFilter: Constant = DFLT, rightFilter: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_lt)
def lt(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_ltrim)
# def ltrim(X: Constant) -> Constant:
#     ...


# @builtin_function(_lu)
# def lu(obj: Constant, permute: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_ma)
def ma(X: Constant, window: Constant, maType: Constant) -> Constant:
    ...


# @builtin_function(_mad)
# def mad(X: Constant, useMedian: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_makeCall)
# def makeCall(func: Constant, *args) -> Constant:
#     ...


# @builtin_function(_makeKey)
# def makeKey(*args) -> Constant:
#     ...


# @builtin_function(_makeSortedKey)
# def makeSortedKey(*args) -> Constant:
#     ...


# @builtin_function(_makeUnifiedCall)
# def makeUnifiedCall(func: Constant, args: Constant) -> Constant:
#     ...


# @builtin_function(_mannWhitneyUTest)
# def mannWhitneyUTest(X: Constant, Y: Constant, correct: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_manova)
# def manova(X: Constant, group: Constant) -> Constant:
#     ...


# @builtin_function(_mask)
# def mask(X: Constant, Y: Constant) -> Constant:
#     ...


@builtin_function(_mavg)
def mavg(X: Constant, window: Union[Alias[Literal["weights"]], Constant], minPeriods: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_mavgTopN)
# def mavgTopN(X: Constant, S: Constant, window: Constant, top: Constant, ascending: Constant = DFLT, tiesMethod: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_max)
def max(X: Constant, Y: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_maxIgnoreNull)
# def maxIgnoreNull(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_maxPositiveStreak)
# def maxPositiveStreak(X: Constant) -> Constant:
#     ...


# @builtin_function(_mbeta)
# def mbeta(Y: Constant, X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mbetaTopN)
# def mbetaTopN(X: Constant, Y: Constant, S: Constant, window: Constant, top: Constant, ascending: Constant = DFLT, tiesMethod: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_mcorr)
def mcorr(X: Constant, Y: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_mcorrTopN)
# def mcorrTopN(X: Constant, Y: Constant, S: Constant, window: Constant, top: Constant, ascending: Constant = DFLT, tiesMethod: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mcount)
# def mcount(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_mcovar)
def mcovar(X: Constant, Y: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_mcovarTopN)
# def mcovarTopN(X: Constant, Y: Constant, S: Constant, window: Constant, top: Constant, ascending: Constant = DFLT, tiesMethod: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_md5)
# def md5(X: Constant) -> Constant:
#     ...


# @builtin_function(_mean)
# def mean(X: Constant) -> Constant:
#     ...


# @builtin_function(_med)
# def med(X: Constant) -> Constant:
#     ...


# @builtin_function(_mem)
# def mem(freeUnusedBlocks: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_member)
# def member(obj: Constant, keys: Constant) -> Constant:
#     ...


# @builtin_function(_merge)
# def merge(left: Constant, right: Constant, how: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mfirst)
# def mfirst(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mfirstNot)
# def mfirstNot(X: Constant, window: Constant, k: Constant = DFLT, minPeriods: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_microsecond)
# def microsecond(X: Constant) -> Constant:
#     ...


# @builtin_function(_mifirstNot)
# def mifirstNot(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_milastNot)
# def milastNot(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_millisecond)
# def millisecond(X: Constant) -> Constant:
#     ...


@builtin_function(_mimax)
def mimax(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


@builtin_function(_mimaxLast)
def mimaxLast(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


@builtin_function(_mimin)
def mimin(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


@builtin_function(_miminLast)
def miminLast(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


@builtin_function(_min)
def min(X: Constant, Y: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_minIgnoreNull)
# def minIgnoreNull(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_minuteOfHour)
# def minuteOfHour(X: Constant) -> Constant:
#     ...


@builtin_function(_mkurtosis)
def mkurtosis(X: Constant, window: Constant, biased: Constant = DFLT, minPeriods: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_mlast)
# def mlast(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mlastNot)
# def mlastNot(X: Constant, window: Constant, k: Constant = DFLT, minPeriods: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mLowRange)
# def mLowRange(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_mmad)
def mmad(X: Constant, window: Constant, useMedian: Constant = DFLT, minPeriods: Constant = DFLT) -> Constant:
    ...


@builtin_function(_mmax)
def mmax(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_mmaxPositiveStreak)
# def mmaxPositiveStreak(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_mmed)
def mmed(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


@builtin_function(_mmin)
def mmin(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_mmse)
# def mmse(Y: Constant, X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_mod)
def mod(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_mode)
# def mode(X: Constant) -> Constant:
#     ...


# @builtin_function(_month)
# def month(X: Constant) -> Constant:
#     ...


# @builtin_function(_monthBegin)
# def monthBegin(X: Constant, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_monthEnd)
# def monthEnd(X: Constant, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_monthOfYear)
# def monthOfYear(X: Constant) -> Constant:
#     ...


@builtin_function(_move)
def move(X: Constant, steps: Constant) -> Constant:
    ...


@builtin_function(_moving)
def moving(func: Constant, funcArgs: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_movingTopNIndex)
# def movingTopNIndex(X: Constant, window: Constant, top: Constant, ascending: Constant = DFLT, fixed: Constant = DFLT, tiesMethod: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_movingWindowIndex)
# def movingWindowIndex(X: Constant, window: Constant, fixed: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mpercentile)
# def mpercentile(X: Constant, percent: Constant, window: Constant, interpolation: Constant = DFLT, minPeriods: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mpercentileTopN)
# def mpercentileTopN(X: Constant, S: Constant, percent: Constant, window: Constant, top: Constant, interpolation: Constant = DFLT, ascending: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mprod)
# def mprod(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_mrank)
def mrank(X: Constant, ascending: Constant, window: Constant, ignoreNA: Constant = DFLT, tiesMethod: Constant = DFLT, percent: Constant = DFLT, minPeriods: Constant = DFLT) -> Constant:
    ...


@builtin_function(_mskew)
def mskew(X: Constant, window: Constant, biased: Constant = DFLT, minPeriods: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_mslr)
# def mslr(Y: Constant, X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_mstd)
def mstd(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


@builtin_function(_mstdp)
def mstdp(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_mstdpTopN)
# def mstdpTopN(X: Constant, S: Constant, window: Constant, top: Constant, ascending: Constant = DFLT, tiesMethod: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mstdTopN)
# def mstdTopN(X: Constant, S: Constant, window: Constant, top: Constant, ascending: Constant = DFLT, tiesMethod: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_msum)
def msum(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


@builtin_function(_msum2)
def msum2(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


@builtin_function(_msumTopN)
def msumTopN(X: Constant, S: Constant, window: Constant, top: Constant, ascending: Constant = DFLT, tiesMethod: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_mTopRange)
# def mTopRange(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_mul)
def mul(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_multinomialNB)
# def multinomialNB(Y: Constant, X: Constant, varSmoothing: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mutualInfo)
# def mutualInfo(X: Constant, Y: Constant) -> Constant:
#     ...


@builtin_function(_mvar)
def mvar(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_mvarp)
# def mvarp(X: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mvarpTopN)
# def mvarpTopN(X: Constant, S: Constant, window: Constant, top: Constant, ascending: Constant = DFLT, tiesMethod: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mvarTopN)
# def mvarTopN(X: Constant, S: Constant, window: Constant, top: Constant, ascending: Constant = DFLT, tiesMethod: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mwavg)
# def mwavg(X: Constant, Y: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mwsum)
# def mwsum(X: Constant, Y: Constant, window: Constant, minPeriods: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_mwsumTopN)
# def mwsumTopN(X: Constant, Y: Constant, S: Constant, window: Constant, top: Constant, ascending: Constant = DFLT, tiesMethod: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_nanInfFill)
# def nanInfFill(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_nanosecond)
# def nanosecond(X: Constant) -> Constant:
#     ...


@builtin_function(_ne)
def ne(X: Constant, Y: Constant) -> Constant:
    ...


@builtin_function(_neg)
def neg(X: Constant) -> Constant:
    ...


# @builtin_function(_neville)
# def neville(X: Constant, Y: Constant, resampleRule: Constant, closed: Constant = DFLT, origin: Constant = DFLT, outputX: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_next)
# def next(X: Constant) -> Constant:
#     ...


# @builtin_function(_nextState)
# def nextState(X: Constant) -> Constant:
#     ...


# @builtin_function(_norm)
# def norm(mean: Constant, std: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_normal)
# def normal(mean: Constant, std: Constant, count: Constant) -> Constant:
#     ...


@builtin_function(_Not)
def Not(X: Constant) -> Constant:
    ...


# @builtin_function(_now)
# def now(nanoSecond: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_nss)
# def nss(maturity: Constant, _yield: Constant, method: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_nullCompare)
def nullCompare(func: Constant, X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_nullFill)
# def nullFill(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_nullFill_)
# def nullFill_(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_nullIf)
# def nullIf(a: Constant, b: Constant) -> Constant:
#     ...


# @builtin_function(_nunique)
# def nunique(X: Constant, ignoreNull: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_objByName)
# def objByName(name: Constant, sharedVar: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_objectChecksum)
# def objectChecksum(vector: Constant, prev: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_objs)
# def objs(shared: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_ols)
def ols(Y: Constant, X: Constant, intercept: Constant = DFLT, mode: Constant = DFLT, method: Constant = DFLT, usePinv: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_olsEx)
# def olsEx(ds: Constant, Y: Constant, X: Constant, intercept: Constant = DFLT, mode: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_oneHot)
# def oneHot(obj: Constant, encodingColumns: Constant) -> Constant:
#     ...


@builtin_function(_Or)
def Or(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_osqp)
# def osqp(q: Constant, P: Constant = DFLT, A: Constant = DFLT, l: Constant = DFLT, u: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_pack)
# def pack(format: Constant, *args) -> Constant:
#     ...


@builtin_function(_pair)
def pair(first: Constant, second: Constant) -> Constant:
    ...


@builtin_function(_panel)
def panel(row: Constant, col: Constant, metrics: Constant, rowLabel: Constant = DFLT, colLabel: Constant = DFLT, parallel: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_parseExpr)
# def parseExpr(X: Constant, varDict: Constant = DFLT, modules: Constant = DFLT, overloadedOperators: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_parseInt)
# def parseInt(X: Constant, type: Constant, radix: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_parseInteger)
# def parseInteger(X: Constant, type: Constant, radix: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_partial)
def partial(func: Constant, *args) -> Constant:
    ...


# @builtin_function(_partition)
# def partition(partitionCol: Constant, keys: Constant) -> Constant:
#     ...


# @builtin_function(_pca)
# def pca(X: Constant, colNames: Constant = DFLT, k: Constant = DFLT, normalize: Constant = DFLT, maxIter: Constant = DFLT, svdSolver: Constant = DFLT, randomState: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_pcall)
# def pcall(func: Constant, *args) -> Constant:
#     ...


# @builtin_function(_pcross)
# def pcross(func: Constant, X: Constant, Y: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_percentChange)
def percentChange(X: Constant, n: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_percentile)
# def percentile(X: Constant, percent: Constant, interpolation: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_percentileRank)
# def percentileRank(X: Constant, score: Constant, method: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_piecewiseLinFit)
# def piecewiseLinFit(X: Constant, Y: Constant, numSegments: Constant, XC: Constant = DFLT, YC: Constant = DFLT, bounds: Constant = DFLT, lapackDriver: Constant = DFLT, degree: Constant = DFLT, weights: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_pivot)
def pivot(func: Constant, funcArgs: Constant, rowAlignCol: Constant, colAlignCol: Constant) -> Constant:
    ...


# @builtin_function(_pj)
# def pj(leftTable: Constant, rightTable: Constant, matchingCols: Constant, rightMatchingCols: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_ploadText)
# def ploadText(filename: Constant, delimiter: Constant = DFLT, schema: Constant = DFLT, skipRows: Constant = DFLT, arrayDelimiter: Constant = DFLT, containHeader: Constant = DFLT, arrayMarker: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_ploop)
# def ploop(func: Constant, *args) -> Constant:
#     ...


# @builtin_function(_poly1d)
# def poly1d(z: Constant, x: Constant) -> Constant:
#     ...


# @builtin_function(_polyFit)
# def polyFit(X: Constant, Y: Constant, n: Constant) -> Constant:
#     ...


# @builtin_function(_polynomial)
# def polynomial(X: Constant, coeffs: Constant) -> Constant:
#     ...


# @builtin_function(_pop_)
# def pop_(obj: Constant) -> Constant:
#     ...


@builtin_function(_pow)
def pow(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_predict)
# def predict(model: Constant, X: Constant) -> Constant:
#     ...


@builtin_function(_prev)
def prev(X: Constant) -> Constant:
    ...


# @builtin_function(_prevState)
# def prevState(X: Constant) -> Constant:
#     ...


# @builtin_function(_print)
# def print(*args) -> Constant:
#     ...


@builtin_function(_prod)
def prod(X: Constant) -> Constant:
    ...


# @builtin_function(_push_)
# def push_(obj: Constant, newData: Constant) -> Constant:
#     ...


# @builtin_function(_pwj)
# def pwj(leftTable: Constant, rightTable: Constant, window: Constant, aggs: Constant, matchingCols: Constant, rightMatchingCols: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_pwlfPredict)
# def pwlfPredict(model: Constant, X: Constant, beta: Constant = DFLT, breaks: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_qclp)
# def qclp(r: Constant, V: Constant, k: Constant, A: Constant = DFLT, b: Constant = DFLT, Aeq: Constant = DFLT, beq: Constant = DFLT, x0: Constant = DFLT, c: Constant = DFLT, eps: Constant = DFLT, alpha: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_qr)
# def qr(obj: Constant, mode: Constant = DFLT, pivoting: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_quadprog)
# def quadprog(H: Constant, f: Constant, A: Constant = DFLT, b: Constant = DFLT, Aeq: Constant = DFLT, beq: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_quantile)
def quantile(X: Constant, q: Constant, interpolation: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_quantileSeries)
# def quantileSeries(X: Constant, q: Constant, interpolation: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_quarterBegin)
# def quarterBegin(X: Constant, startingMonth: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_quarterEnd)
# def quarterEnd(X: Constant, endingMonth: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_rad2deg)
def rad2deg(X: Constant) -> Constant:
    ...


@builtin_function(_rand)
def rand(X: Constant, count: Constant) -> Constant:
    ...


# @builtin_function(_randBeta)
# def randBeta(alpha: Constant, beta: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_randBinomial)
# def randBinomial(trials: Constant, prob: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_randChiSquare)
# def randChiSquare(df: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_randDiscrete)
# def randDiscrete(v: Constant, p: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_randExp)
# def randExp(mean: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_randF)
# def randF(numeratorDF: Constant, denominatorDF: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_randGamma)
# def randGamma(shape: Constant, scale: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_randLogistic)
# def randLogistic(mean: Constant, s: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_randMultivariateNormal)
# def randMultivariateNormal(mean: Constant, covar: Constant, count: Constant, sampleAsRow: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_randNormal)
# def randNormal(mean: Constant, stdev: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_randomForestClassifier)
# def randomForestClassifier(ds: Constant, yColName: Constant, xColNames: Constant, numClasses: Constant, maxFeatures: Constant = DFLT, numTrees: Constant = DFLT, numBins: Constant = DFLT, maxDepth: Constant = DFLT, minImpurityDecrease: Constant = DFLT, numJobs: Constant = DFLT, randomSeed: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_randomForestRegressor)
# def randomForestRegressor(ds: Constant, yColName: Constant, xColNames: Constant, maxFeatures: Constant = DFLT, numTrees: Constant = DFLT, numBins: Constant = DFLT, maxDepth: Constant = DFLT, minImpurityDecrease: Constant = DFLT, numJobs: Constant = DFLT, randomSeed: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_randPoisson)
# def randPoisson(mean: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_randStudent)
# def randStudent(df: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_randUniform)
# def randUniform(lower: Constant, upper: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_randWeibull)
# def randWeibull(alpha: Constant, beta: Constant, count: Constant) -> Constant:
#     ...


# @builtin_function(_rank)
# def rank(X: Constant, ascending: Constant = DFLT, groupNum: Constant = DFLT, ignoreNA: Constant = DFLT, tiesMethod: Constant = DFLT, percent: Constant = DFLT, precision: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_ratio)
def ratio(X: Constant, Y: Constant) -> Constant:
    ...


@builtin_function(_ratios)
def ratios(X: Constant) -> Constant:
    ...


# @builtin_function(_rdp)
# def rdp(X: Constant, epsilon: Constant) -> Constant:
#     ...


@builtin_function(_reciprocal)
def reciprocal(X: Constant) -> Constant:
    ...


# @builtin_function(_reduce)
# def reduce(func: Constant, X: Constant, init: Constant = DFLT, consistent: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_refCount)
# def refCount(obj: Constant) -> Constant:
#     ...


# @builtin_function(_regexCount)
# def regexCount(str: Constant, pattern: Constant, offset: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_regexFind)
# def regexFind(str: Constant, pattern: Constant, offset: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_regexFindStr)
# def regexFindStr(str: Constant, pattern: Constant, onlyFirst: Constant = DFLT, offset: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_regexReplace)
# def regexReplace(str: Constant, pattern: Constant, replacement: Constant, offset: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_regroup)
# def regroup(X: Constant, label: Constant, func: Constant, byRow: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_removeHead_)
# def removeHead_(obj: Constant, n: Constant) -> Constant:
#     ...


# @builtin_function(_removeTail_)
# def removeTail_(obj: Constant, n: Constant) -> Constant:
#     ...


@builtin_function(_rename_)
def rename_(a: Constant, b: Constant, c: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_reorderColumns_)
# def reorderColumns_(table: Constant, reorderedColNames: Constant) -> Constant:
#     ...


# @builtin_function(_repeat)
# def repeat(X: Constant, n: Constant) -> Constant:
#     ...


# @builtin_function(_replace)
# def replace(X: Constant, oldValue: Constant, newValue: Constant) -> Constant:
#     ...


# @builtin_function(_replace_)
# def replace_(obj: Constant, oldValue: Constant, newValue: Constant) -> Constant:
#     ...


# @builtin_function(_replaceColumn_)
# def replaceColumn_(table: Constant, colName: Constant, newCol: Constant) -> Constant:
#     ...


# @builtin_function(_repmat)
# def repmat(X: Constant, rowRep: Constant, colRep: Constant) -> Constant:
#     ...


# @builtin_function(_resample)
# def resample(X: Constant, rule: Constant, func: Constant, closed: Constant = DFLT, label: Constant = DFLT, origin: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_reshape)
def reshape(obj: Constant, dim: Constant = DFLT) -> Constant:
    ...


@builtin_function(_residual)
def residual(Y: Constant, X: Constant, params: Constant, intercept: Constant = DFLT) -> Constant:
    ...


# @builtin_function(_reverse)
# def reverse(X: Constant) -> Constant:
#     ...


# @builtin_function(_ridge)
# def ridge(ds: Constant, yColName: Constant, xColNames: Constant, alpha: Constant = DFLT, intercept: Constant = DFLT, normalize: Constant = DFLT, maxIter: Constant = DFLT, tolerance: Constant = DFLT, solver: Constant = DFLT, swColName: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_ridgeBasic)
# def ridgeBasic(Y: Constant, X: Constant, mode: Constant = DFLT, alpha: Constant = DFLT, intercept: Constant = DFLT, normalize: Constant = DFLT, maxIter: Constant = DFLT, tolerance: Constant = DFLT, solver: Constant = DFLT, swColName: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_right)
# def right(X: Constant, n: Constant) -> Constant:
#     ...


# @builtin_function(_rolling)
# def rolling(func: Constant, funcArgs: Constant, window: Constant, step: Constant = DFLT, fill: Constant = DFLT, explicitOffset: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_rollingPanel)
# def rollingPanel(X: Constant, window: Constant, groupingCol: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_round)
# def round(X: Constant, precision: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_row)
# def row(obj: Constant, index: Constant) -> Constant:
#     ...


# @builtin_function(_rowAlign)
# def rowAlign(left: Constant, right: Constant, how: Constant) -> Constant:
#     ...


# @builtin_function(_rowAnd)
# def rowAnd(*args) -> Constant:
#     ...


# @builtin_function(_rowAt)
# def rowAt(X: Constant, Y: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_rowAvg)
# def rowAvg(*args) -> Constant:
#     ...


# @builtin_function(_rowBeta)
# def rowBeta(Y: Constant, X: Constant) -> Constant:
#     ...


# @builtin_function(_rowCorr)
# def rowCorr(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_rowCount)
# def rowCount(*args) -> Constant:
#     ...


# @builtin_function(_rowCovar)
# def rowCovar(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_rowDenseRank)
# def rowDenseRank(X: Constant, ascending: Constant = DFLT, ignoreNA: Constant = DFLT, percent: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_rowDot)
# def rowDot(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_rowEuclidean)
# def rowEuclidean(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_rowGroupby)
# def rowGroupby(func: Constant, funcArgs: Constant, groupingCol: Constant, mode: Constant = DFLT, ascending: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_rowImax)
# def rowImax(*args) -> Constant:
#     ...


# @builtin_function(_rowImaxLast)
# def rowImaxLast(*args) -> Constant:
#     ...


# @builtin_function(_rowImin)
# def rowImin(*args) -> Constant:
#     ...


# @builtin_function(_rowIminLast)
# def rowIminLast(*args) -> Constant:
#     ...


# @builtin_function(_rowKurtosis)
# def rowKurtosis(X: Constant, biased: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_rowMax)
# def rowMax(*args) -> Constant:
#     ...


# @builtin_function(_rowMin)
# def rowMin(*args) -> Constant:
#     ...


# @builtin_function(_rowMove)
# def rowMove(X: Constant, steps: Constant) -> Constant:
#     ...


# @builtin_function(_rowNext)
# def rowNext(X: Constant) -> Constant:
#     ...


# @builtin_function(_rowOr)
# def rowOr(*args) -> Constant:
#     ...


# @builtin_function(_rowPrev)
# def rowPrev(X: Constant) -> Constant:
#     ...


# @builtin_function(_rowProd)
# def rowProd(*args) -> Constant:
#     ...


@builtin_function(_rowRank)
def rowRank(X: Constant, ascending: Constant = DFLT, groupNum: Constant = DFLT, ignoreNA: Constant = DFLT, tiesMethod: Constant = DFLT, percent: Constant = DFLT, precision: Constant = DFLT) -> Constant:
    ...


@builtin_function(_rows)
def rows(obj: Constant) -> Constant:
    ...


# @builtin_function(_rowSize)
# def rowSize(*args) -> Constant:
#     ...


# @builtin_function(_rowSkew)
# def rowSkew(X: Constant, biased: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_rowStd)
# def rowStd(*args) -> Constant:
#     ...


# @builtin_function(_rowStdp)
# def rowStdp(*args) -> Constant:
#     ...


# @builtin_function(_rowSum)
# def rowSum(*args) -> Constant:
#     ...


# @builtin_function(_rowSum2)
# def rowSum2(*args) -> Constant:
#     ...


# @builtin_function(_rowTanimoto)
# def rowTanimoto(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_rowVar)
# def rowVar(*args) -> Constant:
#     ...


# @builtin_function(_rowVarp)
# def rowVarp(*args) -> Constant:
#     ...


# @builtin_function(_rowWavg)
# def rowWavg(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_rowWsum)
# def rowWsum(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_rowXor)
# def rowXor(*args) -> Constant:
#     ...


# @builtin_function(_rpad)
# def rpad(str: Constant, length: Constant, pattern: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_rshift)
def rshift(X: Constant, bits: Constant) -> Constant:
    ...


# @builtin_function(_rtrim)
# def rtrim(X: Constant) -> Constant:
#     ...


# @builtin_function(_sample)
# def sample(partitionCol: Constant, size: Constant) -> Constant:
#     ...


# @builtin_function(_saveText)
# def saveText(obj: Constant, filename: Constant, delimiter: Constant = DFLT, append: Constant = DFLT, header: Constant = DFLT, bom: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_schema)
def schema(table: Union[Alias[Literal["dbHandle"]], Constant]) -> Constant:
    ...


# @builtin_function(_schur)
# def schur(obj: Constant, sort: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_scs)
# def scs(f: Constant, P: Constant = DFLT, A: Constant = DFLT, b: Constant = DFLT, Aeq: Constant = DFLT, beq: Constant = DFLT, lb: Constant = DFLT, ub: Constant = DFLT, x0: Constant = DFLT, c: Constant = DFLT, eps: Constant = DFLT, alpha: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_searchK)
# def searchK(X: Constant, k: Constant) -> Constant:
#     ...


# @builtin_function(_seasonalEsd)
# def seasonalEsd(data: Constant, period: Constant, hybrid: Constant = DFLT, maxAnomalies: Constant = DFLT, alpha: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_secondOfMinute)
# def secondOfMinute(X: Constant) -> Constant:
#     ...


# @builtin_function(_segment)
# def segment(X: Constant, segmentOffset: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_segmentby)
# def segmentby(func: Constant, funcArgs: Constant, segment: Constant) -> Constant:
#     ...


# @builtin_function(_sej)
# def sej(leftTable: Constant, rightTable: Constant, matchingCols: Constant, rightMatchingCols: Constant = DFLT, leftFilter: Constant = DFLT, rightFilter: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_sem)
# def sem(X: Constant) -> Constant:
#     ...


# @builtin_function(_semiMonthBegin)
# def semiMonthBegin(X: Constant, dayOfMonth: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_semiMonthEnd)
# def semiMonthEnd(X: Constant, dayOfMonth: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_seq)
def seq(start: Constant, end: Constant) -> Constant:
    ...


# @builtin_function(_sessionWindow)
# def sessionWindow(X: Constant, sessionGap: Constant) -> Constant:
#     ...


# @builtin_function(_setRandomSeed)
# def setRandomSeed(seed: Constant) -> Constant:
#     ...


# @builtin_function(_shape)
# def shape(obj: Constant) -> Constant:
#     ...


# @builtin_function(_shapiroTest)
# def shapiroTest(X: Constant) -> Constant:
#     ...


# @builtin_function(_shuffle)
# def shuffle(X: Constant) -> Constant:
#     ...


# @builtin_function(_shuffle_)
# def shuffle_(obj: Constant) -> Constant:
#     ...


# @builtin_function(_signbit)
# def signbit(X: Constant) -> Constant:
#     ...


@builtin_function(_signum)
def signum(X: Constant) -> Constant:
    ...


@builtin_function(_sin)
def sin(X: Constant) -> Constant:
    ...


# @builtin_function(_sinh)
# def sinh(X: Constant) -> Constant:
#     ...


@builtin_function(_size)
def size(obj: Constant) -> Constant:
    ...


# @builtin_function(_skew)
# def skew(X: Constant, biased: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_slice)
# def slice(obj: Constant, index: Union[Alias[Literal["rowIndex"]], Constant], colIndex: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_sliceByKey)
# def sliceByKey(table: Constant, rowKeys: Constant, colNames: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_sma)
def sma(X: Constant, window: Constant) -> Constant:
    ...


# @builtin_function(_snippet)
# def snippet(obj: Constant) -> Constant:
#     ...


# @builtin_function(_socp)
# def socp(f: Constant, G: Constant = DFLT, h: Constant = DFLT, l: Constant = DFLT, q: Constant = DFLT, A: Constant = DFLT, b: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_solve)
# def solve(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_sort)
# def sort(X: Constant, ascending: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_sort_)
# def sort_(obj: Constant, ascending: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_sortBy_)
def sortBy_(table: Constant, sortColumns: Constant, sortDirections: Constant = DFLT) -> Constant:
    ...


@builtin_function(_spearmanr)
def spearmanr(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_splev)
# def splev(X: Constant, tck: Constant) -> Constant:
#     ...


# @builtin_function(_spline)
# def spline(X: Constant, Y: Constant, resampleRule: Constant, closed: Constant = DFLT, origin: Constant = DFLT, outputX: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_split)
# def split(str: Constant, delimiter: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_splrep)
# def splrep(X: Constant, Y: Constant, t: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_sql)
# def sql(select: Constant, _from: Constant, where: Constant = DFLT, groupBy: Constant = DFLT, groupFlag: Constant = DFLT, csort: Constant = DFLT, ascSort: Constant = DFLT, having: Constant = DFLT, orderBy: Constant = DFLT, ascOrder: Constant = DFLT, limit: Constant = DFLT, hint: Constant = DFLT, exec: Constant = DFLT, map: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_sqlCol)
# def sqlCol(colName: Constant, func: Constant = DFLT, alias: Constant = DFLT, qualifier: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_sqlColAlias)
# def sqlColAlias(colDefs: Constant, colNames: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_sqlDelete)
# def sqlDelete(table: Constant, where: Constant = DFLT, _from: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_sqlUpdate)
# def sqlUpdate(table: Constant, updates: Constant, _from: Constant = DFLT, where: Constant = DFLT, contextBy: Constant = DFLT, csort: Constant = DFLT, ascSort: Constant = DFLT, having: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_sqrt)
# def sqrt(X: Constant) -> Constant:
#     ...


@builtin_function(_square)
def square(X: Constant) -> Constant:
    ...


# @builtin_function(_startsWith)
# def startsWith(X: Constant, str: Constant) -> Constant:
#     ...


# @builtin_function(_stat)
# def stat(X: Constant) -> Constant:
#     ...


@builtin_function(_std)
def std(X: Constant) -> Constant:
    ...


# @builtin_function(_stdp)
# def stdp(X: Constant) -> Constant:
#     ...


# @builtin_function(_stl)
# def stl(data: Constant, period: Constant, sWindow: Constant, sDegree: Constant = DFLT, sJump: Constant = DFLT, tWindow: Constant = DFLT, tDegree: Constant = DFLT, tJump: Constant = DFLT, lWindow: Constant = DFLT, lDegree: Constant = DFLT, lJump: Constant = DFLT, robust: Constant = DFLT, inner: Constant = DFLT, outer: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_stretch)
# def stretch(X: Constant, n: Constant) -> Constant:
#     ...


# @builtin_function(_stringFormat)
# def stringFormat(format: Constant, *args) -> Constant:
#     ...


# @builtin_function(_strip)
# def strip(X: Constant) -> Constant:
#     ...


# @builtin_function(_strlen)
# def strlen(X: Constant) -> Constant:
#     ...


# @builtin_function(_strlenu)
# def strlenu(X: Constant) -> Constant:
#     ...


# @builtin_function(_strpos)
# def strpos(X: Constant, str: Constant) -> Constant:
#     ...


# @builtin_function(_strReplace)
# def strReplace(str: Constant, pattern: Constant, replacement: Constant) -> Constant:
#     ...


@builtin_function(_sub)
def sub(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_subarray)
# def subarray(X: Constant, range: Constant) -> Constant:
#     ...


# @builtin_function(_substr)
# def substr(str: Constant, offset: Constant, length: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_substru)
# def substru(str: Constant, offset: Constant, length: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_subtuple)
# def subtuple(X: Constant, range: Constant) -> Constant:
#     ...


@builtin_function(_sum)
def sum(X: Constant) -> Constant:
    ...


# @builtin_function(_sum2)
# def sum2(X: Constant) -> Constant:
#     ...


# @builtin_function(_sum3)
# def sum3(X: Constant) -> Constant:
#     ...


# @builtin_function(_sum4)
# def sum4(X: Constant) -> Constant:
#     ...


# @builtin_function(_sumbars)
# def sumbars(X: Constant, threshold: Constant) -> Constant:
#     ...


# @builtin_function(_summary)
# def summary(X: Constant, interpolation: Constant = DFLT, characteristic: Constant = DFLT, percentile: Constant = DFLT, precision: Constant = DFLT, partitionSampling: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_svd)
# def svd(obj: Constant, fullMatrices: Constant = DFLT, computeUV: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_symbolCode)
# def symbolCode(X: Constant) -> Constant:
#     ...


# @builtin_function(_symmetricDifference)
# def symmetricDifference(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_syntax)
# def syntax(func: Constant) -> Constant:
#     ...


# @builtin_function(_t3)
# def t3(X: Constant, window: Constant, vfactor: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_tableInsert)
# def tableInsert(table: Constant, *args) -> Constant:
#     ...


# @builtin_function(_tableUpsert)
# def tableUpsert(obj: Constant, newData: Constant, ignoreNull: Constant = DFLT, keyColNames: Constant = DFLT, sortColumns: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_tail)
def tail(obj: Constant, n: Constant = DFLT) -> Constant:
    ...


@builtin_function(_take)
def take(X: Constant, n: Constant) -> Constant:
    ...


@builtin_function(_talib)
def talib(func: Constant, *args) -> Constant:
    ...


@builtin_function(_talibNull)
def talibNull(*args) -> Constant:
    ...


# @builtin_function(_tan)
# def tan(X: Constant) -> Constant:
#     ...


# @builtin_function(_tanh)
# def tanh(X: Constant) -> Constant:
#     ...


# @builtin_function(_tanimoto)
# def tanimoto(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_tema)
# def tema(X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_temporalAdd)
# def temporalAdd(obj: Constant, duration: Constant, unit: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_temporalFormat)
# def temporalFormat(X: Constant, format: Constant) -> Constant:
#     ...


# @builtin_function(_temporalParse)
# def temporalParse(X: Constant, format: Constant) -> Constant:
#     ...


# @builtin_function(_temporalSeq)
# def temporalSeq(start: Constant, end: Constant, rule: Constant, closed: Constant = DFLT, label: Constant = DFLT, origin: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_til)
# def til(n: Constant) -> Constant:
#     ...


# @builtin_function(_timestamp)
# def timestamp(X: Constant) -> Constant:
#     ...


# @builtin_function(_tmavg)
# def tmavg(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmbeta)
# def tmbeta(T: Constant, Y: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmcorr)
# def tmcorr(T: Constant, X: Constant, Y: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmcount)
# def tmcount(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmcovar)
# def tmcovar(T: Constant, X: Constant, Y: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmfirst)
# def tmfirst(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmkurtosis)
# def tmkurtosis(T: Constant, X: Constant, window: Constant, biased: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_tmlast)
# def tmlast(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmLowRange)
# def tmLowRange(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmmax)
# def tmmax(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmmed)
# def tmmed(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmmin)
# def tmmin(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmove)
# def tmove(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmoving)
# def tmoving(func: Constant, T: Constant, funcArgs: Constant, window: Constant, excludedPeriod: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_tmpercentile)
# def tmpercentile(T: Constant, X: Constant, percent: Constant, window: Constant, interpolation: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_tmprod)
# def tmprod(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmrank)
# def tmrank(T: Constant, X: Constant, ascending: Constant, window: Constant, ignoreNA: Constant = DFLT, tiesMethod: Constant = DFLT, percent: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_tmskew)
# def tmskew(T: Constant, X: Constant, window: Constant, biased: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_tmstd)
# def tmstd(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmstdp)
# def tmstdp(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmsum)
# def tmsum(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmsum2)
# def tmsum2(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmTopRange)
# def tmTopRange(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmvar)
# def tmvar(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmvarp)
# def tmvarp(T: Constant, X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmwavg)
# def tmwavg(T: Constant, X: Constant, Y: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_tmwsum)
# def tmwsum(T: Constant, X: Constant, Y: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_toCharArray)
# def toCharArray(X: Constant) -> Constant:
#     ...


# @builtin_function(_today)
# def today() -> Constant:
#     ...


# @builtin_function(_toJson)
# def toJson(obj: Constant) -> Constant:
#     ...


# @builtin_function(_topRange)
# def topRange(X: Constant) -> Constant:
#     ...


# @builtin_function(_toStdJson)
# def toStdJson(obj: Constant) -> Constant:
#     ...


# @builtin_function(_toUTF8)
# def toUTF8(str: Constant, encode: Constant) -> Constant:
#     ...


# @builtin_function(_transFreq)
# def transFreq(X: Constant, rule: Constant, closed: Constant = DFLT, label: Constant = DFLT, origin: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_transpose)
# def transpose(obj: Constant) -> Constant:
#     ...


# @builtin_function(_tril)
# def tril(X: Constant, k: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_trim)
# def trim(X: Constant) -> Constant:
#     ...


# @builtin_function(_trima)
# def trima(X: Constant, window: Constant) -> Constant:
#     ...


# @builtin_function(_triu)
# def triu(X: Constant, k: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_trueRange)
def trueRange(high: Constant, low: Constant, close: Constant) -> Constant:
    ...


# @builtin_function(_tTest)
# def tTest(X: Constant, Y: Constant = DFLT, mu: Constant = DFLT, confLevel: Constant = DFLT, equalVar: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_twindow)
# def twindow(func: Constant, funcArgs: Constant, T: Constant, range: Constant, prevailing: Constant = DFLT, excludedPeriod: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_type)
# def type(X: Constant) -> Constant:
#     ...


# @builtin_function(_typestr)
# def typestr(obj: Constant) -> Constant:
#     ...


# @builtin_function(_undef)
# def undef(obj: Constant, objType: Constant = DFLT, objAddr: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_ungroup)
# def ungroup(X: Constant) -> Constant:
#     ...


# @builtin_function(_unifiedCall)
# def unifiedCall(func: Constant, args: Constant) -> Constant:
#     ...


# @builtin_function(_unifiedExpr)
# def unifiedExpr(objs: Constant, optrs: Constant) -> Constant:
#     ...


# @builtin_function(_union)
# def union(X: Constant, Y: Constant) -> Constant:
#     ...


# @builtin_function(_unionAll)
# def unionAll(tableA: Union[Alias[Literal["tables"]], Constant], tableB: Union[Alias[Literal["partition"]], Constant] = DFLT, byColName: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_unpack)
# def unpack(format: Constant, buffer: Constant) -> Constant:
#     ...


# @builtin_function(_unpivot)
# def unpivot(obj: Constant, keyColNames: Constant, valueColNames: Constant, func: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_update_)
# def update_(table: Constant, colNames: Constant, newValues: Constant, filter: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_updateLicense)
# def updateLicense() -> Constant:
#     ...


# @builtin_function(_upper)
# def upper(X: Constant) -> Constant:
#     ...


# @builtin_function(_upsert_)
# def upsert_(obj: Constant, newData: Constant, ignoreNull: Constant = DFLT, keyColNames: Constant = DFLT, sortColumns: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_uuid)
# def uuid(X: Constant) -> Constant:
#     ...


# @builtin_function(_valueChanged)
# def valueChanged(X: Constant, mode: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_values)
def values(obj: Constant) -> Constant:
    ...


# @builtin_function(_VaR)
# def VaR(returns: Constant, method: Constant, confidenceLevel: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_var)
# def var(X: Constant) -> Constant:
#     ...


# @builtin_function(_varp)
# def varp(X: Constant) -> Constant:
#     ...


# @builtin_function(_vectorAR)
# def vectorAR(ds: Constant, endogColNames: Constant, exog: Constant = DFLT, trend: Constant = DFLT, maxLag: Constant = DFLT, ic: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_vectorNorm)
# def vectorNorm(x: Constant, ord: Constant = DFLT, axis: Constant = DFLT, keepDims: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_version)
# def version() -> Constant:
#     ...


# @builtin_function(_volumeBar)
# def volumeBar(X: Constant, interval: Constant, label: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_wavg)
def wavg(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_wc)
# def wc(X: Constant) -> Constant:
#     ...


# @builtin_function(_wcovar)
# def wcovar(X: Constant, Y: Constant, W: Constant) -> Constant:
#     ...


# @builtin_function(_weekBegin)
# def weekBegin(X: Constant, weekday: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_weekday)
# def weekday(X: Constant, startFromSunday: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_weekEnd)
# def weekEnd(X: Constant, weekday: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_weekOfMonth)
# def weekOfMonth(X: Constant, week: Constant = DFLT, weekday: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_weekOfYear)
# def weekOfYear(X: Constant) -> Constant:
#     ...


@builtin_function(_wilder)
def wilder(X: Constant, window: Constant) -> Constant:
    ...


# @builtin_function(_window)
# def window(func: Constant, funcArgs: Constant, range: Constant) -> Constant:
#     ...


# @builtin_function(_winsorize)
# def winsorize(X: Constant, limit: Constant, inclusive: Constant = DFLT, nanPolicy: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_winsorize_)
# def winsorize_(X: Constant, limit: Constant, inclusive: Constant = DFLT, nanPolicy: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_withNullFill)
# def withNullFill(func: Constant, X: Constant, Y: Constant, fillValue: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_wj)
# def wj(leftTable: Constant, rightTable: Constant, window: Constant, aggs: Constant, matchingCols: Constant, rightMatchingCols: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_wls)
# def wls(Y: Constant, X: Constant, W: Constant, intercept: Constant = DFLT, mode: Constant = DFLT) -> Constant:
#     ...


@builtin_function(_wma)
def wma(X: Constant, window: Constant) -> Constant:
    ...


# @builtin_function(_writeLog)
# def writeLog(*args) -> Constant:
#     ...


# @builtin_function(_writeLogLevel)
# def writeLogLevel(level: Constant, *args) -> Constant:
#     ...


# @builtin_function(_wsum)
# def wsum(X: Constant, Y: Constant) -> Constant:
#     ...


@builtin_function(_xor)
def xor(X: Constant, Y: Constant) -> Constant:
    ...


# @builtin_function(_year)
# def year(X: Constant) -> Constant:
#     ...


# @builtin_function(_yearBegin)
# def yearBegin(X: Constant, startingMonth: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_yearEnd)
# def yearEnd(X: Constant, endingMonth: Constant = DFLT, offset: Constant = DFLT, n: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_zigzag)
# def zigzag(HL: Constant, change: Constant = DFLT, percent: Constant = DFLT, retrace: Constant = DFLT, lastExtreme: Constant = DFLT) -> Constant:
#     ...


# @builtin_function(_zscore)
# def zscore(X: Constant) -> Constant:
#     ...


# @builtin_function(_zTest)
# def zTest(X: Constant, Y: Constant = DFLT, mu: Constant = DFLT, sigmaX: Constant = DFLT, sigmaY: Constant = DFLT, confLevel: Constant = DFLT) -> Constant:
#     ...
