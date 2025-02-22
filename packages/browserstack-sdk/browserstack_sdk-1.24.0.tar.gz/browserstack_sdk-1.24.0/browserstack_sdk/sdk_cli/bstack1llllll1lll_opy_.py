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
import json
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import (
    bstack1111l1llll_opy_,
    bstack111l111111_opy_,
    bstack1111lllll1_opy_,
    bstack11111l1l11_opy_,
)
from browserstack_sdk.sdk_cli.bstack11111ll1ll_opy_ import bstack1111l1ll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack111111lll1_opy_, bstack11111111ll_opy_, bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack111111l111_opy_ import bstack111111ll1l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lllllllll1_opy_(bstack111111ll1l_opy_):
    bstack11111l1l1l_opy_ = bstack11l1l1l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡲࡪࡸࡨࡶࡸࠨရ")
    bstack1llllll11ll_opy_ = bstack11l1l1l_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢလ")
    bstack1111111l11_opy_ = bstack11l1l1l_opy_ (u"ࠤࡱࡳࡳࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦဝ")
    bstack11111l11ll_opy_ = bstack11l1l1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥသ")
    bstack1llllllllll_opy_ = bstack11l1l1l_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡢࡶࡪ࡬ࡳࠣဟ")
    bstack1llllll1l11_opy_ = bstack11l1l1l_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡧࡷ࡫ࡡࡵࡧࡧࠦဠ")
    bstack111111111l_opy_ = bstack11l1l1l_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡳࡧ࡭ࡦࠤအ")
    bstack1llllll1ll1_opy_ = bstack11l1l1l_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡹࡴࡢࡶࡸࡷࠧဢ")
    def __init__(self):
        super().__init__(bstack11111111l1_opy_=self.bstack11111l1l1l_opy_, frameworks=[bstack1111l1ll1l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1111ll1l1l_opy_((bstack111111lll1_opy_.BEFORE_EACH, bstack11111111ll_opy_.POST), self.bstack1llllllll11_opy_)
        TestFramework.bstack1111ll1l1l_opy_((bstack111111lll1_opy_.TEST, bstack11111111ll_opy_.PRE), self.bstack111111ll11_opy_)
        TestFramework.bstack1111ll1l1l_opy_((bstack111111lll1_opy_.TEST, bstack11111111ll_opy_.POST), self.bstack1lllllll1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llllllll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
        *args,
        **kwargs,
    ):
        bstack11111l111l_opy_ = self.bstack111111l1ll_opy_(instance.context)
        if not bstack11111l111l_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦဣ") + str(bstack111l11llll_opy_) + bstack11l1l1l_opy_ (u"ࠤࠥဤ"))
        f.bstack1111l1l11l_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll11ll_opy_, bstack11111l111l_opy_)
        bstack1111111lll_opy_ = self.bstack111111l1ll_opy_(instance.context, bstack1lllllll11l_opy_=False)
        f.bstack1111l1l11l_opy_(instance, bstack1lllllllll1_opy_.bstack1111111l11_opy_, bstack1111111lll_opy_)
    def bstack111111ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llllllll11_opy_(f, instance, bstack111l11llll_opy_, *args, **kwargs)
        if not f.bstack111l1111l1_opy_(instance, bstack1lllllllll1_opy_.bstack111111111l_opy_, False):
            self.__1lllllll111_opy_(f,instance,bstack111l11llll_opy_)
    def bstack1lllllll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llllllll11_opy_(f, instance, bstack111l11llll_opy_, *args, **kwargs)
        if not f.bstack111l1111l1_opy_(instance, bstack1lllllllll1_opy_.bstack111111111l_opy_, False):
            self.__1lllllll111_opy_(f, instance, bstack111l11llll_opy_)
        if not f.bstack111l1111l1_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll1ll1_opy_, False):
            self.__111111llll_opy_(f, instance, bstack111l11llll_opy_)
    def bstack11111l1111_opy_(
        self,
        f: bstack1111l1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack1111lllll1_opy_, str],
        bstack111l11llll_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack11111l1ll1_opy_(instance):
            return
        if f.bstack111l1111l1_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll1ll1_opy_, False):
            return
        driver.execute_script(
            bstack11l1l1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣဥ").format(
                json.dumps(
                    {
                        bstack11l1l1l_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦဦ"): bstack11l1l1l_opy_ (u"ࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣဧ"),
                        bstack11l1l1l_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤဨ"): {bstack11l1l1l_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢဩ"): result},
                    }
                )
            )
        )
        f.bstack1111l1l11l_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll1ll1_opy_, True)
    def bstack111111l1ll_opy_(self, context: bstack11111l1l11_opy_, bstack1lllllll11l_opy_= True):
        if bstack1lllllll11l_opy_:
            bstack11111l111l_opy_ = self.bstack111111l1l1_opy_(context, reverse=True)
        else:
            bstack11111l111l_opy_ = self.bstack11111l11l1_opy_(context, reverse=True)
        return [f for f in bstack11111l111l_opy_ if f[1].state != bstack1111l1llll_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1ll11lllll_opy_, stage=STAGE.SINGLE)
    def __111111llll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
    ):
        bstack11111l111l_opy_ = f.bstack111l1111l1_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll11ll_opy_, [])
        if not bstack11111l111l_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦဪ") + str(bstack111l11llll_opy_) + bstack11l1l1l_opy_ (u"ࠤࠥါ"))
            return
        driver = bstack11111l111l_opy_[0][0]()
        status = f.bstack111l1111l1_opy_(instance, TestFramework.bstack1111111111_opy_, None)
        if not status:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧာ") + str(bstack111l11llll_opy_) + bstack11l1l1l_opy_ (u"ࠦࠧိ"))
            return
        bstack1llllllll1l_opy_ = {bstack11l1l1l_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧီ"): status.lower()}
        bstack1111111l1l_opy_ = f.bstack111l1111l1_opy_(instance, TestFramework.bstack111111l11l_opy_, None)
        if status.lower() == bstack11l1l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ု") and bstack1111111l1l_opy_ is not None:
            bstack1llllllll1l_opy_[bstack11l1l1l_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧူ")] = bstack1111111l1l_opy_[0][bstack11l1l1l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫေ")][0] if isinstance(bstack1111111l1l_opy_, list) else str(bstack1111111l1l_opy_)
        driver.execute_script(
            bstack11l1l1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢဲ").format(
                json.dumps(
                    {
                        bstack11l1l1l_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥဳ"): bstack11l1l1l_opy_ (u"ࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢဴ"),
                        bstack11l1l1l_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣဵ"): bstack1llllllll1l_opy_,
                    }
                )
            )
        )
        f.bstack1111l1l11l_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll1ll1_opy_, True)
    def __1lllllll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_]
    ):
        test_name = f.bstack111l1111l1_opy_(instance, TestFramework.bstack11111l1lll_opy_, None)
        if not test_name:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡯ࡣࡰࡩࠧံ"))
            return
        bstack11111l111l_opy_ = f.bstack111l1111l1_opy_(instance, bstack1lllllllll1_opy_.bstack1llllll11ll_opy_, [])
        if not bstack11111l111l_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤ့") + str(bstack111l11llll_opy_) + bstack11l1l1l_opy_ (u"ࠣࠤး"))
            return
        for bstack1111111ll1_opy_, bstack1llllll1l1l_opy_ in bstack11111l111l_opy_:
            if not bstack1111l1ll1l_opy_.bstack11111l1ll1_opy_(bstack1llllll1l1l_opy_):
                continue
            driver = bstack1111111ll1_opy_()
            if not driver:
                continue
            driver.execute_script(
                bstack11l1l1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃ္ࠢ").format(
                    json.dumps(
                        {
                            bstack11l1l1l_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰ်ࠥ"): bstack11l1l1l_opy_ (u"ࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧျ"),
                            bstack11l1l1l_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣြ"): {bstack11l1l1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦွ"): test_name},
                        }
                    )
                )
            )
        f.bstack1111l1l11l_opy_(instance, bstack1lllllllll1_opy_.bstack111111111l_opy_, True)