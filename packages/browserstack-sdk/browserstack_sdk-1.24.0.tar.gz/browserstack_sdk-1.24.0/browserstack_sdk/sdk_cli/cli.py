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
import subprocess
import threading
import time
import sys
import grpc
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack11111ll1l1_opy_ import bstack11111ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1111l1l1l1_opy_ import bstack1111l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1ll1ll11l1l_opy_ import bstack1ll1l11llll_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llll1l1_opy_ import bstack1ll1lllll1l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1ll111l1_opy_ import bstack1ll1l1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1111l11111_opy_ import bstack1111l111l1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1lllllllll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll11l1ll1l_opy_ import bstack1ll11l11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1l1llll11l_opy_ import bstack1l1llll11l_opy_, Events, bstack11l11lll1_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1ll1ll1lll1_opy_ import bstack1ll11l11l11_opy_
from browserstack_sdk.sdk_cli.bstack11111ll1ll_opy_ import bstack1111l1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import bstack1lllll1l1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from bstack_utils.helper import Notset, bstack1ll1l11ll11_opy_, get_cli_dir, bstack1ll1ll11l11_opy_, bstack11l1ll111l_opy_, bstack1l11llll1l_opy_, bstack1lll111l1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack111111lll1_opy_, bstack1lllllll1l1_opy_, bstack11111111ll_opy_, bstack1lll1l1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import bstack1111lllll1_opy_, bstack1111l1llll_opy_, bstack111l111111_opy_
from bstack_utils.constants import *
from bstack_utils import bstack111111l1l_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack111ll1111_opy_, bstack11llllllll_opy_
logger = bstack111111l1l_opy_.get_logger(__name__, bstack111111l1l_opy_.bstack1ll1l1l111l_opy_())
def bstack1ll1l1l11ll_opy_(bs_config):
    bstack1ll1l1llll1_opy_ = None
    bstack1ll11ll1lll_opy_ = None
    try:
        bstack1ll11ll1lll_opy_ = get_cli_dir()
        bstack1ll1l1llll1_opy_ = bstack1ll1ll11l11_opy_(bstack1ll11ll1lll_opy_)
        bstack1ll111llll1_opy_ = bstack1ll1l11ll11_opy_(bstack1ll1l1llll1_opy_, bstack1ll11ll1lll_opy_, bs_config)
        bstack1ll1l1llll1_opy_ = bstack1ll111llll1_opy_ if bstack1ll111llll1_opy_ else bstack1ll1l1llll1_opy_
        if not bstack1ll1l1llll1_opy_:
            raise ValueError(bstack11l1l1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡗࡉࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡒࡄࡘࡍࠨᄒ"))
    except Exception as ex:
        logger.debug(bstack11l1l1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡦࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡰࡦࡺࡥࡴࡶࠣࡦ࡮ࡴࡡࡳࡻࠥᄓ"))
        bstack1ll1l1llll1_opy_ = os.environ.get(bstack11l1l1l_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡓࡅ࡙ࡎࠢᄔ"))
        if bstack1ll1l1llll1_opy_:
            logger.debug(bstack11l1l1l_opy_ (u"ࠧࡌࡡ࡭࡮࡬ࡲ࡬ࠦࡢࡢࡥ࡮ࠤࡹࡵࠠࡔࡆࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤࡖࡁࡕࡊࠣࡪࡷࡵ࡭ࠡࡧࡱࡺ࡮ࡸ࡯࡯࡯ࡨࡲࡹࡀࠠࠣᄕ") + str(bstack1ll1l1llll1_opy_) + bstack11l1l1l_opy_ (u"ࠨࠢᄖ"))
        else:
            logger.debug(bstack11l1l1l_opy_ (u"ࠢࡏࡱࠣࡺࡦࡲࡩࡥࠢࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡦࡰࡹ࡭ࡷࡵ࡮࡮ࡧࡱࡸࡀࠦࡳࡦࡶࡸࡴࠥࡳࡡࡺࠢࡥࡩࠥ࡯࡮ࡤࡱࡰࡴࡱ࡫ࡴࡦ࠰ࠥᄗ"))
    return bstack1ll1l1llll1_opy_, bstack1ll11ll1lll_opy_
bstack1ll1l11lll1_opy_ = bstack11l1l1l_opy_ (u"ࠣ࠻࠼࠽࠾ࠨᄘ")
bstack1ll111ll11l_opy_ = bstack11l1l1l_opy_ (u"ࠤࡵࡩࡦࡪࡹࠣᄙ")
bstack1ll11l111ll_opy_ = bstack11l1l1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡗࡊ࡙ࡓࡊࡑࡑࡣࡎࡊࠢᄚ")
bstack1ll1ll11111_opy_ = bstack11l1l1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡑࡏࡓࡕࡇࡑࡣࡆࡊࡄࡓࠤᄛ")
bstack1l111111l_opy_ = bstack11l1l1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠣᄜ")
bstack1ll11ll11ll_opy_ = re.compile(bstack11l1l1l_opy_ (u"ࡸࠢࠩࡁ࡬࠭࠳࠰ࠨࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࢂࡂࡔࠫ࠱࠮ࠧᄝ"))
bstack1ll1l111ll1_opy_ = bstack11l1l1l_opy_ (u"ࠢࡥࡧࡹࡩࡱࡵࡰ࡮ࡧࡱࡸࠧᄞ")
bstack1ll1l1l1lll_opy_ = [
    Events.bstack1lll1l11l_opy_,
    Events.CONNECT,
    Events.bstack11l1ll1ll1_opy_,
]
class SDKCLI:
    _1lllll111l1_opy_ = None
    process: Union[None, Any]
    bstack1ll1ll1l1l1_opy_: bool
    bstack1ll1l1ll11l_opy_: bool
    bstack1ll11lll11l_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1ll11llll1l_opy_: Union[None, grpc.Channel]
    bstack1ll11l1ll11_opy_: str
    test_framework: TestFramework
    bstack1111l11lll_opy_: bstack1lllll1l1l1_opy_
    config: Union[None, Dict[str, Any]]
    web_driver: bstack1111l111l1_opy_
    bstack1ll11ll1111_opy_: bstack1lllllllll1_opy_
    bstack1ll1l111111_opy_: bstack1ll11l11l1l_opy_
    accessibility: bstack1ll1l11llll_opy_
    ai: bstack1ll1lllll1l_opy_
    bstack1ll1ll1ll1l_opy_: bstack1ll1l1l1ll1_opy_
    bstack1ll11l1111l_opy_: List[bstack1111l1ll11_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1ll1ll1l1ll_opy_: Any
    bstack1ll1ll1llll_opy_: Dict[str, timedelta]
    bstack1ll1ll1111l_opy_: str
    bstack11111ll1l1_opy_: bstack11111ll11l_opy_
    def __new__(cls):
        if not cls._1lllll111l1_opy_:
            cls._1lllll111l1_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1lllll111l1_opy_
    def __init__(self):
        self.process = None
        self.bstack1ll1ll1l1l1_opy_ = False
        self.bstack1ll11llll1l_opy_ = None
        self.bstack1111l11ll1_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1ll1ll11111_opy_, None)
        self.bstack1ll11ll1l11_opy_ = os.environ.get(bstack1ll11l111ll_opy_, bstack11l1l1l_opy_ (u"ࠣࠤᄟ")) == bstack11l1l1l_opy_ (u"ࠤࠥᄠ")
        self.bstack1ll1l1ll11l_opy_ = False
        self.bstack1ll11lll11l_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1ll1ll1l1ll_opy_ = None
        self.test_framework = None
        self.bstack1111l11lll_opy_ = None
        self.bstack1ll11l1ll11_opy_=bstack11l1l1l_opy_ (u"ࠥࠦᄡ")
        self.logger = bstack111111l1l_opy_.get_logger(self.__class__.__name__, bstack111111l1l_opy_.bstack1ll1l1l111l_opy_())
        self.bstack1ll1ll1llll_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack11111ll1l1_opy_ = bstack11111ll11l_opy_()
        self.web_driver = bstack1111l111l1_opy_()
        self.bstack1ll11ll1111_opy_ = bstack1lllllllll1_opy_()
        self.bstack1ll1l111111_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1ll11l1111l_opy_ = [
            self.web_driver,
            self.bstack1ll11ll1111_opy_,
        ]
    def bstack11l1111ll1_opy_(self):
        return os.environ.get(bstack1l111111l_opy_).lower().__eq__(bstack11l1l1l_opy_ (u"ࠦࡹࡸࡵࡦࠤᄢ"))
    def is_enabled(self, config):
        if bstack11l1l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩᄣ") in config and str(config[bstack11l1l1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪᄤ")]).lower() != bstack11l1l1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ᄥ"):
            return False
        bstack1ll1l111lll_opy_ = [bstack11l1l1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣᄦ"), bstack11l1l1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨᄧ")]
        bstack1ll1l11111l_opy_ = config.get(bstack11l1l1l_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠨᄨ")) in bstack1ll1l111lll_opy_ or os.environ.get(bstack11l1l1l_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬᄩ")) in bstack1ll1l111lll_opy_
        os.environ[bstack11l1l1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡎ࡙࡟ࡓࡗࡑࡒࡎࡔࡇࠣᄪ")] = str(bstack1ll1l11111l_opy_) # bstack1ll1l1ll1l1_opy_ bstack1ll1l1lll11_opy_ VAR to bstack1ll11ll111l_opy_ is binary running
        return bstack1ll1l11111l_opy_
    def bstack1ll1llll11_opy_(self):
        for event in bstack1ll1l1l1lll_opy_:
            bstack1l1llll11l_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1l1llll11l_opy_.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡻࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࢁࠥࡃ࠾ࠡࡽࡤࡶ࡬ࡹࡽࠡࠤᄫ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠢࠣᄬ"))
            )
        bstack1l1llll11l_opy_.register(Events.bstack1lll1l11l_opy_, self.__1ll1ll1l111_opy_)
        bstack1l1llll11l_opy_.register(Events.CONNECT, self.__1ll111l1lll_opy_)
        bstack1l1llll11l_opy_.register(Events.bstack11l1ll1ll1_opy_, self.__1ll1ll11ll1_opy_)
        bstack1l1llll11l_opy_.register(Events.bstack1ll1lll11_opy_, self.__1ll1lll1111_opy_)
    def bstack11ll1111l_opy_(self):
        return not self.bstack1ll11ll1l11_opy_ and os.environ.get(bstack1ll11l111ll_opy_, bstack11l1l1l_opy_ (u"ࠣࠤᄭ")) != bstack11l1l1l_opy_ (u"ࠤࠥᄮ")
    def is_running(self):
        if self.bstack1ll11ll1l11_opy_:
            return self.bstack1ll1ll1l1l1_opy_
        else:
            return bool(self.bstack1ll11llll1l_opy_)
    def bstack1ll1l11l1ll_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1ll11l1111l_opy_) and cli.is_running()
    def __1ll11llllll_opy_(self, bstack1ll1l111l11_opy_=10):
        if self.bstack1111l11ll1_opy_:
            return
        bstack1l1lll1l1l_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1ll1ll11111_opy_, self.cli_listen_addr)
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠥ࡟ࠧᄯ") + str(id(self)) + bstack11l1l1l_opy_ (u"ࠦࡢࠦࡣࡰࡰࡱࡩࡨࡺࡩ࡯ࡩࠥᄰ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack11l1l1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠱ࡩࡳࡧࡢ࡭ࡧࡢ࡬ࡹࡺࡰࡠࡲࡵࡳࡽࡿࠢᄱ"), 0), (bstack11l1l1l_opy_ (u"ࠨࡧࡳࡲࡦ࠲ࡪࡴࡡࡣ࡮ࡨࡣ࡭ࡺࡴࡱࡵࡢࡴࡷࡵࡸࡺࠤᄲ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1ll1l111l11_opy_)
        self.bstack1ll11llll1l_opy_ = channel
        self.bstack1111l11ll1_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1ll11llll1l_opy_)
        self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡩ࡯࡯ࡰࡨࡧࡹࠨᄳ"), datetime.now() - bstack1l1lll1l1l_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1ll1ll11111_opy_] = self.cli_listen_addr
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡤࡱࡱࡲࡪࡩࡴࡦࡦ࠽ࠤ࡮ࡹ࡟ࡤࡪ࡬ࡰࡩࡥࡰࡳࡱࡦࡩࡸࡹ࠽ࠣᄴ") + str(self.bstack11ll1111l_opy_()) + bstack11l1l1l_opy_ (u"ࠤࠥᄵ"))
    def __1ll1ll11ll1_opy_(self, event_name):
        if self.bstack11ll1111l_opy_():
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡸࡺ࡯ࡱࡲ࡬ࡲ࡬ࠦࡃࡍࡋࠥᄶ"))
        self.__1ll111lll1l_opy_()
    def __1ll1lll1111_opy_(self, event_name, bstack1ll11l11ll1_opy_ = None, bstack111l1l111_opy_=1):
        if bstack111l1l111_opy_ == 1:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠦࡘࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪࠦᄷ"))
        bstack1ll11ll1ll1_opy_ = Path(bstack1ll1lll111l_opy_ (u"ࠧࢁࡳࡦ࡮ࡩ࠲ࡨࡲࡩࡠࡦ࡬ࡶࢂ࠵ࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࡳ࠯࡬ࡶࡳࡳࠨᄸ"))
        if self.bstack1ll11ll1lll_opy_ and bstack1ll11ll1ll1_opy_.exists():
            with open(bstack1ll11ll1ll1_opy_, bstack11l1l1l_opy_ (u"࠭ࡲࠨᄹ"), encoding=bstack11l1l1l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᄺ")) as fp:
                data = json.load(fp)
                try:
                    bstack1l11llll1l_opy_(bstack11l1l1l_opy_ (u"ࠨࡒࡒࡗ࡙࠭ᄻ"), bstack1lll111l1l_opy_(bstack11l1111l1l_opy_), data, {
                        bstack11l1l1l_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᄼ"): (self.config[bstack11l1l1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᄽ")], self.config[bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᄾ")])
                    })
                except Exception as e:
                    logger.debug(bstack11llllllll_opy_.format(str(e)))
            bstack1ll11ll1ll1_opy_.unlink()
        sys.exit(bstack111l1l111_opy_)
    @measure(event_name=EVENTS.bstack1ll111l1ll1_opy_, stage=STAGE.SINGLE)
    def __1ll1ll1l111_opy_(self, event_name: str, data):
        self.bstack1ll11l1ll11_opy_, self.bstack1ll11ll1lll_opy_ = bstack1ll1l1l11ll_opy_(data.bs_config)
        os.environ[bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡜ࡘࡉࡕࡃࡅࡐࡊࡥࡄࡊࡔࠪᄿ")] = self.bstack1ll11ll1lll_opy_
        if not self.bstack1ll11l1ll11_opy_ or not self.bstack1ll11ll1lll_opy_:
            raise ValueError(bstack11l1l1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡵࡪࡨࠤࡘࡊࡋࠡࡅࡏࡍࠥࡨࡩ࡯ࡣࡵࡽࠧᅀ"))
        if self.bstack11ll1111l_opy_():
            self.__1ll111l1lll_opy_(event_name, bstack11l11lll1_opy_())
            return
        start = datetime.now()
        is_started = self.__1ll11ll1l1l_opy_()
        self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠢࡴࡲࡤࡻࡳࡥࡴࡪ࡯ࡨࠦᅁ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1ll11llllll_opy_()
            self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢᅂ"), datetime.now() - start)
            start = datetime.now()
            self.__1ll1l1lllll_opy_(data)
            self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢᅃ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1ll11l1lll1_opy_, stage=STAGE.SINGLE)
    def __1ll111l1lll_opy_(self, event_name: str, data: bstack11l11lll1_opy_):
        if not self.bstack11ll1111l_opy_():
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡰࡰࡱࡩࡨࡺ࠺ࠡࡰࡲࡸࠥࡧࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹࠢᅄ"))
            return
        bin_session_id = os.environ.get(bstack1ll11l111ll_opy_)
        start = datetime.now()
        self.__1ll11llllll_opy_()
        self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࡤࡺࡩ࡮ࡧࠥᅅ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤࠡࡶࡲࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦࡃࡍࡋࠣࠦᅆ") + str(bin_session_id) + bstack11l1l1l_opy_ (u"ࠨࠢᅇ"))
        start = datetime.now()
        self.__1ll1l1ll1ll_opy_()
        self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡵ࡫ࡰࡩࠧᅈ"), datetime.now() - start)
    def __1ll11l1l1l1_opy_(self):
        if not self.bstack1111l11ll1_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠣࡥࡤࡲࡳࡵࡴࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡨࠤࡲࡵࡤࡶ࡮ࡨࡷࠧᅉ"))
            return
        if not self.bstack1ll1l111111_opy_ and self.config_observability and self.config_observability.success: # bstack1111llll11_opy_
            self.bstack1ll1l111111_opy_ = bstack1ll11l11l1l_opy_() # bstack1ll111l1l11_opy_
            self.bstack1ll11l1111l_opy_.append(self.bstack1ll1l111111_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1ll1l11llll_opy_()
            self.bstack1ll11l1111l_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack11l1l1l_opy_ (u"ࠤࡶࡩࡱ࡬ࡈࡦࡣ࡯ࠦᅊ"), False) == True:
            self.ai = bstack1ll1lllll1l_opy_()
            self.bstack1ll11l1111l_opy_.append(self.ai)
        if not self.percy and self.bstack1ll1ll1l1ll_opy_ and self.bstack1ll1ll1l1ll_opy_.success:
            self.percy = bstack1ll1l1l1ll1_opy_(self.bstack1ll1ll1l1ll_opy_)
            self.bstack1ll11l1111l_opy_.append(self.percy)
        for mod in self.bstack1ll11l1111l_opy_:
            if not mod.bstack11111ll111_opy_():
                mod.configure(self.bstack1111l11ll1_opy_, self.config, self.cli_bin_session_id, self.bstack11111ll1l1_opy_)
    def __1ll11l11111_opy_(self):
        for mod in self.bstack1ll11l1111l_opy_:
            if mod.bstack11111ll111_opy_():
                mod.configure(self.bstack1111l11ll1_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1ll11lll1l1_opy_, stage=STAGE.SINGLE)
    def __1ll1l1lllll_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1ll1l1ll11l_opy_:
            return
        self.__1ll1l1111l1_opy_(data)
        bstack1l1lll1l1l_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack11l1l1l_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࠥᅋ")
        req.sdk_language = bstack11l1l1l_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࠦᅌ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1ll11ll11ll_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡡࠢᅍ") + str(id(self)) + bstack11l1l1l_opy_ (u"ࠨ࡝ࠡ࡯ࡤ࡭ࡳ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡵࡷࡥࡷࡺ࡟ࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧᅎ"))
            r = self.bstack1111l11ll1_opy_.StartBinSession(req)
            self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡴࡢࡴࡷࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤᅏ"), datetime.now() - bstack1l1lll1l1l_opy_)
            os.environ[bstack1ll11l111ll_opy_] = r.bin_session_id
            self.__1ll111ll111_opy_(r)
            self.__1ll11l1l1l1_opy_()
            self.bstack11111ll1l1_opy_.start()
            self.bstack1ll1l1ll11l_opy_ = True
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠣ࡝ࠥᅐ") + str(id(self)) + bstack11l1l1l_opy_ (u"ࠤࡠࠤࡲࡧࡩ࡯࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡨࡵ࡮࡯ࡧࡦࡸࡪࡪࠢᅑ"))
        except grpc.bstack1ll11lll1ll_opy_ as bstack1ll1l1l1111_opy_:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡷ࡭ࡲ࡫࡯ࡦࡷࡷ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᅒ") + str(bstack1ll1l1l1111_opy_) + bstack11l1l1l_opy_ (u"ࠦࠧᅓ"))
            traceback.print_exc()
            raise bstack1ll1l1l1111_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᅔ") + str(e) + bstack11l1l1l_opy_ (u"ࠨࠢᅕ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1ll11ll11l1_opy_, stage=STAGE.SINGLE)
    def __1ll1l1ll1ll_opy_(self):
        if not self.bstack11ll1111l_opy_() or not self.cli_bin_session_id or self.bstack1ll11lll11l_opy_:
            return
        bstack1l1lll1l1l_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᅖ"), bstack11l1l1l_opy_ (u"ࠨ࠲ࠪᅗ")))
        try:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠤ࡞ࠦᅘ") + str(id(self)) + bstack11l1l1l_opy_ (u"ࠥࡡࠥࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡣࡰࡰࡱࡩࡨࡺ࡟ࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧᅙ"))
            r = self.bstack1111l11ll1_opy_.ConnectBinSession(req)
            self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡦࡳࡳࡴࡥࡤࡶࡢࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣᅚ"), datetime.now() - bstack1l1lll1l1l_opy_)
            self.__1ll111ll111_opy_(r)
            self.__1ll11l1l1l1_opy_()
            self.bstack11111ll1l1_opy_.start()
            self.bstack1ll11lll11l_opy_ = True
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡡࠢᅛ") + str(id(self)) + bstack11l1l1l_opy_ (u"ࠨ࡝ࠡࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡦࡳࡳࡴࡥࡤࡶࡨࡨࠧᅜ"))
        except grpc.bstack1ll11lll1ll_opy_ as bstack1ll1l1l1111_opy_:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡴࡪ࡯ࡨࡳࡪࡻࡴ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᅝ") + str(bstack1ll1l1l1111_opy_) + bstack11l1l1l_opy_ (u"ࠣࠤᅞ"))
            traceback.print_exc()
            raise bstack1ll1l1l1111_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᅟ") + str(e) + bstack11l1l1l_opy_ (u"ࠥࠦᅠ"))
            traceback.print_exc()
            raise e
    def __1ll111ll111_opy_(self, r):
        self.bstack1ll111ll1l1_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack11l1l1l_opy_ (u"ࠦࡺࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡵࡨࡶࡻ࡫ࡲࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥᅡ") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack11l1l1l_opy_ (u"ࠧ࡫࡭ࡱࡶࡼࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࡫ࡵࡵ࡯ࡦࠥᅢ"))
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack11l1l1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡔࡪࡸࡣࡺࠢ࡬ࡷࠥࡹࡥ࡯ࡶࠣࡳࡳࡲࡹࠡࡣࡶࠤࡵࡧࡲࡵࠢࡲࡪࠥࡺࡨࡦࠢࠥࡇࡴࡴ࡮ࡦࡥࡷࡆ࡮ࡴࡓࡦࡵࡶ࡭ࡴࡴࠬࠣࠢࡤࡲࡩࠦࡴࡩ࡫ࡶࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡩࡴࠢࡤࡰࡸࡵࠠࡶࡵࡨࡨࠥࡨࡹࠡࡕࡷࡥࡷࡺࡂࡪࡰࡖࡩࡸࡹࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡦࡴࡨࡪࡴࡸࡥ࠭ࠢࡑࡳࡳ࡫ࠠࡩࡣࡱࡨࡱ࡯࡮ࡨࠢ࡬ࡷࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᅣ")
        self.bstack1ll1ll1l1ll_opy_ = getattr(r, bstack11l1l1l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᅤ"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᅥ")] = self.config_testhub.jwt
        os.environ[bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᅦ")] = self.config_testhub.build_hashed_id
    def bstack1ll1l11ll1l_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1ll1ll1l1l1_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1ll11lll111_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1ll11lll111_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1ll1l11ll1l_opy_(event_name=EVENTS.bstack1ll1l1l1l11_opy_, stage=STAGE.SINGLE)
    def __1ll11ll1l1l_opy_(self, bstack1ll1l111l11_opy_=10):
        if self.bstack1ll1ll1l1l1_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡷࡹࡧࡲࡵ࠼ࠣࡥࡱࡸࡥࡢࡦࡼࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠧᅧ"))
            return True
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡸࡺࡡࡳࡶࠥᅨ"))
        if os.getenv(bstack11l1l1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡇࡑ࡚ࠧᅩ")) == bstack1ll1l111ll1_opy_:
            self.cli_bin_session_id = bstack1ll1l111ll1_opy_
            self.cli_listen_addr = bstack11l1l1l_opy_ (u"ࠨࡵ࡯࡫ࡻ࠾࠴ࡺ࡭ࡱ࠱ࡶࡨࡰ࠳ࡰ࡭ࡣࡷࡪࡴࡸ࡭࠮ࠧࡶ࠲ࡸࡵࡣ࡬ࠤᅪ") % (self.cli_bin_session_id)
            self.bstack1ll1ll1l1l1_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1ll11l1ll11_opy_, bstack11l1l1l_opy_ (u"ࠢࡴࡦ࡮ࠦᅫ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1ll1l11l111_opy_ compat for text=True in bstack1ll1l1ll111_opy_ python
            encoding=bstack11l1l1l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᅬ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1ll111lll11_opy_ = threading.Thread(target=self.__1ll11l1llll_opy_, args=(bstack1ll1l111l11_opy_,))
        bstack1ll111lll11_opy_.start()
        bstack1ll111lll11_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡵࡳࡥࡼࡴ࠺ࠡࡴࡨࡸࡺࡸ࡮ࡤࡱࡧࡩࡂࢁࡳࡦ࡮ࡩ࠲ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡸࡥࡵࡷࡵࡲࡨࡵࡤࡦࡿࠣࡳࡺࡺ࠽ࡼࡵࡨࡰ࡫࠴ࡰࡳࡱࡦࡩࡸࡹ࠮ࡴࡶࡧࡳࡺࡺ࠮ࡳࡧࡤࡨ࠭࠯ࡽࠡࡧࡵࡶࡂࠨᅭ") + str(self.process.stderr.read()) + bstack11l1l1l_opy_ (u"ࠥࠦᅮ"))
        if not self.bstack1ll1ll1l1l1_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡠࠨᅯ") + str(id(self)) + bstack11l1l1l_opy_ (u"ࠧࡣࠠࡤ࡮ࡨࡥࡳࡻࡰࠣᅰ"))
            self.__1ll111lll1l_opy_()
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡶࡲࡰࡥࡨࡷࡸࡥࡲࡦࡣࡧࡽ࠿ࠦࠢᅱ") + str(self.bstack1ll1ll1l1l1_opy_) + bstack11l1l1l_opy_ (u"ࠢࠣᅲ"))
        return self.bstack1ll1ll1l1l1_opy_
    def __1ll11l1llll_opy_(self, bstack1ll1l1l1l1l_opy_=10):
        bstack1ll1l1111ll_opy_ = time.time()
        while self.process and time.time() - bstack1ll1l1111ll_opy_ < bstack1ll1l1l1l1l_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack11l1l1l_opy_ (u"ࠣ࡫ࡧࡁࠧᅳ") in line:
                    self.cli_bin_session_id = line.split(bstack11l1l1l_opy_ (u"ࠤ࡬ࡨࡂࠨᅴ"))[-1:][0].strip()
                    self.logger.debug(bstack11l1l1l_opy_ (u"ࠥࡧࡱ࡯࡟ࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠻ࠤᅵ") + str(self.cli_bin_session_id) + bstack11l1l1l_opy_ (u"ࠦࠧᅶ"))
                    continue
                if bstack11l1l1l_opy_ (u"ࠧࡲࡩࡴࡶࡨࡲࡂࠨᅷ") in line:
                    self.cli_listen_addr = line.split(bstack11l1l1l_opy_ (u"ࠨ࡬ࡪࡵࡷࡩࡳࡃࠢᅸ"))[-1:][0].strip()
                    self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡤ࡮࡬ࡣࡱ࡯ࡳࡵࡧࡱࡣࡦࡪࡤࡳ࠼ࠥᅹ") + str(self.cli_listen_addr) + bstack11l1l1l_opy_ (u"ࠣࠤᅺ"))
                    continue
                if bstack11l1l1l_opy_ (u"ࠤࡳࡳࡷࡺ࠽ࠣᅻ") in line:
                    port = line.split(bstack11l1l1l_opy_ (u"ࠥࡴࡴࡸࡴ࠾ࠤᅼ"))[-1:][0].strip()
                    self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡵࡵࡲࡵ࠼ࠥᅽ") + str(port) + bstack11l1l1l_opy_ (u"ࠧࠨᅾ"))
                    continue
                if line.strip() == bstack1ll111ll11l_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack11l1l1l_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡏࡏࡠࡕࡗࡖࡊࡇࡍࠣᅿ"), bstack11l1l1l_opy_ (u"ࠢ࠲ࠤᆀ")) == bstack11l1l1l_opy_ (u"ࠣ࠳ࠥᆁ"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1ll1ll1l1l1_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠤࡨࡶࡷࡵࡲ࠻ࠢࠥᆂ") + str(e) + bstack11l1l1l_opy_ (u"ࠥࠦᆃ"))
        return False
    @measure(event_name=EVENTS.bstack1ll11l111l1_opy_, stage=STAGE.SINGLE)
    def __1ll111lll1l_opy_(self):
        if self.bstack1ll11llll1l_opy_:
            self.bstack11111ll1l1_opy_.stop()
            start = datetime.now()
            if self.bstack1ll11llll11_opy_():
                self.cli_bin_session_id = None
                if self.bstack1ll11lll11l_opy_:
                    self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠦࡸࡺ࡯ࡱࡡࡶࡩࡸࡹࡩࡰࡰࡢࡸ࡮ࡳࡥࠣᆄ"), datetime.now() - start)
                else:
                    self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠧࡹࡴࡰࡲࡢࡷࡪࡹࡳࡪࡱࡱࡣࡹ࡯࡭ࡦࠤᆅ"), datetime.now() - start)
            self.__1ll11l11111_opy_()
            start = datetime.now()
            self.bstack1ll11llll1l_opy_.close()
            self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠨࡤࡪࡵࡦࡳࡳࡴࡥࡤࡶࡢࡸ࡮ࡳࡥࠣᆆ"), datetime.now() - start)
            self.bstack1ll11llll1l_opy_ = None
        if self.process:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡴࡶࡲࡴࠧᆇ"))
            start = datetime.now()
            self.process.terminate()
            self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠣ࡭࡬ࡰࡱࡥࡴࡪ࡯ࡨࠦᆈ"), datetime.now() - start)
            self.process = None
            if self.bstack1ll11ll1l11_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1l1l11111_opy_()
                self.logger.info(
                    bstack11l1l1l_opy_ (u"ࠤ࡙࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠧᆉ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack11l1l1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩᆊ")] = self.config_testhub.build_hashed_id
        self.bstack1ll1ll1l1l1_opy_ = False
    def __1ll1l1111l1_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack11l1l1l_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨᆋ")] = selenium.__version__
            data.frameworks.append(bstack11l1l1l_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢᆌ"))
        except:
            pass
    def bstack1ll1ll111ll_opy_(self, hub_url: str, platform_index: int, bstack11lllll1l1_opy_: Any):
        if self.bstack1111l11lll_opy_:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠠࡴࡧࡷࡹࡵࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡷࡪࡺࠠࡶࡲࠥᆍ"))
            return
        try:
            bstack1l1lll1l1l_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack11l1l1l_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤᆎ")
            self.bstack1111l11lll_opy_ = bstack1111l1ll1l_opy_(
                hub_url,
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1111ll1111_opy_={bstack11l1l1l_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡠࡱࡳࡸ࡮ࡵ࡮ࡴࡡࡩࡶࡴࡳ࡟ࡤࡣࡳࡷࠧᆏ"): bstack11lllll1l1_opy_}
            )
            def bstack1ll11l1l1ll_opy_(self):
                return
            if self.config.get(bstack11l1l1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠦᆐ"), True):
                Service.start = bstack1ll11l1l1ll_opy_
                Service.stop = bstack1ll11l1l1ll_opy_
            def get_accessibility_results(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results(driver, framework_name=framework)
            def get_accessibility_results_summary(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results_summary(driver, framework_name=framework)
            def perform_scan(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.perform_scan(driver, method=None, framework_name=framework)
            WebDriver.getAccessibilityResults = get_accessibility_results
            WebDriver.get_accessibility_results = get_accessibility_results
            WebDriver.getAccessibilityResultsSummary = get_accessibility_results_summary
            WebDriver.get_accessibility_results_summary = get_accessibility_results_summary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠦᆑ"), datetime.now() - bstack1l1lll1l1l_opy_)
        except Exception as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠻ࠢࠥᆒ") + str(e) + bstack11l1l1l_opy_ (u"ࠧࠨᆓ"))
    def bstack1ll111l1l1l_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠠࡴࡧࡷࡹࡵࠦࡰࡺࡶࡨࡷࡹࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡵࡨࡸࠥࡻࡰࠣᆔ"))
            return
        if bstack11l1ll111l_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack11l1l1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢᆕ"): pytest.__version__ }, [bstack11l1l1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧᆖ")])
            return
        try:
            import pytest
            self.test_framework = bstack1ll11l11l11_opy_({ bstack11l1l1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤᆗ"): pytest.__version__ }, [bstack11l1l1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥᆘ")])
        except Exception as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰࡺࡶࡨࡷࡹࡀࠠࠣᆙ") + str(e) + bstack11l1l1l_opy_ (u"ࠧࠨᆚ"))
        self.bstack1ll11l1l111_opy_()
    def bstack1ll11l1l111_opy_(self):
        if not self.bstack11l1111ll1_opy_():
            return
        bstack1l1l1l111l_opy_ = None
        def bstack11lll1llll_opy_(config, startdir):
            return bstack11l1l1l_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࠲ࢀࠦᆛ").format(bstack11l1l1l_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨᆜ"))
        def bstack1l1111lll1_opy_():
            return
        def bstack1llllll11l_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack11l1l1l_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨᆝ"):
                return bstack11l1l1l_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣᆞ")
            else:
                return bstack1l1l1l111l_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack1l1l1l111l_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack11lll1llll_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l1111lll1_opy_
            Config.getoption = bstack1llllll11l_opy_
        except Exception as e:
            self.logger.error(bstack11l1l1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡶࡦ࡬ࠥࡶࡹࡵࡧࡶࡸࠥࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠠࡧࡱࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠽ࠤࠧᆟ") + str(e) + bstack11l1l1l_opy_ (u"ࠦࠧᆠ"))
    def bstack1ll1l111l1l_opy_(self):
        bstack1ll1ll11lll_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1ll1ll11lll_opy_, dict):
            if cli.config_observability:
                bstack1ll1ll11lll_opy_.update(
                    {bstack11l1l1l_opy_ (u"ࠧࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠧᆡ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack11l1l1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࡠࡶࡲࡣࡼࡸࡡࡱࠤᆢ") in accessibility.get(bstack11l1l1l_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣᆣ"), {}):
                    bstack1ll11l11lll_opy_ = accessibility.get(bstack11l1l1l_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᆤ"))
                    bstack1ll11l11lll_opy_.update({ bstack11l1l1l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡶࡘࡴ࡝ࡲࡢࡲࠥᆥ"): bstack1ll11l11lll_opy_.pop(bstack11l1l1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷࡤࡺ࡯ࡠࡹࡵࡥࡵࠨᆦ")) })
                bstack1ll1ll11lll_opy_.update({bstack11l1l1l_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠦᆧ"): accessibility })
        return bstack1ll1ll11lll_opy_
    @measure(event_name=EVENTS.bstack1ll11l1l11l_opy_, stage=STAGE.SINGLE)
    def bstack1ll11llll11_opy_(self, bstack1ll1l11l11l_opy_: str = None, bstack1ll1l11l1l1_opy_: str = None, bstack111l1l111_opy_: int = None):
        if not self.cli_bin_session_id or not self.bstack1111l11ll1_opy_:
            return
        bstack1l1lll1l1l_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if bstack111l1l111_opy_:
            req.bstack111l1l111_opy_ = bstack111l1l111_opy_
        if bstack1ll1l11l11l_opy_:
            req.bstack1ll1l11l11l_opy_ = bstack1ll1l11l11l_opy_
        if bstack1ll1l11l1l1_opy_:
            req.bstack1ll1l11l1l1_opy_ = bstack1ll1l11l1l1_opy_
        try:
            r = self.bstack1111l11ll1_opy_.StopBinSession(req)
            self.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡹࡵࡰࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᆨ"), datetime.now() - bstack1l1lll1l1l_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack1ll1l1lll_opy_(self, key: str, value: timedelta):
        tag = bstack11l1l1l_opy_ (u"ࠨࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࠨᆩ") if self.bstack11ll1111l_opy_() else bstack11l1l1l_opy_ (u"ࠢ࡮ࡣ࡬ࡲ࠲ࡶࡲࡰࡥࡨࡷࡸࠨᆪ")
        self.bstack1ll1ll1llll_opy_[bstack11l1l1l_opy_ (u"ࠣ࠼ࠥᆫ").join([tag + bstack11l1l1l_opy_ (u"ࠤ࠰ࠦᆬ") + str(id(self)), key])] += value
    def bstack1l1l11111_opy_(self):
        if not os.getenv(bstack11l1l1l_opy_ (u"ࠥࡈࡊࡈࡕࡈࡡࡓࡉࡗࡌࠢᆭ"), bstack11l1l1l_opy_ (u"ࠦ࠵ࠨᆮ")) == bstack11l1l1l_opy_ (u"ࠧ࠷ࠢᆯ"):
            return
        bstack1ll1ll1l11l_opy_ = dict()
        bstack1lll11ll11l_opy_ = []
        if self.test_framework:
            bstack1lll11ll11l_opy_.extend(list(self.test_framework.bstack1lll11ll11l_opy_.values()))
        if self.bstack1111l11lll_opy_:
            bstack1lll11ll11l_opy_.extend(list(self.bstack1111l11lll_opy_.bstack1lll11ll11l_opy_.values()))
        for instance in bstack1lll11ll11l_opy_:
            if not instance.platform_index in bstack1ll1ll1l11l_opy_:
                bstack1ll1ll1l11l_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1ll1ll1l11l_opy_[instance.platform_index]
            for k, v in instance.bstack1lllll11lll_opy_().items():
                report[k] += v
                report[k.split(bstack11l1l1l_opy_ (u"ࠨ࠺ࠣᆰ"))[0]] += v
        bstack1ll1ll1ll11_opy_ = sorted([(k, v) for k, v in self.bstack1ll1ll1llll_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1ll111lllll_opy_ = 0
        for r in bstack1ll1ll1ll11_opy_:
            bstack1ll111ll1ll_opy_ = r[1].total_seconds()
            bstack1ll111lllll_opy_ += bstack1ll111ll1ll_opy_
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠢ࡜ࡲࡨࡶ࡫ࡣࠠࡤ࡮࡬࠾ࢀࡸ࡛࠱࡟ࢀࡁࠧᆱ") + str(bstack1ll111ll1ll_opy_) + bstack11l1l1l_opy_ (u"ࠣࠤᆲ"))
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠤ࠰࠱ࠧᆳ"))
        bstack1ll1l1l11l1_opy_ = []
        for platform_index, report in bstack1ll1ll1l11l_opy_.items():
            bstack1ll1l1l11l1_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1ll1l1l11l1_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1llllllll_opy_ = set()
        bstack1ll11lllll1_opy_ = 0
        for r in bstack1ll1l1l11l1_opy_:
            bstack1ll111ll1ll_opy_ = r[2].total_seconds()
            bstack1ll11lllll1_opy_ += bstack1ll111ll1ll_opy_
            bstack1llllllll_opy_.add(r[0])
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠥ࡟ࡵ࡫ࡲࡧ࡟ࠣࡸࡪࡹࡴ࠻ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠰ࡿࡷࡡ࠰࡞ࡿ࠽ࡿࡷࡡ࠱࡞ࡿࡀࠦᆴ") + str(bstack1ll111ll1ll_opy_) + bstack11l1l1l_opy_ (u"ࠦࠧᆵ"))
        if self.bstack11ll1111l_opy_():
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠧ࠳࠭ࠣᆶ"))
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠨ࡛ࡱࡧࡵࡪࡢࠦࡣ࡭࡫࠽ࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵࡀࡿࡹࡵࡴࡢ࡮ࡢࡧࡱ࡯ࡽࠡࡶࡨࡷࡹࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴ࠯ࡾࡷࡹࡸࠨࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠬࢁࡂࠨᆷ") + str(bstack1ll11lllll1_opy_) + bstack11l1l1l_opy_ (u"ࠢࠣᆸ"))
        else:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡥ࡯࡭࠿ࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶࡁࠧᆹ") + str(bstack1ll111lllll_opy_) + bstack11l1l1l_opy_ (u"ࠤࠥᆺ"))
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠥ࠱࠲ࠨᆻ"))
    def bstack1ll111ll1l1_opy_(self, r):
        if r is not None and getattr(r, bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࠬᆼ"), None) and getattr(r.testhub, bstack11l1l1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬᆽ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack11l1l1l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᆾ")))
            for bstack1ll1l1lll1l_opy_, err in errors.items():
                if err[bstack11l1l1l_opy_ (u"ࠧࡵࡻࡳࡩࠬᆿ")] == bstack11l1l1l_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ᇀ"):
                    self.logger.info(err[bstack11l1l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᇁ")])
                else:
                    self.logger.error(err[bstack11l1l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᇂ")])
cli = SDKCLI()