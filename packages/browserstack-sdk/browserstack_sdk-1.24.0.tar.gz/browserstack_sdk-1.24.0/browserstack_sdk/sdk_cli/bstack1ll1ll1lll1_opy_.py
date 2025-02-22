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
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1lllll11l1l_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack111111lll1_opy_,
    bstack1lllllll1l1_opy_,
    bstack11111111ll_opy_,
    bstack1lll1l11l1l_opy_,
    bstack1lll1l1l1l1_opy_,
)
import traceback
from bstack_utils.bstack1l1l1ll1_opy_ import bstack1l1ll11l_opy_
class bstack1ll11l11l11_opy_(TestFramework):
    bstack1lll1111l1l_opy_ = bstack11l1l1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦጽ")
    bstack1lll1l1111l_opy_ = bstack11l1l1l_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࠥጾ")
    bstack1llll1l1l11_opy_ = bstack11l1l1l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧጿ")
    bstack1lll1lll111_opy_ = bstack11l1l1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡰࡦࡹࡴࡠࡵࡷࡥࡷࡺࡥࡥࠤፀ")
    bstack1lll11ll1ll_opy_ = bstack11l1l1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡱࡧࡳࡵࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࠦፁ")
    bstack1llll111111_opy_: bool
    bstack1lll1lll11l_opy_ = [
        bstack111111lll1_opy_.BEFORE_ALL,
        bstack111111lll1_opy_.AFTER_ALL,
        bstack111111lll1_opy_.BEFORE_EACH,
        bstack111111lll1_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1llll1l1lll_opy_: Dict[str, str],
        bstack1lll1llllll_opy_: List[str]=[bstack11l1l1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤፂ")],
    ):
        super().__init__(bstack1lll1llllll_opy_, bstack1llll1l1lll_opy_)
        self.bstack1llll111111_opy_ = any(bstack11l1l1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥፃ") in item.lower() for item in bstack1lll1llllll_opy_)
    def track_event(
        self,
        context: bstack1lll1l11l1l_opy_,
        test_framework_state: bstack111111lll1_opy_,
        test_hook_state: bstack11111111ll_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack111111lll1_opy_.NONE:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨࡨࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࠠࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࠧፄ") + str(test_hook_state) + bstack11l1l1l_opy_ (u"ࠧࠨፅ"))
            return
        if not self.bstack1llll111111_opy_:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡴࡷࡳࡴࡴࡸࡴࡦࡦࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡃࠢፆ") + str(str(self.bstack1lll1llllll_opy_)) + bstack11l1l1l_opy_ (u"ࠢࠣፇ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥፈ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠤࠥፉ"))
            return
        instance = self.__1lll1llll11_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡥࡷ࡭ࡳ࠾ࠤፊ") + str(args) + bstack11l1l1l_opy_ (u"ࠦࠧፋ"))
            return
        try:
            if not TestFramework.bstack1111ll111l_opy_(instance, TestFramework.bstack1lll1l111l1_opy_) and test_hook_state == bstack11111111ll_opy_.PRE:
                test = bstack1ll11l11l11_opy_.__1lll1l11111_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡲ࡯ࡢࡦࡨࡨࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧፌ") + str(test_hook_state) + bstack11l1l1l_opy_ (u"ࠨࠢፍ"))
            if test_framework_state == bstack111111lll1_opy_.TEST:
                if test_hook_state == bstack11111111ll_opy_.PRE and not TestFramework.bstack1111ll111l_opy_(instance, TestFramework.bstack1lll11llll1_opy_):
                    TestFramework.bstack1111l1l11l_opy_(instance, TestFramework.bstack1lll11llll1_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡴࡧࡷࠤࡹ࡫ࡳࡵ࠯ࡶࡸࡦࡸࡴࠡࡨࡲࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧፎ") + str(test_hook_state) + bstack11l1l1l_opy_ (u"ࠣࠤፏ"))
                elif test_hook_state == bstack11111111ll_opy_.POST and not TestFramework.bstack1111ll111l_opy_(instance, TestFramework.bstack1llll11ll11_opy_):
                    TestFramework.bstack1111l1l11l_opy_(instance, TestFramework.bstack1llll11ll11_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l1l1l_opy_ (u"ࠤࡶࡩࡹࠦࡴࡦࡵࡷ࠱ࡪࡴࡤࠡࡨࡲࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧፐ") + str(test_hook_state) + bstack11l1l1l_opy_ (u"ࠥࠦፑ"))
            elif test_framework_state == bstack111111lll1_opy_.LOG and test_hook_state == bstack11111111ll_opy_.POST:
                bstack1ll11l11l11_opy_.__1lll111lll1_opy_(instance, *args)
            elif test_framework_state == bstack111111lll1_opy_.LOG_REPORT and test_hook_state == bstack11111111ll_opy_.POST:
                self.__1lll1l1llll_opy_(instance, *args)
            elif test_framework_state in bstack1ll11l11l11_opy_.bstack1lll1lll11l_opy_:
                self.__1lll1llll1l_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧፒ") + str(instance.ref()) + bstack11l1l1l_opy_ (u"ࠧࠨፓ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1lll1l11l11_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
    def bstack1lll11l1111_opy_(self):
        return self.bstack1llll111111_opy_
    def __1lll11ll111_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11l1l1l_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡹࡵ࡭ࡶࠥፔ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1lll1ll1lll_opy_(rep, [bstack11l1l1l_opy_ (u"ࠢࡸࡪࡨࡲࠧፕ"), bstack11l1l1l_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤፖ"), bstack11l1l1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤፗ"), bstack11l1l1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥፘ"), bstack11l1l1l_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠧፙ"), bstack11l1l1l_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦፚ")])
        return None
    def __1lll1l1llll_opy_(self, instance: bstack1lllllll1l1_opy_, *args):
        result = self.__1lll11ll111_opy_(*args)
        if not result:
            return
        failure = None
        bstack111l1ll111_opy_ = None
        if result.get(bstack11l1l1l_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢ፛"), None) == bstack11l1l1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ፜") and len(args) > 1 and getattr(args[1], bstack11l1l1l_opy_ (u"ࠣࡧࡻࡧ࡮ࡴࡦࡰࠤ፝"), None) is not None:
            failure = [{bstack11l1l1l_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬ፞"): [args[1].excinfo.exconly(), result.get(bstack11l1l1l_opy_ (u"ࠥࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠤ፟"), None)]}]
            bstack111l1ll111_opy_ = bstack11l1l1l_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧ፠") if bstack11l1l1l_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣ፡") in getattr(args[1].excinfo, bstack11l1l1l_opy_ (u"ࠨࡴࡺࡲࡨࡲࡦࡳࡥࠣ።"), bstack11l1l1l_opy_ (u"ࠢࠣ፣")) else bstack11l1l1l_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤ፤")
        bstack1llll1l1l1l_opy_ = result.get(bstack11l1l1l_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥ፥"), TestFramework.bstack1lll11ll1l1_opy_)
        if bstack1llll1l1l1l_opy_ != TestFramework.bstack1lll11ll1l1_opy_:
            TestFramework.bstack1111l1l11l_opy_(instance, TestFramework.bstack1lll1l111ll_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1lll1l1ll1l_opy_(instance, {
            TestFramework.bstack111111l11l_opy_: failure,
            TestFramework.bstack1lll111ll1l_opy_: bstack111l1ll111_opy_,
            TestFramework.bstack1111111111_opy_: bstack1llll1l1l1l_opy_,
        })
    def __1lll1llll11_opy_(
        self,
        context: bstack1lll1l11l1l_opy_,
        test_framework_state: bstack111111lll1_opy_,
        test_hook_state: bstack11111111ll_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack111111lll1_opy_.SETUP_FIXTURE:
            instance = self.__1lll11l11l1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1llll1ll11l_opy_ bstack1lll111ll11_opy_ this to be bstack11l1l1l_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥ፦")
            if test_framework_state == bstack111111lll1_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1lll111l11l_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack111111lll1_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11l1l1l_opy_ (u"ࠦࡳࡵࡤࡦࠤ፧"), None), bstack11l1l1l_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧ፨"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11l1l1l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨ፩"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1lll11l1ll1_opy_(target) if target else None
        return instance
    def __1lll1llll1l_opy_(
        self,
        instance: bstack1lllllll1l1_opy_,
        test_framework_state: bstack111111lll1_opy_,
        test_hook_state: bstack11111111ll_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1lll111llll_opy_ = TestFramework.bstack111l1111l1_opy_(instance, bstack1ll11l11l11_opy_.bstack1lll1l1111l_opy_, {})
        if not key in bstack1lll111llll_opy_:
            bstack1lll111llll_opy_[key] = []
        bstack1llll11l1l1_opy_ = TestFramework.bstack111l1111l1_opy_(instance, bstack1ll11l11l11_opy_.bstack1llll1l1l11_opy_, {})
        if not key in bstack1llll11l1l1_opy_:
            bstack1llll11l1l1_opy_[key] = []
        bstack1lll111l1ll_opy_ = {
            bstack1ll11l11l11_opy_.bstack1lll1l1111l_opy_: bstack1lll111llll_opy_,
            bstack1ll11l11l11_opy_.bstack1llll1l1l11_opy_: bstack1llll11l1l1_opy_,
        }
        if test_hook_state == bstack11111111ll_opy_.PRE:
            hook = {
                bstack11l1l1l_opy_ (u"ࠢ࡬ࡧࡼࠦ፪"): key,
                TestFramework.bstack1llll11l1ll_opy_: uuid4().__str__(),
                TestFramework.bstack1llll111l1l_opy_: TestFramework.bstack1lll11lllll_opy_,
                TestFramework.bstack1lll111l111_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1llll1l11ll_opy_: [],
                TestFramework.bstack1llll1l1ll1_opy_: args[1] if len(args) > 1 else bstack11l1l1l_opy_ (u"ࠨࠩ፫")
            }
            bstack1lll111llll_opy_[key].append(hook)
            bstack1lll111l1ll_opy_[bstack1ll11l11l11_opy_.bstack1lll1lll111_opy_] = key
        elif test_hook_state == bstack11111111ll_opy_.POST:
            bstack1lll11l11ll_opy_ = bstack1lll111llll_opy_.get(key, [])
            hook = bstack1lll11l11ll_opy_.pop() if bstack1lll11l11ll_opy_ else None
            if hook:
                result = self.__1lll11ll111_opy_(*args)
                if result:
                    bstack1llll111ll1_opy_ = result.get(bstack11l1l1l_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥ፬"), TestFramework.bstack1lll11lllll_opy_)
                    if bstack1llll111ll1_opy_ != TestFramework.bstack1lll11lllll_opy_:
                        hook[TestFramework.bstack1llll111l1l_opy_] = bstack1llll111ll1_opy_
                hook[TestFramework.bstack1lll1111ll1_opy_] = datetime.now(tz=timezone.utc)
                bstack1llll11l1l1_opy_[key].append(hook)
                bstack1lll111l1ll_opy_[bstack1ll11l11l11_opy_.bstack1lll11ll1ll_opy_] = key
        TestFramework.bstack1lll1l1ll1l_opy_(instance, bstack1lll111l1ll_opy_)
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡ࡫ࡳࡴࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾ࡯ࡪࡿࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࡂࢁࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࢃࠠࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤ࠾ࠤ፭") + str(bstack1llll11l1l1_opy_) + bstack11l1l1l_opy_ (u"ࠦࠧ፮"))
    def __1lll11l11l1_opy_(
        self,
        context: bstack1lll1l11l1l_opy_,
        test_framework_state: bstack111111lll1_opy_,
        test_hook_state: bstack11111111ll_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1lll1ll1lll_opy_(args[0], [bstack11l1l1l_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦ፯"), bstack11l1l1l_opy_ (u"ࠨࡡࡳࡩࡱࡥࡲ࡫ࠢ፰"), bstack11l1l1l_opy_ (u"ࠢࡱࡣࡵࡥࡲࡹࠢ፱"), bstack11l1l1l_opy_ (u"ࠣ࡫ࡧࡷࠧ፲"), bstack11l1l1l_opy_ (u"ࠤࡸࡲ࡮ࡺࡴࡦࡵࡷࠦ፳"), bstack11l1l1l_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥ፴")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack11l1l1l_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥ፵")) else fixturedef.get(bstack11l1l1l_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦ፶"), None)
        fixturename = request.fixturename if hasattr(request, bstack11l1l1l_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࠦ፷")) else None
        node = request.node if hasattr(request, bstack11l1l1l_opy_ (u"ࠢ࡯ࡱࡧࡩࠧ፸")) else None
        target = request.node.nodeid if hasattr(node, bstack11l1l1l_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣ፹")) else None
        baseid = fixturedef.get(bstack11l1l1l_opy_ (u"ࠤࡥࡥࡸ࡫ࡩࡥࠤ፺"), None) or bstack11l1l1l_opy_ (u"ࠥࠦ፻")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11l1l1l_opy_ (u"ࠦࡤࡶࡹࡧࡷࡱࡧ࡮ࡺࡥ࡮ࠤ፼")):
            target = bstack1ll11l11l11_opy_.__1lll1111lll_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11l1l1l_opy_ (u"ࠧࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢ፽")) else None
            if target and not TestFramework.bstack1lll11l1ll1_opy_(target):
                self.__1lll111l11l_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡰࡲࡨࡪࡃࡻ࡯ࡱࡧࡩࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣ፾") + str(test_hook_state) + bstack11l1l1l_opy_ (u"ࠢࠣ፿"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࡃࡻࡧ࡫ࡻࡸࡺࡸࡥࡥࡧࡩࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨᎀ") + str(target) + bstack11l1l1l_opy_ (u"ࠤࠥᎁ"))
            return None
        instance = TestFramework.bstack1lll11l1ll1_opy_(target)
        if not instance:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡥࡥࡸ࡫ࡩࡥ࠿ࡾࡦࡦࡹࡥࡪࡦࢀࠤࡹࡧࡲࡨࡧࡷࡁࠧᎂ") + str(target) + bstack11l1l1l_opy_ (u"ࠦࠧᎃ"))
            return None
        bstack1lll1l1ll11_opy_ = TestFramework.bstack111l1111l1_opy_(instance, bstack1ll11l11l11_opy_.bstack1lll1111l1l_opy_, {})
        if os.getenv(bstack11l1l1l_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡋࡏࡘࡕࡗࡕࡉࡘࠨᎄ"), bstack11l1l1l_opy_ (u"ࠨ࠱ࠣᎅ")) == bstack11l1l1l_opy_ (u"ࠢ࠲ࠤᎆ"):
            bstack1lll1ll11ll_opy_ = bstack11l1l1l_opy_ (u"ࠣ࠼ࠥᎇ").join((scope, fixturename))
            bstack1lll11lll1l_opy_ = datetime.now(tz=timezone.utc)
            bstack1llll1ll1l1_opy_ = {
                bstack11l1l1l_opy_ (u"ࠤ࡮ࡩࡾࠨᎈ"): bstack1lll1ll11ll_opy_,
                bstack11l1l1l_opy_ (u"ࠥࡸࡦ࡭ࡳࠣᎉ"): bstack1ll11l11l11_opy_.__1llll1l1111_opy_(request.node),
                bstack11l1l1l_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩࠧᎊ"): fixturedef,
                bstack11l1l1l_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᎋ"): scope,
                bstack11l1l1l_opy_ (u"ࠨࡴࡺࡲࡨࠦᎌ"): None,
            }
            try:
                if test_hook_state == bstack11111111ll_opy_.POST and callable(getattr(args[-1], bstack11l1l1l_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦᎍ"), None)):
                    bstack1llll1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠣࡶࡼࡴࡪࠨᎎ")] = TestFramework.bstack1lll11l1l1l_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack11111111ll_opy_.PRE:
                bstack1llll1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠤࡸࡹ࡮ࡪࠢᎏ")] = uuid4().__str__()
                bstack1llll1ll1l1_opy_[bstack1ll11l11l11_opy_.bstack1lll111l111_opy_] = bstack1lll11lll1l_opy_
            elif test_hook_state == bstack11111111ll_opy_.POST:
                bstack1llll1ll1l1_opy_[bstack1ll11l11l11_opy_.bstack1lll1111ll1_opy_] = bstack1lll11lll1l_opy_
            if bstack1lll1ll11ll_opy_ in bstack1lll1l1ll11_opy_:
                bstack1lll1l1ll11_opy_[bstack1lll1ll11ll_opy_].update(bstack1llll1ll1l1_opy_)
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡹࡵࡪࡡࡵࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࠦ᎐") + str(bstack1lll1l1ll11_opy_[bstack1lll1ll11ll_opy_]) + bstack11l1l1l_opy_ (u"ࠦࠧ᎑"))
            else:
                bstack1lll1l1ll11_opy_[bstack1lll1ll11ll_opy_] = bstack1llll1ll1l1_opy_
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࡿࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࢀࠤࡹࡸࡡࡤ࡭ࡨࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࡹ࠽ࠣ᎒") + str(len(bstack1lll1l1ll11_opy_)) + bstack11l1l1l_opy_ (u"ࠨࠢ᎓"))
        TestFramework.bstack1111l1l11l_opy_(instance, bstack1ll11l11l11_opy_.bstack1lll1111l1l_opy_, bstack1lll1l1ll11_opy_)
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࡽ࡯ࡩࡳ࠮ࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠫࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢ᎔") + str(instance.ref()) + bstack11l1l1l_opy_ (u"ࠣࠤ᎕"))
        return instance
    def __1lll111l11l_opy_(
        self,
        context: bstack1lll1l11l1l_opy_,
        test_framework_state: bstack111111lll1_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1lllll11l1l_opy_.create_context(target)
        ob = bstack1lllllll1l1_opy_(ctx, self.bstack1lll1llllll_opy_, self.bstack1llll1l1lll_opy_, test_framework_state)
        TestFramework.bstack1lll1l1ll1l_opy_(ob, {
            TestFramework.bstack1lll1lll1ll_opy_: context.test_framework_name,
            TestFramework.bstack1lll1ll1l11_opy_: context.test_framework_version,
            TestFramework.bstack1llll1ll111_opy_: [],
            bstack1ll11l11l11_opy_.bstack1lll1111l1l_opy_: {},
            bstack1ll11l11l11_opy_.bstack1llll1l1l11_opy_: {},
            bstack1ll11l11l11_opy_.bstack1lll1l1111l_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1111l1l11l_opy_(ob, TestFramework.bstack1lll1l1lll1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1111l1l11l_opy_(ob, TestFramework.bstack1111ll11l1_opy_, context.platform_index)
        TestFramework.bstack1lll11ll11l_opy_[ctx.id] = ob
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡧࡹࡾ࠮ࡪࡦࡀࡿࡨࡺࡸ࠯࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤ᎖") + str(TestFramework.bstack1lll11ll11l_opy_.keys()) + bstack11l1l1l_opy_ (u"ࠥࠦ᎗"))
        return ob
    def bstack1llll1111ll_opy_(self, instance: bstack1lllllll1l1_opy_, bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_]):
        bstack1lll1lllll1_opy_ = (
            bstack1ll11l11l11_opy_.bstack1lll1lll111_opy_
            if bstack111l11llll_opy_[1] == bstack11111111ll_opy_.PRE
            else bstack1ll11l11l11_opy_.bstack1lll11ll1ll_opy_
        )
        hook = bstack1ll11l11l11_opy_.bstack1lll11l1lll_opy_(instance, bstack1lll1lllll1_opy_)
        entries = hook.get(TestFramework.bstack1llll1l11ll_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1llll1ll111_opy_, []))
        return entries
    def bstack1lll11l111l_opy_(self, instance: bstack1lllllll1l1_opy_, bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_]):
        bstack1lll1lllll1_opy_ = (
            bstack1ll11l11l11_opy_.bstack1lll1lll111_opy_
            if bstack111l11llll_opy_[1] == bstack11111111ll_opy_.PRE
            else bstack1ll11l11l11_opy_.bstack1lll11ll1ll_opy_
        )
        bstack1ll11l11l11_opy_.bstack1lll1l11ll1_opy_(instance, bstack1lll1lllll1_opy_)
        TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1llll1ll111_opy_, []).clear()
    @staticmethod
    def bstack1lll11l1lll_opy_(instance: bstack1lllllll1l1_opy_, bstack1lll1lllll1_opy_: str):
        bstack1lll1l1l11l_opy_ = (
            bstack1ll11l11l11_opy_.bstack1llll1l1l11_opy_
            if bstack1lll1lllll1_opy_ == bstack1ll11l11l11_opy_.bstack1lll11ll1ll_opy_
            else bstack1ll11l11l11_opy_.bstack1lll1l1111l_opy_
        )
        bstack1llll11l111_opy_ = TestFramework.bstack111l1111l1_opy_(instance, bstack1lll1lllll1_opy_, None)
        bstack1lll111l1l1_opy_ = TestFramework.bstack111l1111l1_opy_(instance, bstack1lll1l1l11l_opy_, None) if bstack1llll11l111_opy_ else None
        return (
            bstack1lll111l1l1_opy_[bstack1llll11l111_opy_][-1]
            if isinstance(bstack1lll111l1l1_opy_, dict) and len(bstack1lll111l1l1_opy_.get(bstack1llll11l111_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1lll1l11ll1_opy_(instance: bstack1lllllll1l1_opy_, bstack1lll1lllll1_opy_: str):
        hook = bstack1ll11l11l11_opy_.bstack1lll11l1lll_opy_(instance, bstack1lll1lllll1_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1llll1l11ll_opy_, []).clear()
    @staticmethod
    def __1lll111lll1_opy_(instance: bstack1lllllll1l1_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11l1l1l_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡧࡴࡸࡤࡴࠤ᎘"), None)):
            return
        if os.getenv(bstack11l1l1l_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡑࡕࡇࡔࠤ᎙"), bstack11l1l1l_opy_ (u"ࠨ࠱ࠣ᎚")) != bstack11l1l1l_opy_ (u"ࠢ࠲ࠤ᎛"):
            bstack1ll11l11l11_opy_.logger.warning(bstack11l1l1l_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡩ࡯ࡩࠣࡧࡦࡶ࡬ࡰࡩࠥ᎜"))
            return
        bstack1llll11ll1l_opy_ = {
            bstack11l1l1l_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣ᎝"): (bstack1ll11l11l11_opy_.bstack1lll1lll111_opy_, bstack1ll11l11l11_opy_.bstack1lll1l1111l_opy_),
            bstack11l1l1l_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧ᎞"): (bstack1ll11l11l11_opy_.bstack1lll11ll1ll_opy_, bstack1ll11l11l11_opy_.bstack1llll1l1l11_opy_),
        }
        for when in (bstack11l1l1l_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥ᎟"), bstack11l1l1l_opy_ (u"ࠧࡩࡡ࡭࡮ࠥᎠ"), bstack11l1l1l_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣᎡ")):
            bstack1llll11111l_opy_ = args[1].get_records(when)
            if not bstack1llll11111l_opy_:
                continue
            records = [
                bstack1lll1l1l1l1_opy_(
                    kind=TestFramework.bstack1llll111l11_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11l1l1l_opy_ (u"ࠢ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠥᎢ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11l1l1l_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡥࠤᎣ")) and r.created
                        else None
                    ),
                )
                for r in bstack1llll11111l_opy_
                if isinstance(getattr(r, bstack11l1l1l_opy_ (u"ࠤࡰࡩࡸࡹࡡࡨࡧࠥᎤ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1lll11l1l11_opy_, bstack1lll1l1l11l_opy_ = bstack1llll11ll1l_opy_.get(when, (None, None))
            bstack1llll111lll_opy_ = TestFramework.bstack111l1111l1_opy_(instance, bstack1lll11l1l11_opy_, None) if bstack1lll11l1l11_opy_ else None
            bstack1lll111l1l1_opy_ = TestFramework.bstack111l1111l1_opy_(instance, bstack1lll1l1l11l_opy_, None) if bstack1llll111lll_opy_ else None
            if isinstance(bstack1lll111l1l1_opy_, dict) and len(bstack1lll111l1l1_opy_.get(bstack1llll111lll_opy_, [])) > 0:
                hook = bstack1lll111l1l1_opy_[bstack1llll111lll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1llll1l11ll_opy_ in hook:
                    hook[TestFramework.bstack1llll1l11ll_opy_].extend(records)
                    continue
            logs = TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1llll1ll111_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1lll1l11111_opy_(test) -> Dict[str, Any]:
        test_id = bstack1ll11l11l11_opy_.__1lll1111lll_opy_(test.location) if hasattr(test, bstack11l1l1l_opy_ (u"ࠥࡰࡴࡩࡡࡵ࡫ࡲࡲࠧᎥ")) else getattr(test, bstack11l1l1l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᎦ"), None)
        test_name = test.name if hasattr(test, bstack11l1l1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᎧ")) else None
        bstack1llll11l11l_opy_ = test.fspath.strpath if hasattr(test, bstack11l1l1l_opy_ (u"ࠨࡦࡴࡲࡤࡸ࡭ࠨᎨ")) and test.fspath else None
        if not test_id or not test_name or not bstack1llll11l11l_opy_:
            return None
        code = None
        if hasattr(test, bstack11l1l1l_opy_ (u"ࠢࡰࡤ࡭ࠦᎩ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack1l1l11ll1l1_opy_ = []
        try:
            bstack1l1l11ll1l1_opy_ = bstack1l1ll11l_opy_.bstack1l1l11ll_opy_(test)
        except:
            bstack1ll11l11l11_opy_.logger.warning(bstack11l1l1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡷࡩࡸࡺࠠࡴࡥࡲࡴࡪࡹࠬࠡࡶࡨࡷࡹࠦࡳࡤࡱࡳࡩࡸࠦࡷࡪ࡮࡯ࠤࡧ࡫ࠠࡳࡧࡶࡳࡱࡼࡥࡥࠢ࡬ࡲࠥࡉࡌࡊࠤᎪ"))
        return {
            TestFramework.bstack1lll1ll1ll1_opy_: uuid4().__str__(),
            TestFramework.bstack1lll1l111l1_opy_: test_id,
            TestFramework.bstack1lll1ll1111_opy_: test_name,
            TestFramework.bstack1lll11lll11_opy_: getattr(test, bstack11l1l1l_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᎫ"), None),
            TestFramework.bstack1lll1ll11l1_opy_: bstack1llll11l11l_opy_,
            TestFramework.bstack1lll1lll1l1_opy_: bstack1ll11l11l11_opy_.__1llll1l1111_opy_(test),
            TestFramework.bstack1llll1l111l_opy_: code,
            TestFramework.bstack1111111111_opy_: TestFramework.bstack1lll11ll1l1_opy_,
            TestFramework.bstack11111l1lll_opy_: test_id,
            TestFramework.bstack1l1ll111l1l_opy_: bstack1l1l11ll1l1_opy_
        }
    @staticmethod
    def __1llll1l1111_opy_(test) -> List[str]:
        return (
            [getattr(f, bstack11l1l1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᎬ"), None) for f in test.own_markers if getattr(f, bstack11l1l1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᎭ"), None)]
            if isinstance(getattr(test, bstack11l1l1l_opy_ (u"ࠧࡵࡷ࡯ࡡࡰࡥࡷࡱࡥࡳࡵࠥᎮ"), None), list)
            else []
        )
    @staticmethod
    def __1lll1111lll_opy_(location):
        return bstack11l1l1l_opy_ (u"ࠨ࠺࠻ࠤᎯ").join(filter(lambda x: isinstance(x, str), location))