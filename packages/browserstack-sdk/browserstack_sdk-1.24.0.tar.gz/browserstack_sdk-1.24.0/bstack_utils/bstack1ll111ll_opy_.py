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
from uuid import uuid4
from bstack_utils.helper import bstack11llllll_opy_, bstack11lll11ll11_opy_
from bstack_utils.bstack11ll11l111_opy_ import bstack1l111ll1l1l_opy_
class bstack1ll1l1ll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack11ll111l111_opy_=None, bstack11ll111ll1l_opy_=True, bstack1lll1ll1l1l_opy_=None, bstack11111l11l_opy_=None, result=None, duration=None, bstack11lll1l1_opy_=None, meta={}):
        self.bstack11lll1l1_opy_ = bstack11lll1l1_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack11ll111ll1l_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack11ll111l111_opy_ = bstack11ll111l111_opy_
        self.bstack1lll1ll1l1l_opy_ = bstack1lll1ll1l1l_opy_
        self.bstack11111l11l_opy_ = bstack11111l11l_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1l111l1l_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1ll11_opy_(self, meta):
        self.meta = meta
    def bstack11l1ll1l_opy_(self, hooks):
        self.hooks = hooks
    def bstack11ll1111l11_opy_(self):
        bstack11ll111ll11_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11l1l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭᩻"): bstack11ll111ll11_opy_,
            bstack11l1l1l_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭᩼"): bstack11ll111ll11_opy_,
            bstack11l1l1l_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪ᩽"): bstack11ll111ll11_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11l1l1l_opy_ (u"ࠨࡕ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࠿ࠦࠢ᩾") + key)
            setattr(self, key, val)
    def bstack11ll11l111l_opy_(self):
        return {
            bstack11l1l1l_opy_ (u"ࠧ࡯ࡣࡰࡩ᩿ࠬ"): self.name,
            bstack11l1l1l_opy_ (u"ࠨࡤࡲࡨࡾ࠭᪀"): {
                bstack11l1l1l_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧ᪁"): bstack11l1l1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ᪂"),
                bstack11l1l1l_opy_ (u"ࠫࡨࡵࡤࡦࠩ᪃"): self.code
            },
            bstack11l1l1l_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬ᪄"): self.scope,
            bstack11l1l1l_opy_ (u"࠭ࡴࡢࡩࡶࠫ᪅"): self.tags,
            bstack11l1l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ᪆"): self.framework,
            bstack11l1l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ᪇"): self.started_at
        }
    def bstack11ll111lll1_opy_(self):
        return {
         bstack11l1l1l_opy_ (u"ࠩࡰࡩࡹࡧࠧ᪈"): self.meta
        }
    def bstack11ll11l1111_opy_(self):
        return {
            bstack11l1l1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡕࡩࡷࡻ࡮ࡑࡣࡵࡥࡲ࠭᪉"): {
                bstack11l1l1l_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠨ᪊"): self.bstack11ll111l111_opy_
            }
        }
    def bstack11ll111l11l_opy_(self, bstack11ll111l1l1_opy_, details):
        step = next(filter(lambda st: st[bstack11l1l1l_opy_ (u"ࠬ࡯ࡤࠨ᪋")] == bstack11ll111l1l1_opy_, self.meta[bstack11l1l1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ᪌")]), None)
        step.update(details)
    def bstack11ll11ll_opy_(self, bstack11ll111l1l1_opy_):
        step = next(filter(lambda st: st[bstack11l1l1l_opy_ (u"ࠧࡪࡦࠪ᪍")] == bstack11ll111l1l1_opy_, self.meta[bstack11l1l1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧ᪎")]), None)
        step.update({
            bstack11l1l1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭᪏"): bstack11llllll_opy_()
        })
    def bstack1l1ll111_opy_(self, bstack11ll111l1l1_opy_, result, duration=None):
        bstack1lll1ll1l1l_opy_ = bstack11llllll_opy_()
        if bstack11ll111l1l1_opy_ is not None and self.meta.get(bstack11l1l1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩ᪐")):
            step = next(filter(lambda st: st[bstack11l1l1l_opy_ (u"ࠫ࡮ࡪࠧ᪑")] == bstack11ll111l1l1_opy_, self.meta[bstack11l1l1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫ᪒")]), None)
            step.update({
                bstack11l1l1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ᪓"): bstack1lll1ll1l1l_opy_,
                bstack11l1l1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩ᪔"): duration if duration else bstack11lll11ll11_opy_(step[bstack11l1l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ᪕")], bstack1lll1ll1l1l_opy_),
                bstack11l1l1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ᪖"): result.result,
                bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ᪗"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack11ll11l11ll_opy_):
        if self.meta.get(bstack11l1l1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪ᪘")):
            self.meta[bstack11l1l1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫ᪙")].append(bstack11ll11l11ll_opy_)
        else:
            self.meta[bstack11l1l1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ᪚")] = [ bstack11ll11l11ll_opy_ ]
    def bstack11ll11l1l11_opy_(self):
        return {
            bstack11l1l1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ᪛"): self.bstack1l111l1l_opy_(),
            **self.bstack11ll11l111l_opy_(),
            **self.bstack11ll1111l11_opy_(),
            **self.bstack11ll111lll1_opy_()
        }
    def bstack11ll111l1ll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭᪜"): self.bstack1lll1ll1l1l_opy_,
            bstack11l1l1l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪ᪝"): self.duration,
            bstack11l1l1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ᪞"): self.result.result
        }
        if data[bstack11l1l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ᪟")] == bstack11l1l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ᪠"):
            data[bstack11l1l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬ᪡")] = self.result.bstack111l1ll111_opy_()
            data[bstack11l1l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ᪢")] = [{bstack11l1l1l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ᪣"): self.result.bstack11lll11ll1l_opy_()}]
        return data
    def bstack11ll1111lll_opy_(self):
        return {
            bstack11l1l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ᪤"): self.bstack1l111l1l_opy_(),
            **self.bstack11ll11l111l_opy_(),
            **self.bstack11ll1111l11_opy_(),
            **self.bstack11ll111l1ll_opy_(),
            **self.bstack11ll111lll1_opy_()
        }
    def bstack1l111lll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11l1l1l_opy_ (u"ࠪࡗࡹࡧࡲࡵࡧࡧࠫ᪥") in event:
            return self.bstack11ll11l1l11_opy_()
        elif bstack11l1l1l_opy_ (u"ࠫࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭᪦") in event:
            return self.bstack11ll1111lll_opy_()
    def bstack1l11111l_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1lll1ll1l1l_opy_ = time if time else bstack11llllll_opy_()
        self.duration = duration if duration else bstack11lll11ll11_opy_(self.started_at, self.bstack1lll1ll1l1l_opy_)
        if result:
            self.result = result
class bstack1ll11lll_opy_(bstack1ll1l1ll_opy_):
    def __init__(self, hooks=[], bstack1l11llll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l11llll_opy_ = bstack1l11llll_opy_
        super().__init__(*args, **kwargs, bstack11111l11l_opy_=bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࠪᪧ"))
    @classmethod
    def bstack11ll1111ll1_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11l1l1l_opy_ (u"࠭ࡩࡥࠩ᪨"): id(step),
                bstack11l1l1l_opy_ (u"ࠧࡵࡧࡻࡸࠬ᪩"): step.name,
                bstack11l1l1l_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩ᪪"): step.keyword,
            })
        return bstack1ll11lll_opy_(
            **kwargs,
            meta={
                bstack11l1l1l_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪ᪫"): {
                    bstack11l1l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ᪬"): feature.name,
                    bstack11l1l1l_opy_ (u"ࠫࡵࡧࡴࡩࠩ᪭"): feature.filename,
                    bstack11l1l1l_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ᪮"): feature.description
                },
                bstack11l1l1l_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ᪯"): {
                    bstack11l1l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ᪰"): scenario.name
                },
                bstack11l1l1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧ᪱"): steps,
                bstack11l1l1l_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫ᪲"): bstack1l111ll1l1l_opy_(test)
            }
        )
    def bstack11ll11111ll_opy_(self):
        return {
            bstack11l1l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ᪳"): self.hooks
        }
    def bstack11ll111llll_opy_(self):
        if self.bstack1l11llll_opy_:
            return {
                bstack11l1l1l_opy_ (u"ࠫ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠪ᪴"): self.bstack1l11llll_opy_
            }
        return {}
    def bstack11ll1111lll_opy_(self):
        return {
            **super().bstack11ll1111lll_opy_(),
            **self.bstack11ll11111ll_opy_()
        }
    def bstack11ll11l1l11_opy_(self):
        return {
            **super().bstack11ll11l1l11_opy_(),
            **self.bstack11ll111llll_opy_()
        }
    def bstack1l11111l_opy_(self):
        return bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ᪵ࠧ")
class bstack1ll11ll1_opy_(bstack1ll1l1ll_opy_):
    def __init__(self, hook_type, *args,bstack1l11llll_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack11ll11l11l1_opy_ = None
        self.bstack1l11llll_opy_ = bstack1l11llll_opy_
        super().__init__(*args, **kwargs, bstack11111l11l_opy_=bstack11l1l1l_opy_ (u"࠭ࡨࡰࡱ࡮᪶ࠫ"))
    def bstack1l1l11l1_opy_(self):
        return self.hook_type
    def bstack11ll1111l1l_opy_(self):
        return {
            bstack11l1l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧ᪷ࠪ"): self.hook_type
        }
    def bstack11ll1111lll_opy_(self):
        return {
            **super().bstack11ll1111lll_opy_(),
            **self.bstack11ll1111l1l_opy_()
        }
    def bstack11ll11l1l11_opy_(self):
        return {
            **super().bstack11ll11l1l11_opy_(),
            bstack11l1l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢ࡭ࡩ᪸࠭"): self.bstack11ll11l11l1_opy_,
            **self.bstack11ll1111l1l_opy_()
        }
    def bstack1l11111l_opy_(self):
        return bstack11l1l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱ᪹ࠫ")
    def bstack11l1l1l1_opy_(self, bstack11ll11l11l1_opy_):
        self.bstack11ll11l11l1_opy_ = bstack11ll11l11l1_opy_