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
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack1l1l111l111_opy_, bstack11ll1ll1ll_opy_, bstack11llll1l_opy_, bstack11l1l1lll_opy_, \
    bstack1l1l111ll11_opy_
from bstack_utils.measure import measure
def bstack1l1l1ll111_opy_(bstack1l1l111ll1l_opy_):
    for driver in bstack1l1l111ll1l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1ll11lllll_opy_, stage=STAGE.SINGLE)
def bstack11ll11l1ll_opy_(driver, status, reason=bstack11l1l1l_opy_ (u"ࠨࠩᏍ")):
    bstack11111l11_opy_ = Config.bstack111ll1ll_opy_()
    if bstack11111l11_opy_.bstack111ll1l1_opy_():
        return
    bstack1l11l1ll1l_opy_ = bstack1l1lllll1l_opy_(bstack11l1l1l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᏎ"), bstack11l1l1l_opy_ (u"ࠪࠫᏏ"), status, reason, bstack11l1l1l_opy_ (u"ࠫࠬᏐ"), bstack11l1l1l_opy_ (u"ࠬ࠭Ꮡ"))
    driver.execute_script(bstack1l11l1ll1l_opy_)
@measure(event_name=EVENTS.bstack1ll11lllll_opy_, stage=STAGE.SINGLE)
def bstack11lll1ll1_opy_(page, status, reason=bstack11l1l1l_opy_ (u"࠭ࠧᏒ")):
    try:
        if page is None:
            return
        bstack11111l11_opy_ = Config.bstack111ll1ll_opy_()
        if bstack11111l11_opy_.bstack111ll1l1_opy_():
            return
        bstack1l11l1ll1l_opy_ = bstack1l1lllll1l_opy_(bstack11l1l1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᏓ"), bstack11l1l1l_opy_ (u"ࠨࠩᏔ"), status, reason, bstack11l1l1l_opy_ (u"ࠩࠪᏕ"), bstack11l1l1l_opy_ (u"ࠪࠫᏖ"))
        page.evaluate(bstack11l1l1l_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧᏗ"), bstack1l11l1ll1l_opy_)
    except Exception as e:
        print(bstack11l1l1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡼࡿࠥᏘ"), e)
def bstack1l1lllll1l_opy_(type, name, status, reason, bstack1l1llll1ll_opy_, bstack11lll111l_opy_):
    bstack1l11lll1ll_opy_ = {
        bstack11l1l1l_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭Ꮩ"): type,
        bstack11l1l1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᏚ"): {}
    }
    if type == bstack11l1l1l_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪᏛ"):
        bstack1l11lll1ll_opy_[bstack11l1l1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᏜ")][bstack11l1l1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᏝ")] = bstack1l1llll1ll_opy_
        bstack1l11lll1ll_opy_[bstack11l1l1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᏞ")][bstack11l1l1l_opy_ (u"ࠬࡪࡡࡵࡣࠪᏟ")] = json.dumps(str(bstack11lll111l_opy_))
    if type == bstack11l1l1l_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᏠ"):
        bstack1l11lll1ll_opy_[bstack11l1l1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᏡ")][bstack11l1l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭Ꮲ")] = name
    if type == bstack11l1l1l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᏣ"):
        bstack1l11lll1ll_opy_[bstack11l1l1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭Ꮴ")][bstack11l1l1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᏥ")] = status
        if status == bstack11l1l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᏦ") and str(reason) != bstack11l1l1l_opy_ (u"ࠨࠢᏧ"):
            bstack1l11lll1ll_opy_[bstack11l1l1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᏨ")][bstack11l1l1l_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨᏩ")] = json.dumps(str(reason))
    bstack11lll111ll_opy_ = bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧᏪ").format(json.dumps(bstack1l11lll1ll_opy_))
    return bstack11lll111ll_opy_
def bstack111llllll_opy_(url, config, logger, bstack11111lll1_opy_=False):
    hostname = bstack11ll1ll1ll_opy_(url)
    is_private = bstack11l1l1lll_opy_(hostname)
    try:
        if is_private or bstack11111lll1_opy_:
            file_path = bstack1l1l111l111_opy_(bstack11l1l1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᏫ"), bstack11l1l1l_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪᏬ"), logger)
            if os.environ.get(bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪᏭ")) and eval(
                    os.environ.get(bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫᏮ"))):
                return
            if (bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫᏯ") in config and not config[bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᏰ")]):
                os.environ[bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᏱ")] = str(True)
                bstack1l1l1111lll_opy_ = {bstack11l1l1l_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬᏲ"): hostname}
                bstack1l1l111ll11_opy_(bstack11l1l1l_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪᏳ"), bstack11l1l1l_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪᏴ"), bstack1l1l1111lll_opy_, logger)
    except Exception as e:
        pass
def bstack1l111111l1_opy_(caps, bstack1l1l111l1ll_opy_):
    if bstack11l1l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᏵ") in caps:
        caps[bstack11l1l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᏶")][bstack11l1l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࠧ᏷")] = True
        if bstack1l1l111l1ll_opy_:
            caps[bstack11l1l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᏸ")][bstack11l1l1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᏹ")] = bstack1l1l111l1ll_opy_
    else:
        caps[bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࠩᏺ")] = True
        if bstack1l1l111l1ll_opy_:
            caps[bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᏻ")] = bstack1l1l111l1ll_opy_
def bstack1l1l111l1l1_opy_(bstack1l1llll1_opy_):
    bstack1l1l111l11l_opy_ = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪᏼ"), bstack11l1l1l_opy_ (u"ࠧࠨᏽ"))
    if bstack1l1l111l11l_opy_ == bstack11l1l1l_opy_ (u"ࠨࠩ᏾") or bstack1l1l111l11l_opy_ == bstack11l1l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ᏿"):
        threading.current_thread().testStatus = bstack1l1llll1_opy_
    else:
        if bstack1l1llll1_opy_ == bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ᐀"):
            threading.current_thread().testStatus = bstack1l1llll1_opy_