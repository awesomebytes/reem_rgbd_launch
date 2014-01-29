#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Jan 28 21:39:00 2014

@author: Sam Pfeiffer

Set openni dynamic params for the Asus Xtion of REEM.
We must lower the quantity of data sent.


"""

import rospy
from dynamic_reconfigure import client


if __name__=='__main__':
    rospy.init_node("set_xtion_dyn_params", anonymous=True)
    rospy.loginfo("Trying to connect a service client to head_mount_xtion dynamic reconfigure...")
    client = client.Client("/head_mount_xtion/driver") # xtion node
    rospy.loginfo("Got a client! Setting parameters.")
    params = { 'data_skip' : 10, 'ir_mode' : 6, 'color_mode': 6, 'depth_mode' : 6 } # drop rate
    config = client.update_configuration(params)
    # check if it was really set
    
    rospy.loginfo("Parameters set: " + str(config))

