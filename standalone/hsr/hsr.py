
from typing import Optional
import numpy as np

from omni.isaac.core.robots.robot import Robot
from omni.isaac.core.utils.prims import get_prim_at_path
from omni.isaac.core.utils.nucleus import find_nucleus_server
from omni.isaac.core.utils.stage import add_reference_to_stage, get_stage_units
from omni.kit import commands

import carb


class HSR(Robot):
    def __init__(
        self,
        urdf_path: str,
        name: str = "robot",
        position: Optional[np.ndarray] = None,
        orientation: Optional[np.ndarray] = None,
    ):
        status, import_config = commands.execute(
            "URDFCreateImportConfig")
        import_config.merge_fixed_joints = False
        import_config.fix_base = True
        import_config.make_default_prim = True
        import_config.create_physics_scene = True
        commands.execute(
            name="URDFParseAndImportFile",
            urdf_path=urdf_path,
            import_config=import_config,
        )
        """
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
                    carb.log_error(
                        "Could not find nucleus server with /Isaac folder")
        """
