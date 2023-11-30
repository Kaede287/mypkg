import rclpy
from rclpy.node import Node
from std_msgs.msg import person

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Person, "countup", cb, 10)
rclpy.spin(node)
