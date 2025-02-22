#from swordfish.data import FunctionDef
from deepquant.oplib.data import FunctionDef

# def sigmoid(x):
#     return 1 / (1 + F.exp(-x))
udf_SIGMOID = FunctionDef('def (x)  { return 1 \ (1 + exp(-x))}')

# def hardsigmoid(x):
#     return F.clip((x+3)/6, 0, 1)
udf_HARDSIGMOID = FunctionDef('def(x) { return clip((x+3) \ 6, 0, 1)}')

# def leakyrelu(x, a):
#     return F.max(x, 0) + a * F.min(x, 0)
udf_LEAKYRELU = FunctionDef('def (x, a) { return max(x, 0) + a * min(x, 0) }')

# def gelu(x):
#     return x * F.cdfNormal(0, 1, x)
udf_GELU = FunctionDef('def (x) { return x * cdfNormal(0, 1, x) }')

###################################### Panel operator #######################################
udf_xs_cutquartile = FunctionDef('''
def (X, a) {
    cutquartile = def(X, a){
        q3 = quantile(X, 0.75)
        q1 = quantile(X, 0.25)
        iqr = q3 - q1
        return clip(X, q1 - a*iqr, q3 + a*iqr)
    }

    return byRow(cutquartile{,a},X)
}
''')

udf_xs_cutzscore = FunctionDef('''
def (X, a) {
    cutzscore = def(X,a) {
        return clip(X, avg(X)-a*std(X), avg(X)+a*std(X))
    }

    return byRow(cutzscore{,a},X)
}
''')

udf_rank_pct = FunctionDef('''
def (X, ascending) {
    return rowRank(X, ascending=ascending, tiesMethod='average', percent=true, precision=8)
}
''')

udf_xs_regres = FunctionDef('''
def (X,Y, intercept) {
    return residual(Y, X, ols(Y,X, intercept), intercept)
}
''')

udf_xs_sortreverse = FunctionDef('''
def (X, n, mode) {
    sortreverse_two_side = def(X, n) {
        return (1 - 2 * in(0..(size(X)-1), X.isortTop(n, false)<-X.isortTop(n, true)))*X
    }
    sortreverse_acs = def(X, n) {
        return (1 - 2 * in(0..(size(X)-1), X.isortTop(n, true)))*X
    }

    sortreverse_dec = def(X, n) {
        return (1 - 2 * in(0..(size(X)-1), X.isortTop(n, false)))*X
    }

    if(mode == 2) {
        return byRow(sortreverse_two_side{, n}, X)
    } else if(mode == 1) {
        return byRow(sortreverse_dec{, n}, X)
    } else {
        return byRow(sortreverse_acs{, n}, X)
    }
}
''')

udf_xs_zscorereverse = FunctionDef('''
def (X, a, mode) {
    zscore2 = def(x) { 
        zstd = std(x)
        if (eqFloat(zstd, 0.0)) {
                return take(double(), x.size())
        }
        else {
                return (x - avg(x))\zstd
        }
    }

    zscorereverse_gt = def(X, a, zscore2) {
        return (1-2*(zscore2(X)>a))*X
    }
    zscorereverse_lt = def(X, a, zscore2) {
        return (1-2*(zscore2(X)<a))*X
    }
    zscorereverse_ne = def(X, a, zscore2) {
        return (1-2*(zscore2(X)!=a))*X
    }

    if( mode == 0 ) {
        return byRow(zscorereverse_gt{, a, zscore2}, X)
    } else if(mode==1) {
        return byRow(zscorereverse_lt{, a, zscore2}, X)
    } else {
        return byRow(zscorereverse_ne{, a, zscore2}, X)
    }
}
''')

