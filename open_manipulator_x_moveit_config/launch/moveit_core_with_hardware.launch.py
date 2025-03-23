#!/usr/bin/env python3
# Author: JWNY2105

import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    ld = LaunchDescription()
    hardware_launch_dir = os.path.join(
        get_package_share_directory(
            'open_manipulator_x_bringup'), 'launch')

    moveit_launch_dir = os.path.join(
        get_package_share_directory(
            'open_manipulator_x_moveit_config'), 'launch')

    # Hardware
    hardware_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([hardware_launch_dir, '/hardware.launch.py'])
    )
    ld.add_action(hardware_launch)

    # RViz
    rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([moveit_launch_dir, '/moveit_rviz.launch.py'])
    )
    ld.add_action(rviz_launch)

    # move_group
    move_group_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([moveit_launch_dir, '/move_group.launch.py'])
    )
    ld.add_action(move_group_launch)

    return ld
