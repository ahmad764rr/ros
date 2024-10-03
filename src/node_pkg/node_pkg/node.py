#!/usr/bin/env python3
#tell the interperter to use python3
import rclpy
#python library to ros2
from rclpy.node import Node
class MyNode(Node):
    def __init__(self):
        super().__init__("node_name")
        #send massege when the node is activated
        self.get_logger().info("hello from ros 2")
def main(args=None):
    #the args of init are equal of ags of main
    rclpy.init(args=args)
    #any think you want you rin here
    node=MyNode()
    #shutdonw your ros communication
    rclpy.shutdown()
#here to make the code excutable from the terminal
if __name__ == '__main__':
    main()
