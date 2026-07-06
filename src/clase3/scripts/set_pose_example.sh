ros2 topic pub --once /goal_pose geometry_msgs/msg/PoseStamped "
header:
  frame_id: 'base_link'
pose:
  position:
    x: 0.0
    y: 0.4
    z: 0.1
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0
"
