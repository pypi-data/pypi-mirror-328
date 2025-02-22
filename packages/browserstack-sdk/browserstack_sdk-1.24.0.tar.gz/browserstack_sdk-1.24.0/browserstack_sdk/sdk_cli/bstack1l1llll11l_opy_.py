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
from collections import defaultdict
from threading import Lock
from dataclasses import dataclass
import logging
import traceback
from typing import List, Dict, Any
import os
@dataclass
class bstack11ll1l1lll_opy_:
    sdk_version: str
    path_config: str
    path_project: str
    test_framework: str
    frameworks: List[str]
    framework_versions: Dict[str, str]
    bs_config: Dict[str, Any]
@dataclass
class bstack11l11lll1_opy_:
    pass
class Events:
    bstack1lll1l11l_opy_ = bstack11l1l1l_opy_ (u"ࠦࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠢ၉")
    CONNECT = bstack11l1l1l_opy_ (u"ࠧࡩ࡯࡯ࡰࡨࡧࡹࠨ၊")
    bstack11l1ll1ll1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡳࡩࡷࡷࡨࡴࡽ࡮ࠣ။")
    CONFIG = bstack11l1l1l_opy_ (u"ࠢࡤࡱࡱࡪ࡮࡭ࠢ၌")
    bstack1lllll1111l_opy_ = bstack11l1l1l_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡷࠧ၍")
    bstack1ll1lll11_opy_ = bstack11l1l1l_opy_ (u"ࠤࡨࡼ࡮ࡺࠢ၎")
class bstack1lllll11l11_opy_:
    bstack1lllll11111_opy_ = bstack11l1l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡶࡸࡦࡸࡴࡦࡦࠥ၏")
    FINISHED = bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧၐ")
class bstack1llll1llll1_opy_:
    bstack1lllll11111_opy_ = bstack11l1l1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠣၑ")
    FINISHED = bstack11l1l1l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࠥၒ")
class bstack1llll1lll1l_opy_:
    bstack1lllll11111_opy_ = bstack11l1l1l_opy_ (u"ࠢࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡶࡸࡦࡸࡴࡦࡦࠥၓ")
    FINISHED = bstack11l1l1l_opy_ (u"ࠣࡪࡲࡳࡰࡥࡲࡶࡰࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧၔ")
class bstack1lllll111ll_opy_:
    bstack1llll1lll11_opy_ = bstack11l1l1l_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡤࡴࡨࡥࡹ࡫ࡤࠣၕ")
class bstack1llll1lllll_opy_:
    _1lllll111l1_opy_ = None
    def __new__(cls):
        if not cls._1lllll111l1_opy_:
            cls._1lllll111l1_opy_ = super(bstack1llll1lllll_opy_, cls).__new__(cls)
        return cls._1lllll111l1_opy_
    def __init__(self):
        self._hooks = defaultdict(lambda: defaultdict(list))
        self._lock = Lock()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def clear(self):
        with self._lock:
            self._hooks = defaultdict(list)
    def register(self, event_name, callback):
        with self._lock:
            if not callable(callback):
                raise ValueError(bstack11l1l1l_opy_ (u"ࠥࡇࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡳࡵࡴࡶࠣࡦࡪࠦࡣࡢ࡮࡯ࡥࡧࡲࡥࠡࡨࡲࡶࠥࠨၖ") + event_name)
            pid = os.getpid()
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡗ࡫ࡧࡪࡵࡷࡩࡷ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺࠠࠨࡽࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࢃࠧࠡࡹ࡬ࡸ࡭ࠦࡰࡪࡦࠣࠦၗ") + str(pid) + bstack11l1l1l_opy_ (u"ࠧࠨၘ"))
            self._hooks[event_name][pid].append(callback)
    def invoke(self, event_name, *args, **kwargs):
        with self._lock:
            pid = os.getpid()
            callbacks = self._hooks.get(event_name, {}).get(pid, [])
            if not callbacks:
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠨࡎࡰࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࡷࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࠡࠩࡾࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࡽࠨࠢࡺ࡭ࡹ࡮ࠠࡱ࡫ࡧࠤࠧၙ") + str(pid) + bstack11l1l1l_opy_ (u"ࠢࠣၚ"))
                return
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠣࡋࡱࡺࡴࡱࡩ࡯ࡩࠣࡿࡱ࡫࡮ࠩࡥࡤࡰࡱࡨࡡࡤ࡭ࡶ࠭ࢂࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࡴࠢࡩࡳࡷࠦࡥࡷࡧࡱࡸࠥ࠭ࡻࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࢁࠬࠦࡷࡪࡶ࡫ࠤࡵ࡯ࡤࠡࠤၛ") + str(pid) + bstack11l1l1l_opy_ (u"ࠤࠥၜ"))
            for callback in callbacks:
                try:
                    self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡍࡳࡼ࡯࡬ࡧࡧࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵࠢࠪࡿࡪࡼࡥ࡯ࡶࡢࡲࡦࡳࡥࡾࠩࠣࡻ࡮ࡺࡨࠡࡲ࡬ࡨࠥࠨၝ") + str(pid) + bstack11l1l1l_opy_ (u"ࠦࠧၞ"))
                    callback(event_name, *args, **kwargs)
                except Exception as e:
                    self.logger.error(bstack11l1l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࠤࠬࢁࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࢀࠫࠥࡽࡩࡵࡪࠣࡴ࡮ࡪࠠࡼࡲ࡬ࡨࢂࡀࠠࠣၟ") + str(e) + bstack11l1l1l_opy_ (u"ࠨࠢၠ"))
                    traceback.print_exc()
bstack1l1llll11l_opy_ = bstack1llll1lllll_opy_()