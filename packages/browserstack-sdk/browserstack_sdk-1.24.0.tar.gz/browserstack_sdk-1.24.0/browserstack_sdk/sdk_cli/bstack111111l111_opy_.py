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
from browserstack_sdk.sdk_cli.bstack1111l1l1l1_opy_ import bstack1111l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import (
    bstack1111l1llll_opy_,
    bstack111l111111_opy_,
    bstack1lllll1l1l1_opy_,
    bstack1111lllll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack11111ll1ll_opy_ import bstack1111l1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack11111l1l11_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1111l1l1l1_opy_ import bstack1111l1ll11_opy_
import weakref
class bstack111111ll1l_opy_(bstack1111l1ll11_opy_):
    bstack11111111l1_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1111lllll1_opy_]]
    def __init__(self, bstack11111111l1_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.bstack1lllll1l1ll_opy_ = dict()
        self.bstack11111111l1_opy_ = bstack11111111l1_opy_
        self.frameworks = frameworks
        if any(bstack1111l1ll1l_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1111l1ll1l_opy_.bstack1111ll1l1l_opy_(
                (bstack1111l1llll_opy_.bstack111l11111l_opy_, bstack111l111111_opy_.PRE), self.__1lllll1llll_opy_
            )
            bstack1111l1ll1l_opy_.bstack1111ll1l1l_opy_(
                (bstack1111l1llll_opy_.QUIT, bstack111l111111_opy_.POST), self.__1lllll1l11l_opy_
            )
    def __1lllll1llll_opy_(
        self,
        f: bstack1111l1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack1111lllll1_opy_, str],
        bstack111l11llll_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lllll1l1l1_opy_.bstack111l1111l1_opy_(instance, self.bstack11111111l1_opy_, False):
            return
        if not f.bstack1lllll1lll1_opy_(f.hub_url(driver)):
            self.bstack1lllll1l1ll_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lllll1l1l1_opy_.bstack1111l1l11l_opy_(instance, self.bstack11111111l1_opy_, True)
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡠࡡࡲࡲࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡪࡰ࡬ࡸ࠿ࠦ࡮ࡰࡰࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧှ") + str(instance.ref()) + bstack11l1l1l_opy_ (u"ࠣࠤဿ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lllll1l1l1_opy_.bstack1111l1l11l_opy_(instance, self.bstack11111111l1_opy_, True)
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠤࡢࡣࡴࡴ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡ࡬ࡲ࡮ࡺ࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦ၀") + str(instance.ref()) + bstack11l1l1l_opy_ (u"ࠥࠦ၁"))
    def __1lllll1l11l_opy_(
        self,
        f: bstack1111l1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack1111lllll1_opy_, str],
        bstack111l11llll_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1lllll1ll1l_opy_(instance)
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࡣࡶࡻࡩࡵ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨ၂") + str(instance.ref()) + bstack11l1l1l_opy_ (u"ࠧࠨ၃"))
    def bstack111111l1l1_opy_(self, context: bstack11111l1l11_opy_, reverse=True) -> List[Tuple[Callable, bstack1111lllll1_opy_]]:
        matches = []
        for data in self.drivers.values():
            if (
                bstack1111l1ll1l_opy_.bstack11111l1ll1_opy_(data[1])
                and data[1].bstack1llllll1111_opy_(context)
                and getattr(data[0](), bstack11l1l1l_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥ၄"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lllll1ll11_opy_, reverse=reverse)
    def bstack11111l11l1_opy_(self, context: bstack11111l1l11_opy_, reverse=True) -> List[Tuple[Callable, bstack1111lllll1_opy_]]:
        matches = []
        for data in self.bstack1lllll1l1ll_opy_.values():
            if (
                data[1].bstack1llllll1111_opy_(context)
                and getattr(data[0](), bstack11l1l1l_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦ၅"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lllll1ll11_opy_, reverse=reverse)
    def bstack1llllll111l_opy_(self, instance: bstack1111lllll1_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1lllll1ll1l_opy_(self, instance: bstack1111lllll1_opy_) -> bool:
        if self.bstack1llllll111l_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lllll1l1l1_opy_.bstack1111l1l11l_opy_(instance, self.bstack11111111l1_opy_, False)
            return True
        return False