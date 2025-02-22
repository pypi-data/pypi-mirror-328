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
import os
import re
from enum import Enum
bstack11l111ll1_opy_ = {
  bstack11l1l1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪᑒ"): bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡷ࠭ᑓ"),
  bstack11l1l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᑔ"): bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡯ࡪࡿࠧᑕ"),
  bstack11l1l1l_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨᑖ"): bstack11l1l1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪᑗ"),
  bstack11l1l1l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᑘ"): bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨࡣࡼ࠹ࡣࠨᑙ"),
  bstack11l1l1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᑚ"): bstack11l1l1l_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࠫᑛ"),
  bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᑜ"): bstack11l1l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࠫᑝ"),
  bstack11l1l1l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᑞ"): bstack11l1l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᑟ"),
  bstack11l1l1l_opy_ (u"ࠨࡦࡨࡦࡺ࡭ࠧᑠ"): bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡦࡨࡦࡺ࡭ࠧᑡ"),
  bstack11l1l1l_opy_ (u"ࠪࡧࡴࡴࡳࡰ࡮ࡨࡐࡴ࡭ࡳࠨᑢ"): bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡳࡰ࡮ࡨࠫᑣ"),
  bstack11l1l1l_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࠪᑤ"): bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࠪᑥ"),
  bstack11l1l1l_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫᑦ"): bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫᑧ"),
  bstack11l1l1l_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࠨᑨ"): bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡹ࡭ࡩ࡫࡯ࠨᑩ"),
  bstack11l1l1l_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡒ࡯ࡨࡵࠪᑪ"): bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡒ࡯ࡨࡵࠪᑫ"),
  bstack11l1l1l_opy_ (u"࠭ࡴࡦ࡮ࡨࡱࡪࡺࡲࡺࡎࡲ࡫ࡸ࠭ᑬ"): bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦ࡮ࡨࡱࡪࡺࡲࡺࡎࡲ࡫ࡸ࠭ᑭ"),
  bstack11l1l1l_opy_ (u"ࠨࡩࡨࡳࡑࡵࡣࡢࡶ࡬ࡳࡳ࠭ᑮ"): bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡩࡨࡳࡑࡵࡣࡢࡶ࡬ࡳࡳ࠭ᑯ"),
  bstack11l1l1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡻࡱࡱࡩࠬᑰ"): bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸ࡮ࡳࡥࡻࡱࡱࡩࠬᑱ"),
  bstack11l1l1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧᑲ"): bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᑳ"),
  bstack11l1l1l_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡈࡵ࡭࡮ࡣࡱࡨࡸ࠭ᑴ"): bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡮ࡣࡶ࡯ࡈࡵ࡭࡮ࡣࡱࡨࡸ࠭ᑵ"),
  bstack11l1l1l_opy_ (u"ࠩ࡬ࡨࡱ࡫ࡔࡪ࡯ࡨࡳࡺࡺࠧᑶ"): bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡬ࡨࡱ࡫ࡔࡪ࡯ࡨࡳࡺࡺࠧᑷ"),
  bstack11l1l1l_opy_ (u"ࠫࡲࡧࡳ࡬ࡄࡤࡷ࡮ࡩࡁࡶࡶ࡫ࠫᑸ"): bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡲࡧࡳ࡬ࡄࡤࡷ࡮ࡩࡁࡶࡶ࡫ࠫᑹ"),
  bstack11l1l1l_opy_ (u"࠭ࡳࡦࡰࡧࡏࡪࡿࡳࠨᑺ"): bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡳࡦࡰࡧࡏࡪࡿࡳࠨᑻ"),
  bstack11l1l1l_opy_ (u"ࠨࡣࡸࡸࡴ࡝ࡡࡪࡶࠪᑼ"): bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡸࡸࡴ࡝ࡡࡪࡶࠪᑽ"),
  bstack11l1l1l_opy_ (u"ࠪ࡬ࡴࡹࡴࡴࠩᑾ"): bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡬ࡴࡹࡴࡴࠩᑿ"),
  bstack11l1l1l_opy_ (u"ࠬࡨࡦࡤࡣࡦ࡬ࡪ࠭ᒀ"): bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡦࡤࡣࡦ࡬ࡪ࠭ᒁ"),
  bstack11l1l1l_opy_ (u"ࠧࡸࡵࡏࡳࡨࡧ࡬ࡔࡷࡳࡴࡴࡸࡴࠨᒂ"): bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡸࡵࡏࡳࡨࡧ࡬ࡔࡷࡳࡴࡴࡸࡴࠨᒃ"),
  bstack11l1l1l_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡆࡳࡷࡹࡒࡦࡵࡷࡶ࡮ࡩࡴࡪࡱࡱࡷࠬᒄ"): bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧ࡭ࡸࡧࡢ࡭ࡧࡆࡳࡷࡹࡒࡦࡵࡷࡶ࡮ࡩࡴࡪࡱࡱࡷࠬᒅ"),
  bstack11l1l1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨᒆ"): bstack11l1l1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬᒇ"),
  bstack11l1l1l_opy_ (u"࠭ࡲࡦࡣ࡯ࡑࡴࡨࡩ࡭ࡧࠪᒈ"): bstack11l1l1l_opy_ (u"ࠧࡳࡧࡤࡰࡤࡳ࡯ࡣ࡫࡯ࡩࠬᒉ"),
  bstack11l1l1l_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᒊ"): bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡳࡴ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᒋ"),
  bstack11l1l1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡑࡩࡹࡽ࡯ࡳ࡭ࠪᒌ"): bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡺࡹࡴࡰ࡯ࡑࡩࡹࡽ࡯ࡳ࡭ࠪᒍ"),
  bstack11l1l1l_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡖࡲࡰࡨ࡬ࡰࡪ࠭ᒎ"): bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡴࡥࡵࡹࡲࡶࡰࡖࡲࡰࡨ࡬ࡰࡪ࠭ᒏ"),
  bstack11l1l1l_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭ᒐ"): bstack11l1l1l_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡔࡵ࡯ࡇࡪࡸࡴࡴࠩᒑ"),
  bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᒒ"): bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᒓ"),
  bstack11l1l1l_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᒔ"): bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸࡵࡵࡳࡥࡨࠫᒕ"),
  bstack11l1l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᒖ"): bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᒗ"),
  bstack11l1l1l_opy_ (u"ࠨࡪࡲࡷࡹࡔࡡ࡮ࡧࠪᒘ"): bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡪࡲࡷࡹࡔࡡ࡮ࡧࠪᒙ"),
  bstack11l1l1l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡖ࡭ࡲ࠭ᒚ"): bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡩࡳࡧࡢ࡭ࡧࡖ࡭ࡲ࠭ᒛ"),
  bstack11l1l1l_opy_ (u"ࠬࡹࡩ࡮ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᒜ"): bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡩ࡮ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᒝ"),
  bstack11l1l1l_opy_ (u"ࠧࡶࡲ࡯ࡳࡦࡪࡍࡦࡦ࡬ࡥࠬᒞ"): bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡲ࡯ࡳࡦࡪࡍࡦࡦ࡬ࡥࠬᒟ"),
  bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᒠ"): bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᒡ"),
  bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᒢ"): bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᒣ")
}
bstack1l11l1l1l11_opy_ = [
  bstack11l1l1l_opy_ (u"࠭࡯ࡴࠩᒤ"),
  bstack11l1l1l_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪᒥ"),
  bstack11l1l1l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪᒦ"),
  bstack11l1l1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᒧ"),
  bstack11l1l1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧᒨ"),
  bstack11l1l1l_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨᒩ"),
  bstack11l1l1l_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᒪ"),
]
bstack1l1l11lll_opy_ = {
  bstack11l1l1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᒫ"): [bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨᒬ"), bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡤࡔࡁࡎࡇࠪᒭ")],
  bstack11l1l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᒮ"): bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭ᒯ"),
  bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᒰ"): bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡒࡆࡓࡅࠨᒱ"),
  bstack11l1l1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᒲ"): bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠬᒳ"),
  bstack11l1l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᒴ"): bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫᒵ"),
  bstack11l1l1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᒶ"): bstack11l1l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡆࡘࡁࡍࡎࡈࡐࡘࡥࡐࡆࡔࡢࡔࡑࡇࡔࡇࡑࡕࡑࠬᒷ"),
  bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᒸ"): bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࠫᒹ"),
  bstack11l1l1l_opy_ (u"ࠧࡳࡧࡵࡹࡳ࡚ࡥࡴࡶࡶࠫᒺ"): bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬᒻ"),
  bstack11l1l1l_opy_ (u"ࠩࡤࡴࡵ࠭ᒼ"): [bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡔࡕࡥࡉࡅࠩᒽ"), bstack11l1l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡕࡖࠧᒾ")],
  bstack11l1l1l_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᒿ"): bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡙ࡄࡌࡡࡏࡓࡌࡒࡅࡗࡇࡏࠫᓀ"),
  bstack11l1l1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᓁ"): bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᓂ"),
  bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᓃ"): bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡐࡄࡖࡉࡗ࡜ࡁࡃࡋࡏࡍ࡙࡟ࠧᓄ"),
  bstack11l1l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨᓅ"): bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙࡛ࡒࡃࡑࡖࡇࡆࡒࡅࠨᓆ")
}
bstack1111ll111_opy_ = {
  bstack11l1l1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᓇ"): [bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡵࡣࡳࡧ࡭ࡦࠩᓈ"), bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨࡶࡓࡧ࡭ࡦࠩᓉ")],
  bstack11l1l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᓊ"): [bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴࡡ࡮ࡩࡾ࠭ᓋ"), bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᓌ")],
  bstack11l1l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᓍ"): bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᓎ"),
  bstack11l1l1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᓏ"): bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᓐ"),
  bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᓑ"): bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᓒ"),
  bstack11l1l1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫᓓ"): [bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡵࡶࡰࠨᓔ"), bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬᓕ")],
  bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫᓖ"): bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭ᓗ"),
  bstack11l1l1l_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡕࡧࡶࡸࡸ࠭ᓘ"): bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡵࡩࡷࡻ࡮ࡕࡧࡶࡸࡸ࠭ᓙ"),
  bstack11l1l1l_opy_ (u"ࠫࡦࡶࡰࠨᓚ"): bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡶࡰࠨᓛ"),
  bstack11l1l1l_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᓜ"): bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᓝ"),
  bstack11l1l1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᓞ"): bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᓟ")
}
bstack11111ll11_opy_ = {
  bstack11l1l1l_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᓠ"): bstack11l1l1l_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᓡ"),
  bstack11l1l1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧᓢ"): [bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᓣ"), bstack11l1l1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠪᓤ")],
  bstack11l1l1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᓥ"): bstack11l1l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᓦ"),
  bstack11l1l1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧᓧ"): bstack11l1l1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫᓨ"),
  bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᓩ"): [bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧᓪ"), bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭ᓫ")],
  bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᓬ"): bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫᓭ"),
  bstack11l1l1l_opy_ (u"ࠪࡶࡪࡧ࡬ࡎࡱࡥ࡭ࡱ࡫ࠧᓮ"): bstack11l1l1l_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡡࡰࡳࡧ࡯࡬ࡦࠩᓯ"),
  bstack11l1l1l_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᓰ"): [bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡰࡱ࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᓱ"), bstack11l1l1l_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᓲ")],
  bstack11l1l1l_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡊࡰࡶࡩࡨࡻࡲࡦࡅࡨࡶࡹࡹࠧᓳ"): [bstack11l1l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡕࡶࡰࡈ࡫ࡲࡵࡵࠪᓴ"), bstack11l1l1l_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡖࡷࡱࡉࡥࡳࡶࠪᓵ")]
}
bstack1lllll1111_opy_ = [
  bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡍࡳࡹࡥࡤࡷࡵࡩࡈ࡫ࡲࡵࡵࠪᓶ"),
  bstack11l1l1l_opy_ (u"ࠬࡶࡡࡨࡧࡏࡳࡦࡪࡓࡵࡴࡤࡸࡪ࡭ࡹࠨᓷ"),
  bstack11l1l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬᓸ"),
  bstack11l1l1l_opy_ (u"ࠧࡴࡧࡷ࡛࡮ࡴࡤࡰࡹࡕࡩࡨࡺࠧᓹ"),
  bstack11l1l1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡵࡵࡵࡵࠪᓺ"),
  bstack11l1l1l_opy_ (u"ࠩࡶࡸࡷ࡯ࡣࡵࡈ࡬ࡰࡪࡏ࡮ࡵࡧࡵࡥࡨࡺࡡࡣ࡫࡯࡭ࡹࡿࠧᓻ"),
  bstack11l1l1l_opy_ (u"ࠪࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡖࡲࡰ࡯ࡳࡸࡇ࡫ࡨࡢࡸ࡬ࡳࡷ࠭ᓼ"),
  bstack11l1l1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᓽ"),
  bstack11l1l1l_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪᓾ"),
  bstack11l1l1l_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᓿ"),
  bstack11l1l1l_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᔀ"),
  bstack11l1l1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᔁ"),
]
bstack11l1l1l1ll_opy_ = [
  bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᔂ"),
  bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧᔃ"),
  bstack11l1l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪᔄ"),
  bstack11l1l1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬᔅ"),
  bstack11l1l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᔆ"),
  bstack11l1l1l_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᔇ"),
  bstack11l1l1l_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᔈ"),
  bstack11l1l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᔉ"),
  bstack11l1l1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᔊ"),
  bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩᔋ"),
  bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᔌ"),
  bstack11l1l1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠨᔍ"),
  bstack11l1l1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡔࡢࡩࠪᔎ"),
  bstack11l1l1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᔏ"),
  bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᔐ"),
  bstack11l1l1l_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡖࡨࡷࡹࡹࠧᔑ"),
  bstack11l1l1l_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠳ࠪᔒ"),
  bstack11l1l1l_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠵ࠫᔓ"),
  bstack11l1l1l_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠷ࠬᔔ"),
  bstack11l1l1l_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠹࠭ᔕ"),
  bstack11l1l1l_opy_ (u"ࠨࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤ࠻ࠧᔖ"),
  bstack11l1l1l_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠶ࠨᔗ"),
  bstack11l1l1l_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠸ࠩᔘ"),
  bstack11l1l1l_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠺ࠪᔙ"),
  bstack11l1l1l_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠼ࠫᔚ"),
  bstack11l1l1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᔛ"),
  bstack11l1l1l_opy_ (u"ࠧࡱࡧࡵࡧࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᔜ"),
  bstack11l1l1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨࠫᔝ"),
  bstack11l1l1l_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫᔞ"),
  bstack11l1l1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧᔟ"),
  bstack11l1l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᔠ")
]
bstack1l11ll111l1_opy_ = [
  bstack11l1l1l_opy_ (u"ࠬࡻࡰ࡭ࡱࡤࡨࡒ࡫ࡤࡪࡣࠪᔡ"),
  bstack11l1l1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᔢ"),
  bstack11l1l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᔣ"),
  bstack11l1l1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᔤ"),
  bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺࡐࡳ࡫ࡲࡶ࡮ࡺࡹࠨᔥ"),
  bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᔦ"),
  bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡗࡥ࡬࠭ᔧ"),
  bstack11l1l1l_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᔨ"),
  bstack11l1l1l_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᔩ"),
  bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᔪ"),
  bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᔫ"),
  bstack11l1l1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨᔬ"),
  bstack11l1l1l_opy_ (u"ࠪࡳࡸ࠭ᔭ"),
  bstack11l1l1l_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧᔮ"),
  bstack11l1l1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡶࠫᔯ"),
  bstack11l1l1l_opy_ (u"࠭ࡡࡶࡶࡲ࡛ࡦ࡯ࡴࠨᔰ"),
  bstack11l1l1l_opy_ (u"ࠧࡳࡧࡪ࡭ࡴࡴࠧᔱ"),
  bstack11l1l1l_opy_ (u"ࠨࡶ࡬ࡱࡪࢀ࡯࡯ࡧࠪᔲ"),
  bstack11l1l1l_opy_ (u"ࠩࡰࡥࡨ࡮ࡩ࡯ࡧࠪᔳ"),
  bstack11l1l1l_opy_ (u"ࠪࡶࡪࡹ࡯࡭ࡷࡷ࡭ࡴࡴࠧᔴ"),
  bstack11l1l1l_opy_ (u"ࠫ࡮ࡪ࡬ࡦࡖ࡬ࡱࡪࡵࡵࡵࠩᔵ"),
  bstack11l1l1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡔࡸࡩࡦࡰࡷࡥࡹ࡯࡯࡯ࠩᔶ"),
  bstack11l1l1l_opy_ (u"࠭ࡶࡪࡦࡨࡳࠬᔷ"),
  bstack11l1l1l_opy_ (u"ࠧ࡯ࡱࡓࡥ࡬࡫ࡌࡰࡣࡧࡘ࡮ࡳࡥࡰࡷࡷࠫᔸ"),
  bstack11l1l1l_opy_ (u"ࠨࡤࡩࡧࡦࡩࡨࡦࠩᔹ"),
  bstack11l1l1l_opy_ (u"ࠩࡧࡩࡧࡻࡧࠨᔺ"),
  bstack11l1l1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡖࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧᔻ"),
  bstack11l1l1l_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡗࡪࡴࡤࡌࡧࡼࡷࠬᔼ"),
  bstack11l1l1l_opy_ (u"ࠬࡸࡥࡢ࡮ࡐࡳࡧ࡯࡬ࡦࠩᔽ"),
  bstack11l1l1l_opy_ (u"࠭࡮ࡰࡒ࡬ࡴࡪࡲࡩ࡯ࡧࠪᔾ"),
  bstack11l1l1l_opy_ (u"ࠧࡤࡪࡨࡧࡰ࡛ࡒࡍࠩᔿ"),
  bstack11l1l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᕀ"),
  bstack11l1l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡅࡲࡳࡰ࡯ࡥࡴࠩᕁ"),
  bstack11l1l1l_opy_ (u"ࠪࡧࡦࡶࡴࡶࡴࡨࡇࡷࡧࡳࡩࠩᕂ"),
  bstack11l1l1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨᕃ"),
  bstack11l1l1l_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᕄ"),
  bstack11l1l1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰ࡙ࡩࡷࡹࡩࡰࡰࠪᕅ"),
  bstack11l1l1l_opy_ (u"ࠧ࡯ࡱࡅࡰࡦࡴ࡫ࡑࡱ࡯ࡰ࡮ࡴࡧࠨᕆ"),
  bstack11l1l1l_opy_ (u"ࠨ࡯ࡤࡷࡰ࡙ࡥ࡯ࡦࡎࡩࡾࡹࠧᕇ"),
  bstack11l1l1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡎࡲ࡫ࡸ࠭ᕈ"),
  bstack11l1l1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡌࡨࠬᕉ"),
  bstack11l1l1l_opy_ (u"ࠫࡩ࡫ࡤࡪࡥࡤࡸࡪࡪࡄࡦࡸ࡬ࡧࡪ࠭ᕊ"),
  bstack11l1l1l_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡕࡧࡲࡢ࡯ࡶࠫᕋ"),
  bstack11l1l1l_opy_ (u"࠭ࡰࡩࡱࡱࡩࡓࡻ࡭ࡣࡧࡵࠫᕌ"),
  bstack11l1l1l_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࠬᕍ"),
  bstack11l1l1l_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸࡕࡰࡵ࡫ࡲࡲࡸ࠭ᕎ"),
  bstack11l1l1l_opy_ (u"ࠩࡦࡳࡳࡹ࡯࡭ࡧࡏࡳ࡬ࡹࠧᕏ"),
  bstack11l1l1l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᕐ"),
  bstack11l1l1l_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰࡐࡴ࡭ࡳࠨᕑ"),
  bstack11l1l1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡇ࡯࡯࡮ࡧࡷࡶ࡮ࡩࠧᕒ"),
  bstack11l1l1l_opy_ (u"࠭ࡶࡪࡦࡨࡳ࡛࠸ࠧᕓ"),
  bstack11l1l1l_opy_ (u"ࠧ࡮࡫ࡧࡗࡪࡹࡳࡪࡱࡱࡍࡳࡹࡴࡢ࡮࡯ࡅࡵࡶࡳࠨᕔ"),
  bstack11l1l1l_opy_ (u"ࠨࡧࡶࡴࡷ࡫ࡳࡴࡱࡖࡩࡷࡼࡥࡳࠩᕕ"),
  bstack11l1l1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࡐࡴ࡭ࡳࠨᕖ"),
  bstack11l1l1l_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࡈࡪࡰࠨᕗ"),
  bstack11l1l1l_opy_ (u"ࠫࡹ࡫࡬ࡦ࡯ࡨࡸࡷࡿࡌࡰࡩࡶࠫᕘ"),
  bstack11l1l1l_opy_ (u"ࠬࡹࡹ࡯ࡥࡗ࡭ࡲ࡫ࡗࡪࡶ࡫ࡒ࡙ࡖࠧᕙ"),
  bstack11l1l1l_opy_ (u"࠭ࡧࡦࡱࡏࡳࡨࡧࡴࡪࡱࡱࠫᕚ"),
  bstack11l1l1l_opy_ (u"ࠧࡨࡲࡶࡐࡴࡩࡡࡵ࡫ࡲࡲࠬᕛ"),
  bstack11l1l1l_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩᕜ"),
  bstack11l1l1l_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡐࡨࡸࡼࡵࡲ࡬ࠩᕝ"),
  bstack11l1l1l_opy_ (u"ࠪࡪࡴࡸࡣࡦࡅ࡫ࡥࡳ࡭ࡥࡋࡣࡵࠫᕞ"),
  bstack11l1l1l_opy_ (u"ࠫࡽࡳࡳࡋࡣࡵࠫᕟ"),
  bstack11l1l1l_opy_ (u"ࠬࡾ࡭ࡹࡌࡤࡶࠬᕠ"),
  bstack11l1l1l_opy_ (u"࠭࡭ࡢࡵ࡮ࡇࡴࡳ࡭ࡢࡰࡧࡷࠬᕡ"),
  bstack11l1l1l_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧᕢ"),
  bstack11l1l1l_opy_ (u"ࠨࡹࡶࡐࡴࡩࡡ࡭ࡕࡸࡴࡵࡵࡲࡵࠩᕣ"),
  bstack11l1l1l_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡆࡳࡷࡹࡒࡦࡵࡷࡶ࡮ࡩࡴࡪࡱࡱࡷࠬᕤ"),
  bstack11l1l1l_opy_ (u"ࠪࡥࡵࡶࡖࡦࡴࡶ࡭ࡴࡴࠧᕥ"),
  bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡍࡳࡹࡥࡤࡷࡵࡩࡈ࡫ࡲࡵࡵࠪᕦ"),
  bstack11l1l1l_opy_ (u"ࠬࡸࡥࡴ࡫ࡪࡲࡆࡶࡰࠨᕧ"),
  bstack11l1l1l_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁ࡯࡫ࡰࡥࡹ࡯࡯࡯ࡵࠪᕨ"),
  bstack11l1l1l_opy_ (u"ࠧࡤࡣࡱࡥࡷࡿࠧᕩ"),
  bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩᕪ"),
  bstack11l1l1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩᕫ"),
  bstack11l1l1l_opy_ (u"ࠪ࡭ࡪ࠭ᕬ"),
  bstack11l1l1l_opy_ (u"ࠫࡪࡪࡧࡦࠩᕭ"),
  bstack11l1l1l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬᕮ"),
  bstack11l1l1l_opy_ (u"࠭ࡱࡶࡧࡸࡩࠬᕯ"),
  bstack11l1l1l_opy_ (u"ࠧࡪࡰࡷࡩࡷࡴࡡ࡭ࠩᕰ"),
  bstack11l1l1l_opy_ (u"ࠨࡣࡳࡴࡘࡺ࡯ࡳࡧࡆࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠩᕱ"),
  bstack11l1l1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡅࡤࡱࡪࡸࡡࡊ࡯ࡤ࡫ࡪࡏ࡮࡫ࡧࡦࡸ࡮ࡵ࡮ࠨᕲ"),
  bstack11l1l1l_opy_ (u"ࠪࡲࡪࡺࡷࡰࡴ࡮ࡐࡴ࡭ࡳࡆࡺࡦࡰࡺࡪࡥࡉࡱࡶࡸࡸ࠭ᕳ"),
  bstack11l1l1l_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࡋࡱࡧࡱࡻࡤࡦࡊࡲࡷࡹࡹࠧᕴ"),
  bstack11l1l1l_opy_ (u"ࠬࡻࡰࡥࡣࡷࡩࡆࡶࡰࡔࡧࡷࡸ࡮ࡴࡧࡴࠩᕵ"),
  bstack11l1l1l_opy_ (u"࠭ࡲࡦࡵࡨࡶࡻ࡫ࡄࡦࡸ࡬ࡧࡪ࠭ᕶ"),
  bstack11l1l1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧᕷ"),
  bstack11l1l1l_opy_ (u"ࠨࡵࡨࡲࡩࡑࡥࡺࡵࠪᕸ"),
  bstack11l1l1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡒࡤࡷࡸࡩ࡯ࡥࡧࠪᕹ"),
  bstack11l1l1l_opy_ (u"ࠪࡹࡵࡪࡡࡵࡧࡌࡳࡸࡊࡥࡷ࡫ࡦࡩࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭ᕺ"),
  bstack11l1l1l_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡅࡺࡪࡩࡰࡋࡱ࡮ࡪࡩࡴࡪࡱࡱࠫᕻ"),
  bstack11l1l1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡆࡶࡰ࡭ࡧࡓࡥࡾ࠭ᕼ"),
  bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧᕽ"),
  bstack11l1l1l_opy_ (u"ࠧࡸࡦ࡬ࡳࡘ࡫ࡲࡷ࡫ࡦࡩࠬᕾ"),
  bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᕿ"),
  bstack11l1l1l_opy_ (u"ࠩࡳࡶࡪࡼࡥ࡯ࡶࡆࡶࡴࡹࡳࡔ࡫ࡷࡩ࡙ࡸࡡࡤ࡭࡬ࡲ࡬࠭ᖀ"),
  bstack11l1l1l_opy_ (u"ࠪ࡬࡮࡭ࡨࡄࡱࡱࡸࡷࡧࡳࡵࠩᖁ"),
  bstack11l1l1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡔࡷ࡫ࡦࡦࡴࡨࡲࡨ࡫ࡳࠨᖂ"),
  bstack11l1l1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡘ࡯࡭ࠨᖃ"),
  bstack11l1l1l_opy_ (u"࠭ࡳࡪ࡯ࡒࡴࡹ࡯࡯࡯ࡵࠪᖄ"),
  bstack11l1l1l_opy_ (u"ࠧࡳࡧࡰࡳࡻ࡫ࡉࡐࡕࡄࡴࡵ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࡌࡰࡥࡤࡰ࡮ࢀࡡࡵ࡫ࡲࡲࠬᖅ"),
  bstack11l1l1l_opy_ (u"ࠨࡪࡲࡷࡹࡔࡡ࡮ࡧࠪᖆ"),
  bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᖇ"),
  bstack11l1l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬᖈ"),
  bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪᖉ"),
  bstack11l1l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧᖊ"),
  bstack11l1l1l_opy_ (u"࠭ࡰࡢࡩࡨࡐࡴࡧࡤࡔࡶࡵࡥࡹ࡫ࡧࡺࠩᖋ"),
  bstack11l1l1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭ᖌ"),
  bstack11l1l1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡵࡵࡵࡵࠪᖍ"),
  bstack11l1l1l_opy_ (u"ࠩࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡕࡸ࡯࡮ࡲࡷࡆࡪ࡮ࡡࡷ࡫ࡲࡶࠬᖎ")
]
bstack1lll11111_opy_ = {
  bstack11l1l1l_opy_ (u"ࠪࡺࠬᖏ"): bstack11l1l1l_opy_ (u"ࠫࡻ࠭ᖐ"),
  bstack11l1l1l_opy_ (u"ࠬ࡬ࠧᖑ"): bstack11l1l1l_opy_ (u"࠭ࡦࠨᖒ"),
  bstack11l1l1l_opy_ (u"ࠧࡧࡱࡵࡧࡪ࠭ᖓ"): bstack11l1l1l_opy_ (u"ࠨࡨࡲࡶࡨ࡫ࠧᖔ"),
  bstack11l1l1l_opy_ (u"ࠩࡲࡲࡱࡿࡡࡶࡶࡲࡱࡦࡺࡥࠨᖕ"): bstack11l1l1l_opy_ (u"ࠪࡳࡳࡲࡹࡂࡷࡷࡳࡲࡧࡴࡦࠩᖖ"),
  bstack11l1l1l_opy_ (u"ࠫ࡫ࡵࡲࡤࡧ࡯ࡳࡨࡧ࡬ࠨᖗ"): bstack11l1l1l_opy_ (u"ࠬ࡬࡯ࡳࡥࡨࡰࡴࡩࡡ࡭ࠩᖘ"),
  bstack11l1l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡭ࡵࡳࡵࠩᖙ"): bstack11l1l1l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡎ࡯ࡴࡶࠪᖚ"),
  bstack11l1l1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡰࡰࡴࡷࠫᖛ"): bstack11l1l1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬᖜ"),
  bstack11l1l1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡷࡶࡩࡷ࠭ᖝ"): bstack11l1l1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧᖞ"),
  bstack11l1l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡴࡦࡹࡳࠨᖟ"): bstack11l1l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩᖠ"),
  bstack11l1l1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼ࡬ࡴࡹࡴࠨᖡ"): bstack11l1l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽࡍࡵࡳࡵࠩᖢ"),
  bstack11l1l1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡱࡴࡲࡼࡾࡶ࡯ࡳࡶࠪᖣ"): bstack11l1l1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡒࡵࡳࡽࡿࡐࡰࡴࡷࠫᖤ"),
  bstack11l1l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡶࡵࡨࡶࠬᖥ"): bstack11l1l1l_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡘࡷࡪࡸࠧᖦ"),
  bstack11l1l1l_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡹࡸ࡫ࡲࠨᖧ"): bstack11l1l1l_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽ࡚ࡹࡥࡳࠩᖨ"),
  bstack11l1l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽࡵࡧࡳࡴࠩᖩ"): bstack11l1l1l_opy_ (u"ࠩ࠰ࡰࡴࡩࡡ࡭ࡒࡵࡳࡽࡿࡐࡢࡵࡶࠫᖪ"),
  bstack11l1l1l_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡱࡣࡶࡷࠬᖫ"): bstack11l1l1l_opy_ (u"ࠫ࠲ࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡒࡤࡷࡸ࠭ᖬ"),
  bstack11l1l1l_opy_ (u"ࠬࡨࡩ࡯ࡣࡵࡽࡵࡧࡴࡩࠩᖭ"): bstack11l1l1l_opy_ (u"࠭ࡢࡪࡰࡤࡶࡾࡶࡡࡵࡪࠪᖮ"),
  bstack11l1l1l_opy_ (u"ࠧࡱࡣࡦࡪ࡮ࡲࡥࠨᖯ"): bstack11l1l1l_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫᖰ"),
  bstack11l1l1l_opy_ (u"ࠩࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫᖱ"): bstack11l1l1l_opy_ (u"ࠪ࠱ࡵࡧࡣ࠮ࡨ࡬ࡰࡪ࠭ᖲ"),
  bstack11l1l1l_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧᖳ"): bstack11l1l1l_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨᖴ"),
  bstack11l1l1l_opy_ (u"࠭࡬ࡰࡩࡩ࡭ࡱ࡫ࠧᖵ"): bstack11l1l1l_opy_ (u"ࠧ࡭ࡱࡪࡪ࡮ࡲࡥࠨᖶ"),
  bstack11l1l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᖷ"): bstack11l1l1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᖸ"),
  bstack11l1l1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠬᖹ"): bstack11l1l1l_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡖࡪࡶࡥࡢࡶࡨࡶࠬᖺ")
}
bstack1l11l11ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡧࡪࡶ࡫ࡹࡧ࠴ࡣࡰ࡯࠲ࡴࡪࡸࡣࡺ࠱ࡦࡰ࡮࠵ࡲࡦ࡮ࡨࡥࡸ࡫ࡳ࠰࡮ࡤࡸࡪࡹࡴ࠰ࡦࡲࡻࡳࡲ࡯ࡢࡦࠥᖻ")
bstack1l11l1lllll_opy_ = bstack11l1l1l_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠵ࡨࡦࡣ࡯ࡸ࡭ࡩࡨࡦࡥ࡮ࠦᖼ")
bstack1ll1l11l1l_opy_ = bstack11l1l1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡧࡧࡷ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡵࡨࡲࡩࡥࡳࡥ࡭ࡢࡩࡻ࡫࡮ࡵࡵࠥᖽ")
bstack1ll11lll1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱࡫ࡹࡧ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡺࡨ࠴࡮ࡵࡣࠩᖾ")
bstack111lll11l_opy_ = bstack11l1l1l_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱࡫ࡹࡧ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠬᖿ")
bstack11l111l111_opy_ = bstack11l1l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳࡭ࡻࡢ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡳ࡫ࡸࡵࡡ࡫ࡹࡧࡹࠧᗀ")
bstack1l11l11l11l_opy_ = {
  bstack11l1l1l_opy_ (u"ࠫࡨࡸࡩࡵ࡫ࡦࡥࡱ࠭ᗁ"): 50,
  bstack11l1l1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᗂ"): 40,
  bstack11l1l1l_opy_ (u"࠭ࡷࡢࡴࡱ࡭ࡳ࡭ࠧᗃ"): 30,
  bstack11l1l1l_opy_ (u"ࠧࡪࡰࡩࡳࠬᗄ"): 20,
  bstack11l1l1l_opy_ (u"ࠨࡦࡨࡦࡺ࡭ࠧᗅ"): 10
}
bstack11lll1l1ll_opy_ = bstack1l11l11l11l_opy_[bstack11l1l1l_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧᗆ")]
bstack1ll11lll1l_opy_ = bstack11l1l1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࠩᗇ")
bstack1l111lll1l_opy_ = bstack11l1l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࠩᗈ")
bstack1llll1lll_opy_ = bstack11l1l1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࠫᗉ")
bstack1ll1l11ll1_opy_ = bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࠬᗊ")
bstack1111ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴࠡࡣࡱࡨࠥࡶࡹࡵࡧࡶࡸ࠲ࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠠࡱࡣࡦ࡯ࡦ࡭ࡥࡴ࠰ࠣࡤࡵ࡯ࡰࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡶࡩࡱ࡫࡮ࡪࡷࡰࡤࠬᗋ")
bstack1l11l1l111l_opy_ = [bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩᗌ"), bstack11l1l1l_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩᗍ")]
bstack1l11l11l1ll_opy_ = [bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭ᗎ"), bstack11l1l1l_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭ᗏ")]
bstack11llll1ll_opy_ = re.compile(bstack11l1l1l_opy_ (u"ࠬࡤ࡛࡝࡞ࡺ࠱ࡢ࠱࠺࠯ࠬࠧࠫᗐ"))
bstack111l1ll1l_opy_ = [
  bstack11l1l1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡑࡥࡲ࡫ࠧᗑ"),
  bstack11l1l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩᗒ"),
  bstack11l1l1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬᗓ"),
  bstack11l1l1l_opy_ (u"ࠩࡱࡩࡼࡉ࡯࡮࡯ࡤࡲࡩ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ᗔ"),
  bstack11l1l1l_opy_ (u"ࠪࡥࡵࡶࠧᗕ"),
  bstack11l1l1l_opy_ (u"ࠫࡺࡪࡩࡥࠩᗖ"),
  bstack11l1l1l_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧᗗ"),
  bstack11l1l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡪ࠭ᗘ"),
  bstack11l1l1l_opy_ (u"ࠧࡰࡴ࡬ࡩࡳࡺࡡࡵ࡫ࡲࡲࠬᗙ"),
  bstack11l1l1l_opy_ (u"ࠨࡣࡸࡸࡴ࡝ࡥࡣࡸ࡬ࡩࡼ࠭ᗚ"),
  bstack11l1l1l_opy_ (u"ࠩࡱࡳࡗ࡫ࡳࡦࡶࠪᗛ"), bstack11l1l1l_opy_ (u"ࠪࡪࡺࡲ࡬ࡓࡧࡶࡩࡹ࠭ᗜ"),
  bstack11l1l1l_opy_ (u"ࠫࡨࡲࡥࡢࡴࡖࡽࡸࡺࡥ࡮ࡈ࡬ࡰࡪࡹࠧᗝ"),
  bstack11l1l1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡘ࡮ࡳࡩ࡯ࡩࡶࠫᗞ"),
  bstack11l1l1l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡖࡥࡳࡨࡲࡶࡲࡧ࡮ࡤࡧࡏࡳ࡬࡭ࡩ࡯ࡩࠪᗟ"),
  bstack11l1l1l_opy_ (u"ࠧࡰࡶ࡫ࡩࡷࡇࡰࡱࡵࠪᗠ"),
  bstack11l1l1l_opy_ (u"ࠨࡲࡵ࡭ࡳࡺࡐࡢࡩࡨࡗࡴࡻࡲࡤࡧࡒࡲࡋ࡯࡮ࡥࡈࡤ࡭ࡱࡻࡲࡦࠩᗡ"),
  bstack11l1l1l_opy_ (u"ࠩࡤࡴࡵࡇࡣࡵ࡫ࡹ࡭ࡹࡿࠧᗢ"), bstack11l1l1l_opy_ (u"ࠪࡥࡵࡶࡐࡢࡥ࡮ࡥ࡬࡫ࠧᗣ"), bstack11l1l1l_opy_ (u"ࠫࡦࡶࡰࡘࡣ࡬ࡸࡆࡩࡴࡪࡸ࡬ࡸࡾ࠭ᗤ"), bstack11l1l1l_opy_ (u"ࠬࡧࡰࡱ࡙ࡤ࡭ࡹࡖࡡࡤ࡭ࡤ࡫ࡪ࠭ᗥ"), bstack11l1l1l_opy_ (u"࠭ࡡࡱࡲ࡚ࡥ࡮ࡺࡄࡶࡴࡤࡸ࡮ࡵ࡮ࠨᗦ"),
  bstack11l1l1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡒࡦࡣࡧࡽ࡙࡯࡭ࡦࡱࡸࡸࠬᗧ"),
  bstack11l1l1l_opy_ (u"ࠨࡣ࡯ࡰࡴࡽࡔࡦࡵࡷࡔࡦࡩ࡫ࡢࡩࡨࡷࠬᗨ"),
  bstack11l1l1l_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡆࡳࡻ࡫ࡲࡢࡩࡨࠫᗩ"), bstack11l1l1l_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡇࡴࡼࡥࡳࡣࡪࡩࡊࡴࡤࡊࡰࡷࡩࡳࡺࠧᗪ"),
  bstack11l1l1l_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡉ࡫ࡶࡪࡥࡨࡖࡪࡧࡤࡺࡖ࡬ࡱࡪࡵࡵࡵࠩᗫ"),
  bstack11l1l1l_opy_ (u"ࠬࡧࡤࡣࡒࡲࡶࡹ࠭ᗬ"),
  bstack11l1l1l_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡄࡦࡸ࡬ࡧࡪ࡙࡯ࡤ࡭ࡨࡸࠬᗭ"),
  bstack11l1l1l_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡊࡰࡶࡸࡦࡲ࡬ࡕ࡫ࡰࡩࡴࡻࡴࠨᗮ"),
  bstack11l1l1l_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡋࡱࡷࡹࡧ࡬࡭ࡒࡤࡸ࡭࠭ᗯ"),
  bstack11l1l1l_opy_ (u"ࠩࡤࡺࡩ࠭ᗰ"), bstack11l1l1l_opy_ (u"ࠪࡥࡻࡪࡌࡢࡷࡱࡧ࡭࡚ࡩ࡮ࡧࡲࡹࡹ࠭ᗱ"), bstack11l1l1l_opy_ (u"ࠫࡦࡼࡤࡓࡧࡤࡨࡾ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ᗲ"), bstack11l1l1l_opy_ (u"ࠬࡧࡶࡥࡃࡵ࡫ࡸ࠭ᗳ"),
  bstack11l1l1l_opy_ (u"࠭ࡵࡴࡧࡎࡩࡾࡹࡴࡰࡴࡨࠫᗴ"), bstack11l1l1l_opy_ (u"ࠧ࡬ࡧࡼࡷࡹࡵࡲࡦࡒࡤࡸ࡭࠭ᗵ"), bstack11l1l1l_opy_ (u"ࠨ࡭ࡨࡽࡸࡺ࡯ࡳࡧࡓࡥࡸࡹࡷࡰࡴࡧࠫᗶ"),
  bstack11l1l1l_opy_ (u"ࠩ࡮ࡩࡾࡇ࡬ࡪࡣࡶࠫᗷ"), bstack11l1l1l_opy_ (u"ࠪ࡯ࡪࡿࡐࡢࡵࡶࡻࡴࡸࡤࠨᗸ"),
  bstack11l1l1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡈࡼࡪࡩࡵࡵࡣࡥࡰࡪ࠭ᗹ"), bstack11l1l1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡅࡷ࡭ࡳࠨᗺ"), bstack11l1l1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡊࡾࡥࡤࡷࡷࡥࡧࡲࡥࡅ࡫ࡵࠫᗻ"), bstack11l1l1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡉࡨࡳࡱࡰࡩࡒࡧࡰࡱ࡫ࡱ࡫ࡋ࡯࡬ࡦࠩᗼ"), bstack11l1l1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡕࡴࡧࡖࡽࡸࡺࡥ࡮ࡇࡻࡩࡨࡻࡴࡢࡤ࡯ࡩࠬᗽ"),
  bstack11l1l1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡑࡱࡵࡸࠬᗾ"), bstack11l1l1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡒࡲࡶࡹࡹࠧᗿ"),
  bstack11l1l1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡇ࡭ࡸࡧࡢ࡭ࡧࡅࡹ࡮ࡲࡤࡄࡪࡨࡧࡰ࠭ᘀ"),
  bstack11l1l1l_opy_ (u"ࠬࡧࡵࡵࡱ࡚ࡩࡧࡼࡩࡦࡹࡗ࡭ࡲ࡫࡯ࡶࡶࠪᘁ"),
  bstack11l1l1l_opy_ (u"࠭ࡩ࡯ࡶࡨࡲࡹࡇࡣࡵ࡫ࡲࡲࠬᘂ"), bstack11l1l1l_opy_ (u"ࠧࡪࡰࡷࡩࡳࡺࡃࡢࡶࡨ࡫ࡴࡸࡹࠨᘃ"), bstack11l1l1l_opy_ (u"ࠨ࡫ࡱࡸࡪࡴࡴࡇ࡮ࡤ࡫ࡸ࠭ᘄ"), bstack11l1l1l_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡣ࡯ࡍࡳࡺࡥ࡯ࡶࡄࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᘅ"),
  bstack11l1l1l_opy_ (u"ࠪࡨࡴࡴࡴࡔࡶࡲࡴࡆࡶࡰࡐࡰࡕࡩࡸ࡫ࡴࠨᘆ"),
  bstack11l1l1l_opy_ (u"ࠫࡺࡴࡩࡤࡱࡧࡩࡐ࡫ࡹࡣࡱࡤࡶࡩ࠭ᘇ"), bstack11l1l1l_opy_ (u"ࠬࡸࡥࡴࡧࡷࡏࡪࡿࡢࡰࡣࡵࡨࠬᘈ"),
  bstack11l1l1l_opy_ (u"࠭࡮ࡰࡕ࡬࡫ࡳ࠭ᘉ"),
  bstack11l1l1l_opy_ (u"ࠧࡪࡩࡱࡳࡷ࡫ࡕ࡯࡫ࡰࡴࡴࡸࡴࡢࡰࡷ࡚࡮࡫ࡷࡴࠩᘊ"),
  bstack11l1l1l_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡱࡨࡷࡵࡩࡥ࡙ࡤࡸࡨ࡮ࡥࡳࡵࠪᘋ"),
  bstack11l1l1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᘌ"),
  bstack11l1l1l_opy_ (u"ࠪࡶࡪࡩࡲࡦࡣࡷࡩࡈ࡮ࡲࡰ࡯ࡨࡈࡷ࡯ࡶࡦࡴࡖࡩࡸࡹࡩࡰࡰࡶࠫᘍ"),
  bstack11l1l1l_opy_ (u"ࠫࡳࡧࡴࡪࡸࡨ࡛ࡪࡨࡓࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪᘎ"),
  bstack11l1l1l_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩ࡙ࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡒࡤࡸ࡭࠭ᘏ"),
  bstack11l1l1l_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡓࡱࡧࡨࡨࠬᘐ"),
  bstack11l1l1l_opy_ (u"ࠧࡨࡲࡶࡉࡳࡧࡢ࡭ࡧࡧࠫᘑ"),
  bstack11l1l1l_opy_ (u"ࠨ࡫ࡶࡌࡪࡧࡤ࡭ࡧࡶࡷࠬᘒ"),
  bstack11l1l1l_opy_ (u"ࠩࡤࡨࡧࡋࡸࡦࡥࡗ࡭ࡲ࡫࡯ࡶࡶࠪᘓ"),
  bstack11l1l1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡧࡖࡧࡷ࡯ࡰࡵࠩᘔ"),
  bstack11l1l1l_opy_ (u"ࠫࡸࡱࡩࡱࡆࡨࡺ࡮ࡩࡥࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠨᘕ"),
  bstack11l1l1l_opy_ (u"ࠬࡧࡵࡵࡱࡊࡶࡦࡴࡴࡑࡧࡵࡱ࡮ࡹࡳࡪࡱࡱࡷࠬᘖ"),
  bstack11l1l1l_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡎࡢࡶࡸࡶࡦࡲࡏࡳ࡫ࡨࡲࡹࡧࡴࡪࡱࡱࠫᘗ"),
  bstack11l1l1l_opy_ (u"ࠧࡴࡻࡶࡸࡪࡳࡐࡰࡴࡷࠫᘘ"),
  bstack11l1l1l_opy_ (u"ࠨࡴࡨࡱࡴࡺࡥࡂࡦࡥࡌࡴࡹࡴࠨᘙ"),
  bstack11l1l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡕ࡯࡮ࡲࡧࡰ࠭ᘚ"), bstack11l1l1l_opy_ (u"ࠪࡹࡳࡲ࡯ࡤ࡭ࡗࡽࡵ࡫ࠧᘛ"), bstack11l1l1l_opy_ (u"ࠫࡺࡴ࡬ࡰࡥ࡮ࡏࡪࡿࠧᘜ"),
  bstack11l1l1l_opy_ (u"ࠬࡧࡵࡵࡱࡏࡥࡺࡴࡣࡩࠩᘝ"),
  bstack11l1l1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡐࡴ࡭ࡣࡢࡶࡆࡥࡵࡺࡵࡳࡧࠪᘞ"),
  bstack11l1l1l_opy_ (u"ࠧࡶࡰ࡬ࡲࡸࡺࡡ࡭࡮ࡒࡸ࡭࡫ࡲࡑࡣࡦ࡯ࡦ࡭ࡥࡴࠩᘟ"),
  bstack11l1l1l_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦ࡙࡬ࡲࡩࡵࡷࡂࡰ࡬ࡱࡦࡺࡩࡰࡰࠪᘠ"),
  bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡕࡱࡲࡰࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᘡ"),
  bstack11l1l1l_opy_ (u"ࠪࡩࡳ࡬࡯ࡳࡥࡨࡅࡵࡶࡉ࡯ࡵࡷࡥࡱࡲࠧᘢ"),
  bstack11l1l1l_opy_ (u"ࠫࡪࡴࡳࡶࡴࡨ࡛ࡪࡨࡶࡪࡧࡺࡷࡍࡧࡶࡦࡒࡤ࡫ࡪࡹࠧᘣ"), bstack11l1l1l_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼࡊࡥࡷࡶࡲࡳࡱࡹࡐࡰࡴࡷࠫᘤ"), bstack11l1l1l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪ࡝ࡥࡣࡸ࡬ࡩࡼࡊࡥࡵࡣ࡬ࡰࡸࡉ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠩᘥ"),
  bstack11l1l1l_opy_ (u"ࠧࡳࡧࡰࡳࡹ࡫ࡁࡱࡲࡶࡇࡦࡩࡨࡦࡎ࡬ࡱ࡮ࡺࠧᘦ"),
  bstack11l1l1l_opy_ (u"ࠨࡥࡤࡰࡪࡴࡤࡢࡴࡉࡳࡷࡳࡡࡵࠩᘧ"),
  bstack11l1l1l_opy_ (u"ࠩࡥࡹࡳࡪ࡬ࡦࡋࡧࠫᘨ"),
  bstack11l1l1l_opy_ (u"ࠪࡰࡦࡻ࡮ࡤࡪࡗ࡭ࡲ࡫࡯ࡶࡶࠪᘩ"),
  bstack11l1l1l_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࡙ࡥࡳࡸ࡬ࡧࡪࡹࡅ࡯ࡣࡥࡰࡪࡪࠧᘪ"), bstack11l1l1l_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࡓࡦࡴࡹ࡭ࡨ࡫ࡳࡂࡷࡷ࡬ࡴࡸࡩࡻࡧࡧࠫᘫ"),
  bstack11l1l1l_opy_ (u"࠭ࡡࡶࡶࡲࡅࡨࡩࡥࡱࡶࡄࡰࡪࡸࡴࡴࠩᘬ"), bstack11l1l1l_opy_ (u"ࠧࡢࡷࡷࡳࡉ࡯ࡳ࡮࡫ࡶࡷࡆࡲࡥࡳࡶࡶࠫᘭ"),
  bstack11l1l1l_opy_ (u"ࠨࡰࡤࡸ࡮ࡼࡥࡊࡰࡶࡸࡷࡻ࡭ࡦࡰࡷࡷࡑ࡯ࡢࠨᘮ"),
  bstack11l1l1l_opy_ (u"ࠩࡱࡥࡹ࡯ࡶࡦ࡙ࡨࡦ࡙ࡧࡰࠨᘯ"),
  bstack11l1l1l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࡌࡲ࡮ࡺࡩࡢ࡮ࡘࡶࡱ࠭ᘰ"), bstack11l1l1l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࡅࡱࡲ࡯ࡸࡒࡲࡴࡺࡶࡳࠨᘱ"), bstack11l1l1l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࡎ࡭࡮ࡰࡴࡨࡊࡷࡧࡵࡥ࡙ࡤࡶࡳ࡯࡮ࡨࠩᘲ"), bstack11l1l1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡕࡰࡦࡰࡏ࡭ࡳࡱࡳࡊࡰࡅࡥࡨࡱࡧࡳࡱࡸࡲࡩ࠭ᘳ"),
  bstack11l1l1l_opy_ (u"ࠧ࡬ࡧࡨࡴࡐ࡫ࡹࡄࡪࡤ࡭ࡳࡹࠧᘴ"),
  bstack11l1l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡩࡻࡣࡥࡰࡪ࡙ࡴࡳ࡫ࡱ࡫ࡸࡊࡩࡳࠩᘵ"),
  bstack11l1l1l_opy_ (u"ࠩࡳࡶࡴࡩࡥࡴࡵࡄࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᘶ"),
  bstack11l1l1l_opy_ (u"ࠪ࡭ࡳࡺࡥࡳࡍࡨࡽࡉ࡫࡬ࡢࡻࠪᘷ"),
  bstack11l1l1l_opy_ (u"ࠫࡸ࡮࡯ࡸࡋࡒࡗࡑࡵࡧࠨᘸ"),
  bstack11l1l1l_opy_ (u"ࠬࡹࡥ࡯ࡦࡎࡩࡾ࡙ࡴࡳࡣࡷࡩ࡬ࡿࠧᘹ"),
  bstack11l1l1l_opy_ (u"࠭ࡷࡦࡤ࡮࡭ࡹࡘࡥࡴࡲࡲࡲࡸ࡫ࡔࡪ࡯ࡨࡳࡺࡺࠧᘺ"), bstack11l1l1l_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷ࡛ࡦ࡯ࡴࡕ࡫ࡰࡩࡴࡻࡴࠨᘻ"),
  bstack11l1l1l_opy_ (u"ࠨࡴࡨࡱࡴࡺࡥࡅࡧࡥࡹ࡬ࡖࡲࡰࡺࡼࠫᘼ"),
  bstack11l1l1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡃࡶࡽࡳࡩࡅࡹࡧࡦࡹࡹ࡫ࡆࡳࡱࡰࡌࡹࡺࡰࡴࠩᘽ"),
  bstack11l1l1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡍࡱࡪࡇࡦࡶࡴࡶࡴࡨࠫᘾ"),
  bstack11l1l1l_opy_ (u"ࠫࡼ࡫ࡢ࡬࡫ࡷࡈࡪࡨࡵࡨࡒࡵࡳࡽࡿࡐࡰࡴࡷࠫᘿ"),
  bstack11l1l1l_opy_ (u"ࠬ࡬ࡵ࡭࡮ࡆࡳࡳࡺࡥࡹࡶࡏ࡭ࡸࡺࠧᙀ"),
  bstack11l1l1l_opy_ (u"࠭ࡷࡢ࡫ࡷࡊࡴࡸࡁࡱࡲࡖࡧࡷ࡯ࡰࡵࠩᙁ"),
  bstack11l1l1l_opy_ (u"ࠧࡸࡧࡥࡺ࡮࡫ࡷࡄࡱࡱࡲࡪࡩࡴࡓࡧࡷࡶ࡮࡫ࡳࠨᙂ"),
  bstack11l1l1l_opy_ (u"ࠨࡣࡳࡴࡓࡧ࡭ࡦࠩᙃ"),
  bstack11l1l1l_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡕࡖࡐࡈ࡫ࡲࡵࠩᙄ"),
  bstack11l1l1l_opy_ (u"ࠪࡸࡦࡶࡗࡪࡶ࡫ࡗ࡭ࡵࡲࡵࡒࡵࡩࡸࡹࡄࡶࡴࡤࡸ࡮ࡵ࡮ࠨᙅ"),
  bstack11l1l1l_opy_ (u"ࠫࡸࡩࡡ࡭ࡧࡉࡥࡨࡺ࡯ࡳࠩᙆ"),
  bstack11l1l1l_opy_ (u"ࠬࡽࡤࡢࡎࡲࡧࡦࡲࡐࡰࡴࡷࠫᙇ"),
  bstack11l1l1l_opy_ (u"࠭ࡳࡩࡱࡺ࡜ࡨࡵࡤࡦࡎࡲ࡫ࠬᙈ"),
  bstack11l1l1l_opy_ (u"ࠧࡪࡱࡶࡍࡳࡹࡴࡢ࡮࡯ࡔࡦࡻࡳࡦࠩᙉ"),
  bstack11l1l1l_opy_ (u"ࠨࡺࡦࡳࡩ࡫ࡃࡰࡰࡩ࡭࡬ࡌࡩ࡭ࡧࠪᙊ"),
  bstack11l1l1l_opy_ (u"ࠩ࡮ࡩࡾࡩࡨࡢ࡫ࡱࡔࡦࡹࡳࡸࡱࡵࡨࠬᙋ"),
  bstack11l1l1l_opy_ (u"ࠪࡹࡸ࡫ࡐࡳࡧࡥࡹ࡮ࡲࡴࡘࡆࡄࠫᙌ"),
  bstack11l1l1l_opy_ (u"ࠫࡵࡸࡥࡷࡧࡱࡸ࡜ࡊࡁࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠬᙍ"),
  bstack11l1l1l_opy_ (u"ࠬࡽࡥࡣࡆࡵ࡭ࡻ࡫ࡲࡂࡩࡨࡲࡹ࡛ࡲ࡭ࠩᙎ"),
  bstack11l1l1l_opy_ (u"࠭࡫ࡦࡻࡦ࡬ࡦ࡯࡮ࡑࡣࡷ࡬ࠬᙏ"),
  bstack11l1l1l_opy_ (u"ࠧࡶࡵࡨࡒࡪࡽࡗࡅࡃࠪᙐ"),
  bstack11l1l1l_opy_ (u"ࠨࡹࡧࡥࡑࡧࡵ࡯ࡥ࡫ࡘ࡮ࡳࡥࡰࡷࡷࠫᙑ"), bstack11l1l1l_opy_ (u"ࠩࡺࡨࡦࡉ࡯࡯ࡰࡨࡧࡹ࡯࡯࡯ࡖ࡬ࡱࡪࡵࡵࡵࠩᙒ"),
  bstack11l1l1l_opy_ (u"ࠪࡼࡨࡵࡤࡦࡑࡵ࡫ࡎࡪࠧᙓ"), bstack11l1l1l_opy_ (u"ࠫࡽࡩ࡯ࡥࡧࡖ࡭࡬ࡴࡩ࡯ࡩࡌࡨࠬᙔ"),
  bstack11l1l1l_opy_ (u"ࠬࡻࡰࡥࡣࡷࡩࡩ࡝ࡄࡂࡄࡸࡲࡩࡲࡥࡊࡦࠪᙕ"),
  bstack11l1l1l_opy_ (u"࠭ࡲࡦࡵࡨࡸࡔࡴࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡵࡸࡔࡴ࡬ࡺࠩᙖ"),
  bstack11l1l1l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡕ࡫ࡰࡩࡴࡻࡴࡴࠩᙗ"),
  bstack11l1l1l_opy_ (u"ࠨࡹࡧࡥࡘࡺࡡࡳࡶࡸࡴࡗ࡫ࡴࡳ࡫ࡨࡷࠬᙘ"), bstack11l1l1l_opy_ (u"ࠩࡺࡨࡦ࡙ࡴࡢࡴࡷࡹࡵࡘࡥࡵࡴࡼࡍࡳࡺࡥࡳࡸࡤࡰࠬᙙ"),
  bstack11l1l1l_opy_ (u"ࠪࡧࡴࡴ࡮ࡦࡥࡷࡌࡦࡸࡤࡸࡣࡵࡩࡐ࡫ࡹࡣࡱࡤࡶࡩ࠭ᙚ"),
  bstack11l1l1l_opy_ (u"ࠫࡲࡧࡸࡕࡻࡳ࡭ࡳ࡭ࡆࡳࡧࡴࡹࡪࡴࡣࡺࠩᙛ"),
  bstack11l1l1l_opy_ (u"ࠬࡹࡩ࡮ࡲ࡯ࡩࡎࡹࡖࡪࡵ࡬ࡦࡱ࡫ࡃࡩࡧࡦ࡯ࠬᙜ"),
  bstack11l1l1l_opy_ (u"࠭ࡵࡴࡧࡆࡥࡷࡺࡨࡢࡩࡨࡗࡸࡲࠧᙝ"),
  bstack11l1l1l_opy_ (u"ࠧࡴࡪࡲࡹࡱࡪࡕࡴࡧࡖ࡭ࡳ࡭࡬ࡦࡶࡲࡲ࡙࡫ࡳࡵࡏࡤࡲࡦ࡭ࡥࡳࠩᙞ"),
  bstack11l1l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡉࡘࡆࡓࠫᙟ"),
  bstack11l1l1l_opy_ (u"ࠩࡤࡰࡱࡵࡷࡕࡱࡸࡧ࡭ࡏࡤࡆࡰࡵࡳࡱࡲࠧᙠ"),
  bstack11l1l1l_opy_ (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࡋ࡭ࡩࡪࡥ࡯ࡃࡳ࡭ࡕࡵ࡬ࡪࡥࡼࡉࡷࡸ࡯ࡳࠩᙡ"),
  bstack11l1l1l_opy_ (u"ࠫࡲࡵࡣ࡬ࡎࡲࡧࡦࡺࡩࡰࡰࡄࡴࡵ࠭ᙢ"),
  bstack11l1l1l_opy_ (u"ࠬࡲ࡯ࡨࡥࡤࡸࡋࡵࡲ࡮ࡣࡷࠫᙣ"), bstack11l1l1l_opy_ (u"࠭࡬ࡰࡩࡦࡥࡹࡌࡩ࡭ࡶࡨࡶࡘࡶࡥࡤࡵࠪᙤ"),
  bstack11l1l1l_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡊࡥ࡭ࡣࡼࡅࡩࡨࠧᙥ"),
  bstack11l1l1l_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡋࡧࡐࡴࡩࡡࡵࡱࡵࡅࡺࡺ࡯ࡤࡱࡰࡴࡱ࡫ࡴࡪࡱࡱࠫᙦ")
]
bstack11l1ll11l_opy_ = bstack11l1l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠭ࡤ࡮ࡲࡹࡩ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥ࠰ࡷࡳࡰࡴࡧࡤࠨᙧ")
bstack11l1ll1111_opy_ = [bstack11l1l1l_opy_ (u"ࠪ࠲ࡦࡶ࡫ࠨᙨ"), bstack11l1l1l_opy_ (u"ࠫ࠳ࡧࡡࡣࠩᙩ"), bstack11l1l1l_opy_ (u"ࠬ࠴ࡩࡱࡣࠪᙪ")]
bstack1l111l1l1_opy_ = [bstack11l1l1l_opy_ (u"࠭ࡩࡥࠩᙫ"), bstack11l1l1l_opy_ (u"ࠧࡱࡣࡷ࡬ࠬᙬ"), bstack11l1l1l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫ᙭"), bstack11l1l1l_opy_ (u"ࠩࡶ࡬ࡦࡸࡥࡢࡤ࡯ࡩࡤ࡯ࡤࠨ᙮")]
bstack111ll1ll11_opy_ = {
  bstack11l1l1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᙯ"): bstack11l1l1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᙰ"),
  bstack11l1l1l_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ᙱ"): bstack11l1l1l_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫᙲ"),
  bstack11l1l1l_opy_ (u"ࠧࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬᙳ"): bstack11l1l1l_opy_ (u"ࠨ࡯ࡶ࠾ࡪࡪࡧࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᙴ"),
  bstack11l1l1l_opy_ (u"ࠩ࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬᙵ"): bstack11l1l1l_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᙶ"),
  bstack11l1l1l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࡓࡵࡺࡩࡰࡰࡶࠫᙷ"): bstack11l1l1l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᙸ")
}
bstack11ll11111_opy_ = [
  bstack11l1l1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᙹ"),
  bstack11l1l1l_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬᙺ"),
  bstack11l1l1l_opy_ (u"ࠨ࡯ࡶ࠾ࡪࡪࡧࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᙻ"),
  bstack11l1l1l_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᙼ"),
  bstack11l1l1l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫᙽ"),
]
bstack11lll11ll_opy_ = bstack11l1l1l1ll_opy_ + bstack1l11ll111l1_opy_ + bstack111l1ll1l_opy_
bstack1lll11llll_opy_ = [
  bstack11l1l1l_opy_ (u"ࠫࡣࡲ࡯ࡤࡣ࡯࡬ࡴࡹࡴࠥࠩᙾ"),
  bstack11l1l1l_opy_ (u"ࠬࡤࡢࡴ࠯࡯ࡳࡨࡧ࡬࠯ࡥࡲࡱࠩ࠭ᙿ"),
  bstack11l1l1l_opy_ (u"࠭࡞࠲࠴࠺࠲ࠬ "),
  bstack11l1l1l_opy_ (u"ࠧ࡟࠳࠳࠲ࠬᚁ"),
  bstack11l1l1l_opy_ (u"ࠨࡠ࠴࠻࠷࠴࠱࡜࠸࠰࠽ࡢ࠴ࠧᚂ"),
  bstack11l1l1l_opy_ (u"ࠩࡡ࠵࠼࠸࠮࠳࡝࠳࠱࠾ࡣ࠮ࠨᚃ"),
  bstack11l1l1l_opy_ (u"ࠪࡢ࠶࠽࠲࠯࠵࡞࠴࠲࠷࡝࠯ࠩᚄ"),
  bstack11l1l1l_opy_ (u"ࠫࡣ࠷࠹࠳࠰࠴࠺࠽࠴ࠧᚅ")
]
bstack1l11l1llll1_opy_ = bstack11l1l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ᚆ")
bstack11l1111l1l_opy_ = bstack11l1l1l_opy_ (u"࠭ࡳࡥ࡭࠲ࡺ࠶࠵ࡥࡷࡧࡱࡸࠬᚇ")
bstack1l1l1lll1_opy_ = [ bstack11l1l1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩᚈ") ]
bstack111ll1lll_opy_ = [ bstack11l1l1l_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᚉ") ]
bstack1l1l1111ll_opy_ = [bstack11l1l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ᚊ")]
bstack11ll111l1_opy_ = [ bstack11l1l1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪᚋ") ]
bstack11l111ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠫࡘࡊࡋࡔࡧࡷࡹࡵ࠭ᚌ")
bstack1lll1lll1_opy_ = bstack11l1l1l_opy_ (u"࡙ࠬࡄࡌࡖࡨࡷࡹࡇࡴࡵࡧࡰࡴࡹ࡫ࡤࠨᚍ")
bstack11lll1ll11_opy_ = bstack11l1l1l_opy_ (u"࠭ࡓࡅࡍࡗࡩࡸࡺࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠪᚎ")
bstack1111111ll_opy_ = bstack11l1l1l_opy_ (u"ࠧ࠵࠰࠳࠲࠵࠭ᚏ")
bstack1llll11l11_opy_ = [
  bstack11l1l1l_opy_ (u"ࠨࡇࡕࡖࡤࡌࡁࡊࡎࡈࡈࠬᚐ"),
  bstack11l1l1l_opy_ (u"ࠩࡈࡖࡗࡥࡔࡊࡏࡈࡈࡤࡕࡕࡕࠩᚑ"),
  bstack11l1l1l_opy_ (u"ࠪࡉࡗࡘ࡟ࡃࡎࡒࡇࡐࡋࡄࡠࡄ࡜ࡣࡈࡒࡉࡆࡐࡗࠫᚒ"),
  bstack11l1l1l_opy_ (u"ࠫࡊࡘࡒࡠࡐࡈࡘ࡜ࡕࡒࡌࡡࡆࡌࡆࡔࡇࡆࡆࠪᚓ"),
  bstack11l1l1l_opy_ (u"ࠬࡋࡒࡓࡡࡖࡓࡈࡑࡅࡕࡡࡑࡓ࡙ࡥࡃࡐࡐࡑࡉࡈ࡚ࡅࡅࠩᚔ"),
  bstack11l1l1l_opy_ (u"࠭ࡅࡓࡔࡢࡇࡔࡔࡎࡆࡅࡗࡍࡔࡔ࡟ࡄࡎࡒࡗࡊࡊࠧᚕ"),
  bstack11l1l1l_opy_ (u"ࠧࡆࡔࡕࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡔࡈࡗࡊ࡚ࠧᚖ"),
  bstack11l1l1l_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡕࡉࡋ࡛ࡓࡆࡆࠪᚗ"),
  bstack11l1l1l_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡅࡇࡕࡒࡕࡇࡇࠫᚘ"),
  bstack11l1l1l_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡋࡇࡉࡍࡇࡇࠫᚙ"),
  bstack11l1l1l_opy_ (u"ࠫࡊࡘࡒࡠࡐࡄࡑࡊࡥࡎࡐࡖࡢࡖࡊ࡙ࡏࡍࡘࡈࡈࠬᚚ"),
  bstack11l1l1l_opy_ (u"ࠬࡋࡒࡓࡡࡄࡈࡉࡘࡅࡔࡕࡢࡍࡓ࡜ࡁࡍࡋࡇࠫ᚛"),
  bstack11l1l1l_opy_ (u"࠭ࡅࡓࡔࡢࡅࡉࡊࡒࡆࡕࡖࡣ࡚ࡔࡒࡆࡃࡆࡌࡆࡈࡌࡆࠩ᚜"),
  bstack11l1l1l_opy_ (u"ࠧࡆࡔࡕࡣ࡙࡛ࡎࡏࡇࡏࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡈࡄࡍࡑࡋࡄࠨ᚝"),
  bstack11l1l1l_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡗࡍࡒࡋࡄࡠࡑࡘࡘࠬ᚞"),
  bstack11l1l1l_opy_ (u"ࠩࡈࡖࡗࡥࡓࡐࡅࡎࡗࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡉࡅࡎࡒࡅࡅࠩ᚟"),
  bstack11l1l1l_opy_ (u"ࠪࡉࡗࡘ࡟ࡔࡑࡆࡏࡘࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡌࡔ࡙ࡔࡠࡗࡑࡖࡊࡇࡃࡉࡃࡅࡐࡊ࠭ᚠ"),
  bstack11l1l1l_opy_ (u"ࠫࡊࡘࡒࡠࡒࡕࡓ࡝࡟࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡋࡇࡉࡍࡇࡇࠫᚡ"),
  bstack11l1l1l_opy_ (u"ࠬࡋࡒࡓࡡࡑࡅࡒࡋ࡟ࡏࡑࡗࡣࡗࡋࡓࡐࡎ࡙ࡉࡉ࠭ᚢ"),
  bstack11l1l1l_opy_ (u"࠭ࡅࡓࡔࡢࡒࡆࡓࡅࡠࡔࡈࡗࡔࡒࡕࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬᚣ"),
  bstack11l1l1l_opy_ (u"ࠧࡆࡔࡕࡣࡒࡇࡎࡅࡃࡗࡓࡗ࡟࡟ࡑࡔࡒ࡜࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭ᚤ"),
]
bstack111l1ll1ll_opy_ = bstack11l1l1l_opy_ (u"ࠨ࠰࠲ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡤࡶࡹ࡯ࡦࡢࡥࡷࡷ࠴࠭ᚥ")
bstack11l1111ll_opy_ = os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠩࢁࠫᚦ")), bstack11l1l1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᚧ"), bstack11l1l1l_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪᚨ"))
bstack1l11l1lll11_opy_ = bstack11l1l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡤࡴ࡮࠭ᚩ")
bstack1l11ll11l11_opy_ = [ bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᚪ"), bstack11l1l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ᚫ"), bstack11l1l1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧᚬ"), bstack11l1l1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩᚭ")]
bstack11l1l11lll_opy_ = [ bstack11l1l1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᚮ"), bstack11l1l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪᚯ"), bstack11l1l1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫᚰ"), bstack11l1l1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ᚱ") ]
bstack1lll111l_opy_ = {
  bstack11l1l1l_opy_ (u"ࠧࡑࡃࡖࡗࠬᚲ"): bstack11l1l1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᚳ"),
  bstack11l1l1l_opy_ (u"ࠩࡉࡅࡎࡒࠧᚴ"): bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᚵ"),
  bstack11l1l1l_opy_ (u"ࠫࡘࡑࡉࡑࠩᚶ"): bstack11l1l1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᚷ")
}
bstack1l11l1lll_opy_ = [
  bstack11l1l1l_opy_ (u"ࠨࡧࡦࡶࠥᚸ"),
  bstack11l1l1l_opy_ (u"ࠢࡨࡱࡅࡥࡨࡱࠢᚹ"),
  bstack11l1l1l_opy_ (u"ࠣࡩࡲࡊࡴࡸࡷࡢࡴࡧࠦᚺ"),
  bstack11l1l1l_opy_ (u"ࠤࡵࡩ࡫ࡸࡥࡴࡪࠥᚻ"),
  bstack11l1l1l_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࡇ࡯ࡩࡲ࡫࡮ࡵࠤᚼ"),
  bstack11l1l1l_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᚽ"),
  bstack11l1l1l_opy_ (u"ࠧࡹࡵࡣ࡯࡬ࡸࡊࡲࡥ࡮ࡧࡱࡸࠧᚾ"),
  bstack11l1l1l_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡈࡰࡪࡳࡥ࡯ࡶࠥᚿ"),
  bstack11l1l1l_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡅࡨࡺࡩࡷࡧࡈࡰࡪࡳࡥ࡯ࡶࠥᛀ"),
  bstack11l1l1l_opy_ (u"ࠣࡥ࡯ࡩࡦࡸࡅ࡭ࡧࡰࡩࡳࡺࠢᛁ"),
  bstack11l1l1l_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࡵࠥᛂ"),
  bstack11l1l1l_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࡗࡨࡸࡩࡱࡶࠥᛃ"),
  bstack11l1l1l_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࡆࡹࡹ࡯ࡥࡖࡧࡷ࡯ࡰࡵࠤᛄ"),
  bstack11l1l1l_opy_ (u"ࠧࡩ࡬ࡰࡵࡨࠦᛅ"),
  bstack11l1l1l_opy_ (u"ࠨࡱࡶ࡫ࡷࠦᛆ"),
  bstack11l1l1l_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡕࡱࡸࡧ࡭ࡇࡣࡵ࡫ࡲࡲࠧᛇ"),
  bstack11l1l1l_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡏࡸࡰࡹ࡯ࡔࡰࡷࡦ࡬ࠧᛈ"),
  bstack11l1l1l_opy_ (u"ࠤࡶ࡬ࡦࡱࡥࠣᛉ"),
  bstack11l1l1l_opy_ (u"ࠥࡧࡱࡵࡳࡦࡃࡳࡴࠧᛊ")
]
bstack1l11l1lll1l_opy_ = [
  bstack11l1l1l_opy_ (u"ࠦࡨࡲࡩࡤ࡭ࠥᛋ"),
  bstack11l1l1l_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᛌ"),
  bstack11l1l1l_opy_ (u"ࠨࡡࡶࡶࡲࠦᛍ"),
  bstack11l1l1l_opy_ (u"ࠢ࡮ࡣࡱࡹࡦࡲࠢᛎ"),
  bstack11l1l1l_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᛏ")
]
bstack1l1llllll_opy_ = {
  bstack11l1l1l_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࠣᛐ"): [bstack11l1l1l_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࡇ࡯ࡩࡲ࡫࡮ࡵࠤᛑ")],
  bstack11l1l1l_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᛒ"): [bstack11l1l1l_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᛓ")],
  bstack11l1l1l_opy_ (u"ࠨࡡࡶࡶࡲࠦᛔ"): [bstack11l1l1l_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡉࡱ࡫࡭ࡦࡰࡷࠦᛕ"), bstack11l1l1l_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࡗࡳࡆࡩࡴࡪࡸࡨࡉࡱ࡫࡭ࡦࡰࡷࠦᛖ"), bstack11l1l1l_opy_ (u"ࠤࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨᛗ"), bstack11l1l1l_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࡇ࡯ࡩࡲ࡫࡮ࡵࠤᛘ")],
  bstack11l1l1l_opy_ (u"ࠦࡲࡧ࡮ࡶࡣ࡯ࠦᛙ"): [bstack11l1l1l_opy_ (u"ࠧࡳࡡ࡯ࡷࡤࡰࠧᛚ")],
  bstack11l1l1l_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣᛛ"): [bstack11l1l1l_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤᛜ")],
}
bstack1l11l1l1l1l_opy_ = {
  bstack11l1l1l_opy_ (u"ࠣࡥ࡯࡭ࡨࡱࡅ࡭ࡧࡰࡩࡳࡺࠢᛝ"): bstack11l1l1l_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࠣᛞ"),
  bstack11l1l1l_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᛟ"): bstack11l1l1l_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᛠ"),
  bstack11l1l1l_opy_ (u"ࠧࡹࡥ࡯ࡦࡎࡩࡾࡹࡔࡰࡇ࡯ࡩࡲ࡫࡮ࡵࠤᛡ"): bstack11l1l1l_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࠣᛢ"),
  bstack11l1l1l_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡅࡨࡺࡩࡷࡧࡈࡰࡪࡳࡥ࡯ࡶࠥᛣ"): bstack11l1l1l_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࠥᛤ"),
  bstack11l1l1l_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦᛥ"): bstack11l1l1l_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧᛦ")
}
bstack1ll11l11_opy_ = {
  bstack11l1l1l_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᛧ"): bstack11l1l1l_opy_ (u"࡙ࠬࡵࡪࡶࡨࠤࡘ࡫ࡴࡶࡲࠪᛨ"),
  bstack11l1l1l_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩᛩ"): bstack11l1l1l_opy_ (u"ࠧࡔࡷ࡬ࡸࡪࠦࡔࡦࡣࡵࡨࡴࡽ࡮ࠨᛪ"),
  bstack11l1l1l_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭᛫"): bstack11l1l1l_opy_ (u"ࠩࡗࡩࡸࡺࠠࡔࡧࡷࡹࡵ࠭᛬"),
  bstack11l1l1l_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧ᛭"): bstack11l1l1l_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡗࡩࡦࡸࡤࡰࡹࡱࠫᛮ")
}
bstack1l11l1ll11l_opy_ = 65536
bstack1l11ll1l11l_opy_ = bstack11l1l1l_opy_ (u"ࠬ࠴࠮࠯࡝ࡗࡖ࡚ࡔࡃࡂࡖࡈࡈࡢ࠭ᛯ")
bstack1l11l1l11l1_opy_ = [
      bstack11l1l1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᛰ"), bstack11l1l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᛱ"), bstack11l1l1l_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᛲ"), bstack11l1l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᛳ"), bstack11l1l1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠬᛴ"),
      bstack11l1l1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧᛵ"), bstack11l1l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨᛶ"), bstack11l1l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡘࡷࡪࡸࠧᛷ"), bstack11l1l1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼࡔࡦࡹࡳࠨᛸ"),
      bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ᛹"), bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ᛺"), bstack11l1l1l_opy_ (u"ࠪࡥࡺࡺࡨࡕࡱ࡮ࡩࡳ࠭᛻")
    ]
