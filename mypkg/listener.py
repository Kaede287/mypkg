import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    time = 10000 - msg.data
    node.get_logger().info("Listen: %d" % time)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb,  10)
rclpy.spin(node)

