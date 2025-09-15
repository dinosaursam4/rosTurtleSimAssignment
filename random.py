import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.time = 0

    def create_twist(self, linear_x, angular_z):
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        return msg

    def get_twist_msg(self):
        # draws the rectangle shape, then draws the diamond shape
        if self.time < 5:
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 5 and self.time < 7:
            msg = self.create_twist(0.0, 1.6)
        elif self.time >= 7 and self.time < 10:
            msg = self.create_twist(0.0, 0.0)
        elif self.time >= 10 and self.time < 15:
            msg = self.create_twist(2.0, 0.0)
        elif self.time >= 15 and self.time < 17:
            msg = self.create_twist(0.0, 1.6)
        elif self.time >= 17 and self.time < 22:
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 22 and self.time < 24:
            msg = self.create_twist(0.0, 1.5)
        elif self.time >= 24 and self.time < 29:
            msg = self.create_twist(2.0, 0.0)
        elif self.time >= 29 and self.time < 31:
            msg = self.create_twist(0.0, 0.0)
        elif self.time >= 31 and self.time < 34: 
            msg = self.create_twist(0.0, 0.8)
        elif self.time >= 36 and self.time < 41:
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 43 and self.time < 45: 
            msg = self.create_twist(0.0, 0.8)
        elif self.time >= 46 and self.time < 51:
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 53 and self.time < 55:
            msg = self.create_twist(0.0, 2.4)
        elif self.time >= 56 and self.time < 61: 
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 63 and self.time < 65: 
            msg = self.create_twist(0.0, 0.8)
        elif self.time >= 66 and self.time < 71: 
            msg = self.create_twist(1.0, 0.0)
        else:
            msg = self.create_twist(0.0, 0.0)

        return msg
    
    def timer_callback(self):
        msg = self.get_twist_msg()       
        self.publisher.publish(msg)
        self.time += 1
        print("time: {}".format(self.time))

def main(args=None):
    rclpy.init(args=args)

    turtle_controller = TurtleController()

    rclpy.spin(turtle_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()