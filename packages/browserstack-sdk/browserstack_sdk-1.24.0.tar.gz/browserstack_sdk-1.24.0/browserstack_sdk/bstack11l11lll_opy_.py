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
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack1ll111ll_opy_ import bstack1ll11ll1_opy_, bstack1ll11lll_opy_
from bstack_utils.bstack1l1l1ll1_opy_ import bstack1l1ll11l_opy_
from bstack_utils.helper import bstack11llll1l_opy_, bstack11llllll_opy_, Result
from bstack_utils.bstack11ll1lll_opy_ import bstack1l11l1ll_opy_
from bstack_utils.capture import bstack1ll1l11l_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11l11lll_opy_:
    def __init__(self):
        self.bstack1lllll11_opy_ = bstack1ll1l11l_opy_(self.bstack1ll1llll_opy_)
        self.tests = {}
    @staticmethod
    def bstack1ll1llll_opy_(log):
        if not (log[bstack11l1l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬू")] and log[bstack11l1l1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ृ")].strip()):
            return
        active = bstack1l1ll11l_opy_.bstack1l11ll1l_opy_()
        log = {
            bstack11l1l1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬॄ"): log[bstack11l1l1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ॅ")],
            bstack11l1l1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫॆ"): bstack11llllll_opy_(),
            bstack11l1l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪे"): log[bstack11l1l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫै")],
        }
        if active:
            if active[bstack11l1l1l_opy_ (u"ࠫࡹࡿࡰࡦࠩॉ")] == bstack11l1l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪॊ"):
                log[bstack11l1l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ो")] = active[bstack11l1l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧौ")]
            elif active[bstack11l1l1l_opy_ (u"ࠨࡶࡼࡴࡪ्࠭")] == bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺࠧॎ"):
                log[bstack11l1l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪॏ")] = active[bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫॐ")]
        bstack1l11l1ll_opy_.bstack1ll1111l_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack1lllll11_opy_.start()
        driver = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫ॑"), None)
        bstack1ll111ll_opy_ = bstack1ll11lll_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack11llllll_opy_(),
            file_path=attrs.feature.filename,
            result=bstack11l1l1l_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭॒ࠢ"),
            framework=bstack11l1l1l_opy_ (u"ࠧࡃࡧ࡫ࡥࡻ࡫ࠧ॓"),
            scope=[attrs.feature.name],
            bstack1l11llll_opy_=bstack1l11l1ll_opy_.bstack11lllll1_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack11l1l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ॔")] = bstack1ll111ll_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack1l11l1ll_opy_.bstack1ll11111_opy_(bstack11l1l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪॕ"), bstack1ll111ll_opy_)
    def end_test(self, attrs):
        bstack11ll1l1l_opy_ = {
            bstack11l1l1l_opy_ (u"ࠥࡲࡦࡳࡥࠣॖ"): attrs.feature.name,
            bstack11l1l1l_opy_ (u"ࠦࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠤॗ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack1ll111ll_opy_ = self.tests[current_test_uuid][bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨक़")]
        meta = {
            bstack11l1l1l_opy_ (u"ࠨࡦࡦࡣࡷࡹࡷ࡫ࠢख़"): bstack11ll1l1l_opy_,
            bstack11l1l1l_opy_ (u"ࠢࡴࡶࡨࡴࡸࠨग़"): bstack1ll111ll_opy_.meta.get(bstack11l1l1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧज़"), []),
            bstack11l1l1l_opy_ (u"ࠤࡶࡧࡪࡴࡡࡳ࡫ࡲࠦड़"): {
                bstack11l1l1l_opy_ (u"ࠥࡲࡦࡳࡥࠣढ़"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack1ll111ll_opy_.bstack11l1ll11_opy_(meta)
        bstack1ll111ll_opy_.bstack11l1ll1l_opy_(bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩफ़"), []))
        bstack11ll111l_opy_, exception = self._11l1lll1_opy_(attrs)
        bstack1ll1l111_opy_ = Result(result=attrs.status.name, exception=exception, bstack1llll111_opy_=[bstack11ll111l_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨय़")].stop(time=bstack11llllll_opy_(), duration=int(attrs.duration)*1000, result=bstack1ll1l111_opy_)
        bstack1l11l1ll_opy_.bstack1ll11111_opy_(bstack11l1l1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨॠ"), self.tests[threading.current_thread().current_test_uuid][bstack11l1l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪॡ")])
    def bstack11ll11ll_opy_(self, attrs):
        bstack1lll11ll_opy_ = {
            bstack11l1l1l_opy_ (u"ࠨ࡫ࡧࠫॢ"): uuid4().__str__(),
            bstack11l1l1l_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪॣ"): attrs.keyword,
            bstack11l1l1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡠࡣࡵ࡫ࡺࡳࡥ࡯ࡶࠪ।"): [],
            bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡸࡵࠩ॥"): attrs.name,
            bstack11l1l1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ०"): bstack11llllll_opy_(),
            bstack11l1l1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭१"): bstack11l1l1l_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ२"),
            bstack11l1l1l_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭३"): bstack11l1l1l_opy_ (u"ࠩࠪ४")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack11l1l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭५")].add_step(bstack1lll11ll_opy_)
        threading.current_thread().current_step_uuid = bstack1lll11ll_opy_[bstack11l1l1l_opy_ (u"ࠫ࡮ࡪࠧ६")]
    def bstack11ll1l11_opy_(self, attrs):
        current_test_id = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ७"), None)
        current_step_uuid = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡶࡨࡴࡤࡻࡵࡪࡦࠪ८"), None)
        bstack11ll111l_opy_, exception = self._11l1lll1_opy_(attrs)
        bstack1ll1l111_opy_ = Result(result=attrs.status.name, exception=exception, bstack1llll111_opy_=[bstack11ll111l_opy_])
        self.tests[current_test_id][bstack11l1l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ९")].bstack1l1ll111_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack1ll1l111_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack11l1l11l_opy_(self, name, attrs):
        try:
            bstack11ll11l1_opy_ = uuid4().__str__()
            self.tests[bstack11ll11l1_opy_] = {}
            self.bstack1lllll11_opy_.start()
            scopes = []
            driver = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ॰"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack11l1l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹࠧॱ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11ll11l1_opy_)
            if name in [bstack11l1l1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢॲ"), bstack11l1l1l_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠢॳ")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack11l1l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨॴ"), bstack11l1l1l_opy_ (u"ࠨࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪࠨॵ")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack11l1l1l_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨॶ")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack1ll11ll1_opy_(
                name=name,
                uuid=bstack11ll11l1_opy_,
                started_at=bstack11llllll_opy_(),
                file_path=file_path,
                framework=bstack11l1l1l_opy_ (u"ࠣࡄࡨ࡬ࡦࡼࡥࠣॷ"),
                bstack1l11llll_opy_=bstack1l11l1ll_opy_.bstack11lllll1_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack11l1l1l_opy_ (u"ࠤࡳࡩࡳࡪࡩ࡯ࡩࠥॸ"),
                hook_type=name
            )
            self.tests[bstack11ll11l1_opy_][bstack11l1l1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡦࡤࡸࡦࠨॹ")] = hook_data
            current_test_id = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠦࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠣॺ"), None)
            if current_test_id:
                hook_data.bstack11l1l1l1_opy_(current_test_id)
            if name == bstack11l1l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤॻ"):
                threading.current_thread().before_all_hook_uuid = bstack11ll11l1_opy_
            threading.current_thread().current_hook_uuid = bstack11ll11l1_opy_
            bstack1l11l1ll_opy_.bstack1ll11111_opy_(bstack11l1l1l_opy_ (u"ࠨࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠢॼ"), hook_data)
        except Exception as e:
            logger.debug(bstack11l1l1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡ࡫ࡱࠤࡸࡺࡡࡳࡶࠣ࡬ࡴࡵ࡫ࠡࡧࡹࡩࡳࡺࡳ࠭ࠢ࡫ࡳࡴࡱࠠ࡯ࡣࡰࡩ࠿ࠦࠥࡴ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠩࡸࠨॽ"), name, e)
    def bstack11l1l111_opy_(self, attrs):
        bstack1l1ll1ll_opy_ = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬॾ"), None)
        hook_data = self.tests[bstack1l1ll1ll_opy_][bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬॿ")]
        status = bstack11l1l1l_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥঀ")
        exception = None
        bstack11ll111l_opy_ = None
        if hook_data.name == bstack11l1l1l_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠢঁ"):
            self.bstack1lllll11_opy_.reset()
            bstack11l1l1ll_opy_ = self.tests[bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬং"), None)][bstack11l1l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩঃ")].result.result
            if bstack11l1l1ll_opy_ == bstack11l1l1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ঄"):
                if attrs.hook_failures == 1:
                    status = bstack11l1l1l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣঅ")
                elif attrs.hook_failures == 2:
                    status = bstack11l1l1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤআ")
            elif attrs.bstack11ll1111_opy_:
                status = bstack11l1l1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥই")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack11l1l1l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠨঈ") and attrs.hook_failures == 1:
                status = bstack11l1l1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧউ")
            elif hasattr(attrs, bstack11l1l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࡤࡳࡥࡴࡵࡤ࡫ࡪ࠭ঊ")) and attrs.error_message:
                status = bstack11l1l1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢঋ")
            bstack11ll111l_opy_, exception = self._11l1lll1_opy_(attrs)
        bstack1ll1l111_opy_ = Result(result=status, exception=exception, bstack1llll111_opy_=[bstack11ll111l_opy_])
        hook_data.stop(time=bstack11llllll_opy_(), duration=0, result=bstack1ll1l111_opy_)
        bstack1l11l1ll_opy_.bstack1ll11111_opy_(bstack11l1l1l_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪঌ"), self.tests[bstack1l1ll1ll_opy_][bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ঍")])
        threading.current_thread().current_hook_uuid = None
    def _11l1lll1_opy_(self, attrs):
        try:
            import traceback
            bstack11l1llll_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11ll111l_opy_ = bstack11l1llll_opy_[-1] if bstack11l1llll_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack11l1l1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡲࡧࡨࡻࡲࡳࡧࡧࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡨࡻࡳࡵࡱࡰࠤࡹࡸࡡࡤࡧࡥࡥࡨࡱࠢ঎"))
            bstack11ll111l_opy_ = None
            exception = None
        return bstack11ll111l_opy_, exception