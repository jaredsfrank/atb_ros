#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D
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
    bike_sim.set_xy(bike_sim.get_coordinates(data.x, data.y, data.theta))

    
def path_parse(data):
    d = np.array(data.data).reshape(len(data.data)/4, 2, 2)
    map_model.paths = d
    paths.unregister()
    lc = mc.LineCollection(map_model.paths, linewidths=2,
        color = "black")
    ax.add_collection(lc)
    plt.plot(d[:,:,0], d[:,:,1], 'ro')


def listener():
    rospy.init_node('sim', anonymous=True)
    rospy.Subscriber("bike_pos", Pose2D, update_graph)
    global paths
    paths = rospy.Subscriber("paths", Int32MultiArray, path_parse)
    rate = rospy.Rate(100)
    rospy.loginfo(rospy.is_shutdown())
    while not rospy.is_shutdown():
        plt.draw()
        plt.pause(1e-17)
        rate.sleep()
    

if __name__ == '__main__':
    new_bike = nav.Bike((1,8), np.radians(0), .02)
    map_model = nav.Map_Model(new_bike, [[],[]], [])
    map_model.add_path((0,9),(10,9))
    map_model.add_point((9,0))
    plt.show()

    fig = plt.figure()
    fig.set_dpi(100)
    ax = plt.axes(xlim=(0, 20), ylim=(0, 20))
    bike_sim = simulator.bike_sim(map_model.bike)
    ax.add_patch(bike_sim)
    listener()