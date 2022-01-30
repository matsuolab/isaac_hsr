
from typing import Optional
import numpy as np

import omni.isaac.core.tasks as tasks
from omni.isaac.core.utils.prims import is_prim_path_valid
from omni.isaac.core.utils.string import find_unique_string_name
from hsr.hsr import HSR


class BaseTask(tasks.BaseTask):
    def __init__(
        self, name: str,
        offset: Optional[np.ndarray] = None,
        hsr_prim_path: Optional[str] = None,
        hsr_robot_name: Optional[str] = None,
    ) -> None:
        tasks.BaseTask.__init__(
            self,
            name=name,
            offset=offset,
        )
        self._hsr_prim_path = hsr_prim_path
        self._hsr_robot_name = hsr_robot_name
        return

    def set_robot(self) -> HSR():
        if self._hsr_prim_path is None:
            self._hsr_prim_path = find_unique_string_name(
                intitial_name='/World/WRS',
                is_unique_fn=lambda x: not is_prim_path_valid(x)
            )
        if self._hsr_robot_name is None:
            self._hsr_robot_name = find_unique_string_name(
                intitial_name="my_hsr",
                is_unique_fn=lambda x: not self.scene.object_exists(x)
            )

        return HSR(
            prim_path=self._hsr_prim_path,
            name=self._hsr_robot_name
        )
