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

from omni.isaac.franka.tasks import FollowTarget
from omni.isaac.franka.controllers import RMPFlowController
from omni.isaac.core import World
from omni.isaac.franka import InverseKinematicsSolver

from omni.isaac.core import World
from omni.isaac.core.utils.nucleus import find_nucleus_server
from omni.isaac.core.utils.prims import create_prim

my_world = World(stage_units_in_meters=0.01)
my_task = FollowTarget(name="follow_target_task")
my_world.add_task(my_task)
my_world.reset()

result, nucleus_server = find_nucleus_server()
create_prim(
    prim_path="/background", usd_path= nucleus_server+ "/Isaac/Environments/Simple_Room/simple_room.usd"
)

task_params = my_world.get_task("follow_target_task").get_params()
franka_name = task_params["robot_name"]["value"]
target_name = task_params["target_name"]["value"]
my_franka = my_world.scene.get_object(franka_name)
# my_controller = InverseKinematicsSolver(
#     name="target_follower_controller",
#     robot_prim_path=my_franka.prim_path)
my_controller = RMPFlowController(name="target_follower_controller", robot_prim_path=my_franka.prim_path)
articulation_controller = my_franka.get_articulation_controller()
while simulation_app.is_running():
    my_world.step(render=True)
    if my_world.is_playing():
        if my_world.current_time_step_index == 0:
            my_world.reset()
            my_controller.reset()
        observations = my_world.get_observations()
        actions = my_controller.forward(
            target_end_effector_position=observations[target_name]["position"],
            target_end_effector_orientation=observations[target_name]["orientation"],
        )
        articulation_controller.apply_action(actions)

simulation_app.close()
