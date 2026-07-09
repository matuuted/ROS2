from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('texto', default_value='Lorem ipsum dolor sit amet'),

        Node(
            package='ejercicio2',
            executable='servidor',
            name='servidor',
            output='screen',
        ),
        Node(
            package='ejercicio2',
            executable='cliente',
            name='cliente',
            output='screen',
            parameters=[{'texto': LaunchConfiguration('texto')}],
        ),
    ])
