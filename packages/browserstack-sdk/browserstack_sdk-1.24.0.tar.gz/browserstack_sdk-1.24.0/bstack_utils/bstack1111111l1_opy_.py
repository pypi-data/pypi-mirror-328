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
import json
class bstack11l1l111lll_opy_(object):
  bstack1lll1l1111_opy_ = os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"࠭ࡾࠨᬭ")), bstack11l1l1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᬮ"))
  bstack11l1l11ll11_opy_ = os.path.join(bstack1lll1l1111_opy_, bstack11l1l1l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵ࠱࡮ࡸࡵ࡮ࠨᬯ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1ll111lll1_opy_ = None
  bstack11111l1l1_opy_ = None
  bstack11l1l11l11l_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11l1l1l_opy_ (u"ࠩ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠫᬰ")):
      cls.instance = super(bstack11l1l111lll_opy_, cls).__new__(cls)
      cls.instance.bstack11l1l11l1l1_opy_()
    return cls.instance
  def bstack11l1l11l1l1_opy_(self):
    try:
      with open(self.bstack11l1l11ll11_opy_, bstack11l1l1l_opy_ (u"ࠪࡶࠬᬱ")) as bstack11l1lll1l_opy_:
        bstack11l1l11l1ll_opy_ = bstack11l1lll1l_opy_.read()
        data = json.loads(bstack11l1l11l1ll_opy_)
        if bstack11l1l1l_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ᬲ") in data:
          self.bstack11l1l11ll1l_opy_(data[bstack11l1l1l_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧᬳ")])
        if bstack11l1l1l_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹ᬴ࠧ") in data:
          self.bstack11l1l11l111_opy_(data[bstack11l1l1l_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨᬵ")])
    except:
      pass
  def bstack11l1l11l111_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack11l1l1l_opy_ (u"ࠨࡵࡦࡥࡳ࠭ᬶ")]
      self.bstack1ll111lll1_opy_ = scripts[bstack11l1l1l_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࠭ᬷ")]
      self.bstack11111l1l1_opy_ = scripts[bstack11l1l1l_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠧᬸ")]
      self.bstack11l1l11l11l_opy_ = scripts[bstack11l1l1l_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩᬹ")]
  def bstack11l1l11ll1l_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack11l1l11ll11_opy_, bstack11l1l1l_opy_ (u"ࠬࡽࠧᬺ")) as file:
        json.dump({
          bstack11l1l1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࠣᬻ"): self.commands_to_wrap,
          bstack11l1l1l_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࡳࠣᬼ"): {
            bstack11l1l1l_opy_ (u"ࠣࡵࡦࡥࡳࠨᬽ"): self.perform_scan,
            bstack11l1l1l_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨᬾ"): self.bstack1ll111lll1_opy_,
            bstack11l1l1l_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠢᬿ"): self.bstack11111l1l1_opy_,
            bstack11l1l1l_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤᭀ"): self.bstack11l1l11l11l_opy_
          }
        }, file)
    except:
      pass
  def bstack1llll1ll1_opy_(self, bstack1lll1111111_opy_):
    try:
      return any(command.get(bstack11l1l1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᭁ")) == bstack1lll1111111_opy_ for command in self.commands_to_wrap)
    except:
      return False
bstack1111111l1_opy_ = bstack11l1l111lll_opy_()