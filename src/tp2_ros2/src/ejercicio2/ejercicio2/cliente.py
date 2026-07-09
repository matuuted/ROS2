import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from ejercicio2_interfaces.action import Data


class Cliente(Node):

    def __init__(self):
        super().__init__('cliente')
        self.declare_parameter('texto', 'Lorem ipsum dolor sit amet')
        self.action_client = ActionClient(self, Data, 'republicar_texto')

    def send_goal(self):
        texto = self.get_parameter('texto').value
        goal_msg = Data.Goal()
        goal_msg.texto = texto

        self.action_client.wait_for_server()
        future = self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        future.add_done_callback(self.goal_response_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(feedback_msg.feedback.palabra)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.result_callback)

    def result_callback(self, future):
        result = future.result().result
        if result.exito:
            self.get_logger().info('Texto republicado!')


def main(args=None):
    rclpy.init(args=args)
    node = Cliente()
    node.send_goal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