bstack1l11ll1l111_opy_= {
  bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ᛼"): bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ᛽"),
  bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ᛾"): bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ᛿"),
  bstack11l1l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧᜀ"): bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ᜁ"),
  bstack11l1l1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᜂ"): bstack11l1l1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫᜃ"),
  bstack11l1l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᜄ"): bstack11l1l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᜅ"),
  bstack11l1l1l_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᜆ"): bstack11l1l1l_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪᜇ"),
  bstack11l1l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᜈ"): bstack11l1l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᜉ"),
  bstack11l1l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᜊ"): bstack11l1l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᜋ"),
  bstack11l1l1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᜌ"): bstack11l1l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪᜍ"),
  bstack11l1l1l_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭ᜎ"): bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠧᜏ"),
  bstack11l1l1l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᜐ"): bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᜑ"),
  bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᜒ"): bstack11l1l1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᜓ"),
  bstack11l1l1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴ᜔ࠩ"): bstack11l1l1l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵ᜕ࠪ"),
  bstack11l1l1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭᜖"): bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ᜗"),
  bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭᜘"): bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧ᜙"),
  bstack11l1l1l_opy_ (u"࠭ࡲࡦࡴࡸࡲ࡙࡫ࡳࡵࡵࠪ᜚"): bstack11l1l1l_opy_ (u"ࠧࡳࡧࡵࡹࡳ࡚ࡥࡴࡶࡶࠫ᜛"),
  bstack11l1l1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ᜜"): bstack11l1l1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ᜝"),
  bstack11l1l1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᜞"): bstack11l1l1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᜟ"),
  bstack11l1l1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨᜠ"): bstack11l1l1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩᜡ"),
  bstack11l1l1l_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩᜢ"): bstack11l1l1l_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪᜣ"),
  bstack11l1l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᜤ"): bstack11l1l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᜥ"),
  bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᜦ"): bstack11l1l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᜧ"),
  bstack11l1l1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪᜨ"): bstack11l1l1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫᜩ"),
  bstack11l1l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷࠬᜪ"): bstack11l1l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᜫ"),
  bstack11l1l1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠪᜬ"): bstack11l1l1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠫᜭ")
}
bstack1l11l1l1111_opy_ = [bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᜮ"), bstack11l1l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬᜯ")]
bstack1ll1ll1ll_opy_ = (bstack11l1l1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢᜰ"),)
bstack1l11ll11111_opy_ = bstack11l1l1l_opy_ (u"ࠨࡵࡧ࡯࠴ࡼ࠱࠰ࡷࡳࡨࡦࡺࡥࡠࡥ࡯࡭ࠬᜱ")
bstack1l1l111l1l_opy_ = bstack11l1l1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠲ࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦ࠱ࡹ࠵࠴࡭ࡲࡪࡦࡶ࠳ࠧᜲ")
bstack11l111llll_opy_ = bstack11l1l1l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳࡬ࡸࡩࡥ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡪࡡࡴࡪࡥࡳࡦࡸࡤ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࠤᜳ")
bstack111ll1l11l_opy_ = bstack11l1l1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡧࡵࡵࡱࡰࡥࡹ࡫࠭ࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨ࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠮࡫ࡵࡲࡲ᜴ࠧ")
class EVENTS(Enum):
  bstack1l11ll1l1l1_opy_ = bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡲ࠵࠶ࡿ࠺ࡱࡴ࡬ࡲࡹ࠳ࡢࡶ࡫࡯ࡨࡱ࡯࡮࡬ࠩ᜵")
  bstack1lll1l1ll1_opy_ = bstack11l1l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡧࡱ࡫ࡡ࡯ࡷࡳࠫ᜶") # final bstack1l11ll1111l_opy_
  bstack1l11ll11l1l_opy_ = bstack11l1l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡸ࡫࡮ࡥ࡮ࡲ࡫ࡸ࠭᜷")
  bstack111l1l11l_opy_ = bstack11l1l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦ࠼ࡳࡶ࡮ࡴࡴ࠮ࡤࡸ࡭ࡱࡪ࡬ࡪࡰ࡮ࠫ᜸") #shift post bstack1l11ll11lll_opy_
  bstack1l1l1llll_opy_ = bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻ࡲࡵ࡭ࡳࡺ࠭ࡣࡷ࡬ࡰࡩࡲࡩ࡯࡭ࠪ᜹") #shift post bstack1l11ll11lll_opy_
  bstack1l11ll1ll11_opy_ = bstack11l1l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡵࡧࡶࡸ࡭ࡻࡢࠨ᜺") #shift
  bstack1l11ll1ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡲࡨࡶࡨࡿ࠺ࡥࡱࡺࡲࡱࡵࡡࡥࠩ᜻") #shift
  bstack11llll1ll1_opy_ = bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪࡀࡨࡶࡤ࠰ࡱࡦࡴࡡࡨࡧࡰࡩࡳࡺࠧ᜼")
  bstack1l11ll111ll_opy_ = bstack11l1l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡥ࠶࠷ࡹ࠻ࡵࡤࡺࡪ࠳ࡲࡦࡵࡸࡰࡹࡹࠧ᜽")
  bstack11lllll1l_opy_ = bstack11l1l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡦ࠷࠱ࡺ࠼ࡧࡶ࡮ࡼࡥࡳ࠯ࡳࡩࡷ࡬࡯ࡳ࡯ࡶࡧࡦࡴࠧ᜾")
  bstack1lllll1ll1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡫࠺࡭ࡱࡦࡥࡱ࠭᜿") #shift
  bstack111llll1l1_opy_ = bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰࡀࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠿ࡧࡰࡱ࠯ࡸࡴࡱࡵࡡࡥࠩᝀ") #shift
  bstack1lllll1l11_opy_ = bstack11l1l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡦ࠼ࡦ࡭࠲ࡧࡲࡵ࡫ࡩࡥࡨࡺࡳࠨᝁ")
  bstack1l111111ll_opy_ = bstack11l1l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡣ࠴࠵ࡾࡀࡧࡦࡶ࠰ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻ࠰ࡶࡪࡹࡵ࡭ࡶࡶ࠱ࡸࡻ࡭࡮ࡣࡵࡽࠬᝂ") #shift
  bstack1111l1111_opy_ = bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡤ࠵࠶ࡿ࠺ࡨࡧࡷ࠱ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼ࠱ࡷ࡫ࡳࡶ࡮ࡷࡷࠬᝃ") #shift
  bstack1l11l11llll_opy_ = bstack11l1l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡴࡪࡸࡣࡺࠩᝄ") #shift
  SDK_PERCY_SCREENSHOT = bstack11l1l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡵ࡫ࡲࡤࡻ࠽ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧᝅ")
  bstack1ll11lllll_opy_ = bstack11l1l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡫࠺ࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡵࡷࡥࡹࡻࡳࠨᝆ") #shift
  bstack11lll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻ࡪࡸࡦ࠲ࡳࡡ࡯ࡣࡪࡩࡲ࡫࡮ࡵࠩᝇ")
  bstack1l11l1l11ll_opy_ = bstack11l1l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡱࡴࡲࡼࡾ࠳ࡳࡦࡶࡸࡴࠬᝈ") #shift
  bstack1lll11l111_opy_ = bstack11l1l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡵࡨࡸࡺࡶࠧᝉ")
  bstack1l11ll1l1ll_opy_ = bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡩࡷࡩࡹ࠻ࡵࡱࡥࡵࡹࡨࡰࡶࠪᝊ") # not bstack1l11l1ll111_opy_ in python
  bstack11lll1lll_opy_ = bstack11l1l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡨࡷ࡯ࡶࡦࡴ࠽ࡵࡺ࡯ࡴࠨᝋ") # used in bstack1l11l1ll1l1_opy_
  bstack1l1ll1l1ll_opy_ = bstack11l1l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡩࡸࡩࡷࡧࡵ࠾࡬࡫ࡴࠨᝌ") # used in bstack1l11l1ll1l1_opy_
  bstack1ll1lll1ll_opy_ = bstack11l1l1l_opy_ (u"ࠨࡵࡧ࡯࠿࡮࡯ࡰ࡭ࠪᝍ")
  bstack111l1ll1l1_opy_ = bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻ࡵࡨࡷࡸ࡯࡯࡯࠯ࡱࡥࡲ࡫ࠧᝎ")
  bstack1llll1ll11_opy_ = bstack11l1l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡦ࠼ࡶࡩࡸࡹࡩࡰࡰ࠰ࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠧᝏ") #
  bstack111ll1llll_opy_ = bstack11l1l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡱ࠴࠵ࡾࡀࡤࡳ࡫ࡹࡩࡷ࠳ࡴࡢ࡭ࡨࡗࡨࡸࡥࡦࡰࡖ࡬ࡴࡺࠧᝐ")
  bstack1l1lllll1_opy_ = bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡩࡷࡩࡹ࠻ࡣࡸࡸࡴ࠳ࡣࡢࡲࡷࡹࡷ࡫ࠧᝑ")
  bstack1l11111l11_opy_ = bstack11l1l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡴࡷ࡫࠭ࡵࡧࡶࡸࠬᝒ")
  bstack11ll111111_opy_ = bstack11l1l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡵࡵࡳࡵ࠯ࡷࡩࡸࡺࠧᝓ")
  bstack11l1ll1lll_opy_ = bstack11l1l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡪࡲࡪࡸࡨࡶ࠿ࡶࡲࡦ࠯࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡦࡺࡩࡰࡰࠪ᝔") #shift
  bstack1lll1ll1ll_opy_ = bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰࡀࡤࡳ࡫ࡹࡩࡷࡀࡰࡰࡵࡷ࠱࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡡࡵ࡫ࡲࡲࠬ᝕") #shift
  bstack1l11l1l1ll1_opy_ = bstack11l1l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳ࠲ࡩࡡࡱࡶࡸࡶࡪ࠭᝖")
  bstack1l11ll11ll1_opy_ = bstack11l1l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴࡳࡡࡵࡧ࠽࡭ࡩࡲࡥ࠮ࡶ࡬ࡱࡪࡵࡵࡵࠩ᝗")
  bstack1ll1l1l1l11_opy_ = bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡦࡰ࡮ࡀࡳࡵࡣࡵࡸࠬ᝘")
  bstack1l11l1l1lll_opy_ = bstack11l1l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡧࡱ࡯࠺ࡥࡱࡺࡲࡱࡵࡡࡥࠩ᝙")
  bstack1l11l11ll11_opy_ = bstack11l1l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡲࡩ࠻ࡥ࡫ࡩࡨࡱ࠭ࡶࡲࡧࡥࡹ࡫ࠧ᝚")
  bstack1ll111l1ll1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡩ࡬ࡪ࠼ࡲࡲ࠲ࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠨ᝛")
  bstack1ll11l1lll1_opy_ = bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰࡀࡣ࡭࡫࠽ࡳࡳ࠳ࡣࡰࡰࡱࡩࡨࡺࠧ᝜")
  bstack1ll11l111l1_opy_ = bstack11l1l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡤ࡮࡬࠾ࡴࡴ࠭ࡴࡶࡲࡴࠬ᝝")
  bstack1ll11lll1l1_opy_ = bstack11l1l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡵࡷࡥࡷࡺࡂࡪࡰࡖࡩࡸࡹࡩࡰࡰࠪ᝞")
  bstack1ll11ll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡦࡳࡳࡴࡥࡤࡶࡅ࡭ࡳ࡙ࡥࡴࡵ࡬ࡳࡳ࠭᝟")
  bstack111l11l11l_opy_ = bstack11l1l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡨࡷ࡯ࡶࡦࡴࡌࡲ࡮ࡺࠧᝠ")
  bstack1l11l11l1l1_opy_ = bstack11l1l1l_opy_ (u"ࠧࡴࡦ࡮࠾࡫࡯࡮ࡥࡐࡨࡥࡷ࡫ࡳࡵࡊࡸࡦࠬᝡ")
  bstack1111l11l11_opy_ = bstack11l1l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡍࡳ࡯ࡴࠨᝢ")
  bstack1111ll1l11_opy_ = bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺࡡࡳࡶࠪᝣ")
  bstack1l1ll1ll11l_opy_ = bstack11l1l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡃࡰࡰࡩ࡭࡬࠭ᝤ")
  bstack1l11l1ll1ll_opy_ = bstack11l1l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡄࡱࡱࡪ࡮࡭ࠧᝥ")
  bstack1ll1lll1lll_opy_ = bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡤ࡭ࡘ࡫࡬ࡧࡊࡨࡥࡱ࡙ࡴࡦࡲࠪᝦ")
  bstack1ll1lll11l1_opy_ = bstack11l1l1l_opy_ (u"࠭ࡳࡥ࡭࠽ࡥ࡮࡙ࡥ࡭ࡨࡋࡩࡦࡲࡇࡦࡶࡕࡩࡸࡻ࡬ࡵࠩᝧ")
  bstack1ll1111lll1_opy_ = bstack11l1l1l_opy_ (u"ࠧࡴࡦ࡮࠾ࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡉࡻ࡫࡮ࡵࠩᝨ")
  bstack1l1llllll1l_opy_ = bstack11l1l1l_opy_ (u"ࠨࡵࡧ࡯࠿ࡺࡥࡴࡶࡖࡩࡸࡹࡩࡰࡰࡈࡺࡪࡴࡴࠨᝩ")
  bstack1ll111l111l_opy_ = bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰࡀࡣ࡭࡫࠽ࡰࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࡅࡷࡧࡱࡸࠬᝪ")
  bstack1l11l11lll1_opy_ = bstack11l1l1l_opy_ (u"ࠪࡷࡩࡱ࠺ࡤ࡮࡬࠾ࡪࡴࡱࡶࡧࡸࡩ࡙࡫ࡳࡵࡇࡹࡩࡳࡺࠧᝫ")
  bstack111l1111ll_opy_ = bstack11l1l1l_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡓࡵࡱࡳࠫᝬ")
  bstack1ll11l1l11l_opy_ = bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬࠼ࡲࡲࡘࡺ࡯ࡱࠩ᝭")
class STAGE(Enum):
  bstack1l1llll111_opy_ = bstack11l1l1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࠬᝮ")
  END = bstack11l1l1l_opy_ (u"ࠧࡦࡰࡧࠫᝯ")
  SINGLE = bstack11l1l1l_opy_ (u"ࠨࡵ࡬ࡲ࡬ࡲࡥࠨᝰ")
bstack1lll11111l_opy_ = {
  bstack11l1l1l_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࠩ᝱"): bstack11l1l1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᝲ"),
  bstack11l1l1l_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗ࠱ࡇࡊࡄࠨᝳ"): bstack11l1l1l_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧ᝴")
}