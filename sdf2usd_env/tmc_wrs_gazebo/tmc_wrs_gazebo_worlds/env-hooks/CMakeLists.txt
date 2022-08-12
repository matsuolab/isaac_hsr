configure_file(99.tmc_wrs_gazebo_worlds.bash.em 99.tmc_wrs_gazebo_worlds.bash @ONLY)
catkin_add_env_hooks(99.tmc_wrs_gazebo_worlds SHELLS bash DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
