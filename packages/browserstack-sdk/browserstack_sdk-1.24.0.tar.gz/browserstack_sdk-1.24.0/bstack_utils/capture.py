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
import builtins
import logging
class bstack1ll1l11l_opy_:
    def __init__(self, handler):
        self._1l111l1lll1_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._1l111l1l1ll_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11l1l1l_opy_ (u"ࠫ࡮ࡴࡦࡰࠩ៕"), bstack11l1l1l_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫ៖"), bstack11l1l1l_opy_ (u"࠭ࡷࡢࡴࡱ࡭ࡳ࡭ࠧៗ"), bstack11l1l1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭៘")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._1l111l1ll11_opy_
        self._1l111l1llll_opy_()
    def _1l111l1ll11_opy_(self, *args, **kwargs):
        self._1l111l1lll1_opy_(*args, **kwargs)
        message = bstack11l1l1l_opy_ (u"ࠨࠢࠪ៙").join(map(str, args)) + bstack11l1l1l_opy_ (u"ࠩ࡟ࡲࠬ៚")
        self._log_message(bstack11l1l1l_opy_ (u"ࠪࡍࡓࡌࡏࠨ៛"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11l1l1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪៜ"): level, bstack11l1l1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭៝"): msg})
    def _1l111l1llll_opy_(self):
        for level, bstack1l111l1l1l1_opy_ in self._1l111l1l1ll_opy_.items():
            setattr(logging, level, self._1l111l1ll1l_opy_(level, bstack1l111l1l1l1_opy_))
    def _1l111l1ll1l_opy_(self, level, bstack1l111l1l1l1_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack1l111l1l1l1_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._1l111l1lll1_opy_
        for level, bstack1l111l1l1l1_opy_ in self._1l111l1l1ll_opy_.items():
            setattr(logging, level, bstack1l111l1l1l1_opy_)