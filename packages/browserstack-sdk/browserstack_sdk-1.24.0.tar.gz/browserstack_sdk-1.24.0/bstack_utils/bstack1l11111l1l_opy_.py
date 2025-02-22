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
class bstack1lll1lll1l_opy_:
    def __init__(self, handler):
        self._1l11l111lll_opy_ = None
        self.handler = handler
        self._1l11l111l1l_opy_ = self.bstack1l11l11l111_opy_()
        self.patch()
    def patch(self):
        self._1l11l111lll_opy_ = self._1l11l111l1l_opy_.execute
        self._1l11l111l1l_opy_.execute = self.bstack1l11l111ll1_opy_()
    def bstack1l11l111ll1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11l1l1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࠨ᝵"), driver_command, None, this, args)
            response = self._1l11l111lll_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11l1l1l_opy_ (u"ࠢࡢࡨࡷࡩࡷࠨ᝶"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1l11l111l1l_opy_.execute = self._1l11l111lll_opy_
    @staticmethod
    def bstack1l11l11l111_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver