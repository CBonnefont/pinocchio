import unittest
import pinocchio as se3
import numpy as np
from pinocchio.utils import eye,zero,rand
from pinocchio.robot_wrapper import RobotWrapper
from os.path import join
import os

ones = lambda n: np.matrix(np.ones([n, 1] if isinstance(n, int) else n), np.double)

class TestFrameBindings(unittest.TestCase):

    v3zero = zero(3)
    v6zero = zero(6)
    v3ones = ones(3)
    m3zero = zero([3,3])
    m6zero = zero([6,6])
    m3ones = eye(3)
    m4ones = eye(4)

    PKG = '/opt/openrobots/share'
    URDF = join(PKG, 'romeo_description/urdf/romeo.urdf')
    robot = RobotWrapper(URDF, [PKG])

    def test_type_get_set(self):
        f = self.robot.model.frames[5]
        self.assertTrue(f.type == se3.FrameType.JOINT)
        f.type = se3.FrameType.BODY
        self.assertTrue(f.type == se3.FrameType.BODY)

    def test_name_get_set(self):
        f = self.robot.model.frames[5]
        self.assertTrue(f.name == 'LHipYaw')
        f.name = 'new_hip_frame'
        self.assertTrue(f.name == 'new_hip_frame')

    def test_parent_get_set(self):
        f = self.robot.model.frames[5]
        self.assertTrue(f.parent == 2)
        f.parent = 5
        self.assertTrue(f.parent == 5)

    def test_placement_get_set(self):
        m = se3.SE3(self.m3ones, np.array([0,0,0],np.double))
        new_m = se3.SE3(rand([3,3]), rand(3))
        f = self.robot.model.frames[2]
        self.assertTrue(np.allclose(f.placement.homogeneous, m.homogeneous))
        f.placement = new_m
        self.assertTrue(np.allclose(f.placement.homogeneous, new_m.homogeneous))


