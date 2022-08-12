cmake_minimum_required(VERSION 2.8.3)
project(tmc_wrs_gazebo_worlds)

find_package(catkin REQUIRED)
find_package(xacro REQUIRED)

catkin_package(
)

file(GLOB _world_xacros "${PROJECT_SOURCE_DIR}/worlds/*.world.xacro")
file(GLOB_RECURSE _component_xacros "${PROJECT_SOURCE_DIR}/worlds/include/*.xacro")

# Generate world files from each *.world.xacro files.
foreach(_xacro ${_world_xacros})
    get_filename_component(_dir ${_xacro} PATH)
    get_filename_component(_name ${_xacro} NAME_WE)

    set(_default_world ${_dir}/${_name}.world)
    set(_default_highrtf_world ${_dir}/${_name}_highrtf.world)
    set(_fast_world ${_dir}/${_name}_fast.world)
    set(_fast_highrtf_world ${_dir}/${_name}_fast_highrtf.world)

    set(_default_knob_world ${_dir}/${_name}_knob.world)
    set(_default_highrtf_knob_world ${_dir}/${_name}_highrtf_knob.world)
    set(_fast_knob_world ${_dir}/${_name}_fast_knob.world)
    set(_fast_highrtf_knob_world ${_dir}/${_name}_fast_highrtf_knob.world)

    add_custom_command(
        OUTPUT ${_default_world}
        DEPENDS ${_xacro} ${_component_xacros}
        COMMAND ${CATKIN_DEVEL_PREFIX}/env.sh rosrun xacro xacro ${_xacro} fast_physics:=false highrtf:=false trofast_knob:=false > ${_default_world})
    add_custom_command(
        OUTPUT ${_default_highrtf_world}
        DEPENDS ${_xacro} ${_component_xacros}
        COMMAND ${CATKIN_DEVEL_PREFIX}/env.sh rosrun xacro xacro ${_xacro} fast_physics:=false highrtf:=true trofast_knob:=false > ${_default_highrtf_world})
    add_custom_command(
        OUTPUT ${_fast_world}
        DEPENDS ${_xacro} ${_component_xacros}
        COMMAND ${CATKIN_DEVEL_PREFIX}/env.sh rosrun xacro xacro ${_xacro} fast_physics:=true highrtf:=false trofast_knob:=false > ${_fast_world})
    add_custom_command(
        OUTPUT ${_fast_highrtf_world}
        DEPENDS ${_xacro} ${_component_xacros}
        COMMAND ${CATKIN_DEVEL_PREFIX}/env.sh rosrun xacro xacro ${_xacro} fast_physics:=true highrtf:=true trofast_knob:=false > ${_fast_highrtf_world})
    add_custom_target(${PROJECT_NAME}_${_name}_gen_default_world ALL DEPENDS ${_default_world})
    add_custom_target(${PROJECT_NAME}_${_name}_gen_default_highrtf_world ALL DEPENDS ${_default_highrtf_world})
    add_custom_target(${PROJECT_NAME}_${_name}_gen_fast_world ALL DEPENDS ${_fast_world})
    add_custom_target(${PROJECT_NAME}_${_name}_gen_fast_highrtf_world ALL DEPENDS ${_fast_highrtf_world})

    add_custom_command(
        OUTPUT ${_default_knob_world}
        DEPENDS ${_xacro} ${_component_xacros}
        COMMAND ${CATKIN_DEVEL_PREFIX}/env.sh rosrun xacro xacro ${_xacro} fast_physics:=false highrtf:=false trofast_knob:=true > ${_default_knob_world})
    add_custom_command(
        OUTPUT ${_default_highrtf_knob_world}
        DEPENDS ${_xacro} ${_component_xacros}
        COMMAND ${CATKIN_DEVEL_PREFIX}/env.sh rosrun xacro xacro ${_xacro} fast_physics:=false highrtf:=true trofast_knob:=true > ${_default_highrtf_knob_world})
    add_custom_command(
        OUTPUT ${_fast_knob_world}
        DEPENDS ${_xacro} ${_component_xacros}
        COMMAND ${CATKIN_DEVEL_PREFIX}/env.sh rosrun xacro xacro ${_xacro} fast_physics:=true highrtf:=false trofast_knob:=true > ${_fast_knob_world})
    add_custom_command(
        OUTPUT ${_fast_highrtf_knob_world}
        DEPENDS ${_xacro} ${_component_xacros}
        COMMAND ${CATKIN_DEVEL_PREFIX}/env.sh rosrun xacro xacro ${_xacro} fast_physics:=true highrtf:=true trofast_knob:=true > ${_fast_highrtf_knob_world})
    add_custom_target(${PROJECT_NAME}_${_name}_gen_default_knob_world ALL DEPENDS ${_default_knob_world})
    add_custom_target(${PROJECT_NAME}_${_name}_gen_default_highrtf_knob_world ALL DEPENDS ${_default_highrtf_knob_world})
    add_custom_target(${PROJECT_NAME}_${_name}_gen_fast_knob_world ALL DEPENDS ${_fast_knob_world})
    add_custom_target(${PROJECT_NAME}_${_name}_gen_fast_highrtf_knob_world ALL DEPENDS ${_fast_highrtf_knob_world})
endforeach()

# set environment variable GAZEBO_MODEL_PATH
add_subdirectory(env-hooks)

install(
  DIRECTORY scripts/
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  USE_SOURCE_PERMISSIONS
  FILES_MATCHING
  PATTERN "scripts/*"
)

install(DIRECTORY
  models
  maps
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(
  DIRECTORY worlds
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  FILES_MATCHING PATTERN "*.world"
  PATTERN "include" EXCLUDE
)
