#!/usr/bin/env python3
#tell the interperter to use python3
import rclpy
#python library to ros2
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
class MyNode(Node):
    def __init__(self):
        super().__init__("pub_sub")
        self.cmd_vel_publisher_ = self.create_publisher(
            Twist ,"/turtle1/cmd_vel",10)
        self.pose_subscriber_ = self.create_subscription(
            Pose,"/turtle1/pose",self.pose_callback,10)
        #send massege when the node is activated
        self.get_logger().info("node has been activated")
    def pose_callback(self ,pose:Pose):
        cmd =Twist()
        if pose.x >9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            cmd.linear.x = 1.0
            cmd.angular.z = 0.9
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        self.cmd_vel_publisher_.publish(cmd)
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