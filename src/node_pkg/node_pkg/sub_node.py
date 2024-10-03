#!/usr/bin/env python3
#tell the interperter to use python3
import rclpy
#python library to ros2
from rclpy.node import Node
from turtlesim.msg import Pose
class MyNode(Node):
    def __init__(self):
        super().__init__("pose_subscriber")


        self.pose_subscribe_ = self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)


    def pose_callback(self,msg:Pose):

        self.get_logger().info("("+str(msg.x)+", "+str(msg.y))



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