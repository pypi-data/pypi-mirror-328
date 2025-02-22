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
from pyexpat import features
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
class PytestBDDFramework(TestFramework):
    bstack1lll1111l1l_opy_ = bstack11l1l1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢၡ")
    bstack1lll1l1111l_opy_ = bstack11l1l1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࠨၢ")
    bstack1llll1l1l11_opy_ = bstack11l1l1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣၣ")
    bstack1lll1lll111_opy_ = bstack11l1l1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣࡸࡺࡡࡳࡶࡨࡨࠧၤ")
    bstack1lll11ll1ll_opy_ = bstack11l1l1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢၥ")
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
        bstack1lll1llllll_opy_: List[str]=[bstack11l1l1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤၦ")],
    ):
        super().__init__(bstack1lll1llllll_opy_, bstack1llll1l1lll_opy_)
        self.bstack1llll111111_opy_ = any(bstack11l1l1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥၧ") in item.lower() for item in bstack1lll1llllll_opy_)
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
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫ࡤࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࠣၨ") + str(test_hook_state) + bstack11l1l1l_opy_ (u"ࠣࠤၩ"))
            return
        if not self.bstack1llll111111_opy_:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠿ࠥၪ") + str(str(self.bstack1lll1llllll_opy_)) + bstack11l1l1l_opy_ (u"ࠥࠦၫ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨၬ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠧࠨၭ"))
            return
        instance = self.__1lll1llll11_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡡࡳࡩࡶࡁࠧၮ") + str(args) + bstack11l1l1l_opy_ (u"ࠢࠣၯ"))
            return
        try:
            if test_framework_state == bstack111111lll1_opy_.TEST:
                if not TestFramework.bstack1111ll111l_opy_(instance, TestFramework.bstack1lll1l111l1_opy_) and test_hook_state == bstack11111111ll_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1lll1l11111_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack11l1l1l_opy_ (u"ࠣ࡮ࡲࡥࡩ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣၰ") + str(test_hook_state) + bstack11l1l1l_opy_ (u"ࠤࠥၱ"))
                if test_hook_state == bstack11111111ll_opy_.PRE and not TestFramework.bstack1111ll111l_opy_(instance, TestFramework.bstack1lll11llll1_opy_):
                    TestFramework.bstack1111l1l11l_opy_(instance, TestFramework.bstack1lll11llll1_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1lll1l1l111_opy_(instance, args)
                    self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡷࡪࡺࠠࡵࡧࡶࡸ࠲ࡹࡴࡢࡴࡷࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣၲ") + str(test_hook_state) + bstack11l1l1l_opy_ (u"ࠦࠧၳ"))
                elif test_hook_state == bstack11111111ll_opy_.POST and not TestFramework.bstack1111ll111l_opy_(instance, TestFramework.bstack1llll11ll11_opy_):
                    TestFramework.bstack1111l1l11l_opy_(instance, TestFramework.bstack1llll11ll11_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡦࡰࡧࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣၴ") + str(test_hook_state) + bstack11l1l1l_opy_ (u"ࠨࠢၵ"))
            elif test_framework_state == bstack111111lll1_opy_.STEP:
                if test_hook_state == bstack11111111ll_opy_.PRE:
                    PytestBDDFramework.__1llll11lll1_opy_(instance, args)
                elif test_hook_state == bstack11111111ll_opy_.POST:
                    PytestBDDFramework.__1lll1l11lll_opy_(instance, args)
            elif test_framework_state == bstack111111lll1_opy_.LOG and test_hook_state == bstack11111111ll_opy_.POST:
                PytestBDDFramework.__1lll111lll1_opy_(instance, *args)
            elif test_framework_state == bstack111111lll1_opy_.LOG_REPORT and test_hook_state == bstack11111111ll_opy_.POST:
                self.__1lll1l1llll_opy_(instance, *args)
            elif test_framework_state in PytestBDDFramework.bstack1lll1lll11l_opy_:
                self.__1lll1llll1l_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣၶ") + str(instance.ref()) + bstack11l1l1l_opy_ (u"ࠣࠤၷ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1lll1l11l11_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
    def bstack1lll11l1111_opy_(self):
        return self.bstack1llll111111_opy_
    def __1lll11ll111_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11l1l1l_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨၸ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1lll1ll1lll_opy_(rep, [bstack11l1l1l_opy_ (u"ࠥࡻ࡭࡫࡮ࠣၹ"), bstack11l1l1l_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧၺ"), bstack11l1l1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧၻ"), bstack11l1l1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨၼ"), bstack11l1l1l_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠣၽ"), bstack11l1l1l_opy_ (u"ࠣ࡮ࡲࡲ࡬ࡸࡥࡱࡴࡷࡩࡽࡺࠢၾ")])
        return None
    def __1lll1l1llll_opy_(self, instance: bstack1lllllll1l1_opy_, *args):
        result = self.__1lll11ll111_opy_(*args)
        if not result:
            return
        failure = None
        bstack111l1ll111_opy_ = None
        if result.get(bstack11l1l1l_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥၿ"), None) == bstack11l1l1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥႀ") and len(args) > 1 and getattr(args[1], bstack11l1l1l_opy_ (u"ࠦࡪࡾࡣࡪࡰࡩࡳࠧႁ"), None) is not None:
            failure = [{bstack11l1l1l_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨႂ"): [args[1].excinfo.exconly(), result.get(bstack11l1l1l_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧႃ"), None)]}]
            bstack111l1ll111_opy_ = bstack11l1l1l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣႄ") if bstack11l1l1l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦႅ") in getattr(args[1].excinfo, bstack11l1l1l_opy_ (u"ࠤࡷࡽࡵ࡫࡮ࡢ࡯ࡨࠦႆ"), bstack11l1l1l_opy_ (u"ࠥࠦႇ")) else bstack11l1l1l_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧႈ")
        bstack1llll1l1l1l_opy_ = result.get(bstack11l1l1l_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨႉ"), TestFramework.bstack1lll11ll1l1_opy_)
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
            target = None # bstack1llll1ll11l_opy_ bstack1lll111ll11_opy_ this to be bstack11l1l1l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨႊ")
            if test_framework_state == bstack111111lll1_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1lll111l11l_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack111111lll1_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11l1l1l_opy_ (u"ࠢ࡯ࡱࡧࡩࠧႋ"), None), bstack11l1l1l_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣႌ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11l1l1l_opy_ (u"ࠤࡱࡳࡩ࡫ႍࠢ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack11l1l1l_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥႎ"), None):
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
        bstack1lll111llll_opy_ = TestFramework.bstack111l1111l1_opy_(instance, PytestBDDFramework.bstack1lll1l1111l_opy_, {})
        if not key in bstack1lll111llll_opy_:
            bstack1lll111llll_opy_[key] = []
        bstack1llll11l1l1_opy_ = TestFramework.bstack111l1111l1_opy_(instance, PytestBDDFramework.bstack1llll1l1l11_opy_, {})
        if not key in bstack1llll11l1l1_opy_:
            bstack1llll11l1l1_opy_[key] = []
        bstack1lll111l1ll_opy_ = {
            PytestBDDFramework.bstack1lll1l1111l_opy_: bstack1lll111llll_opy_,
            PytestBDDFramework.bstack1llll1l1l11_opy_: bstack1llll11l1l1_opy_,
        }
        if test_hook_state == bstack11111111ll_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack11l1l1l_opy_ (u"ࠦࡰ࡫ࡹࠣႏ"): key,
                TestFramework.bstack1llll11l1ll_opy_: uuid4().__str__(),
                TestFramework.bstack1llll111l1l_opy_: TestFramework.bstack1lll11lllll_opy_,
                TestFramework.bstack1lll111l111_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1llll1l11ll_opy_: [],
                TestFramework.bstack1llll1l1ll1_opy_: hook_name
            }
            bstack1lll111llll_opy_[key].append(hook)
            bstack1lll111l1ll_opy_[PytestBDDFramework.bstack1lll1lll111_opy_] = key
        elif test_hook_state == bstack11111111ll_opy_.POST:
            bstack1lll11l11ll_opy_ = bstack1lll111llll_opy_.get(key, [])
            hook = bstack1lll11l11ll_opy_.pop() if bstack1lll11l11ll_opy_ else None
            if hook:
                result = self.__1lll11ll111_opy_(*args)
                if result:
                    bstack1llll111ll1_opy_ = result.get(bstack11l1l1l_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨ႐"), TestFramework.bstack1lll11lllll_opy_)
                    if bstack1llll111ll1_opy_ != TestFramework.bstack1lll11lllll_opy_:
                        hook[TestFramework.bstack1llll111l1l_opy_] = bstack1llll111ll1_opy_
                hook[TestFramework.bstack1lll1111ll1_opy_] = datetime.now(tz=timezone.utc)
                bstack1llll11l1l1_opy_[key].append(hook)
                bstack1lll111l1ll_opy_[PytestBDDFramework.bstack1lll11ll1ll_opy_] = key
        TestFramework.bstack1lll1l1ll1l_opy_(instance, bstack1lll111l1ll_opy_)
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡮࡯ࡰ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࢁ࡫ࡦࡻࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤ࠾ࡽ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥࡿࠣ࡬ࡴࡵ࡫ࡴࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡁࠧ႑") + str(bstack1llll11l1l1_opy_) + bstack11l1l1l_opy_ (u"ࠢࠣ႒"))
    def __1lll11l11l1_opy_(
        self,
        context: bstack1lll1l11l1l_opy_,
        test_framework_state: bstack111111lll1_opy_,
        test_hook_state: bstack11111111ll_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1lll1ll1lll_opy_(args[0], [bstack11l1l1l_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢ႓"), bstack11l1l1l_opy_ (u"ࠤࡤࡶ࡬ࡴࡡ࡮ࡧࠥ႔"), bstack11l1l1l_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡵࠥ႕"), bstack11l1l1l_opy_ (u"ࠦ࡮ࡪࡳࠣ႖"), bstack11l1l1l_opy_ (u"ࠧࡻ࡮ࡪࡶࡷࡩࡸࡺࠢ႗"), bstack11l1l1l_opy_ (u"ࠨࡢࡢࡵࡨ࡭ࡩࠨ႘")]) if len(args) > 0 else {}
        request = args[0] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack11l1l1l_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨ႙")) else fixturedef.get(bstack11l1l1l_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢႚ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11l1l1l_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࠢႛ")) else None
        node = request.node if hasattr(request, bstack11l1l1l_opy_ (u"ࠥࡲࡴࡪࡥࠣႜ")) else None
        target = request.node.nodeid if hasattr(node, bstack11l1l1l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦႝ")) else None
        baseid = fixturedef.get(bstack11l1l1l_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧ႞"), None) or bstack11l1l1l_opy_ (u"ࠨࠢ႟")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11l1l1l_opy_ (u"ࠢࡠࡲࡼࡪࡺࡴࡣࡪࡶࡨࡱࠧႠ")):
            target = PytestBDDFramework.__1lll1111lll_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11l1l1l_opy_ (u"ࠣ࡮ࡲࡧࡦࡺࡩࡰࡰࠥႡ")) else None
            if target and not TestFramework.bstack1lll11l1ll1_opy_(target):
                self.__1lll111l11l_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡩࡥࡱࡲࡢࡢࡥ࡮ࠤࡹࡧࡲࡨࡧࡷࡁࢀࡺࡡࡳࡩࡨࡸࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡳࡵࡤࡦ࠿ࡾࡲࡴࡪࡥࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦႢ") + str(test_hook_state) + bstack11l1l1l_opy_ (u"ࠥࠦႣ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡪࡥࡧ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤႤ") + str(target) + bstack11l1l1l_opy_ (u"ࠧࠨႥ"))
            return None
        instance = TestFramework.bstack1lll11l1ll1_opy_(target)
        if not instance:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡨࡡࡴࡧ࡬ࡨࡂࢁࡢࡢࡵࡨ࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣႦ") + str(target) + bstack11l1l1l_opy_ (u"ࠢࠣႧ"))
            return None
        bstack1lll1l1ll11_opy_ = TestFramework.bstack111l1111l1_opy_(instance, PytestBDDFramework.bstack1lll1111l1l_opy_, {})
        if os.getenv(bstack11l1l1l_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡇࡋ࡛ࡘ࡚ࡘࡅࡔࠤႨ"), bstack11l1l1l_opy_ (u"ࠤ࠴ࠦႩ")) == bstack11l1l1l_opy_ (u"ࠥ࠵ࠧႪ"):
            bstack1lll1ll11ll_opy_ = bstack11l1l1l_opy_ (u"ࠦ࠿ࠨႫ").join((scope, fixturename))
            bstack1lll11lll1l_opy_ = datetime.now(tz=timezone.utc)
            bstack1llll1ll1l1_opy_ = {
                bstack11l1l1l_opy_ (u"ࠧࡱࡥࡺࠤႬ"): bstack1lll1ll11ll_opy_,
                bstack11l1l1l_opy_ (u"ࠨࡴࡢࡩࡶࠦႭ"): PytestBDDFramework.__1llll1l1111_opy_(request.node, scenario),
                bstack11l1l1l_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥࠣႮ"): fixturedef,
                bstack11l1l1l_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢႯ"): scope,
                bstack11l1l1l_opy_ (u"ࠤࡷࡽࡵ࡫ࠢႰ"): None,
            }
            try:
                if test_hook_state == bstack11111111ll_opy_.POST and callable(getattr(args[-1], bstack11l1l1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡶࡹࡱࡺࠢႱ"), None)):
                    bstack1llll1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠦࡹࡿࡰࡦࠤႲ")] = TestFramework.bstack1lll11l1l1l_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack11111111ll_opy_.PRE:
                bstack1llll1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠧࡻࡵࡪࡦࠥႳ")] = uuid4().__str__()
                bstack1llll1ll1l1_opy_[PytestBDDFramework.bstack1lll111l111_opy_] = bstack1lll11lll1l_opy_
            elif test_hook_state == bstack11111111ll_opy_.POST:
                bstack1llll1ll1l1_opy_[PytestBDDFramework.bstack1lll1111ll1_opy_] = bstack1lll11lll1l_opy_
            if bstack1lll1ll11ll_opy_ in bstack1lll1l1ll11_opy_:
                bstack1lll1l1ll11_opy_[bstack1lll1ll11ll_opy_].update(bstack1llll1ll1l1_opy_)
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡵࡱࡦࡤࡸࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡃࠢႴ") + str(bstack1lll1l1ll11_opy_[bstack1lll1ll11ll_opy_]) + bstack11l1l1l_opy_ (u"ࠢࠣႵ"))
            else:
                bstack1lll1l1ll11_opy_[bstack1lll1ll11ll_opy_] = bstack1llll1ll1l1_opy_
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡃࡻࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࢃࠠࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࠦႶ") + str(len(bstack1lll1l1ll11_opy_)) + bstack11l1l1l_opy_ (u"ࠤࠥႷ"))
        TestFramework.bstack1111l1l11l_opy_(instance, PytestBDDFramework.bstack1lll1111l1l_opy_, bstack1lll1l1ll11_opy_)
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢࡩ࡭ࡽࡺࡵࡳࡧࡶࡁࢀࡲࡥ࡯ࠪࡷࡶࡦࡩ࡫ࡦࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࡷ࠮ࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥႸ") + str(instance.ref()) + bstack11l1l1l_opy_ (u"ࠦࠧႹ"))
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
            PytestBDDFramework.bstack1lll1111l1l_opy_: {},
            PytestBDDFramework.bstack1llll1l1l11_opy_: {},
            PytestBDDFramework.bstack1lll1l1111l_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1111l1l11l_opy_(ob, TestFramework.bstack1lll1l1lll1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1111l1l11l_opy_(ob, TestFramework.bstack1111ll11l1_opy_, context.platform_index)
        TestFramework.bstack1lll11ll11l_opy_[ctx.id] = ob
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡣࡵࡺ࠱࡭ࡩࡃࡻࡤࡶࡻ࠲࡮ࡪࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶࡁࠧႺ") + str(TestFramework.bstack1lll11ll11l_opy_.keys()) + bstack11l1l1l_opy_ (u"ࠨࠢႻ"))
        return ob
    @staticmethod
    def __1lll1l1l111_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11l1l1l_opy_ (u"ࠧࡪࡦࠪႼ"): id(step),
                bstack11l1l1l_opy_ (u"ࠨࡶࡨࡼࡹ࠭Ⴝ"): step.name,
                bstack11l1l1l_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪႾ"): step.keyword,
            })
        meta = {
            bstack11l1l1l_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࠫႿ"): {
                bstack11l1l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩჀ"): feature.name,
                bstack11l1l1l_opy_ (u"ࠬࡶࡡࡵࡪࠪჁ"): feature.filename,
                bstack11l1l1l_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫჂ"): feature.description
            },
            bstack11l1l1l_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩჃ"): {
                bstack11l1l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭Ⴤ"): scenario.name
            },
            bstack11l1l1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨჅ"): steps,
            bstack11l1l1l_opy_ (u"ࠪࡩࡽࡧ࡭ࡱ࡮ࡨࡷࠬ჆"): PytestBDDFramework.__1llll11llll_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1llll1111l1_opy_: meta
            }
        )
    @staticmethod
    def __1llll11lll1_opy_(instance, args):
        request, bstack1llll1l11l1_opy_ = args
        bstack1lll1l1l1ll_opy_ = id(bstack1llll1l11l1_opy_)
        bstack1lll1ll111l_opy_ = instance.data[TestFramework.bstack1llll1111l1_opy_]
        step = next(filter(lambda st: st[bstack11l1l1l_opy_ (u"ࠫ࡮ࡪࠧჇ")] == bstack1lll1l1l1ll_opy_, bstack1lll1ll111l_opy_[bstack11l1l1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫ჈")]), None)
        step.update({
            bstack11l1l1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ჉"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1lll1ll111l_opy_[bstack11l1l1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭჊")]) if st[bstack11l1l1l_opy_ (u"ࠨ࡫ࡧࠫ჋")] == step[bstack11l1l1l_opy_ (u"ࠩ࡬ࡨࠬ჌")]), None)
        if index is not None:
            bstack1lll1ll111l_opy_[bstack11l1l1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩჍ")][index] = step
        instance.data[TestFramework.bstack1llll1111l1_opy_] = bstack1lll1ll111l_opy_
    @staticmethod
    def __1lll1l11lll_opy_(instance, args):
        bstack11l1l1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡹ࡫ࡩࡳࠦ࡬ࡦࡰࠣࡥࡷ࡭ࡳࠡ࡫ࡶࠤ࠷࠲ࠠࡪࡶࠣࡷ࡮࡭࡮ࡪࡨ࡬ࡩࡸࠦࡴࡩࡧࡵࡩࠥ࡯ࡳࠡࡰࡲࠤࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡧࡲࡨࡵࠣࡥࡷ࡫ࠠ࠮ࠢ࡞ࡶࡪࡷࡵࡦࡵࡷ࠰ࠥࡹࡴࡦࡲࡠࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡯ࡦࠡࡣࡵ࡫ࡸࠦࡡࡳࡧࠣ࠷ࠥࡺࡨࡦࡰࠣࡸ࡭࡫ࠠ࡭ࡣࡶࡸࠥࡼࡡ࡭ࡷࡨࠤ࡮ࡹࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ჎")
        bstack1lll1ll1l1l_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1llll1l11l1_opy_ = args[1]
        bstack1lll1l1l1ll_opy_ = id(bstack1llll1l11l1_opy_)
        bstack1lll1ll111l_opy_ = instance.data[TestFramework.bstack1llll1111l1_opy_]
        step = None
        if bstack1lll1l1l1ll_opy_ is not None and bstack1lll1ll111l_opy_.get(bstack11l1l1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫ჏")):
            step = next(filter(lambda st: st[bstack11l1l1l_opy_ (u"࠭ࡩࡥࠩა")] == bstack1lll1l1l1ll_opy_, bstack1lll1ll111l_opy_[bstack11l1l1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ბ")]), None)
            step.update({
                bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭გ"): bstack1lll1ll1l1l_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack11l1l1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩდ"): bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪე"),
                bstack11l1l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬვ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack11l1l1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬზ"): bstack11l1l1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭თ"),
                })
        index = next((i for i, st in enumerate(bstack1lll1ll111l_opy_[bstack11l1l1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ი")]) if st[bstack11l1l1l_opy_ (u"ࠨ࡫ࡧࠫკ")] == step[bstack11l1l1l_opy_ (u"ࠩ࡬ࡨࠬლ")]), None)
        if index is not None:
            bstack1lll1ll111l_opy_[bstack11l1l1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩმ")][index] = step
        instance.data[TestFramework.bstack1llll1111l1_opy_] = bstack1lll1ll111l_opy_
    @staticmethod
    def __1llll11llll_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack11l1l1l_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭ნ")):
                examples = list(node.callspec.params[bstack11l1l1l_opy_ (u"ࠬࡥࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡩࡽࡧ࡭ࡱ࡮ࡨࠫო")].values())
            return examples
        except:
            return []
    def bstack1llll1111ll_opy_(self, instance: bstack1lllllll1l1_opy_, bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_]):
        bstack1lll1lllll1_opy_ = (
            PytestBDDFramework.bstack1lll1lll111_opy_
            if bstack111l11llll_opy_[1] == bstack11111111ll_opy_.PRE
            else PytestBDDFramework.bstack1lll11ll1ll_opy_
        )
        hook = PytestBDDFramework.bstack1lll11l1lll_opy_(instance, bstack1lll1lllll1_opy_)
        entries = hook.get(TestFramework.bstack1llll1l11ll_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1llll1ll111_opy_, []))
        return entries
    def bstack1lll11l111l_opy_(self, instance: bstack1lllllll1l1_opy_, bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_]):
        bstack1lll1lllll1_opy_ = (
            PytestBDDFramework.bstack1lll1lll111_opy_
            if bstack111l11llll_opy_[1] == bstack11111111ll_opy_.PRE
            else PytestBDDFramework.bstack1lll11ll1ll_opy_
        )
        PytestBDDFramework.bstack1lll1l11ll1_opy_(instance, bstack1lll1lllll1_opy_)
        TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1llll1ll111_opy_, []).clear()
    @staticmethod
    def bstack1lll11l1lll_opy_(instance: bstack1lllllll1l1_opy_, bstack1lll1lllll1_opy_: str):
        bstack1lll1l1l11l_opy_ = (
            PytestBDDFramework.bstack1llll1l1l11_opy_
            if bstack1lll1lllll1_opy_ == PytestBDDFramework.bstack1lll11ll1ll_opy_
            else PytestBDDFramework.bstack1lll1l1111l_opy_
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
        hook = PytestBDDFramework.bstack1lll11l1lll_opy_(instance, bstack1lll1lllll1_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1llll1l11ll_opy_, []).clear()
    @staticmethod
    def __1lll111lll1_opy_(instance: bstack1lllllll1l1_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11l1l1l_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡩ࡯ࡳࡦࡶࠦპ"), None)):
            return
        if os.getenv(bstack11l1l1l_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡌࡐࡉࡖࠦჟ"), bstack11l1l1l_opy_ (u"ࠣ࠳ࠥრ")) != bstack11l1l1l_opy_ (u"ࠤ࠴ࠦს"):
            PytestBDDFramework.logger.warning(bstack11l1l1l_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳ࡫ࡱ࡫ࠥࡩࡡࡱ࡮ࡲ࡫ࠧტ"))
            return
        bstack1llll11ll1l_opy_ = {
            bstack11l1l1l_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥუ"): (PytestBDDFramework.bstack1lll1lll111_opy_, PytestBDDFramework.bstack1lll1l1111l_opy_),
            bstack11l1l1l_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢფ"): (PytestBDDFramework.bstack1lll11ll1ll_opy_, PytestBDDFramework.bstack1llll1l1l11_opy_),
        }
        for when in (bstack11l1l1l_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧქ"), bstack11l1l1l_opy_ (u"ࠢࡤࡣ࡯ࡰࠧღ"), bstack11l1l1l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥყ")):
            bstack1llll11111l_opy_ = args[1].get_records(when)
            if not bstack1llll11111l_opy_:
                continue
            records = [
                bstack1lll1l1l1l1_opy_(
                    kind=TestFramework.bstack1llll111l11_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11l1l1l_opy_ (u"ࠤ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩࠧშ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11l1l1l_opy_ (u"ࠥࡧࡷ࡫ࡡࡵࡧࡧࠦჩ")) and r.created
                        else None
                    ),
                )
                for r in bstack1llll11111l_opy_
                if isinstance(getattr(r, bstack11l1l1l_opy_ (u"ࠦࡲ࡫ࡳࡴࡣࡪࡩࠧც"), None), str) and r.message.strip()
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
    def __1lll1l11111_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1llll1ll1ll_opy_(request.node, scenario)
        bstack1llll11l11l_opy_ = feature.filename
        if not test_id or not test_name or not bstack1llll11l11l_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1lll1ll1ll1_opy_: uuid4().__str__(),
            TestFramework.bstack1lll1l111l1_opy_: test_id,
            TestFramework.bstack1lll1ll1111_opy_: test_name,
            TestFramework.bstack1lll11lll11_opy_: test_id,
            TestFramework.bstack1lll1ll11l1_opy_: bstack1llll11l11l_opy_,
            TestFramework.bstack1lll1lll1l1_opy_: PytestBDDFramework.__1llll1l1111_opy_(feature, scenario),
            TestFramework.bstack1llll1l111l_opy_: code,
            TestFramework.bstack1111111111_opy_: TestFramework.bstack1lll11ll1l1_opy_,
            TestFramework.bstack11111l1lll_opy_: test_name
        }
    @staticmethod
    def __1llll1ll1ll_opy_(node, scenario):
        if hasattr(node, bstack11l1l1l_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧძ")):
            parts = node.nodeid.rsplit(bstack11l1l1l_opy_ (u"ࠨ࡛ࠣწ"))
            params = parts[-1]
            return bstack11l1l1l_opy_ (u"ࠢࡼࡿࠣ࡟ࢀࢃࠢჭ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1llll1l1111_opy_(feature, scenario) -> List[str]:
        return list(feature.tags) + list(scenario.tags)
    @staticmethod
    def __1lll1111lll_opy_(location):
        return bstack11l1l1l_opy_ (u"ࠣ࠼࠽ࠦხ").join(filter(lambda x: isinstance(x, str), location))