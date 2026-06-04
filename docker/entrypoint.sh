#!/bin/bash
set -e

source /opt/ros/${ROS_DISTRO}/setup.bash

if [ -d "/root/ros2_ws/src" ] && [ "$(ls -A /root/ros2_ws/src 2>/dev/null)" ]; then
  echo "[entrypoint] Compilando workspace..."
  cd /root/ros2_ws
  rosdep install --from-paths src --ignore-src -y --rosdistro ${ROS_DISTRO} 2>/dev/null || true
  colcon build --symlink-install
  source /root/ros2_ws/install/setup.bash
elif [ -f "/root/ros2_ws/install/setup.bash" ]; then
  source /root/ros2_ws/install/setup.bash
else
  echo "[entrypoint] Workspace vacío — montá src/ como volumen para compilar"
fi

exec "$@"