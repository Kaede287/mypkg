#SPDX-FileCopyrightText: 2023 Kaede Ichikawa
#SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import math

def cb(msg):

    global node
    time = 2000 - msg.data


    
    if time % 2 == 0:
        node.get_logger().info("Listen: %d 偶数です" % time)

    else:
        node.get_logger().info("Listen: %d 奇数です" % time)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb,  10)
rclpy.spin(node)
