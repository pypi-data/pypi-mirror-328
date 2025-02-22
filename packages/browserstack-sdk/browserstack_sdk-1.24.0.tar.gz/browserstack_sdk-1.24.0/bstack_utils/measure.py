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
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack111111l1l_opy_ import get_logger
from bstack_utils.bstack11ll1111l1_opy_ import bstack1111lll111_opy_
bstack11ll1111l1_opy_ = bstack1111lll111_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack11ll11ll11_opy_: Optional[str] = None):
    bstack11l1l1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡅࡧࡦࡳࡷࡧࡴࡰࡴࠣࡸࡴࠦ࡬ࡰࡩࠣࡸ࡭࡫ࠠࡴࡶࡤࡶࡹࠦࡴࡪ࡯ࡨࠤࡴ࡬ࠠࡢࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࡦࡲ࡯࡯ࡩࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺࠠ࡯ࡣࡰࡩࠥࡧ࡮ࡥࠢࡶࡸࡦ࡭ࡥ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᎰ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1l1l11ll111_opy_: str = bstack11ll1111l1_opy_.bstack1l1l11ll11l_opy_(label)
            start_mark: str = label + bstack11l1l1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᎱ")
            end_mark: str = label + bstack11l1l1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᎲ")
            result = None
            try:
                if stage.value == STAGE.bstack1l1llll111_opy_.value:
                    bstack11ll1111l1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack11ll1111l1_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack11ll11ll11_opy_)
                elif stage.value == STAGE.SINGLE.value:
                    start_mark: str = bstack1l1l11ll111_opy_ + bstack11l1l1l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᎳ")
                    end_mark: str = bstack1l1l11ll111_opy_ + bstack11l1l1l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᎴ")
                    bstack11ll1111l1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack11ll1111l1_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack11ll11ll11_opy_)
            except Exception as e:
                bstack11ll1111l1_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack11ll11ll11_opy_)
            return result
        return wrapper
    return decorator