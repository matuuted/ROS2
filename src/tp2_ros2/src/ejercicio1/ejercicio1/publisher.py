import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_srvs.srv import Trigger


class Publisher(Node):

    def __init__(self):
        super().__init__('publisher')

        self.declare_parameter('frecuencia', 5.0)
        self.declare_parameter('cantidad_maxima', 1000)

        frecuencia = self.get_parameter('frecuencia').value
        self.cantidad_maxima = self.get_parameter('cantidad_maxima').value

        self.contador = 0
        self.pub = self.create_publisher(Int32, 'contador', 10)
        self.timer = self.create_timer(1.0 / frecuencia, self.timer_callback)
        self.srv = self.create_service(Trigger, 'reset_counter', self.reset_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = self.contador
        self.pub.publish(msg)
        self.get_logger().info(f'Publicando: {self.contador}')

        self.contador += 1
        if self.contador > self.cantidad_maxima:
            self.contador = 0

    def reset_callback(self, request, response):
        self.get_logger().info('Reseteando contador')
        self.contador = 0
        response.success = True
        response.message = 'Contador reiniciado'
        return response


def main(args=None):
    rclpy.init(args=args)
    node = Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()