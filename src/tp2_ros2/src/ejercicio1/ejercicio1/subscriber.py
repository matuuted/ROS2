import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_srvs.srv import Trigger


class Subscriber(Node):

    def __init__(self):
        super().__init__('subscriber')

        self.declare_parameter('reset_en', 50)
        self.reset_en = self.get_parameter('reset_en').value

        self.sub = self.create_subscription(Int32, 'contador', self.listener_callback, 10)
        self.cliente = self.create_client(Trigger, 'reset_counter')
        self.cliente.wait_for_service()

    def listener_callback(self, msg):
        self.get_logger().info(f'Recibido: {msg.data}')
        if msg.data >= self.reset_en:
            request = Trigger.Request()
            self.cliente.call_async(request)


def main(args=None):
    rclpy.init(args=args)
    node = Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
