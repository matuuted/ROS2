from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('frecuencia', default_value='5.0'),
        DeclareLaunchArgument('reset_en', default_value='50'),

        Node(
            package='ejercicio1',
            executable='publisher',
            name='publisher',
            output='screen',
            parameters=[{'frecuencia': LaunchConfiguration('frecuencia')}],
        ),
        Node(
            package='ejercicio1',
            executable='subscriber',
            name='subscriber',
            output='screen',
            parameters=[{'reset_en': LaunchConfiguration('reset_en')}],
        ),
    ])