udf_xs_grouping_sortreverse = FunctionDef('''
def (X, Y, n, mode) {
    sortreverse_two_side = def(X, Y, n) {
        return (1 - 2 * in(0..(size(Y)-1), Y.isortTop(n, false)<-Y.isortTop(n, true)))*X
    }
    sortreverse_acs = def(X, Y, n) {
        return (1 - 2 * in(0..(size(Y)-1), Y.isortTop(n, true)))*X
    }

    sortreverse_dec = def(X, Y, n) {
        return (1 - 2 * in(0..(size(Y)-1), Y.isortTop(n, false)))*X
    }

    if(mode == 2) {
        return byRow(sortreverse_two_side{, , n}, X, Y)
    } else if(mode == 1) {
        return byRow(sortreverse_dec{, , n}, X, Y)
    } else {
        return byRow(sortreverse_acs{, , n}, X, Y)
    }
}
''')

udf_xs_grouping_zscorereverse = FunctionDef('''
def (X, Y, a, mode) {
    zscore2 = def(x) { 
        zstd = std(x)
        if (eqFloat(zstd, 0.0)) {
                return take(double(), x.size())
        }
        else {
                return (x - avg(x))\zstd
        }
    }

    zscorereverse_gt = def(X, Y, a, zscore2) {
        return (1-2*(zscore2(Y)>a))*X
    }
    zscorereverse_lt = def(X, Y, a, zscore2) {
        return (1-2*(zscore2(Y)<a))*X
    }
    zscorereverse_ne = def(X, Y, a, zscore2) {
        return (1-2*(zscore2(Y)!=a))*X
    }

    if(mode == 0) {
        return byRow(zscorereverse_gt{, ,a, zscore2}, X, Y)
    } else if(mode==1) {
        return byRow(zscorereverse_lt{, ,a, zscore2}, X, Y)
    } else {
        return byRow(zscorereverse_ne{, ,a, zscore2}, X, Y)
    }
}
''')


###################################### TimeSeries operator #######################################
udf_ts_cutquantile = FunctionDef('''
def (X, a) {
    q3 = quantile(X, 0.75)
    q1 = quantile(X, 0.25)
    iqr = q3 - q1
    return clip(X, q1 - a*iqr, q3 + a*iqr)
}
''')

udf_ts_cutzscore = FunctionDef('''
def (X, a) {
    return clip(X, avg(X)-a*std(X), avg(X)+a*std(X))
}
''')

udf_ts_rollrank = FunctionDef('''
def (X, d, mode) {
    return mrank(X, mode, d, tiesMethod='average', percent=true)
}
''')

udf_ts_rollzscore = FunctionDef('''
def (X,d) {
    zstd = mstd(X, d) 
    return iif(eqFloat(zstd, 0, 6), double(), (X - mavg(X, d)) \ zstd)
}
''')

# spearmanr: 计算 X 和 Y 的 Spearman 等级相关系数
udf_ts_rankcorr = FunctionDef('''
def (X, Y, d) {
    return moving(spearmanr, (X,Y), d)
}
''')

udf_ts_avgdev = FunctionDef('''
def (X,d) {
    return moving(defg(x) :avg(abs(x-avg(x))), X, d)
}
''')

udf_ts_argmax = FunctionDef(' def (X, d) { return mimax(X, d) \ d } ')

udf_ts_argmin = FunctionDef(' def (X, d) { return mimin(X, d) \ d } ')

udf_ts_decay_linear_mean = FunctionDef(' def (X,d) { return mavg(X, 1..d) } ')

udf_ts_rollweighted_mean = FunctionDef('''
def (X, Y, d) {
    return moving(defg(x, y): wavg(x, (y-min(y))\(max(y)-min(y))), (X,Y), d)
}
''')

udf_ts_regbeta = FunctionDef('''
def (X, Y, d) {
    return moving(defg(y,x): ols(y,x, true)[1], (Y, X), d)
}
''')

udf_ts_regalpha = FunctionDef('''
def (X, Y, d) {
    return moving(defg(y,x): ols(y,x, true)[0], (Y, X), d)
}
''')

udf_ts_regres = FunctionDef('''
def (X, Y, d) {
    return moving(defg(y,x): last(residual(y, x, ols(y,x, true), true)), (Y, X), d)
}
''')

###################################### TA operator #######################################
udf_MIDPOINT = FunctionDef('def (X,d) { return (talib(mmax, X, d) + talib(mmin, X, d)) / 2.0 }')

