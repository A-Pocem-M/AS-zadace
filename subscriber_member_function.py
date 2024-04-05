

import rclpy
from rclpy.node import Node
from rclpy.publisher import Publisher
from std_msgs.msg import Int32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'broj',
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(Int32, 'kvadrat_broja', 10)

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        squared_number = msg.data * msg.data
        self.publish_squared_number(squared_number)

    def publish_squared_number(self, number):
        msg = Int32()
        msg.data = number
        self.publisher.publish(msg)
        self.get_logger().info('Objavljujem kvadrat broja: "%s"' % msg.data)
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
