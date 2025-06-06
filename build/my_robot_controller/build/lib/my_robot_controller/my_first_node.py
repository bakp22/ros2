#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node): # inherited Node from ros2

    def __init__(self):
        super().__init__("first_node")
        self.get_logger().info("Hello from Beren")


def main(args=None):

    # everything you write is between these two lines (
    rclpy.init(args=args)

    node = MyNode()
    rclpy.spin(node) # Node kept alive until you kill it 

    rclpy.shutdown

if __name__ == "__main__":
    main()
