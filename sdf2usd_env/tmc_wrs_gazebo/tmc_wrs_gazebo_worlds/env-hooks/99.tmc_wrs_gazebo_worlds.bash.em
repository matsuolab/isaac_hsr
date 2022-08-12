function tmc_wrs_gazebo_worlds_setup {
    @[if INSTALLSPACE]@
    local model_path=@(CMAKE_INSTALL_PREFIX)/@(CATKIN_PACKAGE_SHARE_DESTINATION)/models
    @[else]@
    local model_path=@(PROJECT_SOURCE_DIR)/models
    @[end if]@

    if [ -z $GAZEBO_MODEL_PATH ]
    then
        export GAZEBO_MODEL_PATH=$model_path
    else
        export GAZEBO_MODEL_PATH=$model_path:$GAZEBO_MODEL_PATH
    fi
}
tmc_wrs_gazebo_worlds_setup
