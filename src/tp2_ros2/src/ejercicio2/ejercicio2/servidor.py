import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from ejercicio2_interfaces.action import Data


class Servidor(Node):

    def __init__(self):
        super().__init__('servidor')
        self.action_server = ActionServer(self, Data, 'republicar_texto', self.execute_callback)

    def execute_callback(self, goal_handle):
        texto = goal_handle.request.texto
        self.get_logger().info(f'Republicando: {texto}')

        palabras = texto.split()
        feedback = Data.Feedback()

        for palabra in palabras:
            feedback.palabra = palabra
            goal_handle.publish_feedback(feedback)
            time.sleep(1.0)

        goal_handle.succeed()

        result = Data.Result()
        result.exito = True
        result.mensaje = 'Texto republicado!'
        return result


def main(args=None):
    rclpy.init(args=args)
    node = Servidor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
