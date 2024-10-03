#!/usr/bin/env python3
#tell the interperter to use python3
import rclpy
#python library to ros2
from rclpy.node import Node
from geometry_msgs.msg import Twist
class MyNode(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub_ = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.timer_ = self.create_timer(0.5,self.send_velocity_command)
        #send massege when the node is activated
        self.get_logger().info("hello from ros 2")
    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x=2.0
        msg.angular.z=1.0
        self.cmd_vel_pub_.publish(msg)
def main(args=None):
    #the args of init are equal of ags of main
    rclpy.init(args=args)
    #any think you want you rin here
    node=MyNode()
    rclpy.spin(node)
    #shutdonw your ros communication
    rclpy.shutdown()
#here to make the code excutable from the terminal
if __name__ == '__main__':
    main()