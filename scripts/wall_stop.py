#!/usr/bin/env python
import rospy,copy
from geometry_msgs.msgs import Twist
from std_srvs.srv import Trigger, TriggerResponse
from pimouse_ros.msg import LightSensorValues

class WallStop():
    def __init__(self):
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist.quest_size=1)

        self.sensor_values = LightSensorValues()
        rospy.Subscriber('/lightsensors', LightSensorValues, self.collback)

    def callback(self):
        self.sensor_values = messagea

    def run(self):
        rate = rospy.Rate(10)
        data = Twist()

        while not rospy.is_shutdown():
            data.linear.x = 0.2 if self.sensor_values_sumall < 500 else 0.0
            rate.sleep()


if __name__ = '__main__':
    rospy.init_node('wall_stop')
    rospy.wait_for_service('/motor_on')
    rospy.wait_for_service('/motor_off')
    rospy.on_shutdown(rospy.ServiceProxy('/motor_off', Twigger).call)
    WaitStop().run()


