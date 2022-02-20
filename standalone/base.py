# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#
from omni.isaac.kit import SimulationApp

CONFIG = {"renderer": "RayTracedLighting", "headless": False}

simulation_app = SimulationApp(CONFIG)
from hsr import task
from hsr.hsr import HSR
from omni.isaac.core import World
from omni.isaac.core.utils import viewports, stage, extensions, prims, rotations, nucleus

BACKGROUND_STAGE_PATH = "/background"
BACKGROUND_USD_PATH = "/Isaac/Environments/Simple_Room/simple_room.usd"

import carb
from pathlib import Path
import numpy as np

# Load project root
project_root_path = Path(__file__).parent.parent.absolute()
urdf_path = project_root_path / "robots" / "hsr" / "urdf" / "hsrb4s.urdf"
HSR(urdf_path=str(urdf_path), name="my_hsr")

# Locate /Isaac folder on nucleus server to load environment and robot stages
result, _nucleus_path = nucleus.find_nucleus_server()
if result is False:
    carb.log_error("Could not find nucleus server with /Isaac folder, exiting")
    simulation_app.close()
    sys.exit()

# Preparing stage
viewports.set_camera_view(eye=np.array([120, 120, 80]), target=np.array([0, 0, 50]))

# Loading the simple_room environment
stage.add_reference_to_stage(_nucleus_path + BACKGROUND_USD_PATH, BACKGROUND_STAGE_PATH)

stage.add_reference_to_stage(_nucleus_path + BACKGROUND_USD_PATH, BACKGROUND_STAGE_PATH)


my_world = World(stage_units_in_meters=0.01)
my_task = task.BaseTask(name="base_task")
my_world.add_task(my_task)
my_world.reset()

while simulation_app.is_running():
    my_world.step(render=True)
    if my_world.is_playing():
        if my_world.current_time_step_index == 0:
            my_world.reset()

simulation_app.close()
