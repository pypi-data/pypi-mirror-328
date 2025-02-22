# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack1lllll1l_opy_ = 7
def bstack11l1l1l_opy_ (bstack1l111ll_opy_):
    global bstack111111l_opy_
    bstack111ll11_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1l111_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11lll11_opy_ = bstack111ll11_opy_ % len (bstack1l1l111_opy_)
    bstack111ll1l_opy_ = bstack1l1l111_opy_ [:bstack11lll11_opy_] + bstack1l1l111_opy_ [bstack11lll11_opy_:]
    if bstack111ll1_opy_:
        bstack11ll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack11ll111_opy_ + bstack111ll11_opy_) % bstack1lllll1l_opy_) for bstack11ll111_opy_, char in enumerate (bstack111ll1l_opy_)])
    else:
        bstack11ll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack11ll111_opy_ + bstack111ll11_opy_) % bstack1lllll1l_opy_) for bstack11ll111_opy_, char in enumerate (bstack111ll1l_opy_)])
    return eval (bstack11ll1ll_opy_)
import os
import threading
import os
from typing import Dict, Any
from dataclasses import dataclass
from collections import defaultdict
from datetime import timedelta
@dataclass
class bstack11111l1l11_opy_:
    id: str
    hash: str
    thread_id: int
    process_id: int
    type: str
class bstack1lllll11l1l_opy_:
    bstack1lllll1l111_opy_ = bstack11l1l1l_opy_ (u"ࠣࡤࡨࡲࡨ࡮࡭ࡢࡴ࡮ࠦ၆")
    context: bstack11111l1l11_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack11111l1l11_opy_):
        self.context = context
        self.data = dict({bstack1lllll11l1l_opy_.bstack1lllll1l111_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ၇"), bstack11l1l1l_opy_ (u"ࠪ࠴ࠬ၈")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1lllll11ll1_opy_(self, target: object):
        return bstack1lllll11l1l_opy_.create_context(target) == self.context
    def bstack1llllll1111_opy_(self, context: bstack11111l1l11_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack1ll1l1lll_opy_(self, key: str, value: timedelta):
        self.data[bstack1lllll11l1l_opy_.bstack1lllll1l111_opy_][key] += value
    def bstack1lllll11lll_opy_(self) -> dict:
        return self.data[bstack1lllll11l1l_opy_.bstack1lllll1l111_opy_]
    @staticmethod
    def create_context(
        target: object,
        thread_id=threading.get_ident(),
        process_id=os.getpid(),
    ):
        return bstack11111l1l11_opy_(
            id=id(target),
            hash=hash(target),
            thread_id=thread_id,
            process_id=process_id,
            type=type(target),
        )