cmake_minimum_required(VERSION 3.8)
project(ros2_services_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_srvs REQUIRED)
find_package(geometry_msgs REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)

  ament_lint_auto_find_test_dependencies()
endif()

add_executable(service_client_node_basic src/service_client_example_1.cpp)
ament_target_dependencies(service_client_node_basic rclcpp std_srvs)

add_executable(service_client_node_oop src/service_client_example_2.cpp)
ament_target_dependencies(service_client_node_oop rclcpp std_srvs)

add_executable(service_server_node src/service_server_example_1.cpp)
ament_target_dependencies(service_server_node rclcpp geometry_msgs std_srvs)

add_executable(service_server_node2 src/service_server_example_2.cpp)
ament_target_dependencies(service_server_node2 rclcpp geometry_msgs std_srvs)


install(TARGETS
   service_client_node_basic
   service_client_node_oop
   service_server_node
   service_server_node2
   DESTINATION lib/${PROJECT_NAME}
 )

# Install launch files.
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
