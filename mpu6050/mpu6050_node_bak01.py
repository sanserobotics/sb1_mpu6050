import mpu6050
import time

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        # Create a new Mpu6050 object
        self.mpu6050 = mpu6050.mpu6050(0x68)

    def timer_callback(self):
        # Read the accelerometer values
#        accelerometer_data = self.mpu6050.get_accel_data()
        # Read the gyroscope values
#        gyroscope_data = self.mpu6050.get_gyro_data()
        # Read temp 
#        temperature = self.mpu6050.get_temp()
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):

    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