udf_MIDPRICE = FunctionDef('def (high, low, d) { return (talib(mmax, high, d) + talib(mmin, low, d)) / 2.0 }')

udf_AROONOSC = FunctionDef('''
def (high, low, d){
	n = high.size()
	b = ifirstNot([high, low])
	if (b < 0 ||  d > n) return array(DOUBLE, n, n, NULL)
	return fill!(100.0/d * (mimaxLast(high, d + 1)-miminLast(low, d + 1)), d - 1 + 0:b, NULL)
}
''')

udf_WILLR = FunctionDef('''
def (high, low, close, d) {
    high_, low_, close_ = talibNull(high, low, close)
    hh = talib(mmax, high_, d)
    ll = talib(mmin, low_, d)
    diffHL = hh - ll
    return iif(eqFloat(diffHL, 0), 0.0, -100 * (hh - close_) \ diffHL)
}
''')

udf_CCI = FunctionDef('''
def (high, low, close, d) {
    high_, low_, close_ = talibNull(high, low, close)
    tp = (high_ + low_ + close_) / 3.0
    x = tp - talib(mavg, tp, d)
    y = talib(mmad, tp, d)
    return iif(eqFloat(y, 0) && abs(x) < 1e-13, 0.0, x / (0.015*y))
}
''')

udf_ADX = FunctionDef('''
def (high, low, close, d) {
    high_, low_, close_ = talibNull(high, low, close)
    highDelta = deltas(high)
    lowDelta = neg(deltas(low))
    tmp = iif(highDelta > lowDelta && highDelta > 0, highDelta, 0.0)
    diffP = iif(nullCompare(<, high, tmp) == NULL, NULL, tmp)
    plusDMsum = wilder(diffP, d) * d
    TRtemp = max(max(high_ - low_, abs(high_ - prev(close_))), abs(low_ - prev(close_)))
    TR = iif(cumcount(high) == 1, 0, TRtemp)
    TRsumtemp = wilder(TR, d) * d
    TRsum = iif(cumcount(high)==d, NULL, TRsumtemp)
    plusDI = iif(eqFloat(TRsum,0), 0, 100.0 * plusDMsum / TRsum)
    tmp = iif(lowDelta > highDelta && lowDelta > 0, lowDelta, 0)
    diffP = iif(nullCompare(<, low_, tmp) == NULL, NULL, tmp)
    minusDMsum = wilder(diffP, d) * d
    minusDI = iif(eqFloat(TRsum,0), 0, 100.0 * minusDMsum / TRsum) 
    dxv = iif(eqFloat(plusDI + minusDI, 0), 0, 100*abs(plusDI - minusDI) / (plusDI + minusDI))
    return wilder(dxv, d)
}
''')

udf_MFI = FunctionDef('''
def (high, low, close, volume, d) {
    tp = (high + low + close) / 3.0
    deltasTp = deltas(tp)
    pos = iif(nullCompare(>, deltasTp, 0), tp, 0)
    neg = iif(nullCompare(<, deltasTp, 0), tp, 0)

    x = talib(msum, pos*volume, d)
    y = talib(msum, neg*volume, d)
    z = x + y
    return iif(eqFloat(z, 0), 0.0, (x*100) \ z)
}
''')

udf_NATR = FunctionDef('def (high, low, close, d) { return wilder(trueRange(high, low, close), d) \ close * 100 }')

udf_BETA = FunctionDef('''
def (high, low, d) {
    x = ratios(high) - 1
    y = ratios(low) - 1
    S_xx = talib(msum2, x, d)
    S_x = talib(msum, x, d)
    S_y = talib(msum, y, d)
    S_xy = talib(msum, x * y, d)
    tmp1 = d * S_xy - S_x * S_y
    tmp2 = d * S_xx - S_x * S_x
    return iif( eqFloat(tmp2, 0) && abs(tmp1) < 1e-8, 0.0, tmp1 \ tmp2)
}
''')

