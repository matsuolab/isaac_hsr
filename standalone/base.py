# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#
from omni.isaac.kit import SimulationApp

simulation_app = SimulationApp({"headless": False})

from hsr import task
from hsr.hsr import HSR
from omni.isaac.core import World


HSR(
            urdf_path='/home/h6x_dev1/.local/share/ov/pkg/isaac_sim-2021.2.1/isaac_hsr/robots/hsr/urdf/hsrb4s.urdf',
            name='my_hsr'
        )
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
