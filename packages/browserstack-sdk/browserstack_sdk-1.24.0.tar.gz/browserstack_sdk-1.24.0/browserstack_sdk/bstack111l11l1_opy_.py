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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.accessibility as bstack111lllll_opy_
from browserstack_sdk.bstack11l1111l_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1111ll1l_opy_
class bstack111lll1l_opy_:
    def __init__(self, args, logger, bstack1111llll_opy_, bstack111l1111_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111llll_opy_ = bstack1111llll_opy_
        self.bstack111l1111_opy_ = bstack111l1111_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack11l11ll1_opy_ = []
        self.bstack11l111ll_opy_ = None
        self.bstack11111l1l_opy_ = []
        self.bstack11l11l1l_opy_ = self.bstack111ll11l_opy_()
        self.bstack1111l111_opy_ = -1
    def bstack11111ll1_opy_(self, bstack11l11111_opy_):
        self.parse_args()
        self.bstack111111ll_opy_()
        self.bstack1111lll1_opy_(bstack11l11111_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111l1lll_opy_():
        import importlib
        if getattr(importlib, bstack11l1l1l_opy_ (u"ࠫ࡫࡯࡮ࡥࡡ࡯ࡳࡦࡪࡥࡳࠩএ"), False):
            bstack1111l11l_opy_ = importlib.find_loader(bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧঐ"))
        else:
            bstack1111l11l_opy_ = importlib.util.find_spec(bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨ঑"))
    def bstack111l11ll_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1111l111_opy_ = -1
        if self.bstack111l1111_opy_ and bstack11l1l1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ঒") in self.bstack1111llll_opy_:
            self.bstack1111l111_opy_ = int(self.bstack1111llll_opy_[bstack11l1l1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨও")])
        try:
            bstack11l111l1_opy_ = [bstack11l1l1l_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫঔ"), bstack11l1l1l_opy_ (u"ࠪ࠱࠲ࡶ࡬ࡶࡩ࡬ࡲࡸ࠭ক"), bstack11l1l1l_opy_ (u"ࠫ࠲ࡶࠧখ")]
            if self.bstack1111l111_opy_ >= 0:
                bstack11l111l1_opy_.extend([bstack11l1l1l_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭গ"), bstack11l1l1l_opy_ (u"࠭࠭࡯ࠩঘ")])
            for arg in bstack11l111l1_opy_:
                self.bstack111l11ll_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111111ll_opy_(self):
        bstack11l111ll_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11l111ll_opy_ = bstack11l111ll_opy_
        return bstack11l111ll_opy_
    def bstack111l1l11_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111l1lll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1111ll1l_opy_)
    def bstack1111lll1_opy_(self, bstack11l11111_opy_):
        bstack11111l11_opy_ = Config.bstack111ll1ll_opy_()
        if bstack11l11111_opy_:
            self.bstack11l111ll_opy_.append(bstack11l1l1l_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫঙ"))
            self.bstack11l111ll_opy_.append(bstack11l1l1l_opy_ (u"ࠨࡖࡵࡹࡪ࠭চ"))
        if bstack11111l11_opy_.bstack111ll1l1_opy_():
            self.bstack11l111ll_opy_.append(bstack11l1l1l_opy_ (u"ࠩ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨছ"))
            self.bstack11l111ll_opy_.append(bstack11l1l1l_opy_ (u"ࠪࡘࡷࡻࡥࠨজ"))
        self.bstack11l111ll_opy_.append(bstack11l1l1l_opy_ (u"ࠫ࠲ࡶࠧঝ"))
        self.bstack11l111ll_opy_.append(bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡴࡱࡻࡧࡪࡰࠪঞ"))
        self.bstack11l111ll_opy_.append(bstack11l1l1l_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨট"))
        self.bstack11l111ll_opy_.append(bstack11l1l1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧঠ"))
        if self.bstack1111l111_opy_ > 1:
            self.bstack11l111ll_opy_.append(bstack11l1l1l_opy_ (u"ࠨ࠯ࡱࠫড"))
            self.bstack11l111ll_opy_.append(str(self.bstack1111l111_opy_))
    def bstack111llll1_opy_(self):
        bstack11111l1l_opy_ = []
        for spec in self.bstack11l11ll1_opy_:
            bstack111ll111_opy_ = [spec]
            bstack111ll111_opy_ += self.bstack11l111ll_opy_
            bstack11111l1l_opy_.append(bstack111ll111_opy_)
        self.bstack11111l1l_opy_ = bstack11111l1l_opy_
        return bstack11111l1l_opy_
    def bstack111ll11l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack11l11l1l_opy_ = True
            return True
        except Exception as e:
            self.bstack11l11l1l_opy_ = False
        return self.bstack11l11l1l_opy_
    def bstack11111lll_opy_(self, bstack1111ll11_opy_, bstack11111ll1_opy_):
        bstack11111ll1_opy_[bstack11l1l1l_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩঢ")] = self.bstack1111llll_opy_
        multiprocessing.set_start_method(bstack11l1l1l_opy_ (u"ࠪࡷࡵࡧࡷ࡯ࠩণ"))
        bstack111l1ll1_opy_ = []
        manager = multiprocessing.Manager()
        bstack111l111l_opy_ = manager.list()
        if bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧত") in self.bstack1111llll_opy_:
            for index, platform in enumerate(self.bstack1111llll_opy_[bstack11l1l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨথ")]):
                bstack111l1ll1_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1111ll11_opy_,
                                                            args=(self.bstack11l111ll_opy_, bstack11111ll1_opy_, bstack111l111l_opy_)))
            bstack111l1l1l_opy_ = len(self.bstack1111llll_opy_[bstack11l1l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩদ")])
        else:
            bstack111l1ll1_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1111ll11_opy_,
                                                        args=(self.bstack11l111ll_opy_, bstack11111ll1_opy_, bstack111l111l_opy_)))
            bstack111l1l1l_opy_ = 1
        i = 0
        for t in bstack111l1ll1_opy_:
            os.environ[bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧধ")] = str(i)
            if bstack11l1l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫন") in self.bstack1111llll_opy_:
                os.environ[bstack11l1l1l_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ঩")] = json.dumps(self.bstack1111llll_opy_[bstack11l1l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭প")][i % bstack111l1l1l_opy_])
            i += 1
            t.start()
        for t in bstack111l1ll1_opy_:
            t.join()
        return list(bstack111l111l_opy_)
    @staticmethod
    def bstack111lll11_opy_(driver, bstack1111l1ll_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨফ"), None)
        if item and getattr(item, bstack11l1l1l_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡦࡥࡸ࡫ࠧব"), None) and not getattr(item, bstack11l1l1l_opy_ (u"࠭࡟ࡢ࠳࠴ࡽࡤࡹࡴࡰࡲࡢࡨࡴࡴࡥࠨভ"), False):
            logger.info(
                bstack11l1l1l_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠨম"))
            bstack11l11l11_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack111lllll_opy_.bstack1111l1l1_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)