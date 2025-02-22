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
import logging
import bstack_utils.accessibility as bstack111lllll_opy_
from bstack_utils.helper import bstack11llll1l_opy_
logger = logging.getLogger(__name__)
def bstack111lll111_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1llllll1l_opy_(context, *args):
    tags = getattr(args[0], bstack11l1l1l_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ៌"), [])
    bstack111ll111l1_opy_ = bstack111lllll_opy_.bstack11l1l111ll_opy_(tags)
    threading.current_thread().isA11yTest = bstack111ll111l1_opy_
    try:
      bstack1l11l1llll_opy_ = threading.current_thread().bstackSessionDriver if bstack111lll111_opy_(bstack11l1l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ៍")) else context.browser
      if bstack1l11l1llll_opy_ and bstack1l11l1llll_opy_.session_id and bstack111ll111l1_opy_ and bstack11llll1l_opy_(
              threading.current_thread(), bstack11l1l1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ៎"), None):
          threading.current_thread().isA11yTest = bstack111lllll_opy_.bstack1l111l1l11_opy_(bstack1l11l1llll_opy_, bstack111ll111l1_opy_)
    except Exception as e:
       logger.debug(bstack11l1l1l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡢ࠳࠴ࡽࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥ࠻ࠢࡾࢁࠬ៏").format(str(e)))
def bstack1l111l1111_opy_(bstack1l11l1llll_opy_):
    if bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ័"), None) and bstack11llll1l_opy_(
      threading.current_thread(), bstack11l1l1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭៑"), None) and not bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡥࡳࡵࡱࡳ្ࠫ"), False):
      threading.current_thread().a11y_stop = True
      bstack111lllll_opy_.bstack1111l1l1_opy_(bstack1l11l1llll_opy_, name=bstack11l1l1l_opy_ (u"ࠤࠥ៓"), path=bstack11l1l1l_opy_ (u"ࠥࠦ។"))