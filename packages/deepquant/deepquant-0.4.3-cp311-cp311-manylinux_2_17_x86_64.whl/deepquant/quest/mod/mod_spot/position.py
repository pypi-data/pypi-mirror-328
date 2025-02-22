from deepquant.quest.const import INSTRUMENT_TYPE

from deepquant.quest.mod.mod_sys_accounts.position_model import FuturePosition, FuturePositionProxy


class SpotPosition(FuturePosition):
    __instrument_types__ = (INSTRUMENT_TYPE.SPOT,)


class SpotPositionProxy(FuturePositionProxy):
    __instrument_types__ = (INSTRUMENT_TYPE.SPOT,)

    type = property(lambda self: INSTRUMENT_TYPE.SPOT)
