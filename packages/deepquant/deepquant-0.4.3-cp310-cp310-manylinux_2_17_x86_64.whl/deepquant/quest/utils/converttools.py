

def convert_exchange_to_wind(market_code):
    if market_code.endswith(".XSHE"):
        return market_code[:-4] + "SZ"
    elif market_code.endswith(".XSHG"):
        return market_code[:-4] + "SH"
    elif market_code.endswith(".XHKG"):
        return market_code[:-4] + "HK"
    return market_code