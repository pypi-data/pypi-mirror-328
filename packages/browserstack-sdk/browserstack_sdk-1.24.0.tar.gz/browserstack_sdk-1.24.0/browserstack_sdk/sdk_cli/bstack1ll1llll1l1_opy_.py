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
    bstack1111lllll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack11111ll1ll_opy_ import bstack1111l1ll1l_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1111l1l1l1_opy_ import bstack1111l1ll11_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1ll1lllll1l_opy_(bstack1111l1ll11_opy_):
    bstack1ll1llllll1_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1111l1ll1l_opy_.bstack1111ll1l1l_opy_((bstack1111l1llll_opy_.bstack111l11111l_opy_, bstack111l111111_opy_.PRE), self.bstack1111l111ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1111l111ll_opy_(
        self,
        f: bstack1111l1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack1111lllll1_opy_, str],
        bstack111l11llll_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1lllll1lll1_opy_(hub_url):
            if not bstack1ll1lllll1l_opy_.bstack1ll1llllll1_opy_:
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠥࡰࡴࡩࡡ࡭ࠢࡶࡩࡱ࡬࠭ࡩࡧࡤࡰࠥ࡬࡬ࡰࡹࠣࡨ࡮ࡹࡡࡣ࡮ࡨࡨࠥ࡬࡯ࡳࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡ࡫ࡱࡪࡷࡧࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠢ࡫ࡹࡧࡥࡵࡳ࡮ࡀࠦჰ") + str(hub_url) + bstack11l1l1l_opy_ (u"ࠦࠧჱ"))
                bstack1ll1lllll1l_opy_.bstack1ll1llllll1_opy_ = True
            return
        bstack1lll1111111_opy_ = f.bstack1ll1lll11ll_opy_(*args)
        bstack1ll1lllll11_opy_ = f.bstack1ll1llll11l_opy_(*args)
        if bstack1lll1111111_opy_ and bstack1lll1111111_opy_.lower() == bstack11l1l1l_opy_ (u"ࠧ࡬ࡩ࡯ࡦࡨࡰࡪࡳࡥ࡯ࡶࠥჲ") and bstack1ll1lllll11_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1ll1lllll11_opy_.get(bstack11l1l1l_opy_ (u"ࠨࡵࡴ࡫ࡱ࡫ࠧჳ"), None), bstack1ll1lllll11_opy_.get(bstack11l1l1l_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࠨჴ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠣࡽࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥࡾ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠤࡴࡸࠠࡢࡴࡪࡷ࠳ࡻࡳࡪࡰࡪࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡵࡲࠡࡣࡵ࡫ࡸ࠴ࡶࡢ࡮ࡸࡩࡂࠨჵ") + str(locator_value) + bstack11l1l1l_opy_ (u"ࠤࠥჶ"))
                return
            def bstack1ll1lllllll_opy_(driver, bstack1ll1llll111_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1ll1llll111_opy_(driver, *args, **kwargs)
                    response = self.bstack1ll1lll1l1l_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack11l1l1l_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶ࠱ࡸࡩࡲࡪࡲࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࠨჷ") + str(locator_value) + bstack11l1l1l_opy_ (u"ࠦࠧჸ"))
                    else:
                        self.logger.warning(bstack11l1l1l_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸ࠳࡮ࡰ࠯ࡶࡧࡷ࡯ࡰࡵ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࢁࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠽ࠣჹ") + str(response) + bstack11l1l1l_opy_ (u"ࠨࠢჺ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1ll1llll1ll_opy_(
                        driver, bstack1ll1llll111_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1ll1lllllll_opy_.__name__ = bstack1lll1111111_opy_
            return bstack1ll1lllllll_opy_
    def __1ll1llll1ll_opy_(
        self,
        driver,
        bstack1ll1llll111_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1ll1lll1l1l_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack11l1l1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡪࡨࡥࡱ࡯࡮ࡨ࠯ࡷࡶ࡮࡭ࡧࡦࡴࡨࡨ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࠢ჻") + str(locator_value) + bstack11l1l1l_opy_ (u"ࠣࠤჼ"))
                bstack1ll1lll1ll1_opy_ = self.bstack1ll1lll1l11_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack11l1l1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰࡬ࡪࡧ࡬ࡪࡰࡪ࠱ࡷ࡫ࡳࡶ࡮ࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࢃࠠࡩࡧࡤࡰ࡮ࡴࡧࡠࡴࡨࡷࡺࡲࡴ࠾ࠤჽ") + str(bstack1ll1lll1ll1_opy_) + bstack11l1l1l_opy_ (u"ࠥࠦჾ"))
                if bstack1ll1lll1ll1_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack11l1l1l_opy_ (u"ࠦࡺࡹࡩ࡯ࡩࠥჿ"): bstack1ll1lll1ll1_opy_.locator_type,
                            bstack11l1l1l_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦᄀ"): bstack1ll1lll1ll1_opy_.locator_value,
                        }
                    )
                    return bstack1ll1llll111_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡉࡠࡆࡈࡆ࡚ࡍࠢᄁ"), False):
                    self.logger.info(bstack1ll1lll111l_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡪࡨࡥࡱ࡯࡮ࡨ࠯ࡵࡩࡸࡻ࡬ࡵ࠯ࡰ࡭ࡸࡹࡩ࡯ࡩ࠽ࠤࡸࡲࡥࡦࡲࠫ࠷࠵࠯ࠠ࡭ࡧࡷࡸ࡮ࡴࡧࠡࡻࡲࡹࠥ࡯࡮ࡴࡲࡨࡧࡹࠦࡴࡩࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࠠ࡭ࡱࡪࡷࠧᄂ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯ࡱࡳ࠲ࡹࡣࡳ࡫ࡳࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫ࡽࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࡀࠦᄃ") + str(response) + bstack11l1l1l_opy_ (u"ࠤࠥᄄ"))
        except Exception as err:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡸࡥࡴࡷ࡯ࡸ࠿ࠦࡥࡳࡴࡲࡶ࠿ࠦࠢᄅ") + str(err) + bstack11l1l1l_opy_ (u"ࠦࠧᄆ"))
        raise exception
    @measure(event_name=EVENTS.bstack1ll1lll1lll_opy_, stage=STAGE.SINGLE)
    def bstack1ll1lll1l1l_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack11l1l1l_opy_ (u"ࠧ࠶ࠢᄇ"),
    ):
        self.bstack1111l11l1l_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack11l1l1l_opy_ (u"ࠨࠢᄈ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1111l11ll1_opy_.AISelfHealStep(req)
            self.logger.info(bstack11l1l1l_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᄉ") + str(r) + bstack11l1l1l_opy_ (u"ࠣࠤᄊ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᄋ") + str(e) + bstack11l1l1l_opy_ (u"ࠥࠦᄌ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1ll1lll11l1_opy_, stage=STAGE.SINGLE)
    def bstack1ll1lll1l11_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack11l1l1l_opy_ (u"ࠦ࠵ࠨᄍ")):
        self.bstack1111l11l1l_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1111l11ll1_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack11l1l1l_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᄎ") + str(r) + bstack11l1l1l_opy_ (u"ࠨࠢᄏ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᄐ") + str(e) + bstack11l1l1l_opy_ (u"ࠣࠤᄑ"))
            traceback.print_exc()
            raise e