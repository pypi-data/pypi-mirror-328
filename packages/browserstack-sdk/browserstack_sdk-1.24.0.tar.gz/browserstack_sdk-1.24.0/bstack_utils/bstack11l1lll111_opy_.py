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
from collections import deque
from bstack_utils.constants import *
class bstack1l11l11111_opy_:
    def __init__(self):
        self._1l111l11l11_opy_ = deque()
        self._1l1111lll1l_opy_ = {}
        self._1l111l1111l_opy_ = False
    def bstack1l1111lllll_opy_(self, test_name, bstack1l1111llll1_opy_):
        bstack1l111l11lll_opy_ = self._1l1111lll1l_opy_.get(test_name, {})
        return bstack1l111l11lll_opy_.get(bstack1l1111llll1_opy_, 0)
    def bstack1l111l1l11l_opy_(self, test_name, bstack1l1111llll1_opy_):
        bstack1l111l11111_opy_ = self.bstack1l1111lllll_opy_(test_name, bstack1l1111llll1_opy_)
        self.bstack1l111l1l111_opy_(test_name, bstack1l1111llll1_opy_)
        return bstack1l111l11111_opy_
    def bstack1l111l1l111_opy_(self, test_name, bstack1l1111llll1_opy_):
        if test_name not in self._1l1111lll1l_opy_:
            self._1l1111lll1l_opy_[test_name] = {}
        bstack1l111l11lll_opy_ = self._1l1111lll1l_opy_[test_name]
        bstack1l111l11111_opy_ = bstack1l111l11lll_opy_.get(bstack1l1111llll1_opy_, 0)
        bstack1l111l11lll_opy_[bstack1l1111llll1_opy_] = bstack1l111l11111_opy_ + 1
    def bstack1l11ll1ll1_opy_(self, bstack1l111l11l1l_opy_, bstack1l111l111ll_opy_):
        bstack1l111l111l1_opy_ = self.bstack1l111l1l11l_opy_(bstack1l111l11l1l_opy_, bstack1l111l111ll_opy_)
        event_name = bstack1l11l1l1l1l_opy_[bstack1l111l111ll_opy_]
        bstack1l1l1ll1111_opy_ = bstack11l1l1l_opy_ (u"ࠨࡻࡾ࠯ࡾࢁ࠲ࢁࡽࠣ៞").format(bstack1l111l11l1l_opy_, event_name, bstack1l111l111l1_opy_)
        self._1l111l11l11_opy_.append(bstack1l1l1ll1111_opy_)
    def bstack1ll11l111l_opy_(self):
        return len(self._1l111l11l11_opy_) == 0
    def bstack11llllll11_opy_(self):
        bstack1l111l11ll1_opy_ = self._1l111l11l11_opy_.popleft()
        return bstack1l111l11ll1_opy_
    def capturing(self):
        return self._1l111l1111l_opy_
    def bstack1lll111l1_opy_(self):
        self._1l111l1111l_opy_ = True
    def bstack11l1ll1l11_opy_(self):
        self._1l111l1111l_opy_ = False