udf_LINEARREG_ANGLE = FunctionDef('def (X, d) { return rad2deg(atan(linearTimeTrend(X, d)[1])) }')

udf_LINEARREG_INTERCEPT = FunctionDef('def (X, d) { return linearTimeTrend(X, d)[0] }')

udf_LINEARREG_SLOPE = FunctionDef('def (X, d) { return linearTimeTrend(X, d)[1] }')

udf_ts_ascsortcut = FunctionDef('''
def (X,d,n,mode) {
    if(mode == 1) {
        return take(double(), d-1) <- msumTopN(X, X, d, n)[(d-1):]
    } else if(mode == 2) {
        return msum(X,d) - msumTopN(X, X, d, n)
    } else {
        return msum(X,d) - 2*msumTopN(X, X, d, n)
    }
}
''')

udf_ts_decsortcut = FunctionDef('''
def (X,d,n,mode) {
    if(mode == 1) {
        return take(double(), d-1) <- msumTopN(X, X, d, n, false)[(d-1):]
    } else if(mode == 2) {
        return msum(X,d) - msumTopN(X, X, d, n, false)
    } else {
        return msum(X,d) - 2*msumTopN(X, X, d, n, false)
    }
}
''')

udf_ts_asczscorecut = FunctionDef('''
def (X,d,a,mode) { 
    zscore2 = def(x) { 
        zstd = std(x)
        if (eqFloat(zstd, 0.0)) {
                return take(double(), x.size())
        }
        else {
                return (x - avg(x))\zstd
        }
    }
    myCut1 = defg (x, a, zscore2) { 
        zs = zscore2(x)
        condition = nullCompare(<, zs, -a) && !eqFloat(zs, -a)
        return sum(iif(any(condition), x[condition], min(x))) 
    }

    myCut2 = defg (x, a, zscore2) {
        zs = zscore2(x)
        condition = nullCompare(<, zs, -a) && !eqFloat(zs, -a)
        return sum(x) - sum(iif(any(condition), x[condition], min(x))) 
    }

    myCut3 = defg (x, a, zscore2) { 
        zs = zscore2(x)
        condition = nullCompare(<, zs, -a) && !eqFloat(zs, -a)
        return sum(x) - 2*sum(iif(any(condition), x[condition], min(x))) 
    }

    if(mode == 1) {
        return moving(myCut1{,a, zscore2}, X, d)
    } else if(mode == 2){
        return moving(myCut2{,a, zscore2}, X, d)
    } else {
        return moving(myCut3{,a, zscore2}, X, d)
    }
}
''')

udf_ts_deczscorecut = FunctionDef('''
def (X,d,a,mode) { 
    zscore2 = def(x) { 
        zstd = std(x)
        if (eqFloat(zstd, 0.0)) {
                return take(double(), x.size())
        }
        else {
                return (x - avg(x))\zstd
        }
    }

    myCut1 = defg (x, a, zscore2) { 
        zs = zscore2(x)
        condition = nullCompare(>, zs, a) && !eqFloat(zs, a)
        return sum(iif(any(condition), x[condition], max(x))) 
    }

    myCut2 = defg (x, a, zscore2) { 
        zs = zscore2(x)
        condition = nullCompare(>, zs, a) && !eqFloat(zs, a)
        return sum(x) - sum(iif(any(condition), x[condition], max(x))) 
    }

    myCut3 = defg (x, a, zscore2) { 
        zs = zscore2(x)
        condition = nullCompare(>, zs, a) && !eqFloat(zs, a)
        return sum(x) - 2*sum(iif(any(condition), x[condition], max(x))) 
    }

    if(mode == 1) {
        return moving(myCut1{,a, zscore2}, X, d)
    } else if(mode == 2){
        return moving(myCut2{,a, zscore2}, X, d)
    } else {
        return moving(myCut3{,a, zscore2}, X, d)
    }
}
''')

