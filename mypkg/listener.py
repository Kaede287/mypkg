import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):

    global node
    
    if msg.data >= 1800:

        node.get_logger().info('1800に到達しました %d' % msg.data)

    else:

        time = 2000 - msg.data
        node.get_logger().info("Listen: %d" % time)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb,  10)
rclpy.spin(node)git push origin main
