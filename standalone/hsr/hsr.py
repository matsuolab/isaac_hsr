
from typing import Optional
import numpy as np

from pxr import Usd
from omni.isaac.core.robots.robot import Robot
from omni.isaac.core.utils.prims import get_prim_at_path
from omni.isaac.core.utils.nucleus import find_nucleus_server
from omni.isaac.core.utils.stage import add_reference_to_stage, get_stage_units

import carb


class HSR(Robot):
    def __init__(
        self,
        prim_path: str,
        name: str = "robot",
        usd_path: Optional[str] = None,
        position: Optional[np.ndarray] = None,
        orientation: Optional[np.ndarray] = None,
    ):
        prim: Usd.Prim = get_prim_at_path(prim_path)
        if not prim.IsValid():
            if not usd_path:
                add_reference_to_stage(
                    usd_path=usd_path,
                    prim_path=prim_path
                )
            else:
                result, nucleus_server = find_nucleus_server()
                if result is False:
                    carb.log_error("Could not find nucleus server with /Isaac folder")
