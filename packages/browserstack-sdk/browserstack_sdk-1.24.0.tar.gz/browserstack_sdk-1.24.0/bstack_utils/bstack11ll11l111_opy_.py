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
import re
from bstack_utils.bstack1ll1111l1l_opy_ import bstack1l1l111l1l1_opy_
def bstack1l111ll1lll_opy_(fixture_name):
    if fixture_name.startswith(bstack11l1l1l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩយ")):
        return bstack11l1l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩរ")
    elif fixture_name.startswith(bstack11l1l1l_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩល")):
        return bstack11l1l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩវ")
    elif fixture_name.startswith(bstack11l1l1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩឝ")):
        return bstack11l1l1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩឞ")
    elif fixture_name.startswith(bstack11l1l1l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫស")):
        return bstack11l1l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩហ")
def bstack1l111lll1ll_opy_(fixture_name):
    return bool(re.match(bstack11l1l1l_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡽ࡯ࡲࡨࡺࡲࡥࠪࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ឡ"), fixture_name))
def bstack1l111ll1111_opy_(fixture_name):
    return bool(re.match(bstack11l1l1l_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪអ"), fixture_name))
def bstack1l111ll1ll1_opy_(fixture_name):
    return bool(re.match(bstack11l1l1l_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪឣ"), fixture_name))
def bstack1l111ll11l1_opy_(fixture_name):
    if fixture_name.startswith(bstack11l1l1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ឤ")):
        return bstack11l1l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ឥ"), bstack11l1l1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫឦ")
    elif fixture_name.startswith(bstack11l1l1l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឧ")):
        return bstack11l1l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧឨ"), bstack11l1l1l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ឩ")
    elif fixture_name.startswith(bstack11l1l1l_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨឪ")):
        return bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨឫ"), bstack11l1l1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩឬ")
    elif fixture_name.startswith(bstack11l1l1l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩឭ")):
        return bstack11l1l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩឮ"), bstack11l1l1l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫឯ")
    return None, None
def bstack1l111lll11l_opy_(hook_name):
    if hook_name in [bstack11l1l1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨឰ"), bstack11l1l1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬឱ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1l111ll1l11_opy_(hook_name):
    if hook_name in [bstack11l1l1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬឲ"), bstack11l1l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫឳ")]:
        return bstack11l1l1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫ឴")
    elif hook_name in [bstack11l1l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭឵"), bstack11l1l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ា")]:
        return bstack11l1l1l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ិ")
    elif hook_name in [bstack11l1l1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧី"), bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ឹ")]:
        return bstack11l1l1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩឺ")
    elif hook_name in [bstack11l1l1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨុ"), bstack11l1l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨូ")]:
        return bstack11l1l1l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫួ")
    return hook_name
def bstack1l111ll11ll_opy_(node, scenario):
    if hasattr(node, bstack11l1l1l_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫើ")):
        parts = node.nodeid.rsplit(bstack11l1l1l_opy_ (u"ࠥ࡟ࠧឿ"))
        params = parts[-1]
        return bstack11l1l1l_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦៀ").format(scenario.name, params)
    return scenario.name
def bstack1l111ll1l1l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11l1l1l_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧេ")):
            examples = list(node.callspec.params[bstack11l1l1l_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩࠬែ")].values())
        return examples
    except:
        return []
def bstack1l111ll111l_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1l111lll111_opy_(report):
    try:
        status = bstack11l1l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧៃ")
        if report.passed or (report.failed and hasattr(report, bstack11l1l1l_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥោ"))):
            status = bstack11l1l1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩៅ")
        elif report.skipped:
            status = bstack11l1l1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫំ")
        bstack1l1l111l1l1_opy_(status)
    except:
        pass
def bstack1l1l1ll1l1_opy_(status):
    try:
        bstack1l111lll1l1_opy_ = bstack11l1l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫះ")
        if status == bstack11l1l1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬៈ"):
            bstack1l111lll1l1_opy_ = bstack11l1l1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭៉")
        elif status == bstack11l1l1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ៊"):
            bstack1l111lll1l1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ់")
        bstack1l1l111l1l1_opy_(bstack1l111lll1l1_opy_)
    except:
        pass
def bstack1l111llll11_opy_(item=None, report=None, summary=None, extra=None):
    return