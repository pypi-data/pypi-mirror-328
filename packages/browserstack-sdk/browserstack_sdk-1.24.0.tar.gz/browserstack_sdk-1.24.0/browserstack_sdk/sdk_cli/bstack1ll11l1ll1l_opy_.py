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
from datetime import datetime, timezone
import os
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import bstack1111lllll1_opy_, bstack1111l1llll_opy_, bstack111l111111_opy_
from browserstack_sdk.sdk_cli.bstack1111l1l1l1_opy_ import bstack1111l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1lllllllll1_opy_
from browserstack_sdk.sdk_cli.bstack11111ll1ll_opy_ import bstack1111l1ll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack111111lll1_opy_, bstack1lllllll1l1_opy_, bstack11111111ll_opy_, bstack1lll1l1l1l1_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1l1llll111l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1ll1111111l_opy_ = [bstack11l1l1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇃ"), bstack11l1l1l_opy_ (u"ࠧࡶࡡࡳࡧࡱࡸࠧᇄ"), bstack11l1l1l_opy_ (u"ࠨࡣࡰࡰࡩ࡭࡬ࠨᇅ"), bstack11l1l1l_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࠣᇆ"), bstack11l1l1l_opy_ (u"ࠣࡲࡤࡸ࡭ࠨᇇ")]
bstack1l1lll11l1l_opy_ = {
    bstack11l1l1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡌࡸࡪࡳࠢᇈ"): bstack1ll1111111l_opy_,
    bstack11l1l1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡔࡦࡩ࡫ࡢࡩࡨࠦᇉ"): bstack1ll1111111l_opy_,
    bstack11l1l1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡒࡵࡤࡶ࡮ࡨࠦᇊ"): bstack1ll1111111l_opy_,
    bstack11l1l1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡉ࡬ࡢࡵࡶࠦᇋ"): bstack1ll1111111l_opy_,
    bstack11l1l1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡆࡶࡰࡦࡸ࡮ࡵ࡮ࠣᇌ"): bstack1ll1111111l_opy_
    + [
        bstack11l1l1l_opy_ (u"ࠢࡰࡴ࡬࡫࡮ࡴࡡ࡭ࡰࡤࡱࡪࠨᇍ"),
        bstack11l1l1l_opy_ (u"ࠣ࡭ࡨࡽࡼࡵࡲࡥࡵࠥᇎ"),
        bstack11l1l1l_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧ࡬ࡲ࡫ࡵࠢᇏ"),
        bstack11l1l1l_opy_ (u"ࠥ࡯ࡪࡿࡷࡰࡴࡧࡷࠧᇐ"),
        bstack11l1l1l_opy_ (u"ࠦࡨࡧ࡬࡭ࡵࡳࡩࡨࠨᇑ"),
        bstack11l1l1l_opy_ (u"ࠧࡩࡡ࡭࡮ࡲࡦ࡯ࠨᇒ"),
        bstack11l1l1l_opy_ (u"ࠨࡳࡵࡣࡵࡸࠧᇓ"),
        bstack11l1l1l_opy_ (u"ࠢࡴࡶࡲࡴࠧᇔ"),
        bstack11l1l1l_opy_ (u"ࠣࡦࡸࡶࡦࡺࡩࡰࡰࠥᇕ"),
        bstack11l1l1l_opy_ (u"ࠤࡺ࡬ࡪࡴࠢᇖ"),
    ],
    bstack11l1l1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡱࡦ࡯࡮࠯ࡕࡨࡷࡸ࡯࡯࡯ࠤᇗ"): [bstack11l1l1l_opy_ (u"ࠦࡸࡺࡡࡳࡶࡳࡥࡹ࡮ࠢᇘ"), bstack11l1l1l_opy_ (u"ࠧࡺࡥࡴࡶࡶࡪࡦ࡯࡬ࡦࡦࠥᇙ"), bstack11l1l1l_opy_ (u"ࠨࡴࡦࡵࡷࡷࡨࡵ࡬࡭ࡧࡦࡸࡪࡪࠢᇚ"), bstack11l1l1l_opy_ (u"ࠢࡪࡶࡨࡱࡸࠨᇛ")],
    bstack11l1l1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡥࡲࡲ࡫࡯ࡧ࠯ࡅࡲࡲ࡫࡯ࡧࠣᇜ"): [bstack11l1l1l_opy_ (u"ࠤ࡬ࡲࡻࡵࡣࡢࡶ࡬ࡳࡳࡥࡰࡢࡴࡤࡱࡸࠨᇝ"), bstack11l1l1l_opy_ (u"ࠥࡥࡷ࡭ࡳࠣᇞ")],
    bstack11l1l1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲࡫࡯ࡸࡵࡷࡵࡩࡸ࠴ࡆࡪࡺࡷࡹࡷ࡫ࡄࡦࡨࠥᇟ"): [bstack11l1l1l_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᇠ"), bstack11l1l1l_opy_ (u"ࠨࡡࡳࡩࡱࡥࡲ࡫ࠢᇡ"), bstack11l1l1l_opy_ (u"ࠢࡧࡷࡱࡧࠧᇢ"), bstack11l1l1l_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣᇣ"), bstack11l1l1l_opy_ (u"ࠤࡸࡲ࡮ࡺࡴࡦࡵࡷࠦᇤ"), bstack11l1l1l_opy_ (u"ࠥ࡭ࡩࡹࠢᇥ")],
    bstack11l1l1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲࡫࡯ࡸࡵࡷࡵࡩࡸ࠴ࡓࡶࡤࡕࡩࡶࡻࡥࡴࡶࠥᇦ"): [bstack11l1l1l_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࠥᇧ"), bstack11l1l1l_opy_ (u"ࠨࡰࡢࡴࡤࡱࠧᇨ"), bstack11l1l1l_opy_ (u"ࠢࡱࡣࡵࡥࡲࡥࡩ࡯ࡦࡨࡼࠧᇩ")],
    bstack11l1l1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡴࡸࡲࡳ࡫ࡲ࠯ࡅࡤࡰࡱࡏ࡮ࡧࡱࠥᇪ"): [bstack11l1l1l_opy_ (u"ࠤࡺ࡬ࡪࡴࠢᇫ"), bstack11l1l1l_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࠥᇬ")],
    bstack11l1l1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡲࡧࡲ࡬࠰ࡶࡸࡷࡻࡣࡵࡷࡵࡩࡸ࠴ࡎࡰࡦࡨࡏࡪࡿࡷࡰࡴࡧࡷࠧᇭ"): [bstack11l1l1l_opy_ (u"ࠧࡴ࡯ࡥࡧࠥᇮ"), bstack11l1l1l_opy_ (u"ࠨࡰࡢࡴࡨࡲࡹࠨᇯ")],
    bstack11l1l1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮࡮ࡣࡵ࡯࠳ࡹࡴࡳࡷࡦࡸࡺࡸࡥࡴ࠰ࡐࡥࡷࡱࠢᇰ"): [bstack11l1l1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᇱ"), bstack11l1l1l_opy_ (u"ࠤࡤࡶ࡬ࡹࠢᇲ"), bstack11l1l1l_opy_ (u"ࠥ࡯ࡼࡧࡲࡨࡵࠥᇳ")],
}
class bstack1ll11l11l1l_opy_(bstack1111l1ll11_opy_):
    bstack1ll11111lll_opy_ = bstack11l1l1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡧࡩ࡫࡫ࡲࡳࡧࡧࠦᇴ")
    bstack1l1lllll1l1_opy_ = bstack11l1l1l_opy_ (u"ࠧࡏࡎࡇࡑࠥᇵ")
    bstack1ll111l11l1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡅࡓࡔࡒࡖࠧᇶ")
    bstack1l1lll1lll1_opy_: Callable
    bstack1l1lll1l11l_opy_: Callable
    def __init__(self):
        super().__init__()
        if os.getenv(bstack11l1l1l_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡏ࠲࠳࡜ࠦᇷ"), bstack11l1l1l_opy_ (u"ࠣ࠳ࠥᇸ")) != bstack11l1l1l_opy_ (u"ࠤ࠴ࠦᇹ") or not self.is_enabled():
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠥࠦᇺ") + str(self.__class__.__name__) + bstack11l1l1l_opy_ (u"ࠦࠥࡪࡩࡴࡣࡥࡰࡪࡪࠢᇻ"))
            return
        TestFramework.bstack1111ll1l1l_opy_((bstack111111lll1_opy_.TEST, bstack11111111ll_opy_.PRE), self.bstack111111ll11_opy_)
        TestFramework.bstack1111ll1l1l_opy_((bstack111111lll1_opy_.TEST, bstack11111111ll_opy_.POST), self.bstack1lllllll1ll_opy_)
        for event in bstack111111lll1_opy_:
            for state in bstack11111111ll_opy_:
                TestFramework.bstack1111ll1l1l_opy_((event, state), self.bstack1l1lllll11l_opy_)
        bstack1111l1ll1l_opy_.bstack1111ll1l1l_opy_((bstack1111l1llll_opy_.bstack111l11111l_opy_, bstack111l111111_opy_.POST), self.bstack1l1llllll11_opy_)
        self.bstack1l1lll1lll1_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l1llll1ll1_opy_(bstack1ll11l11l1l_opy_.bstack1l1lllll1l1_opy_, self.bstack1l1lll1lll1_opy_)
        self.bstack1l1lll1l11l_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l1llll1ll1_opy_(bstack1ll11l11l1l_opy_.bstack1ll111l11l1_opy_, self.bstack1l1lll1l11l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1lllll11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1lll11l1111_opy_() and instance:
            bstack1l1lll1llll_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack111l11llll_opy_
            if test_framework_state == bstack111111lll1_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack111111lll1_opy_.LOG:
                bstack1l1lll1l1l_opy_ = datetime.now()
                entries = f.bstack1llll1111ll_opy_(instance, bstack111l11llll_opy_)
                if entries:
                    self.bstack1ll11111l11_opy_(instance, entries)
                    instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࠧᇼ"), datetime.now() - bstack1l1lll1l1l_opy_)
                    f.bstack1lll11l111l_opy_(instance, bstack111l11llll_opy_)
                instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠨ࡯࠲࠳ࡼ࠾ࡴࡴ࡟ࡢ࡮࡯ࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴࡴࠤᇽ"), datetime.now() - bstack1l1lll1llll_opy_)
                return # do not send this event with the bstack1ll111111ll_opy_ bstack1ll11111111_opy_
            elif (
                test_framework_state == bstack111111lll1_opy_.TEST
                and test_hook_state == bstack11111111ll_opy_.POST
                and not f.bstack1111ll111l_opy_(instance, TestFramework.bstack1lll1l111ll_opy_)
            ):
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠢࡥࡴࡲࡴࡵ࡯࡮ࡨࠢࡧࡹࡪࠦࡴࡰࠢ࡯ࡥࡨࡱࠠࡰࡨࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࠧᇾ") + str(TestFramework.bstack1111ll111l_opy_(instance, TestFramework.bstack1lll1l111ll_opy_)) + bstack11l1l1l_opy_ (u"ࠣࠤᇿ"))
                f.bstack1111l1l11l_opy_(instance, bstack1ll11l11l1l_opy_.bstack1ll11111lll_opy_, True)
                return # do not send this event bstack1ll1111ll11_opy_ bstack1ll1111l11l_opy_
            elif (
                f.bstack111l1111l1_opy_(instance, bstack1ll11l11l1l_opy_.bstack1ll11111lll_opy_, False)
                and test_framework_state == bstack111111lll1_opy_.LOG_REPORT
                and test_hook_state == bstack11111111ll_opy_.POST
                and f.bstack1111ll111l_opy_(instance, TestFramework.bstack1lll1l111ll_opy_)
            ):
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠤ࡬ࡲ࡯࡫ࡣࡵ࡫ࡱ࡫࡚ࠥࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺࡡࡵࡧ࠱ࡘࡊ࡙ࡔ࠭ࠢࡗࡩࡸࡺࡈࡰࡱ࡮ࡗࡹࡧࡴࡦ࠰ࡓࡓࡘ࡚ࠠࠣሀ") + str(TestFramework.bstack1111ll111l_opy_(instance, TestFramework.bstack1lll1l111ll_opy_)) + bstack11l1l1l_opy_ (u"ࠥࠦሁ"))
                self.bstack1l1lllll11l_opy_(f, instance, (bstack111111lll1_opy_.TEST, bstack11111111ll_opy_.POST), *args, **kwargs)
            bstack1l1lll1l1l_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l1llll11ll_opy_ = sorted(
                filter(lambda x: x.get(bstack11l1l1l_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢሂ"), None), data.pop(bstack11l1l1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧሃ"), {}).values()),
                key=lambda x: x[bstack11l1l1l_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠤሄ")],
            )
            if bstack1lllllllll1_opy_.bstack1llllll11ll_opy_ in data:
                data.pop(bstack1lllllllll1_opy_.bstack1llllll11ll_opy_)
            data.update({bstack11l1l1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢህ"): bstack1l1llll11ll_opy_})
            instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠣ࡬ࡶࡳࡳࡀࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨሆ"), datetime.now() - bstack1l1lll1l1l_opy_)
            bstack1l1lll1l1l_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l1llll1l1l_opy_)
            instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠤ࡭ࡷࡴࡴ࠺ࡰࡰࡢࡥࡱࡲ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷࡷࠧሇ"), datetime.now() - bstack1l1lll1l1l_opy_)
            self.bstack1ll11111111_opy_(instance, bstack111l11llll_opy_, event_json=event_json)
            instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠥࡳ࠶࠷ࡹ࠻ࡱࡱࡣࡦࡲ࡬ࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸࡸࠨለ"), datetime.now() - bstack1l1lll1llll_opy_)
    def bstack111111ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
        *args,
        **kwargs,
    ):
        bstack11111l111l_opy_ = [d for d, _ in f.bstack111l1111l1_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll11ll_opy_, [])]
        if not bstack11111l111l_opy_:
            return
        if not bstack1l1llll111l_opy_():
            return
        for bstack1l1lllll111_opy_ in bstack11111l111l_opy_:
            driver = bstack1l1lllll111_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack11l1l1l_opy_ (u"ࠦࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡗࡾࡴࡣ࠻ࠤሉ") + str(timestamp)
            driver.execute_script(
                bstack11l1l1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥሊ").format(
                    json.dumps(
                        {
                            bstack11l1l1l_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨላ"): bstack11l1l1l_opy_ (u"ࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤሌ"),
                            bstack11l1l1l_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦል"): {
                                bstack11l1l1l_opy_ (u"ࠤࡷࡽࡵ࡫ࠢሎ"): bstack11l1l1l_opy_ (u"ࠥࡅࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠢሏ"),
                                bstack11l1l1l_opy_ (u"ࠦࡩࡧࡴࡢࠤሐ"): data,
                                bstack11l1l1l_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࠦሑ"): bstack11l1l1l_opy_ (u"ࠨࡤࡦࡤࡸ࡫ࠧሒ")
                            }
                        }
                    )
                )
            )
    def bstack1lllllll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
        *args,
        **kwargs,
    ):
        keys = [
            bstack1lllllllll1_opy_.bstack1llllll11ll_opy_,
            bstack1lllllllll1_opy_.bstack1111111l11_opy_,
        ]
        bstack11111l111l_opy_ = [
            d for key in keys for _, d in f.bstack111l1111l1_opy_(instance, key, [])
        ]
        if not bstack11111l111l_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡤࡲࡾࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡶࡲࠤࡱ࡯࡮࡬ࠤሓ"))
            return
        self.bstack1l1llll11l1_opy_(f, instance, bstack11111l111l_opy_, bstack111l11llll_opy_)
    @measure(event_name=EVENTS.bstack1l1llllll1l_opy_, stage=STAGE.SINGLE)
    def bstack1l1llll11l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lllllll1l1_opy_,
        bstack11111l111l_opy_: List[bstack1111lllll1_opy_],
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
    ):
        if f.bstack111l1111l1_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll1l11_opy_, False):
            return
        self.bstack1111l11l1l_opy_()
        bstack1l1lll1l1l_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1111ll11l1_opy_)
        req.test_framework_name = TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1lll1lll1ll_opy_)
        req.test_framework_version = TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1lll1ll1l11_opy_)
        req.test_framework_state = bstack111l11llll_opy_[0].name
        req.test_hook_state = bstack111l11llll_opy_[1].name
        req.test_uuid = TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1lll1ll1ll1_opy_)
        for driver in bstack11111l111l_opy_:
            session = req.automation_sessions.add()
            session.provider = (
                bstack11l1l1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠢሔ")
                if bstack1111l1ll1l_opy_.bstack111l1111l1_opy_(driver, bstack1111l1ll1l_opy_.bstack1l1lllllll1_opy_, False)
                else bstack11l1l1l_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࡢ࡫ࡷ࡯ࡤࠣሕ")
            )
            session.ref = driver.ref()
            session.hub_url = bstack1111l1ll1l_opy_.bstack111l1111l1_opy_(driver, bstack1111l1ll1l_opy_.bstack1ll1111llll_opy_, bstack11l1l1l_opy_ (u"ࠥࠦሖ"))
            session.framework_name = driver.framework_name
            session.framework_version = driver.framework_version
            session.framework_session_id = bstack1111l1ll1l_opy_.bstack111l1111l1_opy_(driver, bstack1111l1ll1l_opy_.bstack1ll1111l111_opy_, bstack11l1l1l_opy_ (u"ࠦࠧሗ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        try:
            r = self.bstack1111l11ll1_opy_.TestSessionEvent(req)
            instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠࡶࡨࡷࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡦࡸࡨࡲࡹࠨመ"), datetime.now() - bstack1l1lll1l1l_opy_)
            f.bstack1111l1l11l_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll1l11_opy_, r.success)
            if not r.success:
                self.logger.info(bstack11l1l1l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣሙ") + str(r) + bstack11l1l1l_opy_ (u"ࠢࠣሚ"))
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨማ") + str(e) + bstack11l1l1l_opy_ (u"ࠤࠥሜ"))
            traceback.print_exc()
            raise e
    def bstack1l1llllll11_opy_(
        self,
        f: bstack1111l1ll1l_opy_,
        _driver: object,
        exec: Tuple[bstack1111lllll1_opy_, str],
        _1l1lll1ll11_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1111l1ll1l_opy_.bstack1l1lll11l11_opy_(method_name):
            return
        if f.bstack1ll1lll11ll_opy_(*args) != bstack1111l1ll1l_opy_.bstack1ll11111ll1_opy_:
            return
        bstack1l1lll1llll_opy_ = datetime.now()
        screenshot = result.get(bstack11l1l1l_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤም"), None) if isinstance(result, dict) else None
        if not isinstance(screenshot, str) or len(screenshot) <= 0:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠦ࡮ࡴࡶࡢ࡮࡬ࡨࠥࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠢ࡬ࡱࡦ࡭ࡥࠡࡤࡤࡷࡪ࠼࠴ࠡࡵࡷࡶࠧሞ"))
            return
        bstack1l1llllllll_opy_ = self.bstack1l1lll1l1ll_opy_(instance)
        if bstack1l1llllllll_opy_:
            entry = bstack1lll1l1l1l1_opy_(TestFramework.bstack1l1lll1ll1l_opy_, screenshot)
            self.bstack1ll11111l11_opy_(bstack1l1llllllll_opy_, [entry])
            instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠧࡵ࠱࠲ࡻ࠽ࡳࡳࡥࡡࡧࡶࡨࡶࡤ࡫ࡸࡦࡥࡸࡸࡪࠨሟ"), datetime.now() - bstack1l1lll1llll_opy_)
        else:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠨࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥࡺࡥࡴࡶࠣࡪࡴࡸࠠࡸࡪ࡬ࡧ࡭ࠦࡴࡩ࡫ࡶࠤࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠡࡹࡤࡷࠥࡺࡡ࡬ࡧࡱࠤࡧࡿࠠࡥࡴ࡬ࡺࡪࡸ࠽ࠣሠ") + str(instance.ref()) + bstack11l1l1l_opy_ (u"ࠢࠣሡ"))
    @measure(event_name=EVENTS.bstack1ll111l111l_opy_, stage=STAGE.SINGLE)
    def bstack1ll11111l11_opy_(
        self,
        bstack1l1llllllll_opy_: bstack1lllllll1l1_opy_,
        entries: List[bstack1lll1l1l1l1_opy_],
    ):
        self.bstack1111l11l1l_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack111l1111l1_opy_(bstack1l1llllllll_opy_, TestFramework.bstack1111ll11l1_opy_)
        req.execution_context.hash = str(bstack1l1llllllll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1l1llllllll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1l1llllllll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.bstack111l1111l1_opy_(bstack1l1llllllll_opy_, TestFramework.bstack1lll1lll1ll_opy_)
            log_entry.test_framework_version = TestFramework.bstack111l1111l1_opy_(bstack1l1llllllll_opy_, TestFramework.bstack1lll1ll1l11_opy_)
            log_entry.uuid = TestFramework.bstack111l1111l1_opy_(bstack1l1llllllll_opy_, TestFramework.bstack1lll1ll1ll1_opy_)
            log_entry.test_framework_state = bstack1l1llllllll_opy_.state.name
            log_entry.message = entry.message.encode(bstack11l1l1l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢሢ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
        def bstack1l1lll1l111_opy_():
            bstack1l1lll1l1l_opy_ = datetime.now()
            try:
                self.bstack1111l11ll1_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l1lll1ll1l_opy_:
                    bstack1l1llllllll_opy_.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨሣ"), datetime.now() - bstack1l1lll1l1l_opy_)
                else:
                    bstack1l1llllllll_opy_.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡰࡴ࡭ࠢሤ"), datetime.now() - bstack1l1lll1l1l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l1l1l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤሥ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack11111ll1l1_opy_.enqueue(bstack1l1lll1l111_opy_)
    @measure(event_name=EVENTS.bstack1ll1111lll1_opy_, stage=STAGE.SINGLE)
    def bstack1ll11111111_opy_(
        self,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
        event_json=None,
    ):
        self.bstack1111l11l1l_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1111ll11l1_opy_)
        req.test_framework_name = TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1lll1lll1ll_opy_)
        req.test_framework_version = TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1lll1ll1l11_opy_)
        req.test_framework_state = bstack111l11llll_opy_[0].name
        req.test_hook_state = bstack111l11llll_opy_[1].name
        started_at = TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1lll11llll1_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.bstack111l1111l1_opy_(instance, TestFramework.bstack1llll11ll11_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l1llll1l1l_opy_)).encode(bstack11l1l1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦሦ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1l1lll1l111_opy_():
            bstack1l1lll1l1l_opy_ = datetime.now()
            try:
                self.bstack1111l11ll1_opy_.TestFrameworkEvent(req)
                instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡩࡻ࡫࡮ࡵࠤሧ"), datetime.now() - bstack1l1lll1l1l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l1l1l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧረ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack11111ll1l1_opy_.enqueue(bstack1l1lll1l111_opy_)
    def bstack1l1llll1lll_opy_(self, event_url: str, bstack1l1l1l11_opy_: dict) -> bool:
        return True # always return True so that old bstack1l1lll11lll_opy_ bstack1ll111l11ll_opy_'t bstack1ll11111l1l_opy_
    def bstack1l1lll1l1ll_opy_(self, instance: bstack1111lllll1_opy_):
        bstack1ll1111ll1l_opy_ = TestFramework.bstack1ll1111l1ll_opy_(instance.context)
        for t in bstack1ll1111ll1l_opy_:
            bstack11111l111l_opy_ = TestFramework.bstack111l1111l1_opy_(t, bstack1lllllllll1_opy_.bstack1llllll11ll_opy_, [])
            if any(instance is d[1] for d in bstack11111l111l_opy_):
                return t
    def bstack1ll111l1111_opy_(self, message):
        self.bstack1l1lll1lll1_opy_(message + bstack11l1l1l_opy_ (u"ࠣ࡞ࡱࠦሩ"))
    def log_error(self, message):
        self.bstack1l1lll1l11l_opy_(message + bstack11l1l1l_opy_ (u"ࠤ࡟ࡲࠧሪ"))
    def bstack1l1llll1ll1_opy_(self, level, original_func):
        def bstack1l1llll1111_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            bstack1ll1111ll1l_opy_ = TestFramework.bstack1l1lllll1ll_opy_()
            if not bstack1ll1111ll1l_opy_:
                return return_value
            bstack1l1llllllll_opy_ = next(
                (
                    instance
                    for instance in bstack1ll1111ll1l_opy_
                    if TestFramework.bstack1111ll111l_opy_(instance, TestFramework.bstack1lll1ll1ll1_opy_)
                ),
                None,
            )
            if not bstack1l1llllllll_opy_:
                return
            entry = bstack1lll1l1l1l1_opy_(TestFramework.bstack1llll111l11_opy_, message, level)
            self.bstack1ll11111l11_opy_(bstack1l1llllllll_opy_, [entry])
            return return_value
        return bstack1l1llll1111_opy_
class bstack1l1llll1l1l_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l1lll11ll1_opy_ = set()
        kwargs[bstack11l1l1l_opy_ (u"ࠥࡷࡰ࡯ࡰ࡬ࡧࡼࡷࠧራ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l1llll1l11_opy_(obj, self.bstack1l1lll11ll1_opy_)
def bstack1l1lll1l1l1_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l1llll1l11_opy_(obj, bstack1l1lll11ll1_opy_=None, max_depth=3):
    if bstack1l1lll11ll1_opy_ is None:
        bstack1l1lll11ll1_opy_ = set()
    if id(obj) in bstack1l1lll11ll1_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l1lll11ll1_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1ll111111l1_opy_ = TestFramework.bstack1lll11l1l1l_opy_(obj)
    bstack1ll1111l1l1_opy_ = next((k.lower() in bstack1ll111111l1_opy_.lower() for k in bstack1l1lll11l1l_opy_.keys()), None)
    if bstack1ll1111l1l1_opy_:
        obj = TestFramework.bstack1lll1ll1lll_opy_(obj, bstack1l1lll11l1l_opy_[bstack1ll1111l1l1_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack11l1l1l_opy_ (u"ࠦࡤࡥࡳ࡭ࡱࡷࡷࡤࡥࠢሬ")):
            keys = getattr(obj, bstack11l1l1l_opy_ (u"ࠧࡥ࡟ࡴ࡮ࡲࡸࡸࡥ࡟ࠣር"), [])
        elif hasattr(obj, bstack11l1l1l_opy_ (u"ࠨ࡟ࡠࡦ࡬ࡧࡹࡥ࡟ࠣሮ")):
            keys = getattr(obj, bstack11l1l1l_opy_ (u"ࠢࡠࡡࡧ࡭ࡨࡺ࡟ࡠࠤሯ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack11l1l1l_opy_ (u"ࠣࡡࠥሰ"))}
        if not obj and bstack1ll111111l1_opy_ == bstack11l1l1l_opy_ (u"ࠤࡳࡥࡹ࡮࡬ࡪࡤ࠱ࡔࡴࡹࡩࡹࡒࡤࡸ࡭ࠨሱ"):
            obj = {bstack11l1l1l_opy_ (u"ࠥࡴࡦࡺࡨࠣሲ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l1lll1l1l1_opy_(key) or str(key).startswith(bstack11l1l1l_opy_ (u"ࠦࡤࠨሳ")):
            continue
        if value is not None and bstack1l1lll1l1l1_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l1llll1l11_opy_(value, bstack1l1lll11ll1_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l1llll1l11_opy_(o, bstack1l1lll11ll1_opy_, max_depth) for o in value]))
    return result or None