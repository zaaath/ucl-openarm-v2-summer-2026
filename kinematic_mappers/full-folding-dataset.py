import math

def map_full_folding_dataset_sample_to_openarm_v1_mujoco_qpos(sample):
  actual_state = sample["observation.state"]
  print("actual_state", actual_state)
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
  print("actual_state", actual_state)
  return [
    math.radians(actual_state[8]),  # left_joint_1.pos
    math.radians(actual_state[9]),  # left_joint_2.pos
    math.radians(actual_state[10]), # left_joint_3.pos
    math.radians(actual_state[11]), # left_joint_4.pos
    math.radians(actual_state[12]), # left_joint_5.pos
    math.radians(actual_state[13]), # left_joint_6.pos
    -math.radians(actual_state[14]), # left_joint_7.pos
    -math.radians(actual_state[15]), # left_gripper.pos
    -math.radians(actual_state[15]), # left_gripper.pos
    math.radians(actual_state[0]), # right_joint_1.pos
    math.radians(actual_state[1]), # right_joint_2.pos
    math.radians(actual_state[2]), # right_joint_3.pos
    math.radians(actual_state[3]), # right_joint_4.pos
    math.radians(actual_state[4]), # right_joint_5.pos
    math.radians(actual_state[5]), # right_joint_6.pos
    -math.radians(actual_state[6]), # right_joint_7.pos
    math.radians(actual_state[7]), # right_gripper.pos
    math.radians(actual_state[7]), # right_gripper.pos
  ]
