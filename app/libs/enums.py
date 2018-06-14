"""
create by gaowenfeng on 
"""
from enum import Enum

__author__ = "gaowenfeng"


class PendingStatus(Enum):
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4
