#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from custom_interfaces.msg import BatteryState
from custom_interfaces.srv import SetLED


class LEDPanelServerNode(Node):
    def __init__(self):
        super().__init__("set_led_server")
        self.led_state_ = [0, 0, 0]
        self.led_state_publisher = self.create_publisher(BatteryState, "led_state", 10)
        self.led_state_timer = self.create_timer(4, self.publish_led_state)

        self.set_led_service = self.create_service(
            SetLED, "set_led", self.callback_set_led
        )

        self.get_logger().info("LED panel has been started...")

    def publish_led_state(self):
        msg = BatteryState()
        msg.led_state = self.led_state_
        self.led_state_publisher.publish(msg)

    def callback_set_led(self, request, response):
        led_number = request.led_number
        state = request.state
        
        if led_number > len(self.led_state_) or led_number <= 0:
            response.succsess = False
            response.message = "ERROR! Led NUMBER is not valid!"
            return response
        
        if state != 0 and state != 1:
            response.succsess = False
            response.message = "ERROR! Led STATE is not valid!"
            return response
            
        self.led_state_[led_number - 1] = state
        response.succsess = True
        response.message = "DONE"
        self.publish_led_state()
        return response
        


def main(args=None):
    rclpy.init(args=args)
    node = LEDPanelServerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
