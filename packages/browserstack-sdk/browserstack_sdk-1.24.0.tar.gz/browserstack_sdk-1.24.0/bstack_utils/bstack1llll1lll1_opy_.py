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
from browserstack_sdk.bstack111l11l1_opy_ import bstack111lll1l_opy_
from browserstack_sdk.bstack1lll1l1l_opy_ import RobotHandler
def bstack11llll1lll_opy_(framework):
    if framework.lower() == bstack11l1l1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᴰ"):
        return bstack111lll1l_opy_.version()
    elif framework.lower() == bstack11l1l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪᴱ"):
        return RobotHandler.version()
    elif framework.lower() == bstack11l1l1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬᴲ"):
        import behave
        return behave.__version__
    else:
        return bstack11l1l1l_opy_ (u"࠭ࡵ࡯࡭ࡱࡳࡼࡴࠧᴳ")
def bstack1ll11ll1l_opy_():
    import bstack11l1111llll_opy_
    framework_name=[]
    framework_version=[]
    try:
        from selenium import webdriver
        framework_name.append(bstack11l1l1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩᴴ"))
        framework_version.append(bstack11l1111llll_opy_.bstack11l111l1111_opy_(bstack11l1l1l_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥᴵ")).version)
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11l1l1l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᴶ"))
        framework_version.append(bstack11l1111llll_opy_.bstack11l111l1111_opy_(bstack11l1l1l_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢᴷ")).version)
    except:
        pass
    return {
        bstack11l1l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᴸ"): bstack11l1l1l_opy_ (u"ࠬࡥࠧᴹ").join(framework_name),
        bstack11l1l1l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧᴺ"): bstack11l1l1l_opy_ (u"ࠧࡠࠩᴻ").join(framework_version)
    }