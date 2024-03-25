from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_services_pkg',
            executable='service_client_node_oop',
            output='screen'),
    ])