udf_ts_grouping_ascsortcut = FunctionDef('''
def (X,Y,d,n,mode) {
    if(mode == 1) {
        return take(double(), d-1) <- msumTopN(X, Y, d, n)[(d-1):]
    } else if(mode == 2) {
        return msum(X,d) - msumTopN(X, Y, d, n)
    } else {
        return msum(X,d) - 2*msumTopN(X, Y, d, n)
    }
}
''')

udf_ts_grouping_decsortcut = FunctionDef('''
def (X,Y,d,n,mode) {
    if(mode == 1) {
        return take(double(), d-1) <- msumTopN(X, Y, d, n, false)[(d-1):]
    } else if(mode == 2) {
        return msum(X,d) - msumTopN(X, Y, d, n, false)
    } else {
        return msum(X,d) - 2*msumTopN(X, Y, d, n, false)
    }
}
''')

udf_ts_grouping_asczscorecut = FunctionDef('''
def (X,Y,d,a,mode) {
    zscore2 = def(x) { 
        zstd = std(x)
        if (eqFloat(zstd, 0.0)) {
                return take(double(), x.size())
        }
        else {
                return (x - avg(x))\zstd
        }
    }
    myCut1 = defg (x, y, a, zscore2) { 
        zs = zscore2(y)
        condition = nullCompare(<, zs, -a) && !eqFloat(zs, -a)
        return sum(iif(any(condition), x[condition], min(x))) 
    }

    myCut2 = defg (x, y, a, zscore2) {
        zs = zscore2(y)
        condition = nullCompare(<, zs, -a) && !eqFloat(zs, -a)
        return sum(x) - sum(iif(any(condition), x[condition], min(x))) 
    }

    myCut3 = defg (x, y, a, zscore2) { 
        zs = zscore2(y)
        condition = nullCompare(<, zs, -a) && !eqFloat(zs, -a)
        return sum(x) - 2*sum(iif(any(condition), x[condition], min(x))) 
    }

    if(mode == 1) {
        return moving(myCut1{,,a, zscore2}, (X,Y), d)
    } else if(mode == 2){
        return moving(myCut2{,,a, zscore2}, (X,Y), d)
    } else {
        return moving(myCut3{,,a, zscore2}, (X,Y), d)
    }
}
''')

udf_ts_grouping_deczscorecut = FunctionDef('''
def (X,Y,d,a,mode) {
    zscore2 = def(x) { 
        zstd = std(x)
        if (eqFloat(zstd, 0.0)) {
                return take(double(), x.size())
        }
        else {
                return (x - avg(x))\zstd
        }
    }
    myCut1 = defg (x, y, a, zscore2) { 
        zs = zscore2(y)
        condition = nullCompare(>, zs, a) && !eqFloat(zs, a)
        return sum(iif(any(condition), x[condition], max(x))) 
    }

    myCut2 = defg (x, y, a, zscore2) {
        zs = zscore2(y)
        condition = nullCompare(>, zs, a) && !eqFloat(zs, a)
        return sum(x) - sum(iif(any(condition), x[condition], max(x))) 
    }

    myCut3 = defg (x, y, a, zscore2) { 
        zs = zscore2(y)
        condition = nullCompare(>, zs, a) && !eqFloat(zs, a)
        return sum(x) - 2*sum(iif(any(condition), x[condition], max(x))) 
    }

    if(mode == 1) {
        return moving(myCut1{,,a, zscore2}, (X,Y), d)
    } else if(mode == 2){
        return moving(myCut2{,,a, zscore2}, (X,Y), d)
    } else {
        return moving(myCut3{,,a, zscore2}, (X,Y), d)
    }
}
''')

###################################### cgs package operator #######################################

udf_ATR = FunctionDef('def (high, low, close, d) { return wilder(trueRange(high, low, close), d) }')

udf_MACD = FunctionDef('''
def (data, fastperiod, slowperiod, signalperiod) {
    ewma_fast = ewmMean(data, span=fastperiod)
    ewma_slow = ewmMean(data, span=slowperiod)
    dif = ewma_fast - ewma_slow
    dea = ewmMean(dif, span=signalperiod)
    bar = (dif-dea)
    return dif,dea,bar
}
''')
