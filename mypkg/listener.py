import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):

    global node
    
    if msg.data >= 1500:

        node.get_logger().info('1500に到達しました %d' % msg.data)

    else:

        time = 2000 - msg.data
        node.get_logger().info("Listen: %d" % time)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb,  10)
rclpy.spin(node)
