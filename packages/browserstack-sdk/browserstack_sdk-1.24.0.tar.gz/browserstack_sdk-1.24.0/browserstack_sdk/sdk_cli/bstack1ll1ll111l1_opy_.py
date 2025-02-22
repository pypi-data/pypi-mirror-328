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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1111l1l1l1_opy_ import bstack1111l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import (
    bstack1111l1llll_opy_,
    bstack111l111111_opy_,
    bstack1111lllll1_opy_,
)
from bstack_utils.helper import  bstack11llll1l_opy_
from browserstack_sdk.sdk_cli.bstack11111ll1ll_opy_ import bstack1111l1ll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack111111lll1_opy_, bstack1lllllll1l1_opy_, bstack11111111ll_opy_, bstack1lll1l1l1l1_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack11l1lll111_opy_ import bstack1l11l11111_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1lllllllll1_opy_
from bstack_utils.percy import bstack11111l111_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1ll1l1l1ll1_opy_(bstack1111l1ll11_opy_):
    def __init__(self, bstack1l1l1l1l1ll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack1l1l1l1l1ll_opy_ = bstack1l1l1l1l1ll_opy_
        self.percy = bstack11111l111_opy_()
        self.bstack11ll1l1l1_opy_ = bstack1l11l11111_opy_()
        self.bstack1l1l1l1lll1_opy_()
        bstack1111l1ll1l_opy_.bstack1111ll1l1l_opy_((bstack1111l1llll_opy_.bstack111l11111l_opy_, bstack111l111111_opy_.PRE), self.bstack1l1l1l1ll1l_opy_)
        TestFramework.bstack1111ll1l1l_opy_((bstack111111lll1_opy_.TEST, bstack11111111ll_opy_.POST), self.bstack1lllllll1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1lll1l1ll_opy_(self, instance: bstack1111lllll1_opy_, driver: object):
        bstack1ll1111ll1l_opy_ = TestFramework.bstack1ll1111l1ll_opy_(instance.context)
        for t in bstack1ll1111ll1l_opy_:
            bstack11111l111l_opy_ = TestFramework.bstack111l1111l1_opy_(t, bstack1lllllllll1_opy_.bstack1llllll11ll_opy_, [])
            if any(instance is d[1] for d in bstack11111l111l_opy_) or instance == driver:
                return t
    def bstack1l1l1l1ll1l_opy_(
        self,
        f: bstack1111l1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack1111lllll1_opy_, str],
        bstack111l11llll_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1111l1ll1l_opy_.bstack1l1lll11l11_opy_(method_name):
                return
            platform_index = f.bstack111l1111l1_opy_(instance, bstack1111l1ll1l_opy_.bstack1111ll11l1_opy_, 0)
            bstack1l1llllllll_opy_ = self.bstack1l1lll1l1ll_opy_(instance, driver)
            bstack1l1l1ll1111_opy_ = TestFramework.bstack111l1111l1_opy_(bstack1l1llllllll_opy_, TestFramework.bstack1lll11lll11_opy_, None)
            if not bstack1l1l1ll1111_opy_:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠣࡱࡱࡣࡵࡸࡥࡠࡧࡻࡩࡨࡻࡴࡦ࠼ࠣࡶࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡡࡴࠢࡶࡩࡸࡹࡩࡰࡰࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡽࡪࡺࠠࡴࡶࡤࡶࡹ࡫ࡤࠣዴ"))
                return
            driver_command = f.bstack1ll1lll11ll_opy_(*args)
            for command in bstack1l11l1lll_opy_:
                if command == driver_command:
                    self.bstack1ll1l11111_opy_(driver, platform_index)
            bstack1ll1ll1111_opy_ = self.percy.bstack1l11l1l1l1_opy_()
            if driver_command in bstack1l1llllll_opy_[bstack1ll1ll1111_opy_]:
                self.bstack11ll1l1l1_opy_.bstack1l11ll1ll1_opy_(bstack1l1l1ll1111_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠤࡲࡲࡤࡶࡲࡦࡡࡨࡼࡪࡩࡵࡵࡧ࠽ࠤࡪࡸࡲࡰࡴࠥድ"), e)
    def bstack1lllllll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
        *args,
        **kwargs,
    ):
        bstack11111l111l_opy_ = f.bstack111l1111l1_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll11ll_opy_, [])
        if not bstack11111l111l_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧዶ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠦࠧዷ"))
            return
        if len(bstack11111l111l_opy_) > 1:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢዸ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠨࠢዹ"))
        bstack1111111ll1_opy_, bstack1l1ll1lll1l_opy_ = bstack11111l111l_opy_[0]
        driver = bstack1111111ll1_opy_()
        if not driver:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣዺ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠣࠤዻ"))
            return
        bstack1l1l1l1llll_opy_ = {
            TestFramework.bstack1lll1ll1111_opy_: bstack11l1l1l_opy_ (u"ࠤࡷࡩࡸࡺࠠ࡯ࡣࡰࡩࠧዼ"),
            TestFramework.bstack1lll1ll1ll1_opy_: bstack11l1l1l_opy_ (u"ࠥࡸࡪࡹࡴࠡࡷࡸ࡭ࡩࠨዽ"),
            TestFramework.bstack1lll11lll11_opy_: bstack11l1l1l_opy_ (u"ࠦࡹ࡫ࡳࡵࠢࡵࡩࡷࡻ࡮ࠡࡰࡤࡱࡪࠨዾ")
        }
        bstack1l1l1ll11l1_opy_ = { key: f.bstack111l1111l1_opy_(instance, key) for key in bstack1l1l1l1llll_opy_ }
        bstack1l1l1ll11ll_opy_ = [key for key, value in bstack1l1l1ll11l1_opy_.items() if not value]
        if bstack1l1l1ll11ll_opy_:
            for key in bstack1l1l1ll11ll_opy_:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠣዿ") + str(key) + bstack11l1l1l_opy_ (u"ࠨࠢጀ"))
            return
        platform_index = f.bstack111l1111l1_opy_(instance, bstack1111l1ll1l_opy_.bstack1111ll11l1_opy_, 0)
        if self.bstack1l1l1l1l1ll_opy_.percy_capture_mode == bstack11l1l1l_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤጁ"):
            bstack11l11l111_opy_ = bstack1l1l1ll11l1_opy_.get(TestFramework.bstack1lll11lll11_opy_) + bstack11l1l1l_opy_ (u"ࠣ࠯ࡷࡩࡸࡺࡣࡢࡵࡨࠦጂ")
            PercySDK.screenshot(
                driver,
                bstack11l11l111_opy_,
                bstack11lll11l11_opy_=bstack1l1l1ll11l1_opy_[TestFramework.bstack1lll1ll1111_opy_],
                bstack111lllll11_opy_=bstack1l1l1ll11l1_opy_[TestFramework.bstack1lll1ll1ll1_opy_],
                bstack1ll11l11l1_opy_=platform_index
            )
    def bstack1ll1l11111_opy_(self, driver, platform_index):
        if self.bstack11ll1l1l1_opy_.bstack1ll11l111l_opy_() is True or self.bstack11ll1l1l1_opy_.capturing() is True:
            return
        self.bstack11ll1l1l1_opy_.bstack1lll111l1_opy_()
        while not self.bstack11ll1l1l1_opy_.bstack1ll11l111l_opy_():
            bstack1l1l1ll1111_opy_ = self.bstack11ll1l1l1_opy_.bstack11llllll11_opy_()
            self.bstack11l11111l1_opy_(driver, bstack1l1l1ll1111_opy_, platform_index)
        self.bstack11ll1l1l1_opy_.bstack11l1ll1l11_opy_()
    def bstack11l11111l1_opy_(self, driver, bstack1l1l1ll1l_opy_, platform_index, test=None):
        if test != None:
            bstack11lll11l11_opy_ = getattr(test, bstack11l1l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧጃ"), None)
            bstack111lllll11_opy_ = getattr(test, bstack11l1l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨጄ"), None)
            PercySDK.screenshot(driver, bstack1l1l1ll1l_opy_, bstack11lll11l11_opy_=bstack11lll11l11_opy_, bstack111lllll11_opy_=bstack111lllll11_opy_, bstack1ll11l11l1_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1l1l1ll1l_opy_)
    def bstack1l1l1l1lll1_opy_(self):
        os.environ[bstack11l1l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩጅ")] = str(self.bstack1l1l1l1l1ll_opy_.success)
        os.environ[bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩጆ")] = str(self.bstack1l1l1l1l1ll_opy_.percy_capture_mode)
        self.percy.bstack1l1l1ll111l_opy_(self.bstack1l1l1l1l1ll_opy_.is_percy_auto_enabled)
        self.percy.bstack1l1l1l1ll11_opy_(self.bstack1l1l1l1l1ll_opy_.percy_build_id)