def mock_instrument(market_code="000001", _type="CS", exchange="XSHE", **kwargs):
    from deepquant.quest.model.instrument import Instrument

    ins_dict = {
        "market_code": market_code,
        "type": _type,
        "exchange": exchange,
    }
    ins_dict.update(kwargs)

    return Instrument(ins_dict)


def mock_bar(instrument, **kwargs):
    from deepquant.quest.model.bar import BarObject
    return BarObject(instrument, kwargs)


def mock_tick(instrumnet, **kwargs):
    from deepquant.quest.model.tick import TickObject
    return TickObject(instrumnet, kwargs)
