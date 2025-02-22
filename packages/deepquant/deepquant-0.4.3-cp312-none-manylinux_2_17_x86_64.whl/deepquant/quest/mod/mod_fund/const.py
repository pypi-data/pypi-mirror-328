# -*- coding: utf-8 -*-
from deepquant.quest.const import CustomEnum


class FUND_STATUS(CustomEnum):
    """基金状态"""
    # 有效申赎
    OPEN = 'Open'
    LIMITED = 'Limited'
    # 无效申赎
    SUSPENDED = 'Suspended'
    CLOSE = 'Close'

    @classmethod
    def invalid_state(cls, state):
        return state not in [FUND_STATUS.OPEN, FUND_STATUS.LIMITED]
