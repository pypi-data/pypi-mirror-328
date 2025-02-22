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
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack11ll1111l1_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1llllll1ll_opy_, bstack11lll1l11l_opy_, update, bstack11lllll1l1_opy_,
                                       bstack11lll1llll_opy_, bstack1l1111lll1_opy_, bstack1llll1l1l1_opy_, bstack1l1lll1ll1_opy_,
                                       bstack11l11l1lll_opy_, bstack1ll1l111l1_opy_, bstack1ll11l1l11_opy_, bstack11llllll1l_opy_,
                                       bstack111111l11_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1l1l111l1_opy_)
from browserstack_sdk.bstack111l11l1_opy_ import bstack111lll1l_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack111111l1l_opy_
from bstack_utils.capture import bstack1ll1l11l_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack11lll1l1ll_opy_, bstack1111111ll_opy_, bstack1llll11l11_opy_, \
    bstack1ll1l11ll1_opy_
from bstack_utils.helper import bstack11llll1l_opy_, bstack11ll1ll1l11_opy_, bstack1ll1l1l1_opy_, bstack1l11l111ll_opy_, bstack1l1llll111l_opy_, bstack11llllll_opy_, \
    bstack11ll1lllll1_opy_, \
    bstack11lllll1l11_opy_, bstack1ll1l1111l_opy_, bstack1llll111l1_opy_, bstack11lll1ll111_opy_, bstack11l1ll111l_opy_, Notset, \
    bstack1l11ll1lll_opy_, bstack11lll11ll11_opy_, bstack11lll1lllll_opy_, Result, bstack1l11111l1ll_opy_, bstack11ll1lll11l_opy_, bstack1ll111l1_opy_, \
    bstack1l11ll11ll_opy_, bstack11ll11ll1l_opy_, bstack1l1llllll1_opy_, bstack1l11111llll_opy_
from bstack_utils.bstack1l11lll1l1l_opy_ import bstack1l11llll11l_opy_
from bstack_utils.messages import bstack11ll11l11l_opy_, bstack1ll1lllll1_opy_, bstack1l1ll11l1_opy_, bstack11l11lll11_opy_, bstack1111ll1l_opy_, \
    bstack1l11l11l1l_opy_, bstack1ll11ll11_opy_, bstack1l1111ll1l_opy_, bstack1l111l111l_opy_, bstack11ll1llll_opy_, \
    bstack1l1l1111l1_opy_, bstack1l11l11lll_opy_
from bstack_utils.proxy import bstack1lll1111l1_opy_, bstack1lll11l11l_opy_
from bstack_utils.bstack11ll11l111_opy_ import bstack1l111llll11_opy_, bstack1l111lll11l_opy_, bstack1l111ll1l11_opy_, bstack1l111ll1111_opy_, \
    bstack1l111ll1ll1_opy_, bstack1l111ll11ll_opy_, bstack1l111ll111l_opy_, bstack1l1l1ll1l1_opy_, bstack1l111lll111_opy_
from bstack_utils.bstack1l11111l1l_opy_ import bstack1lll1lll1l_opy_
from bstack_utils.bstack1ll1111l1l_opy_ import bstack1l1lllll1l_opy_, bstack111llllll_opy_, bstack1l111111l1_opy_, \
    bstack11ll11l1ll_opy_, bstack11lll1ll1_opy_
