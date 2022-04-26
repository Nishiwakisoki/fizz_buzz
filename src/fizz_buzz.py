#!/usr/bin/env python
# BEGIN ALL
#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
import math

class fizz_buzz_node:
    def __init__(self):
        self.count_sub = rospy.Subscriber("/counter", Int32,self.fizz_buzz_callback)
        #pub1.header.frame_id = "velodyne"
        self.count_pub = rospy.Publisher("/fizz_buzz", Int32, queue_size = 10)

    def fizz_buzz_callback(self, msg):
        #rospy.init_node("approximation")
        a = msg.data
        if (a % 3 == 0) and (a % 5 == 0):
            rospy.loginfo("FizzBuzz")
        elif (a % 3) == 0:
            rospy.loginfo("Fizz")
        elif (a % 5) == 0:
            rospy.loginfo("Buzz")
        else:
            rospy.loginfo(a)
            self.count_pub.publish(a)
        # while not rospy.is_shutdown():
        rate = rospy.Rate(10)
        rate.sleep()


if __name__ == '__main__':
    try:
        rospy.init_node("fizz_buzz_node", anonymous=True)
        fizz_buzz_node=fizz_buzz_node()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass