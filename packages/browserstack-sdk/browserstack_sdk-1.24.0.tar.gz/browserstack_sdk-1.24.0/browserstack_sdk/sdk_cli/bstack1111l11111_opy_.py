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
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1111l1l1l1_opy_ import bstack1111l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import (
    bstack1111l1llll_opy_,
    bstack111l111111_opy_,
    bstack1111lllll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack11111ll1ll_opy_ import bstack1111l1ll1l_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1l1ll11l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack11ll1111l1_opy_ import bstack1111lll111_opy_
class bstack1111l111l1_opy_(bstack1111l1ll11_opy_):
    bstack1111l1l111_opy_ = bstack11l1l1l_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣ࡮ࡴࡩࡵࠤ࿉")
    bstack111l111l1l_opy_ = bstack11l1l1l_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡢࡴࡷࠦ࿊")
    bstack111l1l11l1_opy_ = bstack11l1l1l_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡱࡳࠦ࿋")
    def __init__(self):
        super().__init__()
        bstack1111l1ll1l_opy_.bstack1111ll1l1l_opy_((bstack1111l1llll_opy_.bstack11111lll1l_opy_, bstack111l111111_opy_.PRE), self.bstack1111l1l1ll_opy_)
        bstack1111l1ll1l_opy_.bstack1111ll1l1l_opy_((bstack1111l1llll_opy_.bstack111l11111l_opy_, bstack111l111111_opy_.PRE), self.bstack1111l111ll_opy_)
        bstack1111l1ll1l_opy_.bstack1111ll1l1l_opy_((bstack1111l1llll_opy_.bstack111l11111l_opy_, bstack111l111111_opy_.POST), self.bstack1111llllll_opy_)
        bstack1111l1ll1l_opy_.bstack1111ll1l1l_opy_((bstack1111l1llll_opy_.bstack111l11111l_opy_, bstack111l111111_opy_.POST), self.bstack1111llll1l_opy_)
        bstack1111l1ll1l_opy_.bstack1111ll1l1l_opy_((bstack1111l1llll_opy_.QUIT, bstack111l111111_opy_.POST), self.bstack111l111l11_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1111l1l1ll_opy_(
        self,
        f: bstack1111l1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack1111lllll1_opy_, str],
        bstack111l11llll_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l1l1l_opy_ (u"ࠧࡥ࡟ࡪࡰ࡬ࡸࡤࡥࠢ࿌"):
            return
        def wrapped(driver, init, *args, **kwargs):
            self.bstack111l11ll11_opy_(instance, f, kwargs)
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷ࠴ࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾ࠽ࡼࡨ࠱ࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࢁ࠿ࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧ࿍") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠢࠣ࿎"))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
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
        instance, method_name = exec
        if f.bstack111l1111l1_opy_(instance, bstack1111l111l1_opy_.bstack1111l1l111_opy_, False):
            return
        if not f.bstack1111ll111l_opy_(instance, bstack1111l1ll1l_opy_.bstack1111ll11l1_opy_):
            return
        platform_index = f.bstack111l1111l1_opy_(instance, bstack1111l1ll1l_opy_.bstack1111ll11l1_opy_)
        if f.bstack111l11l1ll_opy_(method_name, *args) and len(args) > 1:
            bstack1l1lll1l1l_opy_ = datetime.now()
            hub_url = bstack1111l1ll1l_opy_.hub_url(driver)
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠣࡪࡸࡦࡤࡻࡲ࡭࠿ࠥ࿏") + str(hub_url) + bstack11l1l1l_opy_ (u"ࠤࠥ࿐"))
            bstack1111lll1ll_opy_ = args[1][bstack11l1l1l_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤ࿑")] if isinstance(args[1], dict) and bstack11l1l1l_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥ࿒") in args[1] else None
            bstack111l1l111l_opy_ = bstack11l1l1l_opy_ (u"ࠧࡧ࡬ࡸࡣࡼࡷࡒࡧࡴࡤࡪࠥ࿓")
            if isinstance(bstack1111lll1ll_opy_, dict):
                bstack1l1lll1l1l_opy_ = datetime.now()
                r = self.bstack111l11l1l1_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡩ࡯࡫ࡷࠦ࿔"), datetime.now() - bstack1l1lll1l1l_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack11l1l1l_opy_ (u"ࠢࡴࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭࠺ࠡࠤ࿕") + str(r) + bstack11l1l1l_opy_ (u"ࠣࠤ࿖"))
                        return
                    if r.hub_url:
                        f.bstack111l11lll1_opy_(instance, driver, r.hub_url)
                        f.bstack1111l1l11l_opy_(instance, bstack1111l111l1_opy_.bstack1111l1l111_opy_, True)
                except Exception as e:
                    self.logger.error(bstack11l1l1l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ࿗"), e)
    def bstack1111llllll_opy_(
        self,
        f: bstack1111l1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack1111lllll1_opy_, str],
        bstack111l11llll_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1111l1ll1l_opy_.session_id(driver)
            if session_id:
                bstack1111ll1ll1_opy_ = bstack1111ll1ll1_opy_ = bstack11l1l1l_opy_ (u"ࠥࡿࢂࡀࡳࡵࡣࡵࡸࠧ࿘").format(session_id)
                bstack1111lll111_opy_.mark(bstack1111ll1ll1_opy_)
    def bstack1111llll1l_opy_(
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
        if f.bstack111l1111l1_opy_(instance, bstack1111l111l1_opy_.bstack111l111l1l_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1111l1ll1l_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡨࡶࡤࡢࡹࡷࡲ࠽ࠣ࿙") + str(hub_url) + bstack11l1l1l_opy_ (u"ࠧࠨ࿚"))
            return
        framework_session_id = bstack1111l1ll1l_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack11l1l1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠾ࠤ࿛") + str(framework_session_id) + bstack11l1l1l_opy_ (u"ࠢࠣ࿜"))
            return
        if bstack1111l1ll1l_opy_.bstack1111lll11l_opy_(*args) == bstack1111l1ll1l_opy_.bstack1111ll1lll_opy_:
            bstack11111lllll_opy_ = bstack11l1l1l_opy_ (u"ࠣࡽࢀ࠾ࡪࡴࡤࠣ࿝").format(framework_session_id)
            bstack1111ll1ll1_opy_ = bstack11l1l1l_opy_ (u"ࠤࡾࢁ࠿ࡹࡴࡢࡴࡷࠦ࿞").format(framework_session_id)
            bstack1111lll111_opy_.end(
                label=bstack11l1l1l_opy_ (u"ࠥࡷࡩࡱ࠺ࡥࡴ࡬ࡺࡪࡸ࠺ࡱࡱࡶࡸ࠲࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡢࡶ࡬ࡳࡳࠨ࿟"),
                start=bstack1111ll1ll1_opy_,
                end=bstack11111lllll_opy_,
                status=True,
                failure=None
            )
            bstack1l1lll1l1l_opy_ = datetime.now()
            r = self.bstack111l1l11ll_opy_(
                ref,
                f.bstack111l1111l1_opy_(instance, bstack1111l1ll1l_opy_.bstack1111ll11l1_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶࠥ࿠"), datetime.now() - bstack1l1lll1l1l_opy_)
            f.bstack1111l1l11l_opy_(instance, bstack1111l111l1_opy_.bstack111l111l1l_opy_, r.success)
    def bstack111l111l11_opy_(
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
        if f.bstack111l1111l1_opy_(instance, bstack1111l111l1_opy_.bstack111l1l11l1_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1111l1ll1l_opy_.session_id(driver)
        hub_url = bstack1111l1ll1l_opy_.hub_url(driver)
        bstack1l1lll1l1l_opy_ = datetime.now()
        r = self.bstack11111lll11_opy_(
            ref,
            f.bstack111l1111l1_opy_(instance, bstack1111l1ll1l_opy_.bstack1111ll11l1_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲࠥ࿡"), datetime.now() - bstack1l1lll1l1l_opy_)
        f.bstack1111l1l11l_opy_(instance, bstack1111l111l1_opy_.bstack111l1l11l1_opy_, r.success)
    @measure(event_name=EVENTS.bstack111l11l11l_opy_, stage=STAGE.SINGLE)
    def bstack111l11l111_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡹࡨࡦࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࠼ࠣࠦ࿢") + str(req) + bstack11l1l1l_opy_ (u"ࠢࠣ࿣"))
        try:
            r = self.bstack1111l11ll1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࡶࡹࡨࡩࡥࡴࡵࡀࠦ࿤") + str(r.success) + bstack11l1l1l_opy_ (u"ࠤࠥ࿥"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣ࿦") + str(e) + bstack11l1l1l_opy_ (u"ࠦࠧ࿧"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1111l11l11_opy_, stage=STAGE.SINGLE)
    def bstack111l11l1l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1111l11l1l_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢ࿨") + str(req) + bstack11l1l1l_opy_ (u"ࠨࠢ࿩"))
        try:
            r = self.bstack1111l11ll1_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࡵࡸࡧࡨ࡫ࡳࡴ࠿ࠥ࿪") + str(r.success) + bstack11l1l1l_opy_ (u"ࠣࠤ࿫"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢ࿬") + str(e) + bstack11l1l1l_opy_ (u"ࠥࠦ࿭"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1111ll1l11_opy_, stage=STAGE.SINGLE)
    def bstack111l1l11ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1111l11l1l_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡣࡵࡸ࠿ࠦࠢ࿮") + str(req) + bstack11l1l1l_opy_ (u"ࠧࠨ࿯"))
        try:
            r = self.bstack1111l11ll1_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣ࿰") + str(r) + bstack11l1l1l_opy_ (u"ࠢࠣ࿱"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨ࿲") + str(e) + bstack11l1l1l_opy_ (u"ࠤࠥ࿳"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack111l1111ll_opy_, stage=STAGE.SINGLE)
    def bstack11111lll11_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1111l11l1l_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲ࠽ࠤࠧ࿴") + str(req) + bstack11l1l1l_opy_ (u"ࠦࠧ࿵"))
        try:
            r = self.bstack1111l11ll1_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢ࿶") + str(r) + bstack11l1l1l_opy_ (u"ࠨࠢ࿷"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧ࿸") + str(e) + bstack11l1l1l_opy_ (u"ࠣࠤ࿹"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack11l1ll1lll_opy_, stage=STAGE.SINGLE)
    def bstack111l11ll11_opy_(self, instance: bstack1111lllll1_opy_, f: bstack1111l1ll1l_opy_, kwargs):
        bstack1111ll11ll_opy_ = version.parse(f.framework_version)
        bstack111l111ll1_opy_ = kwargs.get(bstack11l1l1l_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥ࿺"))
        bstack1111l1lll1_opy_ = kwargs.get(bstack11l1l1l_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥ࿻"))
        bstack1111l1111l_opy_ = {}
        bstack1111lll1l1_opy_ = {}
        bstack11111llll1_opy_ = None
        bstack111l111lll_opy_ = {}
        if bstack1111l1lll1_opy_ is not None or bstack111l111ll1_opy_ is not None: # check top level caps
            if bstack1111l1lll1_opy_ is not None:
                bstack111l111lll_opy_[bstack11l1l1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ࿼")] = bstack1111l1lll1_opy_
            if bstack111l111ll1_opy_ is not None and callable(getattr(bstack111l111ll1_opy_, bstack11l1l1l_opy_ (u"ࠧࡺ࡯ࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢ࿽"))):
                bstack111l111lll_opy_[bstack11l1l1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡢࡵࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ࿾")] = bstack111l111ll1_opy_.to_capabilities()
        response = self.bstack111l11l111_opy_(f.platform_index, instance.ref(), json.dumps(bstack111l111lll_opy_).encode(bstack11l1l1l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨ࿿")))
        if response is not None and response.capabilities:
            bstack1111l1111l_opy_ = json.loads(response.capabilities.decode(bstack11l1l1l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢက")))
            if not bstack1111l1111l_opy_: # empty caps bstack111l11ll1l_opy_ bstack111l1l1l1l_opy_ bstack111l1l1111_opy_ bstack1111llll11_opy_ or error in processing
                return
            bstack11111llll1_opy_ = f.bstack1111ll1111_opy_[bstack11l1l1l_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࡢࡪࡷࡵ࡭ࡠࡥࡤࡴࡸࠨခ")](bstack1111l1111l_opy_)
        if bstack111l111ll1_opy_ is not None and bstack1111ll11ll_opy_ >= version.parse(bstack11l1l1l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩဂ")):
            bstack1111lll1l1_opy_ = None
        if (
                not bstack111l111ll1_opy_ and not bstack1111l1lll1_opy_
        ) or (
                bstack1111ll11ll_opy_ < version.parse(bstack11l1l1l_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪဃ"))
        ):
            bstack1111lll1l1_opy_ = {}
            bstack1111lll1l1_opy_.update(bstack1111l1111l_opy_)
        self.logger.info(bstack1l1ll11l1_opy_)
        if os.environ.get(bstack11l1l1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠣင")).lower().__eq__(bstack11l1l1l_opy_ (u"ࠨࡴࡳࡷࡨࠦစ")):
            kwargs.update(
                {
                    bstack11l1l1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥဆ"): f.bstack111l1l1l11_opy_,
                }
            )
        if bstack1111ll11ll_opy_ >= version.parse(bstack11l1l1l_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨဇ")):
            if bstack1111l1lll1_opy_ is not None:
                del kwargs[bstack11l1l1l_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤဈ")]
            kwargs.update(
                {
                    bstack11l1l1l_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦဉ"): bstack11111llll1_opy_,
                    bstack11l1l1l_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣည"): True,
                    bstack11l1l1l_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧဋ"): None,
                }
            )
        elif bstack1111ll11ll_opy_ >= version.parse(bstack11l1l1l_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬဌ")):
            kwargs.update(
                {
                    bstack11l1l1l_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢဍ"): bstack1111lll1l1_opy_,
                    bstack11l1l1l_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤဎ"): bstack11111llll1_opy_,
                    bstack11l1l1l_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨဏ"): True,
                    bstack11l1l1l_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥတ"): None,
                }
            )
        elif bstack1111ll11ll_opy_ >= version.parse(bstack11l1l1l_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫထ")):
            kwargs.update(
                {
                    bstack11l1l1l_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧဒ"): bstack1111lll1l1_opy_,
                    bstack11l1l1l_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥဓ"): True,
                    bstack11l1l1l_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢန"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack11l1l1l_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣပ"): bstack1111lll1l1_opy_,
                    bstack11l1l1l_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨဖ"): True,
                    bstack11l1l1l_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥဗ"): None,
                }
            )