from bstack_utils.bstack1ll111ll_opy_ import bstack1ll11lll_opy_
from bstack_utils.bstack1l1l1ll1_opy_ import bstack1l1ll11l_opy_
import bstack_utils.accessibility as bstack111lllll_opy_
from bstack_utils.bstack11ll1lll_opy_ import bstack1l11l1ll_opy_
from bstack_utils.bstack1111111l1_opy_ import bstack1111111l1_opy_
from browserstack_sdk.__init__ import bstack1lllll111l_opy_
from browserstack_sdk.sdk_cli.bstack1ll11l1ll1l_opy_ import bstack1ll11l11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1l1llll11l_opy_ import bstack1l1llll11l_opy_, Events, bstack11l11lll1_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1lll1l11l1l_opy_, bstack111111lll1_opy_, bstack11111111ll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1l1llll11l_opy_ import bstack1l1llll11l_opy_, Events, bstack11l11lll1_opy_
bstack11l11l1ll1_opy_ = None
bstack1lll1lllll_opy_ = None
bstack1l1llll1l1_opy_ = None
bstack111lll1ll_opy_ = None
bstack1l1111l1ll_opy_ = None
bstack11llll111l_opy_ = None
bstack11l1l1l1l1_opy_ = None
bstack1lll1l111l_opy_ = None
bstack1l1ll1l1l1_opy_ = None
bstack1l1lll111_opy_ = None
bstack1l1l1l111l_opy_ = None
bstack1ll111ll11_opy_ = None
bstack1l11llll11_opy_ = None
bstack11l1ll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠨࠩᴼ")
CONFIG = {}
bstack1ll1111ll1_opy_ = False
bstack11l11111l_opy_ = bstack11l1l1l_opy_ (u"ࠩࠪᴽ")
bstack1ll1lll1l1_opy_ = bstack11l1l1l_opy_ (u"ࠪࠫᴾ")
bstack11ll11lll_opy_ = False
bstack11ll1ll1l_opy_ = []
bstack1l11l1111l_opy_ = bstack11lll1l1ll_opy_
bstack111llllll11_opy_ = bstack11l1l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᴿ")
bstack1llll1l111_opy_ = {}
bstack11l1ll111_opy_ = None
bstack1l1lll11l1_opy_ = False
logger = bstack111111l1l_opy_.get_logger(__name__, bstack1l11l1111l_opy_)
store = {
    bstack11l1l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᵀ"): []
}
bstack111llll1lll_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1llll11l_opy_ = {}
current_test_uuid = None
cli_context = bstack1lll1l11l1l_opy_(
    test_framework_name=bstack1lll11111l_opy_[bstack11l1l1l_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙࠳ࡂࡅࡆࠪᵁ")] if bstack11l1ll111l_opy_() else bstack1lll11111l_opy_[bstack11l1l1l_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚ࠧᵂ")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack1l1ll1ll1_opy_(page, bstack1l1ll1lll_opy_):
    try:
        page.evaluate(bstack11l1l1l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᵃ"),
                      bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭ᵄ") + json.dumps(
                          bstack1l1ll1lll_opy_) + bstack11l1l1l_opy_ (u"ࠥࢁࢂࠨᵅ"))
    except Exception as e:
        print(bstack11l1l1l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤᵆ"), e)
def bstack11ll1lllll_opy_(page, message, level):
    try:
        page.evaluate(bstack11l1l1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᵇ"), bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫᵈ") + json.dumps(
            message) + bstack11l1l1l_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪᵉ") + json.dumps(level) + bstack11l1l1l_opy_ (u"ࠨࡿࢀࠫᵊ"))
    except Exception as e:
        print(bstack11l1l1l_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁࠧᵋ"), e)
def pytest_configure(config):
    global bstack11l11111l_opy_
    global CONFIG
    bstack11111l11_opy_ = Config.bstack111ll1ll_opy_()
    config.args = bstack1l1ll11l_opy_.bstack1l11l1111l1_opy_(config.args)
    bstack11111l11_opy_.bstack1lllll1ll_opy_(bstack1l1llllll1_opy_(config.getoption(bstack11l1l1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᵌ"))))
    try:
        bstack111111l1l_opy_.bstack11ll1l11l11_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack1l1llll11l_opy_.invoke(Events.CONNECT, bstack11l11lll1_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11l1l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᵍ"), bstack11l1l1l_opy_ (u"ࠬ࠶ࠧᵎ")))
        config = json.loads(os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠧᵏ"), bstack11l1l1l_opy_ (u"ࠢࡼࡿࠥᵐ")))
        cli.bstack1ll1ll111ll_opy_(bstack1llll111l1_opy_(bstack11l11111l_opy_, CONFIG), cli_context.platform_index, bstack11lllll1l1_opy_)
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
        cli.bstack1ll111l1l1l_opy_()
        logger.debug(bstack11l1l1l_opy_ (u"ࠣࡅࡏࡍࠥ࡯ࡳࠡࡣࡦࡸ࡮ࡼࡥࠡࡨࡲࡶࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࠢᵑ") + str(cli_context.platform_index) + bstack11l1l1l_opy_ (u"ࠤࠥᵒ"))
        cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.BEFORE_ALL, bstack11111111ll_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack11l1l1l_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᵓ"), None)
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_) and when == bstack11l1l1l_opy_ (u"ࠦࡨࡧ࡬࡭ࠤᵔ"):
        cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.LOG_REPORT, bstack11111111ll_opy_.PRE, item, call)
    outcome = yield
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
        if when == bstack11l1l1l_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦᵕ"):
            cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.BEFORE_EACH, bstack11111111ll_opy_.POST, item, call, outcome)
        elif when == bstack11l1l1l_opy_ (u"ࠨࡣࡢ࡮࡯ࠦᵖ"):
            cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.LOG_REPORT, bstack11111111ll_opy_.POST, item, call, outcome)
        elif when == bstack11l1l1l_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤᵗ"):
            cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.AFTER_EACH, bstack11111111ll_opy_.POST, item, call, outcome)
        return # skip all existing bstack111lllll1l1_opy_
    bstack11l111111ll_opy_ = item.config.getoption(bstack11l1l1l_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᵘ"))
    plugins = item.config.getoption(bstack11l1l1l_opy_ (u"ࠤࡳࡰࡺ࡭ࡩ࡯ࡵࠥᵙ"))
    report = outcome.get_result()
    bstack111lllll1ll_opy_(item, call, report)
    if bstack11l1l1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠣᵚ") not in plugins or bstack11l1ll111l_opy_():
        return
    summary = []
    driver = getattr(item, bstack11l1l1l_opy_ (u"ࠦࡤࡪࡲࡪࡸࡨࡶࠧᵛ"), None)
    page = getattr(item, bstack11l1l1l_opy_ (u"ࠧࡥࡰࡢࡩࡨࠦᵜ"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack111llll1l11_opy_(item, report, summary, bstack11l111111ll_opy_)
    if (page is not None):
        bstack11l11111l11_opy_(item, report, summary, bstack11l111111ll_opy_)
def bstack111llll1l11_opy_(item, report, summary, bstack11l111111ll_opy_):
    if report.when == bstack11l1l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᵝ") and report.skipped:
        bstack1l111lll111_opy_(report)
    if report.when in [bstack11l1l1l_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨᵞ"), bstack11l1l1l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥᵟ")]:
        return
    if not bstack1l1llll111l_opy_():
        return
    try:
        if (str(bstack11l111111ll_opy_).lower() != bstack11l1l1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᵠ") and not cli.is_running()):
            item._driver.execute_script(
                bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨᵡ") + json.dumps(
                    report.nodeid) + bstack11l1l1l_opy_ (u"ࠫࢂࢃࠧᵢ"))
        os.environ[bstack11l1l1l_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨᵣ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11l1l1l_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥ࠻ࠢࡾ࠴ࢂࠨᵤ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11l1l1l_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤᵥ")))
    bstack11l11ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠣࠤᵦ")
    bstack1l111lll111_opy_(report)
    if not passed:
        try:
            bstack11l11ll1l_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11l1l1l_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡷ࡫ࡡࡴࡱࡱ࠾ࠥࢁ࠰ࡾࠤᵧ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack11l11ll1l_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11l1l1l_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᵨ")))
        bstack11l11ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠦࠧᵩ")
        if not passed:
            try:
                bstack11l11ll1l_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11l1l1l_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡳࡧࡤࡷࡴࡴ࠺ࠡࡽ࠳ࢁࠧᵪ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack11l11ll1l_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡧࡥࡹࡧࠢ࠻ࠢࠪᵫ")
                    + json.dumps(bstack11l1l1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠡࠣᵬ"))
                    + bstack11l1l1l_opy_ (u"ࠣ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࠦᵭ")
                )
            else:
                item._driver.execute_script(
                    bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡤࡢࡶࡤࠦ࠿ࠦࠧᵮ")
                    + json.dumps(str(bstack11l11ll1l_opy_))
                    + bstack11l1l1l_opy_ (u"ࠥࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࠨᵯ")
                )
        except Exception as e:
            summary.append(bstack11l1l1l_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡤࡲࡳࡵࡴࡢࡶࡨ࠾ࠥࢁ࠰ࡾࠤᵰ").format(e))
def bstack11l11111lll_opy_(test_name, error_message):
    try:
        bstack11l1111ll1l_opy_ = []
        bstack1l11lll11_opy_ = os.environ.get(bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᵱ"), bstack11l1l1l_opy_ (u"࠭࠰ࠨᵲ"))
        bstack1llll1111_opy_ = {bstack11l1l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᵳ"): test_name, bstack11l1l1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᵴ"): error_message, bstack11l1l1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᵵ"): bstack1l11lll11_opy_}
        bstack11l11111ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l1l_opy_ (u"ࠪࡴࡼࡥࡰࡺࡶࡨࡷࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᵶ"))
        if os.path.exists(bstack11l11111ll1_opy_):
            with open(bstack11l11111ll1_opy_) as f:
                bstack11l1111ll1l_opy_ = json.load(f)
        bstack11l1111ll1l_opy_.append(bstack1llll1111_opy_)
        with open(bstack11l11111ll1_opy_, bstack11l1l1l_opy_ (u"ࠫࡼ࠭ᵷ")) as f:
            json.dump(bstack11l1111ll1l_opy_, f)
    except Exception as e:
        logger.debug(bstack11l1l1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡧࡵࡷ࡮ࡹࡴࡪࡰࡪࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡲࡼࡸࡪࡹࡴࠡࡧࡵࡶࡴࡸࡳ࠻ࠢࠪᵸ") + str(e))
def bstack11l11111l11_opy_(item, report, summary, bstack11l111111ll_opy_):
    if report.when in [bstack11l1l1l_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧᵹ"), bstack11l1l1l_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤᵺ")]:
        return
    if (str(bstack11l111111ll_opy_).lower() != bstack11l1l1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᵻ")):
        bstack1l1ll1ll1_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11l1l1l_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦᵼ")))
    bstack11l11ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠥࠦᵽ")
    bstack1l111lll111_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack11l11ll1l_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11l1l1l_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡲࡦࡣࡶࡳࡳࡀࠠࡼ࠲ࢀࠦᵾ").format(e)
                )
        try:
            if passed:
                bstack11lll1ll1_opy_(getattr(item, bstack11l1l1l_opy_ (u"ࠬࡥࡰࡢࡩࡨࠫᵿ"), None), bstack11l1l1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨᶀ"))
            else:
                error_message = bstack11l1l1l_opy_ (u"ࠧࠨᶁ")
                if bstack11l11ll1l_opy_:
                    bstack11ll1lllll_opy_(item._page, str(bstack11l11ll1l_opy_), bstack11l1l1l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢᶂ"))
                    bstack11lll1ll1_opy_(getattr(item, bstack11l1l1l_opy_ (u"ࠩࡢࡴࡦ࡭ࡥࠨᶃ"), None), bstack11l1l1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥᶄ"), str(bstack11l11ll1l_opy_))
                    error_message = str(bstack11l11ll1l_opy_)
                else:
                    bstack11lll1ll1_opy_(getattr(item, bstack11l1l1l_opy_ (u"ࠫࡤࡶࡡࡨࡧࠪᶅ"), None), bstack11l1l1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧᶆ"))
                bstack11l11111lll_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11l1l1l_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡺࡶࡤࡢࡶࡨࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࡻ࠱ࡿࠥᶇ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack11l1l1l_opy_ (u"ࠢ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᶈ"), default=bstack11l1l1l_opy_ (u"ࠣࡈࡤࡰࡸ࡫ࠢᶉ"), help=bstack11l1l1l_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡧࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠣᶊ"))
    parser.addoption(bstack11l1l1l_opy_ (u"ࠥ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᶋ"), default=bstack11l1l1l_opy_ (u"ࠦࡋࡧ࡬ࡴࡧࠥᶌ"), help=bstack11l1l1l_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡯ࡣࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠦᶍ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11l1l1l_opy_ (u"ࠨ࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠣᶎ"), action=bstack11l1l1l_opy_ (u"ࠢࡴࡶࡲࡶࡪࠨᶏ"), default=bstack11l1l1l_opy_ (u"ࠣࡥ࡫ࡶࡴࡳࡥࠣᶐ"),
                         help=bstack11l1l1l_opy_ (u"ࠤࡇࡶ࡮ࡼࡥࡳࠢࡷࡳࠥࡸࡵ࡯ࠢࡷࡩࡸࡺࡳࠣᶑ"))
def bstack1ll1llll_opy_(log):
    if not (log[bstack11l1l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᶒ")] and log[bstack11l1l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᶓ")].strip()):
        return
    active = bstack1l11ll1l_opy_()
    log = {
        bstack11l1l1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᶔ"): log[bstack11l1l1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᶕ")],
        bstack11l1l1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᶖ"): bstack1ll1l1l1_opy_().isoformat() + bstack11l1l1l_opy_ (u"ࠨ࡜ࠪᶗ"),
        bstack11l1l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᶘ"): log[bstack11l1l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᶙ")],
    }
    if active:
        if active[bstack11l1l1l_opy_ (u"ࠫࡹࡿࡰࡦࠩᶚ")] == bstack11l1l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᶛ"):
            log[bstack11l1l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᶜ")] = active[bstack11l1l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᶝ")]
        elif active[bstack11l1l1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᶞ")] == bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺࠧᶟ"):
            log[bstack11l1l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᶠ")] = active[bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᶡ")]
    bstack1l11l1ll_opy_.bstack1ll1111l_opy_([log])
def bstack1l11ll1l_opy_():
    if len(store[bstack11l1l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᶢ")]) > 0 and store[bstack11l1l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᶣ")][-1]:
        return {
            bstack11l1l1l_opy_ (u"ࠧࡵࡻࡳࡩࠬᶤ"): bstack11l1l1l_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᶥ"),
            bstack11l1l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᶦ"): store[bstack11l1l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᶧ")][-1]
        }
    if store.get(bstack11l1l1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᶨ"), None):
        return {
            bstack11l1l1l_opy_ (u"ࠬࡺࡹࡱࡧࠪᶩ"): bstack11l1l1l_opy_ (u"࠭ࡴࡦࡵࡷࠫᶪ"),
            bstack11l1l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᶫ"): store[bstack11l1l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᶬ")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
        cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.INIT_TEST, bstack11111111ll_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
        cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.INIT_TEST, bstack11111111ll_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
        cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.TEST, bstack11111111ll_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._111llll111l_opy_ = True
        bstack111ll111l1_opy_ = bstack111lllll_opy_.bstack11l1l111ll_opy_(bstack11lllll1l11_opy_(item.own_markers))
        if not cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
            item._a11y_test_case = bstack111ll111l1_opy_
            if bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᶭ"), None):
                driver = getattr(item, bstack11l1l1l_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫᶮ"), None)
                item._a11y_started = bstack111lllll_opy_.bstack1l111l1l11_opy_(driver, bstack111ll111l1_opy_)
        if not bstack1l11l1ll_opy_.on() or bstack111llllll11_opy_ != bstack11l1l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᶯ"):
            return
        global current_test_uuid #, bstack1lllll11_opy_
        bstack1l1l111l_opy_ = {
            bstack11l1l1l_opy_ (u"ࠬࡻࡵࡪࡦࠪᶰ"): uuid4().__str__(),
            bstack11l1l1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᶱ"): bstack1ll1l1l1_opy_().isoformat() + bstack11l1l1l_opy_ (u"࡛ࠧࠩᶲ")
        }
        current_test_uuid = bstack1l1l111l_opy_[bstack11l1l1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᶳ")]
        store[bstack11l1l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᶴ")] = bstack1l1l111l_opy_[bstack11l1l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᶵ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1llll11l_opy_[item.nodeid] = {**_1llll11l_opy_[item.nodeid], **bstack1l1l111l_opy_}
        bstack11l111111l1_opy_(item, _1llll11l_opy_[item.nodeid], bstack11l1l1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᶶ"))
    except Exception as err:
        print(bstack11l1l1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡩࡡ࡭࡮࠽ࠤࢀࢃࠧᶷ"), str(err))
def pytest_runtest_setup(item):
    store[bstack11l1l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪᶸ")] = item
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
        cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.BEFORE_EACH, bstack11111111ll_opy_.PRE, item, bstack11l1l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᶹ"))
        return # skip all existing bstack111lllll1l1_opy_
    global bstack111llll1lll_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack11lll1ll111_opy_():
        atexit.register(bstack1l1l1ll111_opy_)
        if not bstack111llll1lll_opy_:
            try:
                bstack111llllll1l_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack1l11111llll_opy_():
                    bstack111llllll1l_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack111llllll1l_opy_:
                    signal.signal(s, bstack11l11111l1l_opy_)
                bstack111llll1lll_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11l1l1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪ࡭ࡩࡴࡶࡨࡶࠥࡹࡩࡨࡰࡤࡰࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࡹ࠺ࠡࠤᶺ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1l111llll11_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11l1l1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᶻ")
    try:
        if not bstack1l11l1ll_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack1l1l111l_opy_ = {
            bstack11l1l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᶼ"): uuid,
            bstack11l1l1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᶽ"): bstack1ll1l1l1_opy_().isoformat() + bstack11l1l1l_opy_ (u"ࠬࡠࠧᶾ"),
            bstack11l1l1l_opy_ (u"࠭ࡴࡺࡲࡨࠫᶿ"): bstack11l1l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࠬ᷀"),
            bstack11l1l1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ᷁"): bstack11l1l1l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎ᷂ࠧ"),
            bstack11l1l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭᷃"): bstack11l1l1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ᷄")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11l1l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ᷅")] = item
        store[bstack11l1l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ᷆")] = [uuid]
        if not _1llll11l_opy_.get(item.nodeid, None):
            _1llll11l_opy_[item.nodeid] = {bstack11l1l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭᷇"): [], bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪ᷈"): []}
        _1llll11l_opy_[item.nodeid][bstack11l1l1l_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ᷉")].append(bstack1l1l111l_opy_[bstack11l1l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ᷊")])
        _1llll11l_opy_[item.nodeid + bstack11l1l1l_opy_ (u"ࠫ࠲ࡹࡥࡵࡷࡳࠫ᷋")] = bstack1l1l111l_opy_
        bstack11l1111ll11_opy_(item, bstack1l1l111l_opy_, bstack11l1l1l_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭᷌"))
    except Exception as err:
        print(bstack11l1l1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡳࡦࡶࡸࡴ࠿ࠦࡻࡾࠩ᷍"), str(err))
def pytest_runtest_teardown(item):
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
        cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.TEST, bstack11111111ll_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.AFTER_EACH, bstack11111111ll_opy_.PRE, item, bstack11l1l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯᷎ࠩ"))
        return # skip all existing bstack111lllll1l1_opy_
    try:
        global bstack1llll1l111_opy_
        bstack1l11lll11_opy_ = 0
        if bstack11ll11lll_opy_ is True:
            bstack1l11lll11_opy_ = int(os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ᷏")))
        if bstack11111l111_opy_.bstack1ll11l111_opy_() == bstack11l1l1l_opy_ (u"ࠤࡷࡶࡺ࡫᷐ࠢ"):
            if bstack11111l111_opy_.bstack1l11l1l1l1_opy_() == bstack11l1l1l_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧ᷑"):
                bstack11l1111l1ll_opy_ = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ᷒"), None)
                bstack11l11l111_opy_ = bstack11l1111l1ll_opy_ + bstack11l1l1l_opy_ (u"ࠧ࠳ࡴࡦࡵࡷࡧࡦࡹࡥࠣᷓ")
                driver = getattr(item, bstack11l1l1l_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᷔ"), None)
                bstack11lll11l11_opy_ = getattr(item, bstack11l1l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᷕ"), None)
                bstack111lllll11_opy_ = getattr(item, bstack11l1l1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᷖ"), None)
                PercySDK.screenshot(driver, bstack11l11l111_opy_, bstack11lll11l11_opy_=bstack11lll11l11_opy_, bstack111lllll11_opy_=bstack111lllll11_opy_, bstack1ll11l11l1_opy_=bstack1l11lll11_opy_)
        if not cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
            if getattr(item, bstack11l1l1l_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡵࡷࡥࡷࡺࡥࡥࠩᷗ"), False):
                bstack111lll1l_opy_.bstack111lll11_opy_(getattr(item, bstack11l1l1l_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫᷘ"), None), bstack1llll1l111_opy_, logger, item)
        if not bstack1l11l1ll_opy_.on():
            return
        bstack1l1l111l_opy_ = {
            bstack11l1l1l_opy_ (u"ࠫࡺࡻࡩࡥࠩᷙ"): uuid4().__str__(),
            bstack11l1l1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᷚ"): bstack1ll1l1l1_opy_().isoformat() + bstack11l1l1l_opy_ (u"࡚࠭ࠨᷛ"),
            bstack11l1l1l_opy_ (u"ࠧࡵࡻࡳࡩࠬᷜ"): bstack11l1l1l_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᷝ"),
            bstack11l1l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᷞ"): bstack11l1l1l_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧᷟ"),
            bstack11l1l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠧᷠ"): bstack11l1l1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᷡ")
        }
        _1llll11l_opy_[item.nodeid + bstack11l1l1l_opy_ (u"࠭࠭ࡵࡧࡤࡶࡩࡵࡷ࡯ࠩᷢ")] = bstack1l1l111l_opy_
        bstack11l1111ll11_opy_(item, bstack1l1l111l_opy_, bstack11l1l1l_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᷣ"))
    except Exception as err:
        print(bstack11l1l1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡳࡷࡱࡸࡪࡹࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰ࠽ࠤࢀࢃࠧᷤ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack1l111ll1111_opy_(fixturedef.argname):
        store[bstack11l1l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡱࡴࡪࡵ࡭ࡧࡢ࡭ࡹ࡫࡭ࠨᷥ")] = request.node
    elif bstack1l111ll1ll1_opy_(fixturedef.argname):
        store[bstack11l1l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡨࡲࡡࡴࡵࡢ࡭ࡹ࡫࡭ࠨᷦ")] = request.node
    if not bstack1l11l1ll_opy_.on():
        if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
            cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.SETUP_FIXTURE, bstack11111111ll_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
            cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.SETUP_FIXTURE, bstack11111111ll_opy_.POST, fixturedef, request, outcome)
        return # skip all existing bstack111lllll1l1_opy_
    start_time = datetime.datetime.now()
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
        cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.SETUP_FIXTURE, bstack11111111ll_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
        cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.SETUP_FIXTURE, bstack11111111ll_opy_.POST, fixturedef, request, outcome)
        return # skip all existing bstack111lllll1l1_opy_
    try:
        fixture = {
            bstack11l1l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᷧ"): fixturedef.argname,
            bstack11l1l1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᷨ"): bstack11ll1lllll1_opy_(outcome),
            bstack11l1l1l_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨᷩ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11l1l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫᷪ")]
        if not _1llll11l_opy_.get(current_test_item.nodeid, None):
            _1llll11l_opy_[current_test_item.nodeid] = {bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪᷫ"): []}
        _1llll11l_opy_[current_test_item.nodeid][bstack11l1l1l_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫᷬ")].append(fixture)
    except Exception as err:
        logger.debug(bstack11l1l1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡷࡪࡺࡵࡱ࠼ࠣࡿࢂ࠭ᷭ"), str(err))
if bstack11l1ll111l_opy_() and bstack1l11l1ll_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
            cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.STEP, bstack11111111ll_opy_.PRE, request, step)
            return
        try:
            _1llll11l_opy_[request.node.nodeid][bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᷮ")].bstack11ll11ll_opy_(id(step))
        except Exception as err:
            print(bstack11l1l1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࡀࠠࡼࡿࠪᷯ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
            cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.STEP, bstack11111111ll_opy_.POST, request, step, exception)
            return
        try:
            _1llll11l_opy_[request.node.nodeid][bstack11l1l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᷰ")].bstack1l1ll111_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11l1l1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡷࡹ࡫ࡰࡠࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠫᷱ"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
            cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.STEP, bstack11111111ll_opy_.POST, request, step)
            return
        try:
            bstack1ll111ll_opy_: bstack1ll11lll_opy_ = _1llll11l_opy_[request.node.nodeid][bstack11l1l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᷲ")]
            bstack1ll111ll_opy_.bstack1l1ll111_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11l1l1l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡹࡴࡦࡲࡢࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂ࠭ᷳ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack111llllll11_opy_
        try:
            if not bstack1l11l1ll_opy_.on() or bstack111llllll11_opy_ != bstack11l1l1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧᷴ"):
                return
            if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
                cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.TEST, bstack11111111ll_opy_.PRE, request, feature, scenario)
                return
            driver = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ᷵"), None)
            if not _1llll11l_opy_.get(request.node.nodeid, None):
                _1llll11l_opy_[request.node.nodeid] = {}
            bstack1ll111ll_opy_ = bstack1ll11lll_opy_.bstack11ll1111ll1_opy_(
                scenario, feature, request.node,
                name=bstack1l111ll11ll_opy_(request.node, scenario),
                started_at=bstack11llllll_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11l1l1l_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧ᷶"),
                tags=bstack1l111ll111l_opy_(feature, scenario),
                bstack1l11llll_opy_=bstack1l11l1ll_opy_.bstack11lllll1_opy_(driver) if driver and driver.session_id else {}
            )
            _1llll11l_opy_[request.node.nodeid][bstack11l1l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢ᷷ࠩ")] = bstack1ll111ll_opy_
            bstack11l1111111l_opy_(bstack1ll111ll_opy_.uuid)
            bstack1l11l1ll_opy_.bstack1ll11111_opy_(bstack11l1l1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ᷸"), bstack1ll111ll_opy_)
        except Exception as err:
            print(bstack11l1l1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࡀࠠࡼࡿ᷹ࠪ"), str(err))
def bstack111lllll11l_opy_(bstack11ll11l1_opy_):
    if bstack11ll11l1_opy_ in store[bstack11l1l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ᷺࠭")]:
        store[bstack11l1l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ᷻")].remove(bstack11ll11l1_opy_)
def bstack11l1111111l_opy_(test_uuid):
    store[bstack11l1l1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ᷼")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack1l11l1ll_opy_.bstack11l11l1ll1l_opy_
def bstack111lllll1ll_opy_(item, call, report):
    logger.debug(bstack11l1l1l_opy_ (u"ࠬ࡮ࡡ࡯ࡦ࡯ࡩࡤࡵ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡵࡷࡥࡷࡺ᷽ࠧ"))
    global bstack111llllll11_opy_
    bstack1l11ll1ll_opy_ = bstack11llllll_opy_()
    if hasattr(report, bstack11l1l1l_opy_ (u"࠭ࡳࡵࡱࡳࠫ᷾")):
        bstack1l11ll1ll_opy_ = bstack1l11111l1ll_opy_(report.stop)
    elif hasattr(report, bstack11l1l1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ᷿࠭")):
        bstack1l11ll1ll_opy_ = bstack1l11111l1ll_opy_(report.start)
    try:
        if getattr(report, bstack11l1l1l_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭Ḁ"), bstack11l1l1l_opy_ (u"ࠩࠪḁ")) == bstack11l1l1l_opy_ (u"ࠪࡧࡦࡲ࡬ࠨḂ"):
            logger.debug(bstack11l1l1l_opy_ (u"ࠫ࡭ࡧ࡮ࡥ࡮ࡨࡣࡴ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡀࠠࡴࡶࡤࡸࡪࠦ࠭ࠡࡽࢀ࠰ࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠡ࠯ࠣࡿࢂ࠭ḃ").format(getattr(report, bstack11l1l1l_opy_ (u"ࠬࡽࡨࡦࡰࠪḄ"), bstack11l1l1l_opy_ (u"࠭ࠧḅ")).__str__(), bstack111llllll11_opy_))
            if bstack111llllll11_opy_ == bstack11l1l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧḆ"):
                _1llll11l_opy_[item.nodeid][bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ḇ")] = bstack1l11ll1ll_opy_
                bstack11l111111l1_opy_(item, _1llll11l_opy_[item.nodeid], bstack11l1l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫḈ"), report, call)
                store[bstack11l1l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧḉ")] = None
            elif bstack111llllll11_opy_ == bstack11l1l1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣḊ"):
                bstack1ll111ll_opy_ = _1llll11l_opy_[item.nodeid][bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨḋ")]
                bstack1ll111ll_opy_.set(hooks=_1llll11l_opy_[item.nodeid].get(bstack11l1l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬḌ"), []))
                exception, bstack1llll111_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1llll111_opy_ = [call.excinfo.exconly(), getattr(report, bstack11l1l1l_opy_ (u"ࠧ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹ࠭ḍ"), bstack11l1l1l_opy_ (u"ࠨࠩḎ"))]
                bstack1ll111ll_opy_.stop(time=bstack1l11ll1ll_opy_, result=Result(result=getattr(report, bstack11l1l1l_opy_ (u"ࠩࡲࡹࡹࡩ࡯࡮ࡧࠪḏ"), bstack11l1l1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪḐ")), exception=exception, bstack1llll111_opy_=bstack1llll111_opy_))
                bstack1l11l1ll_opy_.bstack1ll11111_opy_(bstack11l1l1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ḑ"), _1llll11l_opy_[item.nodeid][bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨḒ")])
        elif getattr(report, bstack11l1l1l_opy_ (u"࠭ࡷࡩࡧࡱࠫḓ"), bstack11l1l1l_opy_ (u"ࠧࠨḔ")) in [bstack11l1l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧḕ"), bstack11l1l1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫḖ")]:
            logger.debug(bstack11l1l1l_opy_ (u"ࠪ࡬ࡦࡴࡤ࡭ࡧࡢࡳ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡳࡵࡣࡷࡩࠥ࠳ࠠࡼࡿ࠯ࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠ࠮ࠢࡾࢁࠬḗ").format(getattr(report, bstack11l1l1l_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩḘ"), bstack11l1l1l_opy_ (u"ࠬ࠭ḙ")).__str__(), bstack111llllll11_opy_))
            bstack1l1ll1ll_opy_ = item.nodeid + bstack11l1l1l_opy_ (u"࠭࠭ࠨḚ") + getattr(report, bstack11l1l1l_opy_ (u"ࠧࡸࡪࡨࡲࠬḛ"), bstack11l1l1l_opy_ (u"ࠨࠩḜ"))
            if getattr(report, bstack11l1l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪḝ"), False):
                hook_type = bstack11l1l1l_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨḞ") if getattr(report, bstack11l1l1l_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩḟ"), bstack11l1l1l_opy_ (u"ࠬ࠭Ḡ")) == bstack11l1l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬḡ") else bstack11l1l1l_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫḢ")
                _1llll11l_opy_[bstack1l1ll1ll_opy_] = {
                    bstack11l1l1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ḣ"): uuid4().__str__(),
                    bstack11l1l1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭Ḥ"): bstack1l11ll1ll_opy_,
                    bstack11l1l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ḥ"): hook_type
                }
            _1llll11l_opy_[bstack1l1ll1ll_opy_][bstack11l1l1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩḦ")] = bstack1l11ll1ll_opy_
            bstack111lllll11l_opy_(_1llll11l_opy_[bstack1l1ll1ll_opy_][bstack11l1l1l_opy_ (u"ࠬࡻࡵࡪࡦࠪḧ")])
            bstack11l1111ll11_opy_(item, _1llll11l_opy_[bstack1l1ll1ll_opy_], bstack11l1l1l_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨḨ"), report, call)
            if getattr(report, bstack11l1l1l_opy_ (u"ࠧࡸࡪࡨࡲࠬḩ"), bstack11l1l1l_opy_ (u"ࠨࠩḪ")) == bstack11l1l1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨḫ"):
                if getattr(report, bstack11l1l1l_opy_ (u"ࠪࡳࡺࡺࡣࡰ࡯ࡨࠫḬ"), bstack11l1l1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫḭ")) == bstack11l1l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬḮ"):
                    bstack1l1l111l_opy_ = {
                        bstack11l1l1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫḯ"): uuid4().__str__(),
                        bstack11l1l1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫḰ"): bstack11llllll_opy_(),
                        bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ḱ"): bstack11llllll_opy_()
                    }
                    _1llll11l_opy_[item.nodeid] = {**_1llll11l_opy_[item.nodeid], **bstack1l1l111l_opy_}
                    bstack11l111111l1_opy_(item, _1llll11l_opy_[item.nodeid], bstack11l1l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪḲ"))
                    bstack11l111111l1_opy_(item, _1llll11l_opy_[item.nodeid], bstack11l1l1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬḳ"), report, call)
    except Exception as err:
        print(bstack11l1l1l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡢࡳ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡻࡾࠩḴ"), str(err))
def bstack11l1111lll1_opy_(test, bstack1l1l111l_opy_, result=None, call=None, bstack11111l11l_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1ll111ll_opy_ = {
        bstack11l1l1l_opy_ (u"ࠬࡻࡵࡪࡦࠪḵ"): bstack1l1l111l_opy_[bstack11l1l1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫḶ")],
        bstack11l1l1l_opy_ (u"ࠧࡵࡻࡳࡩࠬḷ"): bstack11l1l1l_opy_ (u"ࠨࡶࡨࡷࡹ࠭Ḹ"),
        bstack11l1l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧḹ"): test.name,
        bstack11l1l1l_opy_ (u"ࠪࡦࡴࡪࡹࠨḺ"): {
            bstack11l1l1l_opy_ (u"ࠫࡱࡧ࡮ࡨࠩḻ"): bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬḼ"),
            bstack11l1l1l_opy_ (u"࠭ࡣࡰࡦࡨࠫḽ"): inspect.getsource(test.obj)
        },
        bstack11l1l1l_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫḾ"): test.name,
        bstack11l1l1l_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࠧḿ"): test.name,
        bstack11l1l1l_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩṀ"): bstack1l1ll11l_opy_.bstack1l1l11ll_opy_(test),
        bstack11l1l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ṁ"): file_path,
        bstack11l1l1l_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭Ṃ"): file_path,
        bstack11l1l1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬṃ"): bstack11l1l1l_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧṄ"),
        bstack11l1l1l_opy_ (u"ࠧࡷࡥࡢࡪ࡮ࡲࡥࡱࡣࡷ࡬ࠬṅ"): file_path,
        bstack11l1l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬṆ"): bstack1l1l111l_opy_[bstack11l1l1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ṇ")],
        bstack11l1l1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭Ṉ"): bstack11l1l1l_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫṉ"),
        bstack11l1l1l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡗ࡫ࡲࡶࡰࡓࡥࡷࡧ࡭ࠨṊ"): {
            bstack11l1l1l_opy_ (u"࠭ࡲࡦࡴࡸࡲࡤࡴࡡ࡮ࡧࠪṋ"): test.nodeid
        },
        bstack11l1l1l_opy_ (u"ࠧࡵࡣࡪࡷࠬṌ"): bstack11lllll1l11_opy_(test.own_markers)
    }
    if bstack11111l11l_opy_ in [bstack11l1l1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩṍ"), bstack11l1l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫṎ")]:
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠪࡱࡪࡺࡡࠨṏ")] = {
            bstack11l1l1l_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭Ṑ"): bstack1l1l111l_opy_.get(bstack11l1l1l_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧṑ"), [])
        }
    if bstack11111l11l_opy_ == bstack11l1l1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧṒ"):
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧṓ")] = bstack11l1l1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩṔ")
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨṕ")] = bstack1l1l111l_opy_[bstack11l1l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩṖ")]
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩṗ")] = bstack1l1l111l_opy_[bstack11l1l1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪṘ")]
    if result:
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ṙ")] = result.outcome
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨṚ")] = result.duration * 1000
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ṛ")] = bstack1l1l111l_opy_[bstack11l1l1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧṜ")]
        if result.failed:
            bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩṝ")] = bstack1l11l1ll_opy_.bstack111l1ll111_opy_(call.excinfo.typename)
            bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬṞ")] = bstack1l11l1ll_opy_.bstack11l111llll1_opy_(call.excinfo, result)
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫṟ")] = bstack1l1l111l_opy_[bstack11l1l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬṠ")]
    if outcome:
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧṡ")] = bstack11ll1lllll1_opy_(outcome)
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩṢ")] = 0
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧṣ")] = bstack1l1l111l_opy_[bstack11l1l1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨṤ")]
        if bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫṥ")] == bstack11l1l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬṦ"):
            bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬṧ")] = bstack11l1l1l_opy_ (u"ࠧࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠨṨ")  # bstack111llll1ll1_opy_
            bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩṩ")] = [{bstack11l1l1l_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬṪ"): [bstack11l1l1l_opy_ (u"ࠪࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠧṫ")]}]
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪṬ")] = bstack1l1l111l_opy_[bstack11l1l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫṭ")]
    return bstack1ll111ll_opy_
def bstack11l11111111_opy_(test, bstack1ll1ll1l_opy_, bstack11111l11l_opy_, result, call, outcome, bstack111lllll111_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1ll1ll1l_opy_[bstack11l1l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩṮ")]
    hook_name = bstack1ll1ll1l_opy_[bstack11l1l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪṯ")]
    hook_data = {
        bstack11l1l1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭Ṱ"): bstack1ll1ll1l_opy_[bstack11l1l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧṱ")],
        bstack11l1l1l_opy_ (u"ࠪࡸࡾࡶࡥࠨṲ"): bstack11l1l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩṳ"),
        bstack11l1l1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪṴ"): bstack11l1l1l_opy_ (u"࠭ࡻࡾࠩṵ").format(bstack1l111lll11l_opy_(hook_name)),
        bstack11l1l1l_opy_ (u"ࠧࡣࡱࡧࡽࠬṶ"): {
            bstack11l1l1l_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭ṷ"): bstack11l1l1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩṸ"),
            bstack11l1l1l_opy_ (u"ࠪࡧࡴࡪࡥࠨṹ"): None
        },
        bstack11l1l1l_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࠪṺ"): test.name,
        bstack11l1l1l_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬṻ"): bstack1l1ll11l_opy_.bstack1l1l11ll_opy_(test, hook_name),
        bstack11l1l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩṼ"): file_path,
        bstack11l1l1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠩṽ"): file_path,
        bstack11l1l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨṾ"): bstack11l1l1l_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪṿ"),
        bstack11l1l1l_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨẀ"): file_path,
        bstack11l1l1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨẁ"): bstack1ll1ll1l_opy_[bstack11l1l1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩẂ")],
        bstack11l1l1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩẃ"): bstack11l1l1l_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩẄ") if bstack111llllll11_opy_ == bstack11l1l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬẅ") else bstack11l1l1l_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩẆ"),
        bstack11l1l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ẇ"): hook_type
    }
    bstack11ll11l11l1_opy_ = bstack1llll1l1_opy_(_1llll11l_opy_.get(test.nodeid, None))
    if bstack11ll11l11l1_opy_:
        hook_data[bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡩࡥࠩẈ")] = bstack11ll11l11l1_opy_
    if result:
        hook_data[bstack11l1l1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬẉ")] = result.outcome
        hook_data[bstack11l1l1l_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧẊ")] = result.duration * 1000
        hook_data[bstack11l1l1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬẋ")] = bstack1ll1ll1l_opy_[bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭Ẍ")]
        if result.failed:
            hook_data[bstack11l1l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨẍ")] = bstack1l11l1ll_opy_.bstack111l1ll111_opy_(call.excinfo.typename)
            hook_data[bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫẎ")] = bstack1l11l1ll_opy_.bstack11l111llll1_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11l1l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫẏ")] = bstack11ll1lllll1_opy_(outcome)
        hook_data[bstack11l1l1l_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭Ẑ")] = 100
        hook_data[bstack11l1l1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫẑ")] = bstack1ll1ll1l_opy_[bstack11l1l1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬẒ")]
        if hook_data[bstack11l1l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨẓ")] == bstack11l1l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩẔ"):
            hook_data[bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩẕ")] = bstack11l1l1l_opy_ (u"࡚ࠫࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠬẖ")  # bstack111llll1ll1_opy_
            hook_data[bstack11l1l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ẗ")] = [{bstack11l1l1l_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩẘ"): [bstack11l1l1l_opy_ (u"ࠧࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠫẙ")]}]
    if bstack111lllll111_opy_:
        hook_data[bstack11l1l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨẚ")] = bstack111lllll111_opy_.result
        hook_data[bstack11l1l1l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪẛ")] = bstack11lll11ll11_opy_(bstack1ll1ll1l_opy_[bstack11l1l1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧẜ")], bstack1ll1ll1l_opy_[bstack11l1l1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩẝ")])
        hook_data[bstack11l1l1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪẞ")] = bstack1ll1ll1l_opy_[bstack11l1l1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫẟ")]
        if hook_data[bstack11l1l1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧẠ")] == bstack11l1l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨạ"):
            hook_data[bstack11l1l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨẢ")] = bstack1l11l1ll_opy_.bstack111l1ll111_opy_(bstack111lllll111_opy_.exception_type)
            hook_data[bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫả")] = [{bstack11l1l1l_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧẤ"): bstack11lll1lllll_opy_(bstack111lllll111_opy_.exception)}]
    return hook_data
def bstack11l111111l1_opy_(test, bstack1l1l111l_opy_, bstack11111l11l_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack11l1l1l_opy_ (u"ࠬࡹࡥ࡯ࡦࡢࡸࡪࡹࡴࡠࡴࡸࡲࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡇࡴࡵࡧࡰࡴࡹ࡯࡮ࡨࠢࡷࡳࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠤ࠲ࠦࡻࡾࠩấ").format(bstack11111l11l_opy_))
    bstack1ll111ll_opy_ = bstack11l1111lll1_opy_(test, bstack1l1l111l_opy_, result, call, bstack11111l11l_opy_, outcome)
    driver = getattr(test, bstack11l1l1l_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧẦ"), None)
    if bstack11111l11l_opy_ == bstack11l1l1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨầ") and driver:
        bstack1ll111ll_opy_[bstack11l1l1l_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧẨ")] = bstack1l11l1ll_opy_.bstack11lllll1_opy_(driver)
    if bstack11111l11l_opy_ == bstack11l1l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪẩ"):
        bstack11111l11l_opy_ = bstack11l1l1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬẪ")
    bstack1l1111l1_opy_ = {
        bstack11l1l1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨẫ"): bstack11111l11l_opy_,
        bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧẬ"): bstack1ll111ll_opy_
    }
    bstack1l11l1ll_opy_.bstack1lll11l1_opy_(bstack1l1111l1_opy_)
    if bstack11111l11l_opy_ == bstack11l1l1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧậ"):
        threading.current_thread().bstackTestMeta = {bstack11l1l1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧẮ"): bstack11l1l1l_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩắ")}
    elif bstack11111l11l_opy_ == bstack11l1l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫẰ"):
        threading.current_thread().bstackTestMeta = {bstack11l1l1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪằ"): getattr(result, bstack11l1l1l_opy_ (u"ࠫࡴࡻࡴࡤࡱࡰࡩࠬẲ"), bstack11l1l1l_opy_ (u"ࠬ࠭ẳ"))}
def bstack11l1111ll11_opy_(test, bstack1l1l111l_opy_, bstack11111l11l_opy_, result=None, call=None, outcome=None, bstack111lllll111_opy_=None):
    logger.debug(bstack11l1l1l_opy_ (u"࠭ࡳࡦࡰࡧࡣ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡥࡷࡧࡱࡸ࠿ࠦࡁࡵࡶࡨࡱࡵࡺࡩ࡯ࡩࠣࡸࡴࠦࡧࡦࡰࡨࡶࡦࡺࡥࠡࡪࡲࡳࡰࠦࡤࡢࡶࡤ࠰ࠥ࡫ࡶࡦࡰࡷࡘࡾࡶࡥࠡ࠯ࠣࡿࢂ࠭Ẵ").format(bstack11111l11l_opy_))
    hook_data = bstack11l11111111_opy_(test, bstack1l1l111l_opy_, bstack11111l11l_opy_, result, call, outcome, bstack111lllll111_opy_)
    bstack1l1111l1_opy_ = {
        bstack11l1l1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫẵ"): bstack11111l11l_opy_,
        bstack11l1l1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࠪẶ"): hook_data
    }
    bstack1l11l1ll_opy_.bstack1lll11l1_opy_(bstack1l1111l1_opy_)
def bstack1llll1l1_opy_(bstack1l1l111l_opy_):
    if not bstack1l1l111l_opy_:
        return None
    if bstack1l1l111l_opy_.get(bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬặ"), None):
        return getattr(bstack1l1l111l_opy_[bstack11l1l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭Ẹ")], bstack11l1l1l_opy_ (u"ࠫࡺࡻࡩࡥࠩẹ"), None)
    return bstack1l1l111l_opy_.get(bstack11l1l1l_opy_ (u"ࠬࡻࡵࡪࡦࠪẺ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
        cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.LOG, bstack11111111ll_opy_.PRE, request, caplog)
    yield
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
        cli.test_framework.track_event(cli_context, bstack111111lll1_opy_.LOG, bstack11111111ll_opy_.POST, request, caplog)
        return # skip all existing bstack111lllll1l1_opy_
    try:
        if not bstack1l11l1ll_opy_.on():
            return
        places = [bstack11l1l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬẻ"), bstack11l1l1l_opy_ (u"ࠧࡤࡣ࡯ࡰࠬẼ"), bstack11l1l1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪẽ")]
        logs = []
        for bstack111lllllll1_opy_ in places:
            records = caplog.get_records(bstack111lllllll1_opy_)
            bstack11l1111l11l_opy_ = bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩẾ") if bstack111lllllll1_opy_ == bstack11l1l1l_opy_ (u"ࠪࡧࡦࡲ࡬ࠨế") else bstack11l1l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫỀ")
            bstack111llll1l1l_opy_ = request.node.nodeid + (bstack11l1l1l_opy_ (u"ࠬ࠭ề") if bstack111lllllll1_opy_ == bstack11l1l1l_opy_ (u"࠭ࡣࡢ࡮࡯ࠫỂ") else bstack11l1l1l_opy_ (u"ࠧ࠮ࠩể") + bstack111lllllll1_opy_)
            test_uuid = bstack1llll1l1_opy_(_1llll11l_opy_.get(bstack111llll1l1l_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack11ll1lll11l_opy_(record.message):
                    continue
                logs.append({
                    bstack11l1l1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫỄ"): bstack11ll1ll1l11_opy_(record.created).isoformat() + bstack11l1l1l_opy_ (u"ࠩ࡝ࠫễ"),
                    bstack11l1l1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩỆ"): record.levelname,
                    bstack11l1l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬệ"): record.message,
                    bstack11l1111l11l_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack1l11l1ll_opy_.bstack1ll1111l_opy_(logs)
    except Exception as err:
        print(bstack11l1l1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸ࡫ࡣࡰࡰࡧࡣ࡫࡯ࡸࡵࡷࡵࡩ࠿ࠦࡻࡾࠩỈ"), str(err))
def bstack1ll11l11l_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1l1lll11l1_opy_
    bstack1l1ll1l111_opy_ = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪỉ"), None) and bstack11llll1l_opy_(
            threading.current_thread(), bstack11l1l1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭Ị"), None)
    bstack1l1l1ll1ll_opy_ = getattr(driver, bstack11l1l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨị"), None) != None and getattr(driver, bstack11l1l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩỌ"), None) == True
    if sequence == bstack11l1l1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪọ") and driver != None:
      if not bstack1l1lll11l1_opy_ and bstack1l1llll111l_opy_() and bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫỎ") in CONFIG and CONFIG[bstack11l1l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬỏ")] == True and bstack1111111l1_opy_.bstack1llll1ll1_opy_(driver_command) and (bstack1l1l1ll1ll_opy_ or bstack1l1ll1l111_opy_) and not bstack1l1l111l1_opy_(args):
        try:
          bstack1l1lll11l1_opy_ = True
          logger.debug(bstack11l1l1l_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࢁࡽࠨỐ").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11l1l1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡪࡸࡦࡰࡴࡰࠤࡸࡩࡡ࡯ࠢࡾࢁࠬố").format(str(err)))
        bstack1l1lll11l1_opy_ = False
    if sequence == bstack11l1l1l_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧỒ"):
        if driver_command == bstack11l1l1l_opy_ (u"ࠩࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࠭ồ"):
            bstack1l11l1ll_opy_.bstack11ll11l1l1_opy_({
                bstack11l1l1l_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩỔ"): response[bstack11l1l1l_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪổ")],
                bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬỖ"): store[bstack11l1l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪỗ")]
            })
def bstack1l1l1ll111_opy_():
    global bstack11ll1ll1l_opy_
    bstack111111l1l_opy_.bstack1l111ll1ll_opy_()
    logging.shutdown()
    bstack1l11l1ll_opy_.bstack11llll11_opy_()
    for driver in bstack11ll1ll1l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack11l11111l1l_opy_(*args):
    global bstack11ll1ll1l_opy_
    bstack1l11l1ll_opy_.bstack11llll11_opy_()
    for driver in bstack11ll1ll1l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1lll1ll1ll_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack11l11llll1_opy_(self, *args, **kwargs):
    bstack11l1ll1ll_opy_ = bstack11l11l1ll1_opy_(self, *args, **kwargs)
    bstack1lll11l1l1_opy_ = getattr(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡔࡦࡵࡷࡑࡪࡺࡡࠨỘ"), None)
    if bstack1lll11l1l1_opy_ and bstack1lll11l1l1_opy_.get(bstack11l1l1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨộ"), bstack11l1l1l_opy_ (u"ࠩࠪỚ")) == bstack11l1l1l_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫớ"):
        bstack1l11l1ll_opy_.bstack1ll11ll1l1_opy_(self)
    return bstack11l1ll1ll_opy_
@measure(event_name=EVENTS.bstack1lll11l111_opy_, stage=STAGE.bstack1l1llll111_opy_, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack11ll111ll_opy_(framework_name):
    from bstack_utils.config import Config
    bstack11111l11_opy_ = Config.bstack111ll1ll_opy_()
    if bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡲࡵࡤࡠࡥࡤࡰࡱ࡫ࡤࠨỜ")):
        return
    bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡳ࡯ࡥࡡࡦࡥࡱࡲࡥࡥࠩờ"), True)
    global bstack11l1ll11l1_opy_
    global bstack11l111lll1_opy_
    bstack11l1ll11l1_opy_ = framework_name
    logger.info(bstack1l11l11lll_opy_.format(bstack11l1ll11l1_opy_.split(bstack11l1l1l_opy_ (u"࠭࠭ࠨỞ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1l1llll111l_opy_():
            Service.start = bstack1llll1l1l1_opy_
            Service.stop = bstack1l1lll1ll1_opy_
            webdriver.Remote.get = bstack1111ll11l_opy_
            webdriver.Remote.__init__ = bstack1l1l1ll11_opy_
            if not isinstance(os.getenv(bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡂࡔࡄࡐࡑࡋࡌࠨở")), str):
                return
            WebDriver.close = bstack11l11l1lll_opy_
            WebDriver.quit = bstack1l1l1l11ll_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack1l11l1ll_opy_.on():
            webdriver.Remote.__init__ = bstack11l11llll1_opy_
        bstack11l111lll1_opy_ = True
    except Exception as e:
        pass
    bstack1l1111l111_opy_()
    if os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡕࡈࡐࡊࡔࡉࡖࡏࡢࡓࡗࡥࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡍࡓ࡙ࡔࡂࡎࡏࡉࡉ࠭Ỡ")):
        bstack11l111lll1_opy_ = eval(os.environ.get(bstack11l1l1l_opy_ (u"ࠩࡖࡉࡑࡋࡎࡊࡗࡐࡣࡔࡘ࡟ࡑࡎࡄ࡝࡜ࡘࡉࡈࡊࡗࡣࡎࡔࡓࡕࡃࡏࡐࡊࡊࠧỡ")))
    if not bstack11l111lll1_opy_:
        bstack1ll11l1l11_opy_(bstack11l1l1l_opy_ (u"ࠥࡔࡦࡩ࡫ࡢࡩࡨࡷࠥࡴ࡯ࡵࠢ࡬ࡲࡸࡺࡡ࡭࡮ࡨࡨࠧỢ"), bstack1l1l1111l1_opy_)
    if bstack1l111l1l1l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._1llllll111_opy_ = bstack1l11ll111_opy_
        except Exception as e:
            logger.error(bstack1l11l11l1l_opy_.format(str(e)))
    if bstack11l1l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫợ") in str(framework_name).lower():
        if not bstack1l1llll111l_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack11lll1llll_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l1111lll1_opy_
            Config.getoption = bstack1llllll11l_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack11l1l1l11_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11lll1lll_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1l1l1l11ll_opy_(self):
    global bstack11l1ll11l1_opy_
    global bstack1l1lll1111_opy_
    global bstack1lll1lllll_opy_
    try:
        if bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬỤ") in bstack11l1ll11l1_opy_ and self.session_id != None and bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪụ"), bstack11l1l1l_opy_ (u"ࠧࠨỦ")) != bstack11l1l1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩủ"):
            bstack1ll111ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩỨ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪứ")
            bstack11ll11ll1l_opy_(logger, True)
            if self != None:
                bstack11ll11l1ll_opy_(self, bstack1ll111ll1l_opy_, bstack11l1l1l_opy_ (u"ࠫ࠱ࠦࠧỪ").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
            item = store.get(bstack11l1l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩừ"), None)
            if item is not None and bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬỬ"), None):
                bstack111lll1l_opy_.bstack111lll11_opy_(self, bstack1llll1l111_opy_, logger, item)
        threading.current_thread().testStatus = bstack11l1l1l_opy_ (u"ࠧࠨử")
    except Exception as e:
        logger.debug(bstack11l1l1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࠤỮ") + str(e))
    bstack1lll1lllll_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack11l1ll1lll_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1l1l1ll11_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1l1lll1111_opy_
    global bstack11l1ll111_opy_
    global bstack11ll11lll_opy_
    global bstack11l1ll11l1_opy_
    global bstack11l11l1ll1_opy_
    global bstack11ll1ll1l_opy_
    global bstack11l11111l_opy_
    global bstack1ll1lll1l1_opy_
    global bstack1llll1l111_opy_
    CONFIG[bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫữ")] = str(bstack11l1ll11l1_opy_) + str(__version__)
    command_executor = bstack1llll111l1_opy_(bstack11l11111l_opy_, CONFIG)
    logger.debug(bstack11l11lll11_opy_.format(command_executor))
    proxy = bstack111111l11_opy_(CONFIG, proxy)
    bstack1l11lll11_opy_ = 0
    try:
        if bstack11ll11lll_opy_ is True:
            bstack1l11lll11_opy_ = int(os.environ.get(bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪỰ")))
    except:
        bstack1l11lll11_opy_ = 0
    bstack11ll1l1ll1_opy_ = bstack1llllll1ll_opy_(CONFIG, bstack1l11lll11_opy_)
    logger.debug(bstack1l1111ll1l_opy_.format(str(bstack11ll1l1ll1_opy_)))
    bstack1llll1l111_opy_ = CONFIG.get(bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧự"))[bstack1l11lll11_opy_]
    if bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩỲ") in CONFIG and CONFIG[bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪỳ")]:
        bstack1l111111l1_opy_(bstack11ll1l1ll1_opy_, bstack1ll1lll1l1_opy_)
    if bstack111lllll_opy_.bstack1lll11lll1_opy_(CONFIG, bstack1l11lll11_opy_) and bstack111lllll_opy_.bstack111ll1l11_opy_(bstack11ll1l1ll1_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
            bstack111lllll_opy_.set_capabilities(bstack11ll1l1ll1_opy_, CONFIG)
    if desired_capabilities:
        bstack11ll1ll11_opy_ = bstack11lll1l11l_opy_(desired_capabilities)
        bstack11ll1ll11_opy_[bstack11l1l1l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧỴ")] = bstack1l11ll1lll_opy_(CONFIG)
        bstack1111lll11_opy_ = bstack1llllll1ll_opy_(bstack11ll1ll11_opy_)
        if bstack1111lll11_opy_:
            bstack11ll1l1ll1_opy_ = update(bstack1111lll11_opy_, bstack11ll1l1ll1_opy_)
        desired_capabilities = None
    if options:
        bstack1ll1l111l1_opy_(options, bstack11ll1l1ll1_opy_)
    if not options:
        options = bstack11lllll1l1_opy_(bstack11ll1l1ll1_opy_)
    if proxy and bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨỵ")):
        options.proxy(proxy)
    if options and bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨỶ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1ll1l1111l_opy_() < version.parse(bstack11l1l1l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩỷ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack11ll1l1ll1_opy_)
    logger.info(bstack1l1ll11l1_opy_)
    bstack11ll1111l1_opy_.end(EVENTS.bstack1lll11l111_opy_.value, EVENTS.bstack1lll11l111_opy_.value + bstack11l1l1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦỸ"),
                               EVENTS.bstack1lll11l111_opy_.value + bstack11l1l1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥỹ"), True, None)
    if bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭Ỻ")):
        bstack11l11l1ll1_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ỻ")):
        bstack11l11l1ll1_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨỼ")):
        bstack11l11l1ll1_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack11l11l1ll1_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack1llll1111l_opy_ = bstack11l1l1l_opy_ (u"ࠩࠪỽ")
        if bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࡤ࠴ࠫỾ")):
            bstack1llll1111l_opy_ = self.caps.get(bstack11l1l1l_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦỿ"))
        else:
            bstack1llll1111l_opy_ = self.capabilities.get(bstack11l1l1l_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧἀ"))
        if bstack1llll1111l_opy_:
            bstack1l11ll11ll_opy_(bstack1llll1111l_opy_)
            if bstack1ll1l1111l_opy_() <= version.parse(bstack11l1l1l_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ἁ")):
                self.command_executor._url = bstack11l1l1l_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣἂ") + bstack11l11111l_opy_ + bstack11l1l1l_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧἃ")
            else:
                self.command_executor._url = bstack11l1l1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦἄ") + bstack1llll1111l_opy_ + bstack11l1l1l_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦἅ")
            logger.debug(bstack1ll1lllll1_opy_.format(bstack1llll1111l_opy_))
        else:
            logger.debug(bstack11ll11l11l_opy_.format(bstack11l1l1l_opy_ (u"ࠦࡔࡶࡴࡪ࡯ࡤࡰࠥࡎࡵࡣࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧἆ")))
    except Exception as e:
        logger.debug(bstack11ll11l11l_opy_.format(e))
    bstack1l1lll1111_opy_ = self.session_id
    if bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬἇ") in bstack11l1ll11l1_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11l1l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪἈ"), None)
        if item:
            bstack11l1111l1l1_opy_ = getattr(item, bstack11l1l1l_opy_ (u"ࠧࡠࡶࡨࡷࡹࡥࡣࡢࡵࡨࡣࡸࡺࡡࡳࡶࡨࡨࠬἉ"), False)
            if not getattr(item, bstack11l1l1l_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩἊ"), None) and bstack11l1111l1l1_opy_:
                setattr(store[bstack11l1l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭Ἃ")], bstack11l1l1l_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫἌ"), self)
        bstack1lll11l1l1_opy_ = getattr(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥࠬἍ"), None)
        if bstack1lll11l1l1_opy_ and bstack1lll11l1l1_opy_.get(bstack11l1l1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬἎ"), bstack11l1l1l_opy_ (u"࠭ࠧἏ")) == bstack11l1l1l_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨἐ"):
            bstack1l11l1ll_opy_.bstack1ll11ll1l1_opy_(self)
    bstack11ll1ll1l_opy_.append(self)
    if bstack11l1l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫἑ") in CONFIG and bstack11l1l1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧἒ") in CONFIG[bstack11l1l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ἓ")][bstack1l11lll11_opy_]:
        bstack11l1ll111_opy_ = CONFIG[bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧἔ")][bstack1l11lll11_opy_][bstack11l1l1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪἕ")]
    logger.debug(bstack11ll1llll_opy_.format(bstack1l1lll1111_opy_))
@measure(event_name=EVENTS.bstack1l1ll1l1ll_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1111ll11l_opy_(self, url):
    global bstack1l1ll1l1l1_opy_
    global CONFIG
    try:
        bstack111llllll_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1l111l111l_opy_.format(str(err)))
    try:
        bstack1l1ll1l1l1_opy_(self, url)
    except Exception as e:
        try:
            parsed_error = str(e)
            if any(err_msg in parsed_error for err_msg in bstack1llll11l11_opy_):
                bstack111llllll_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1l111l111l_opy_.format(str(err)))
        raise e
def bstack1l11l111l_opy_(item, when):
    global bstack1ll111ll11_opy_
    try:
        bstack1ll111ll11_opy_(item, when)
    except Exception as e:
        pass
def bstack11l1l1l11_opy_(item, call, rep):
    global bstack1l11llll11_opy_
    global bstack11ll1ll1l_opy_
    name = bstack11l1l1l_opy_ (u"࠭ࠧ἖")
    try:
        if rep.when == bstack11l1l1l_opy_ (u"ࠧࡤࡣ࡯ࡰࠬ἗"):
            bstack1l1lll1111_opy_ = threading.current_thread().bstackSessionId
            bstack11l111111ll_opy_ = item.config.getoption(bstack11l1l1l_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪἘ"))
            try:
                if (str(bstack11l111111ll_opy_).lower() != bstack11l1l1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧἙ")):
                    name = str(rep.nodeid)
                    bstack1l11l1ll1l_opy_ = bstack1l1lllll1l_opy_(bstack11l1l1l_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫἚ"), name, bstack11l1l1l_opy_ (u"ࠫࠬἛ"), bstack11l1l1l_opy_ (u"ࠬ࠭Ἔ"), bstack11l1l1l_opy_ (u"࠭ࠧἝ"), bstack11l1l1l_opy_ (u"ࠧࠨ἞"))
                    os.environ[bstack11l1l1l_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫ἟")] = name
                    for driver in bstack11ll1ll1l_opy_:
                        if bstack1l1lll1111_opy_ == driver.session_id:
                            driver.execute_script(bstack1l11l1ll1l_opy_)
            except Exception as e:
                logger.debug(bstack11l1l1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠩἠ").format(str(e)))
            try:
                bstack1l1l1ll1l1_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11l1l1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫἡ"):
                    status = bstack11l1l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫἢ") if rep.outcome.lower() == bstack11l1l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬἣ") else bstack11l1l1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ἤ")
                    reason = bstack11l1l1l_opy_ (u"ࠧࠨἥ")
                    if status == bstack11l1l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨἦ"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11l1l1l_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧἧ") if status == bstack11l1l1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪἨ") else bstack11l1l1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪἩ")
                    data = name + bstack11l1l1l_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩࠧࠧἪ") if status == bstack11l1l1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭Ἣ") else name + bstack11l1l1l_opy_ (u"ࠧࠡࡨࡤ࡭ࡱ࡫ࡤࠢࠢࠪἬ") + reason
                    bstack11l11l111l_opy_ = bstack1l1lllll1l_opy_(bstack11l1l1l_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪἭ"), bstack11l1l1l_opy_ (u"ࠩࠪἮ"), bstack11l1l1l_opy_ (u"ࠪࠫἯ"), bstack11l1l1l_opy_ (u"ࠫࠬἰ"), level, data)
                    for driver in bstack11ll1ll1l_opy_:
                        if bstack1l1lll1111_opy_ == driver.session_id:
                            driver.execute_script(bstack11l11l111l_opy_)
            except Exception as e:
                logger.debug(bstack11l1l1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡦࡳࡳࡺࡥࡹࡶࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠩἱ").format(str(e)))
    except Exception as e:
        logger.debug(bstack11l1l1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡶࡸࡦࡺࡥࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࠦࡳࡵࡣࡷࡹࡸࡀࠠࡼࡿࠪἲ").format(str(e)))
    bstack1l11llll11_opy_(item, call, rep)
notset = Notset()
def bstack1llllll11l_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1l1l1l111l_opy_
    if str(name).lower() == bstack11l1l1l_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸࠧἳ"):
        return bstack11l1l1l_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢἴ")
    else:
        return bstack1l1l1l111l_opy_(self, name, default, skip)
def bstack1l11ll111_opy_(self):
    global CONFIG
    global bstack11l1l1l1l1_opy_
    try:
        proxy = bstack1lll1111l1_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11l1l1l_opy_ (u"ࠩ࠱ࡴࡦࡩࠧἵ")):
                proxies = bstack1lll11l11l_opy_(proxy, bstack1llll111l1_opy_())
                if len(proxies) > 0:
                    protocol, bstack1ll1ll111_opy_ = proxies.popitem()
                    if bstack11l1l1l_opy_ (u"ࠥ࠾࠴࠵ࠢἶ") in bstack1ll1ll111_opy_:
                        return bstack1ll1ll111_opy_
                    else:
                        return bstack11l1l1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧἷ") + bstack1ll1ll111_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11l1l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡲࡵࡳࡽࡿࠠࡶࡴ࡯ࠤ࠿ࠦࡻࡾࠤἸ").format(str(e)))
    return bstack11l1l1l1l1_opy_(self)
def bstack1l111l1l1l_opy_():
    return (bstack11l1l1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩἹ") in CONFIG or bstack11l1l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫἺ") in CONFIG) and bstack1l11l111ll_opy_() and bstack1ll1l1111l_opy_() >= version.parse(
        bstack1111111ll_opy_)
def bstack11l111111_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack11l1ll111_opy_
    global bstack11ll11lll_opy_
    global bstack11l1ll11l1_opy_
    CONFIG[bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪἻ")] = str(bstack11l1ll11l1_opy_) + str(__version__)
    bstack1l11lll11_opy_ = 0
    try:
        if bstack11ll11lll_opy_ is True:
            bstack1l11lll11_opy_ = int(os.environ.get(bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩἼ")))
    except:
        bstack1l11lll11_opy_ = 0
    CONFIG[bstack11l1l1l_opy_ (u"ࠥ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤἽ")] = True
    bstack11ll1l1ll1_opy_ = bstack1llllll1ll_opy_(CONFIG, bstack1l11lll11_opy_)
    logger.debug(bstack1l1111ll1l_opy_.format(str(bstack11ll1l1ll1_opy_)))
    if CONFIG.get(bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨἾ")):
        bstack1l111111l1_opy_(bstack11ll1l1ll1_opy_, bstack1ll1lll1l1_opy_)
    if bstack11l1l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨἿ") in CONFIG and bstack11l1l1l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫὀ") in CONFIG[bstack11l1l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪὁ")][bstack1l11lll11_opy_]:
        bstack11l1ll111_opy_ = CONFIG[bstack11l1l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫὂ")][bstack1l11lll11_opy_][bstack11l1l1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧὃ")]
    import urllib
    import json
    if bstack11l1l1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧὄ") in CONFIG and str(CONFIG[bstack11l1l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨὅ")]).lower() != bstack11l1l1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ὆"):
        bstack11l1l1111l_opy_ = bstack1lllll111l_opy_()
        bstack1l11l1lll1_opy_ = bstack11l1l1111l_opy_ + urllib.parse.quote(json.dumps(bstack11ll1l1ll1_opy_))
    else:
        bstack1l11l1lll1_opy_ = bstack11l1l1l_opy_ (u"࠭ࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠨ὇") + urllib.parse.quote(json.dumps(bstack11ll1l1ll1_opy_))
    browser = self.connect(bstack1l11l1lll1_opy_)
    return browser
def bstack1l1111l111_opy_():
    global bstack11l111lll1_opy_
    global bstack11l1ll11l1_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1lll11ll1l_opy_
        if not bstack1l1llll111l_opy_():
            global bstack111ll11ll1_opy_
            if not bstack111ll11ll1_opy_:
                from bstack_utils.helper import bstack111l11lll_opy_, bstack11lll1lll1_opy_
                bstack111ll11ll1_opy_ = bstack111l11lll_opy_()
                bstack11lll1lll1_opy_(bstack11l1ll11l1_opy_)
            BrowserType.connect = bstack1lll11ll1l_opy_
            return
        BrowserType.launch = bstack11l111111_opy_
        bstack11l111lll1_opy_ = True
    except Exception as e:
        pass
def bstack111llllllll_opy_():
    global CONFIG
    global bstack1ll1111ll1_opy_
    global bstack11l11111l_opy_
    global bstack1ll1lll1l1_opy_
    global bstack11ll11lll_opy_
    global bstack1l11l1111l_opy_
    CONFIG = json.loads(os.environ.get(bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌ࠭Ὀ")))
    bstack1ll1111ll1_opy_ = eval(os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩὉ")))
    bstack11l11111l_opy_ = os.environ.get(bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡊࡘࡆࡤ࡛ࡒࡍࠩὊ"))
    bstack11llllll1l_opy_(CONFIG, bstack1ll1111ll1_opy_)
    bstack1l11l1111l_opy_ = bstack111111l1l_opy_.bstack11ll111lll_opy_(CONFIG, bstack1l11l1111l_opy_)
    if cli.bstack11ll1111l_opy_():
        bstack1l1llll11l_opy_.invoke(Events.CONNECT, bstack11l11lll1_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪὋ"), bstack11l1l1l_opy_ (u"ࠫ࠵࠭Ὄ")))
        cli.bstack1ll1ll111ll_opy_(bstack1llll111l1_opy_(bstack11l11111l_opy_, CONFIG), cli_context.platform_index, bstack11lllll1l1_opy_)
        cli.bstack1ll111l1l1l_opy_()
        logger.debug(bstack11l1l1l_opy_ (u"ࠧࡉࡌࡊࠢ࡬ࡷࠥࡧࡣࡵ࡫ࡹࡩࠥ࡬࡯ࡳࠢࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࠦὍ") + str(cli_context.platform_index) + bstack11l1l1l_opy_ (u"ࠨࠢ὎"))
        return # skip all existing bstack111lllll1l1_opy_
    global bstack11l11l1ll1_opy_
    global bstack1lll1lllll_opy_
    global bstack1l1llll1l1_opy_
    global bstack111lll1ll_opy_
    global bstack1l1111l1ll_opy_
    global bstack11llll111l_opy_
    global bstack1lll1l111l_opy_
    global bstack1l1ll1l1l1_opy_
    global bstack11l1l1l1l1_opy_
    global bstack1l1l1l111l_opy_
    global bstack1ll111ll11_opy_
    global bstack1l11llll11_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack11l11l1ll1_opy_ = webdriver.Remote.__init__
        bstack1lll1lllll_opy_ = WebDriver.quit
        bstack1lll1l111l_opy_ = WebDriver.close
        bstack1l1ll1l1l1_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack11l1l1l_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ὏") in CONFIG or bstack11l1l1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬὐ") in CONFIG) and bstack1l11l111ll_opy_():
        if bstack1ll1l1111l_opy_() < version.parse(bstack1111111ll_opy_):
            logger.error(bstack1ll11ll11_opy_.format(bstack1ll1l1111l_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack11l1l1l1l1_opy_ = RemoteConnection._1llllll111_opy_
            except Exception as e:
                logger.error(bstack1l11l11l1l_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1l1l1l111l_opy_ = Config.getoption
        from _pytest import runner
        bstack1ll111ll11_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack1111ll1l_opy_)
    try:
        from pytest_bdd import reporting
        bstack1l11llll11_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack11l1l1l_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪὑ"))
    bstack1ll1lll1l1_opy_ = CONFIG.get(bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧὒ"), {}).get(bstack11l1l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ὓ"))
    bstack11ll11lll_opy_ = True
    bstack11ll111ll_opy_(bstack1ll1l11ll1_opy_)
if (bstack11lll1ll111_opy_()):
    bstack111llllllll_opy_()
@bstack1ll111l1_opy_(class_method=False)
def bstack111llll11l1_opy_(hook_name, event, bstack1llll111ll1_opy_=None):
    if hook_name not in [bstack11l1l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ὔ"), bstack11l1l1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪὕ"), bstack11l1l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ὖ"), bstack11l1l1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪὗ"), bstack11l1l1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧ὘"), bstack11l1l1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫὙ"), bstack11l1l1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪ὚"), bstack11l1l1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧὛ")]:
        return
    node = store[bstack11l1l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ὜")]
    if hook_name in [bstack11l1l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭Ὕ"), bstack11l1l1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪ὞")]:
        node = store[bstack11l1l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡱࡴࡪࡵ࡭ࡧࡢ࡭ࡹ࡫࡭ࠨὟ")]
    elif hook_name in [bstack11l1l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨὠ"), bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬὡ")]:
        node = store[bstack11l1l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯ࠪὢ")]
    hook_type = bstack1l111ll1l11_opy_(hook_name)
    if event == bstack11l1l1l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭ὣ"):
        if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
            cli.test_framework.track_event(cli_context, bstack111111lll1_opy_[hook_type], bstack11111111ll_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack1ll1ll1l_opy_ = {
            bstack11l1l1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬὤ"): uuid,
            bstack11l1l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬὥ"): bstack11llllll_opy_(),
            bstack11l1l1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧὦ"): bstack11l1l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨὧ"),
            bstack11l1l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧὨ"): hook_type,
            bstack11l1l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨὩ"): hook_name
        }
        store[bstack11l1l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪὪ")].append(uuid)
        bstack11l1111l111_opy_ = node.nodeid
        if hook_type == bstack11l1l1l_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬὫ"):
            if not _1llll11l_opy_.get(bstack11l1111l111_opy_, None):
                _1llll11l_opy_[bstack11l1111l111_opy_] = {bstack11l1l1l_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧὬ"): []}
            _1llll11l_opy_[bstack11l1111l111_opy_][bstack11l1l1l_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨὭ")].append(bstack1ll1ll1l_opy_[bstack11l1l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨὮ")])
        _1llll11l_opy_[bstack11l1111l111_opy_ + bstack11l1l1l_opy_ (u"ࠫ࠲࠭Ὧ") + hook_name] = bstack1ll1ll1l_opy_
        bstack11l1111ll11_opy_(node, bstack1ll1ll1l_opy_, bstack11l1l1l_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ὰ"))
    elif event == bstack11l1l1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬά"):
        if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
            cli.test_framework.track_event(cli_context, bstack111111lll1_opy_[hook_type], bstack11111111ll_opy_.POST, node, None, bstack1llll111ll1_opy_)
            return
        bstack1l1ll1ll_opy_ = node.nodeid + bstack11l1l1l_opy_ (u"ࠧ࠮ࠩὲ") + hook_name
        _1llll11l_opy_[bstack1l1ll1ll_opy_][bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭έ")] = bstack11llllll_opy_()
        bstack111lllll11l_opy_(_1llll11l_opy_[bstack1l1ll1ll_opy_][bstack11l1l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧὴ")])
        bstack11l1111ll11_opy_(node, _1llll11l_opy_[bstack1l1ll1ll_opy_], bstack11l1l1l_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬή"), bstack111lllll111_opy_=bstack1llll111ll1_opy_)
def bstack111llll11ll_opy_():
    global bstack111llllll11_opy_
    if bstack11l1ll111l_opy_():
        bstack111llllll11_opy_ = bstack11l1l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨὶ")
    else:
        bstack111llllll11_opy_ = bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬί")
@bstack1l11l1ll_opy_.bstack11l11l1ll1l_opy_
def bstack111llll1111_opy_():
    bstack111llll11ll_opy_()
    if cli.bstack1ll1l11l1ll_opy_(bstack1ll11l11l1l_opy_):
        try:
            bstack1l11llll11l_opy_(bstack111llll11l1_opy_)
        except Exception as e:
            logger.debug(bstack11l1l1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡶࠤࡵࡧࡴࡤࡪ࠽ࠤࢀࢃࠢὸ").format(e))
        return
    if bstack1l11l111ll_opy_():
        bstack11111l11_opy_ = Config.bstack111ll1ll_opy_()
        if bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫό")):
            return
        bstack1lll1lll1l_opy_(bstack1ll11l11l_opy_)
    try:
        bstack1l11llll11l_opy_(bstack111llll11l1_opy_)
    except Exception as e:
        logger.debug(bstack11l1l1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࡸࠦࡰࡢࡶࡦ࡬࠿ࠦࡻࡾࠤὺ").format(e))
bstack111llll1111_opy_()