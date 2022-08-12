cmake_minimum_required(VERSION 2.8.3)
project(tmc_wrs_gazebo_launch)

find_package(catkin REQUIRED)
catkin_package(
)

install(
  DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  FILES_MATCHING
  PATTERN "*.launch"
)
install(DIRECTORY
  config
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

if (CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
  roslaunch_add_file_check(launch USE_TEST_DEPENDENCIES)
endif()

