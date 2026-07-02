import math
from scipy.spatial.transform import Rotation as R

def map_full_folding_dataset_sample_to_openarm_v1_mujoco_qpos(sample):
  actual_state = sample["observation.state"]
  return [
    math.radians(actual_state[8]),  # left_joint_1.pos
    math.radians(actual_state[9]),  # left_joint_2.pos
    math.radians(actual_state[10]), # left_joint_3.pos
    math.radians(actual_state[11]), # left_joint_4.pos
    math.radians(actual_state[12]), # left_joint_5.pos
    math.radians(actual_state[13]), # left_joint_6.posj
    math.radians(actual_state[14]), # left_joint_7.pos
    -actual_state[15] / 1000, # left_gripper.pos
    -actual_state[15] / 1000, # left_gripper.pos
    math.radians(actual_state[0]), # right_joint_1.pos
    math.radians(actual_state[1]), # right_joint_2.pos
    math.radians(actual_state[2]), # right_joint_3.pos
    math.radians(actual_state[3]), # right_joint_4.pos
    math.radians(actual_state[4]), # right_joint_5.pos
    math.radians(actual_state[5]), # right_joint_6.pos
    math.radians(actual_state[6]), # right_joint_7.pos
    -actual_state[7] / 1000, # right_gripper.pos
    -actual_state[7] / 1000, # right_gripper.pos
  ]

def map_full_folding_dataset_sample_to_openarm_v2_mujoco_qpos(sample):
  actual_state = sample["observation.state"]

  # Left arm wrist conversion (assuming sample is for OpenArm v1)
  q5_l = math.radians(actual_state[12])
  q6_l = math.radians(actual_state[13])
  q7_l = math.radians(actual_state[14])
  r_left = R.from_euler('zxy', [q5_l, q6_l, -q7_l])
  euler_left = r_left.as_euler('zyx')
  qp5_l = -euler_left[0]
  qp6_l = -euler_left[1]
  qp7_l = euler_left[2]

  # Left gripper mapping (converting mm to rad range [-0.7854, 0])
  left_g_dist = -actual_state[15] / 1000.0
  left_g_dist = max(0.0, min(0.044, left_g_dist))
  left_g_angle = -0.7854 * (1.0 - left_g_dist / 0.044)

  # Right arm wrist conversion (assuming sample is for OpenArm v1)
  q5_r = math.radians(actual_state[4])
  q6_r = math.radians(actual_state[5])
  q7_r = math.radians(actual_state[6])
  r_right = R.from_euler('zxy', [q5_r, q6_r, q7_r])
  euler_right = r_right.as_euler('zyx')
  qp5_r = -euler_right[0]
  qp6_r = euler_right[1]
  qp7_r = euler_right[2]

  # Right gripper mapping (converting mm to rad range [-0.7854, 0])
  right_g_dist = -actual_state[7] / 1000.0
  right_g_dist = max(0.0, min(0.044, right_g_dist))
  right_g_angle = -0.7854 * (1.0 - right_g_dist / 0.044)

  return [
    math.radians(actual_state[8]),  # left_joint_1.pos
    math.radians(actual_state[9]),  # left_joint_2.pos
    math.radians(actual_state[10]), # left_joint_3.pos
    math.radians(actual_state[11]), # left_joint_4.pos
    qp5_l,                          # left_joint_5.pos
    qp6_l,                          # left_joint_6.pos
    qp7_l,                          # left_joint_7.pos
    left_g_angle,                   # left_gripper.pos
    left_g_angle,                   # left_gripper.pos
    math.radians(actual_state[0]),  # right_joint_1.pos
    math.radians(actual_state[1]),  # right_joint_2.pos
    math.radians(actual_state[2]),  # right_joint_3.pos
    math.radians(actual_state[3]),  # right_joint_4.pos
    qp5_r,                          # right_joint_5.pos
    qp6_r,                          # right_joint_6.pos
    qp7_r,                          # right_joint_7.pos
    right_g_angle,                  # right_gripper.pos
    right_g_angle,                  # right_gripper.pos
  ]

