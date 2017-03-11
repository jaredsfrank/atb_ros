#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Point
import nav
import numpy as np
from std_msgs.msg import Int32MultiArray


def callback(data):
    new_nav.map_model.bike.xy_coord = (data.x, data.y)
    new_nav.map_model.bike.direction = data.z

def path_parse(data):
    d = np.array(data.data).reshape(len(data.data)/4, 2, 2)
    new_map.paths = d

def talker():
    pub = rospy.Publisher('dir_to_turn', String, queue_size=10)
    rospy.init_node('navigation', anonymous=True)
    rospy.Subscriber("bike_pos", Point, callback)
    rospy.Subscriber("paths", Int32MultiArray, path_parse)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        rospy.loginfo(new_nav.direction_to_turn())
        new_map = new_nav.map_model
        pub.publish(str(new_nav.direction_to_turn()))
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.loginfo('here')
        new_bike = nav.Bike((1,10), np.radians(0), .02)
        new_map = nav.Map_Model(new_bike, [[],[]], [])
        new_nav = nav.Nav(new_map)
        talker()
    except rospy.ROSInterruptException:
        rospy.loginfo('here')
        pass
