#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Point
import time
import random 
import matplotlib
import matplotlib.pyplot as plt
import simulator
import nav
import numpy as np
from matplotlib import collections  as mc
from std_msgs.msg import Int32MultiArray


def update_graph(data):
    bike_sim.update_bike()
    dir_to_turn = int(float(data.data))
    if dir_to_turn == 0:
        bike_sim.move_straight()
    else:
        bike_sim.rotate(dir_to_turn, bike_sim.bike.turning_r)
    
def path_parse(data):
    d = np.array(data.data).reshape(len(data.data)/4, 2, 2)
    map_model.paths = d

def listener():
    pub = rospy.Publisher('bike_pos', Point)
    rospy.init_node('simulator', anonymous=True)
    rospy.Subscriber("dir_to_turn", String, update_graph)
    rospy.Subscriber("paths", Int32MultiArray, path_parse)
    rate = rospy.Rate(100)
    rospy.loginfo(rospy.is_shutdown())
    while not rospy.is_shutdown():
        pub.publish(bike_sim.x, bike_sim.y, bike_sim.theta)
        rate.sleep()
    

if __name__ == '__main__':
    new_bike = nav.Bike((1,8), np.radians(0), .02)
    map_model = nav.Map_Model(new_bike, [[],[]], [])
    bike_sim = simulator.bike_sim(map_model.bike)
    listener()