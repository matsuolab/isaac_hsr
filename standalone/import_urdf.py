"""Import urdf."""

from omni.isaac.kit import SimulationApp

kit = SimulationApp({"headless": False})

import omni.kit.commands
from omni.isaac.dynamic_control import _dynamic_control

from pxr import Sdf, Gf, UsdLux
from pxr import PhysxSchema
from pxr import UsdPhysics

from omni.isaac.core.utils.extensions import get_extension_path_from_name

# Setting up import configuration
status, import_config = omni.kit.commands.execute("URDFCreateImportConfig")
import_config.merge_fixed_joints = False
import_config.convex_decomp = False
import_config.import_inertia_tensor = True
import_config.fix_base = True
import_config.distance_scale = 0.01

# Get path to extension data
extension_path = get_extension_path_from_name("omni.isaac.urdf")
urdf_path = '/home/aoi/.local/share/ov/pkg/isaac_sim-2021.2.1/isaac_hsr/robots/hsr/urdf/hsrb4s.urdf'
status, stage_path = omni.kit.commands.execute(
    "URDFParseAndImportFile",
    urdf_path=urdf_path,
    import_config=import_config,
)
# Get stage handle
stage = omni.usd.get_context().get_stage()


# Enable physics
scene = UsdPhysics.Scene.Define(stage, Sdf.Path("/physicsScene"))
# Set gravity
scene.CreateGravityDirectionAttr().Set(Gf.Vec3f(0.0, 0.0, -1.0))
scene.CreateGravityMagnitudeAttr().Set(981.0)
# Set solver settings
PhysxSchema.PhysxSceneAPI.Apply(stage.GetPrimAtPath("/physicsScene"))
physxSceneAPI = PhysxSchema.PhysxSceneAPI.Get(stage, "/physicsScene")
physxSceneAPI.CreateEnableCCDAttr(True)
physxSceneAPI.CreateEnableStabilizationAttr(True)
physxSceneAPI.CreateEnableGPUDynamicsAttr(False)
physxSceneAPI.CreateBroadphaseTypeAttr("MBP")
physxSceneAPI.CreateSolverTypeAttr("TGS")

# Add ground plane
omni.kit.commands.execute(
    "AddGroundPlaneCommand",
    stage=stage,
    planePath="/groundPlane",
    axis="Z",
    size=1500.0,
    position=Gf.Vec3f(0, 0, -50),
    color=Gf.Vec3f(0.5),
)

# Add lighting
distantLight = UsdLux.DistantLight.Define(stage, Sdf.Path("/DistantLight"))
distantLight.CreateIntensityAttr(500)

# Get handle to the Drive API for both wheels
# left_wheel_drive = UsdPhysics.DriveAPI.Get(stage.GetPrimAtPath("/carter/chassis_link/left_wheel"), "angular")
# right_wheel_drive = UsdPhysics.DriveAPI.Get(stage.GetPrimAtPath("/carter/chassis_link/right_wheel"), "angular")

# Set the velocity drive target in degrees/second
# left_wheel_drive.GetTargetVelocityAttr().Set(150)
# right_wheel_drive.GetTargetVelocityAttr().Set(150)

# Set the drive damping, which controls the strength of the velocity drive
# left_wheel_drive.GetDampingAttr().Set(15000)
# right_wheel_drive.GetDampingAttr().Set(15000)

# Set the drive stiffness, which controls the strength of the position drive
# In this case because we want to do velocity control this should be set to zero
# left_wheel_drive.GetStiffnessAttr().Set(0)
# right_wheel_drive.GetStiffnessAttr().Set(0)

# dynamic control can also be used to interact with the imported urdf.
dc = _dynamic_control.acquire_dynamic_control_interface()

# Start simulation
omni.timeline.get_timeline_interface().play()
# perform one simulation step so physics is loaded and dynamic control works.
kit.update()
art = dc.get_articulation(stage_path)

if art == _dynamic_control.INVALID_HANDLE:
    print(f"{stage_path} is not an articulation")
else:
    print(f"Got articulation {stage_path} with handle {art}")

# perform simulation
for frame in range(100):
    kit.update()

# Shutdown and exit
omni.timeline.get_timeline_interface().stop()
kit.close()

