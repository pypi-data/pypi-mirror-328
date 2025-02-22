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
from datetime import datetime
import os
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import (
    bstack1111l1llll_opy_,
    bstack111l111111_opy_,
    bstack1lllll1l1l1_opy_,
    bstack1111lllll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack11111ll1ll_opy_ import bstack1111l1ll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack111111lll1_opy_, bstack11111111ll_opy_, bstack1lllllll1l1_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1111l1l1l1_opy_ import bstack1111l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1lllllllll1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import grpc
import traceback
class bstack1ll1l11llll_opy_(bstack1111l1ll11_opy_):
    bstack1ll1llllll1_opy_ = False
    bstack1l1ll1l11l1_opy_ = bstack11l1l1l_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴࠥሴ")
    bstack1l1ll1llll1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࠤስ")
    bstack1l1ll1l1ll1_opy_ = bstack11l1l1l_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡪࡰ࡬ࡸࠧሶ")
    bstack1l1ll1ll111_opy_ = bstack11l1l1l_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠ࡫ࡶࡣࡸࡩࡡ࡯ࡰ࡬ࡲ࡬ࠨሷ")
    bstack1l1ll11ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳࡡ࡫ࡥࡸࡥࡵࡳ࡮ࠥሸ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        if not self.is_enabled():
            return
        bstack1111l1ll1l_opy_.bstack1111ll1l1l_opy_((bstack1111l1llll_opy_.bstack111l11111l_opy_, bstack111l111111_opy_.PRE), self.bstack1l1lll111l1_opy_)
        TestFramework.bstack1111ll1l1l_opy_((bstack111111lll1_opy_.TEST, bstack11111111ll_opy_.PRE), self.bstack111111ll11_opy_)
        TestFramework.bstack1111ll1l1l_opy_((bstack111111lll1_opy_.TEST, bstack11111111ll_opy_.POST), self.bstack1lllllll1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack111111ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1ll1l1l11_opy_(instance, args)
        test_framework = f.bstack111l1111l1_opy_(instance, TestFramework.bstack1lll1lll1ll_opy_)
        if bstack11l1l1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧሹ") in instance.bstack1lll1llllll_opy_:
            platform_index = f.bstack111l1111l1_opy_(instance, TestFramework.bstack1111ll11l1_opy_)
            self.accessibility = self.bstack11l1l111ll_opy_(tags) and self.bstack111ll1l11_opy_(self.config[bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧሺ")][platform_index])
        else:
            bstack11111l111l_opy_ = f.bstack111l1111l1_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll11ll_opy_, [])
            if not bstack11111l111l_opy_:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣሻ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠨࠢሼ"))
                return
            if len(bstack11111l111l_opy_) > 1:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥሽ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠣࠤሾ"))
            bstack1111111ll1_opy_, bstack1l1ll1lll1l_opy_ = bstack11111l111l_opy_[0]
            driver = bstack1111111ll1_opy_()
            if not driver:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦሿ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠥࠦቀ"))
                return
            capabilities = f.bstack111l1111l1_opy_(bstack1l1ll1lll1l_opy_, bstack1111l1ll1l_opy_.bstack1l1lll1111l_opy_)
            if not capabilities:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦቁ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠧࠨቂ"))
                return
            self.accessibility = self.bstack11l1l111ll_opy_(tags) and self.bstack111ll1l11_opy_(capabilities[bstack11l1l1l_opy_ (u"࠭ࡡ࡭ࡹࡤࡽࡸࡓࡡࡵࡥ࡫ࠫቃ")])
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡴࡪࡲࡹࡱࡪࠠࡳࡷࡱࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡻࡧ࡬ࡶࡧࡀࠦቄ") + str(self.accessibility) + bstack11l1l1l_opy_ (u"ࠣࠤቅ"))
    def bstack1l1lll111l1_opy_(
        self,
        f: bstack1111l1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack1111lllll1_opy_, str],
        bstack111l11llll_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        bstack1l1lll1l1l_opy_ = datetime.now()
        self.bstack1l1ll1l11ll_opy_(f, exec, *args, **kwargs)
        instance, method_name = exec
        instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡪࡰ࡬ࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡩ࡯࡯ࡨ࡬࡫ࠧቆ"), datetime.now() - bstack1l1lll1l1l_opy_)
        if (
            not f.bstack1l1lll11l11_opy_(method_name)
            or f.bstack1l1ll1l1l1l_opy_(method_name, *args)
            or f.bstack1l1ll1l1lll_opy_(method_name, *args)
        ):
            return
        if not f.bstack111l1111l1_opy_(instance, bstack1ll1l11llll_opy_.bstack1l1ll1l1ll1_opy_, False):
            if not bstack1ll1l11llll_opy_.bstack1ll1llllll1_opy_:
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠥ࡟ࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࠨቇ") + str(f.platform_index) + bstack11l1l1l_opy_ (u"ࠦࡢࠦࡡ࠲࠳ࡼࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣ࡬ࡦࡼࡥࠡࡰࡲࡸࠥࡨࡥࡦࡰࠣࡷࡪࡺࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡶࡩࡸࡹࡩࡰࡰࠥቈ"))
                bstack1ll1l11llll_opy_.bstack1ll1llllll1_opy_ = True
            return
        bstack1l1ll11lll1_opy_ = self.scripts.get(f.framework_name, {})
        if not bstack1l1ll11lll1_opy_:
            platform_index = f.bstack111l1111l1_opy_(instance, bstack1111l1ll1l_opy_.bstack1111ll11l1_opy_, 0)
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡴ࡯ࠡࡣ࠴࠵ࡾࠦࡳࡤࡴ࡬ࡴࡹࡹࠠࡧࡱࡵࠤࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࢁࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥ቉") + str(f.framework_name) + bstack11l1l1l_opy_ (u"ࠨࠢቊ"))
            return
        bstack1lll1111111_opy_ = f.bstack1ll1lll11ll_opy_(*args)
        if not bstack1lll1111111_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠢ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫ࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࠤቋ") + str(method_name) + bstack11l1l1l_opy_ (u"ࠣࠤቌ"))
            return
        bstack1l1ll11l1ll_opy_ = f.bstack111l1111l1_opy_(instance, bstack1ll1l11llll_opy_.bstack1l1ll11ll1l_opy_, False)
        if bstack1lll1111111_opy_ == bstack11l1l1l_opy_ (u"ࠤࡪࡩࡹࠨቍ") and not bstack1l1ll11l1ll_opy_:
            f.bstack1111l1l11l_opy_(instance, bstack1ll1l11llll_opy_.bstack1l1ll11ll1l_opy_, True)
        if not bstack1l1ll11l1ll_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡲࡴࠦࡕࡓࡎࠣࡰࡴࡧࡤࡦࡦࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥ࠾ࠤ቎") + str(bstack1lll1111111_opy_) + bstack11l1l1l_opy_ (u"ࠦࠧ቏"))
            return
        scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(bstack1lll1111111_opy_, [])
        if not scripts_to_run:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡴ࡯ࠡࡣ࠴࠵ࡾࠦࡳࡤࡴ࡬ࡴࡹࡹࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦ࠿ࠥቐ") + str(bstack1lll1111111_opy_) + bstack11l1l1l_opy_ (u"ࠨࠢቑ"))
            return
        self.logger.info(bstack11l1l1l_opy_ (u"ࠢࡳࡷࡱࡲ࡮ࡴࡧࠡࡽ࡯ࡩࡳ࠮ࡳࡤࡴ࡬ࡴࡹࡹ࡟ࡵࡱࡢࡶࡺࡴࠩࡾࠢࡶࡧࡷ࡯ࡰࡵࡵࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥ࠾ࠤቒ") + str(bstack1lll1111111_opy_) + bstack11l1l1l_opy_ (u"ࠣࠤቓ"))
        scripts = [(s, bstack1l1ll11lll1_opy_[s]) for s in scripts_to_run if s in bstack1l1ll11lll1_opy_]
        for bstack1l1lll111ll_opy_, bstack1l1ll11llll_opy_ in scripts:
            try:
                bstack1l1lll1l1l_opy_ = datetime.now()
                if bstack1l1lll111ll_opy_ == bstack11l1l1l_opy_ (u"ࠤࡶࡧࡦࡴࠢቔ"):
                    result = self.perform_scan(driver, method=bstack1lll1111111_opy_, framework_name=f.framework_name)
                instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࠤቕ") + bstack1l1lll111ll_opy_, datetime.now() - bstack1l1lll1l1l_opy_)
                if isinstance(result, dict) and not result.get(bstack11l1l1l_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷࠧቖ"), True):
                    self.logger.warning(bstack11l1l1l_opy_ (u"ࠧࡹ࡫ࡪࡲࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡲ࡬ࠦࡲࡦ࡯ࡤ࡭ࡳ࡯࡮ࡨࠢࡶࡧࡷ࡯ࡰࡵࡵ࠽ࠤࠧ቗") + str(result) + bstack11l1l1l_opy_ (u"ࠨࠢቘ"))
                    break
            except Exception as e:
                self.logger.error(bstack11l1l1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠦࡥࡹࡧࡦࡹࡹ࡯࡮ࡨࠢࡶࡧࡷ࡯ࡰࡵ࠿ࡾࡷࡨࡸࡩࡱࡶࡢࡲࡦࡳࡥࡾࠢࡨࡶࡷࡵࡲ࠾ࠤ቙") + str(e) + bstack11l1l1l_opy_ (u"ࠣࠤቚ"))
    def bstack1lllllll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
        *args,
        **kwargs,
    ):
        if not self.accessibility:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨቛ"))
            return
        bstack11111l111l_opy_ = f.bstack111l1111l1_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll11ll_opy_, [])
        if not bstack11111l111l_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧቜ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠦࠧቝ"))
            return
        if len(bstack11111l111l_opy_) > 1:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢ቞") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠨࠢ቟"))
        bstack1111111ll1_opy_, bstack1l1ll1lll1l_opy_ = bstack11111l111l_opy_[0]
        driver = bstack1111111ll1_opy_()
        if not driver:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣበ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠣࠤቡ"))
            return
        test_name = f.bstack111l1111l1_opy_(instance, TestFramework.bstack1lll1ll1111_opy_)
        if not test_name:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢቢ"))
            return
        test_uuid = f.bstack111l1111l1_opy_(instance, TestFramework.bstack1lll1ll1ll1_opy_)
        if not test_uuid:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡹࡺ࡯ࡤࠣባ"))
            return
        return self.bstack1111l1l1_opy_(driver, test_name, bstack1l1ll1lll1l_opy_.framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        if not self.accessibility:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࠧቤ"))
            return
        bstack1l1lll1l1l_opy_ = datetime.now()
        bstack1l1ll11llll_opy_ = self.scripts.get(framework_name, {}).get(bstack11l1l1l_opy_ (u"ࠧࡹࡣࡢࡰࠥብ"), None)
        if not bstack1l1ll11llll_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡵࡦࡥࡳ࠭ࠠࡴࡥࡵ࡭ࡵࡺࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨቦ") + str(framework_name) + bstack11l1l1l_opy_ (u"ࠢࠡࠤቧ"))
            return
        instance = bstack1lllll1l1l1_opy_.bstack1lll11l1ll1_opy_(driver)
        if instance:
            if not bstack1lllll1l1l1_opy_.bstack111l1111l1_opy_(instance, bstack1ll1l11llll_opy_.bstack1l1ll1ll111_opy_, False):
                bstack1lllll1l1l1_opy_.bstack1111l1l11l_opy_(instance, bstack1ll1l11llll_opy_.bstack1l1ll1ll111_opy_, True)
            else:
                self.logger.info(bstack11l1l1l_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡬ࡲࠥࡶࡲࡰࡩࡵࡩࡸࡹࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡲ࡫ࡴࡩࡱࡧࡁࠧቨ") + str(method) + bstack11l1l1l_opy_ (u"ࠤࠥቩ"))
                return
        self.logger.info(bstack11l1l1l_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࠽ࠣቪ") + str(method) + bstack11l1l1l_opy_ (u"ࠦࠧቫ"))
        result = driver.execute_async_script(bstack1l1ll11llll_opy_, {bstack11l1l1l_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧቬ"): method if method else bstack11l1l1l_opy_ (u"ࠨࠢቭ")})
        if instance:
            bstack1lllll1l1l1_opy_.bstack1111l1l11l_opy_(instance, bstack1ll1l11llll_opy_.bstack1l1ll1ll111_opy_, False)
            instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿ࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱࠦቮ"), datetime.now() - bstack1l1lll1l1l_opy_)
        return result
    @measure(event_name=EVENTS.bstack1111l1111_opy_, stage=STAGE.SINGLE)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠣࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࡸࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠥቯ"))
            return
        bstack1l1ll11llll_opy_ = self.scripts.get(framework_name, {}).get(bstack11l1l1l_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨተ"), None)
        if not bstack1l1ll11llll_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤቱ") + str(framework_name) + bstack11l1l1l_opy_ (u"ࠦࠧቲ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l1lll1l1l_opy_ = datetime.now()
        result = driver.execute_async_script(bstack1l1ll11llll_opy_)
        instance = bstack1lllll1l1l1_opy_.bstack1lll11l1ll1_opy_(driver)
        if instance:
            instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳࠣታ"), datetime.now() - bstack1l1lll1l1l_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111111ll_opy_, stage=STAGE.SINGLE)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶࡣࡸࡻ࡭࡮ࡣࡵࡽ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠤቴ"))
            return
        bstack1l1ll11llll_opy_ = self.scripts.get(framework_name, {}).get(bstack11l1l1l_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠦት"), None)
        if not bstack1l1ll11llll_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢቶ") + str(framework_name) + bstack11l1l1l_opy_ (u"ࠤࠥቷ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l1lll1l1l_opy_ = datetime.now()
        result = driver.execute_async_script(bstack1l1ll11llll_opy_)
        instance = bstack1lllll1l1l1_opy_.bstack1lll11l1ll1_opy_(driver)
        if instance:
            instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࡸࡥࡳࡶ࡯ࡰࡥࡷࡿࠢቸ"), datetime.now() - bstack1l1lll1l1l_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l1ll1ll11l_opy_, stage=STAGE.SINGLE)
    def bstack1l1ll11l1l1_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1111l11l1l_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1111l11ll1_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨቹ") + str(r) + bstack11l1l1l_opy_ (u"ࠧࠨቺ"))
            else:
                self.bstack1l1ll11l111_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦቻ") + str(e) + bstack11l1l1l_opy_ (u"ࠢࠣቼ"))
            traceback.print_exc()
            raise e
    def bstack1l1ll11l111_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠣ࡮ࡲࡥࡩࡥࡣࡰࡰࡩ࡭࡬ࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣች"))
            return False
        if result.accessibility.options:
            options = result.accessibility.options
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l1ll1lll11_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l1ll1l11l1_opy_ and command.module == self.bstack1l1ll1llll1_opy_:
                        if command.method and not command.method in bstack1l1ll1lll11_opy_:
                            bstack1l1ll1lll11_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l1ll1lll11_opy_[command.method]:
                            bstack1l1ll1lll11_opy_[command.method][command.name] = list()
                        bstack1l1ll1lll11_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l1ll1lll11_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l1ll1l11ll_opy_(
        self,
        f: bstack1111l1ll1l_opy_,
        exec: Tuple[bstack1111lllll1_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if bstack1lllll1l1l1_opy_.bstack1111ll111l_opy_(instance, bstack1ll1l11llll_opy_.bstack1l1ll1l1ll1_opy_):
            return
        if not f.bstack11111l1ll1_opy_(instance):
            if not bstack1ll1l11llll_opy_.bstack1ll1llllll1_opy_:
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠤࡤ࠵࠶ࡿࠠࡧ࡮ࡲࡻࠥࡪࡩࡴࡣࡥࡰࡪࡪࠠࡧࡱࡵࠤࡳࡵ࡮࠮ࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡪࡰࡩࡶࡦࠨቾ"))
                bstack1ll1l11llll_opy_.bstack1ll1llllll1_opy_ = True
            return
        if f.bstack111l11l1ll_opy_(method_name, *args):
            bstack1l1ll1l1111_opy_ = False
            desired_capabilities = f.bstack1l1lll11111_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1ll1l111l_opy_(instance)
                platform_index = f.bstack111l1111l1_opy_(instance, bstack1111l1ll1l_opy_.bstack1111ll11l1_opy_, 0)
                bstack1l1ll1ll1l1_opy_ = datetime.now()
                r = self.bstack1l1ll11l1l1_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡥࡲࡲ࡫࡯ࡧࠣቿ"), datetime.now() - bstack1l1ll1ll1l1_opy_)
                bstack1l1ll1l1111_opy_ = r.success
            else:
                self.logger.error(bstack11l1l1l_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡪࡥࡴ࡫ࡵࡩࡩࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࡂࠨኀ") + str(desired_capabilities) + bstack11l1l1l_opy_ (u"ࠧࠨኁ"))
            f.bstack1111l1l11l_opy_(instance, bstack1ll1l11llll_opy_.bstack1l1ll1l1ll1_opy_, bstack1l1ll1l1111_opy_)
    def bstack11l1l111ll_opy_(self, test_tags):
        bstack1l1ll11l1l1_opy_ = self.config.get(bstack11l1l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ኂ"))
        if not bstack1l1ll11l1l1_opy_:
            return True
        try:
            include_tags = bstack1l1ll11l1l1_opy_[bstack11l1l1l_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬኃ")] if bstack11l1l1l_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ኄ") in bstack1l1ll11l1l1_opy_ and isinstance(bstack1l1ll11l1l1_opy_[bstack11l1l1l_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧኅ")], list) else []
            exclude_tags = bstack1l1ll11l1l1_opy_[bstack11l1l1l_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨኆ")] if bstack11l1l1l_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩኇ") in bstack1l1ll11l1l1_opy_ and isinstance(bstack1l1ll11l1l1_opy_[bstack11l1l1l_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪኈ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡻࡧ࡬ࡪࡦࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡥࡳࡴࡩ࡯ࡩ࠱ࠤࡊࡸࡲࡰࡴࠣ࠾ࠥࠨ኉") + str(error))
        return False
    def bstack111ll1l11_opy_(self, caps):
        try:
            bstack1l1ll1ll1ll_opy_ = caps.get(bstack11l1l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨኊ"), {}).get(bstack11l1l1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬኋ"), caps.get(bstack11l1l1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩኌ"), bstack11l1l1l_opy_ (u"ࠪࠫኍ")))
            if bstack1l1ll1ll1ll_opy_:
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡉ࡫ࡳ࡬ࡶࡲࡴࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣ኎"))
                return False
            browser = caps.get(bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ኏"), bstack11l1l1l_opy_ (u"࠭ࠧነ")).lower()
            if browser != bstack11l1l1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧኑ"):
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦኒ"))
                return False
            browser_version = caps.get(bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪና"))
            if browser_version and browser_version != bstack11l1l1l_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪኔ") and int(browser_version.split(bstack11l1l1l_opy_ (u"ࠫ࠳࠭ን"))[0]) <= 98:
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦ࠹࠹࠰ࠥኖ"))
                return False
            bstack1l1ll11l11l_opy_ = caps.get(bstack11l1l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧኗ"), {}).get(bstack11l1l1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧኘ"))
            if bstack1l1ll11l11l_opy_ and bstack11l1l1l_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬኙ") in bstack1l1ll11l11l_opy_.get(bstack11l1l1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧኚ"), []):
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧኛ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨኜ") + str(error))
            return False
    def bstack1111l1l1_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        try:
            bstack1l1ll1lllll_opy_ = {
                bstack11l1l1l_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬኝ"): test_uuid,
                bstack11l1l1l_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫኞ"): os.environ.get(bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬኟ"), bstack11l1l1l_opy_ (u"ࠨࠩአ")),
                bstack11l1l1l_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ࠭ኡ"): os.environ.get(bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧኢ"), bstack11l1l1l_opy_ (u"ࠫࠬኣ"))
            }
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡣࡹ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨኤ") + str(bstack1l1ll1lllll_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            bstack1l1ll11llll_opy_ = self.scripts.get(framework_name, {}).get(bstack11l1l1l_opy_ (u"ࠨࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠦእ"), None)
            if not bstack1l1ll11llll_opy_:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢኦ") + str(framework_name) + bstack11l1l1l_opy_ (u"ࠣࠢࠥኧ"))
                return
            self.logger.debug(driver.execute_async_script(bstack1l1ll11llll_opy_, bstack1l1ll1lllll_opy_))
            self.logger.info(bstack11l1l1l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠧከ"))
        except Exception as bstack1l1ll11ll11_opy_:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧ࠽ࠤࠧኩ") + bstack11l1l1l_opy_ (u"ࠦࡸࡺࡲࠩࡲࡤࡸ࡭࠯ࠢኪ") + bstack11l1l1l_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢካ") + str(bstack1l1ll11ll11_opy_))
    def _1l1ll1l1l11_opy_(self, instance: bstack1lllllll1l1_opy_, args: Tuple) -> list:
        bstack11l1l1l_opy_ (u"ࠨࠢࠣࡇࡻࡸࡷࡧࡣࡵࠢࡷࡥ࡬ࡹࠠࡣࡣࡶࡩࡩࠦ࡯࡯ࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࠣࠤࠥኬ")
        if bstack11l1l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫክ") in instance.bstack1lll1llllll_opy_:
            return args[2].tags if hasattr(args[2], bstack11l1l1l_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ኮ")) else []
        if hasattr(args[0], bstack11l1l1l_opy_ (u"ࠩࡲࡻࡳࡥ࡭ࡢࡴ࡮ࡩࡷࡹࠧኯ")):
            return [marker.name for marker in args[0].own_markers]
        return []