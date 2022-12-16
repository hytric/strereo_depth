#!/usr/bin/python
# -*- coding: utf-8 -*-

# First import the library
import pyrealsense2 as rs
import numpy as np
import cv2

# setup opencv stereo
minDisp = 0
numDisp = 64 - minDisp
windowSize = 5
stereo = cv2.StereoSGBM_create(
    minDisparity = minDisp,
    numDisparities = numDisp,
    blockSize = 16,
    P1 = 8*3*windowSize**2,
    P2 = 32*3*windowSize**2,
    disp12MaxDiff = 1,
    uniquenessRatio = 10,
    speckleWindowSize = 100,
    speckleRange = 32
)

# Declare RealSense pipeline, encapsulating the actual device and sensors
pipe = rs.pipeline()

# Build config object and request pose data
cfg = rs.config()
cfg.enable_stream(rs.stream.fisheye, 1)
cfg.enable_stream(rs.stream.fisheye, 2)

# Start streaming with requested config
pipe.start(cfg)
print('press q to quit this program')
p = 0

try:
    while True:
        # Wait for the next set of frames from the camera
        frames = pipe.wait_for_frames()

        # Get images
        # fisheye 1: left, 2: right
        fisheye_left_frame = frames.get_fisheye_frame(1)
        fisheye_right_frame = frames.get_fisheye_frame(2)
        fisheye_left_image = np.asanyarray(fisheye_left_frame.get_data())
        fisheye_right_image = np.asanyarray(fisheye_right_frame.get_data())

        # Calculate disparity
        width = fisheye_left_frame.get_width()
        height = fisheye_left_frame.get_height()
        x1 = int(width/3 - numDisp / 2)
        x2 = int(width*2/3 + numDisp / 2)
        y1 = int(height/3)
        y2 = int(height*2/3)
        rect_left_image = fisheye_left_image[y1:y2, x1:x2]
        rect_right_image = fisheye_right_image[y1:y2, x1:x2]
        disparity = stereo.compute(rect_left_image, rect_right_image).astype(np.float32)/16

        max_dis = 0
        for i in range(10):
            for j in range(10)
                if max_dis < disparity[i-5][j-5]:
                    max_dis = disparity[i-5][j-5]
        
        disparity = (disparity - minDisp) / numDisp

        # object center detecting
        rows, columns = disparity.shape
        temp = np.ones(shape=(1, rows), dtype=np.float32)
        line1 = (temp @ disparity).argmax()

        temp = np.ones(shape=(columns, 1), dtype=np.float32)
        line2 = (disparity @ temp).argmax()
        
        # Display images
        cv2.rectangle(fisheye_left_image, (x1, y1), (x2, y2), (255,255,255), 5)
        cv2.rectangle(fisheye_right_image, (x1, y1), (x2, y2), (255,255,255), 5)
        cv2.line(disparity,(line1, 0), (line1, rows), (255, 255, 0), thickness=10, lineType=cv2.LINE_AA)
        cv2.line(disparity,(0, line2), (columns, line2), (255, 255, 0), thickness=10, lineType=cv2.LINE_AA)
        cv2.imshow('fisheye target', np.hstack((fisheye_left_image, fisheye_right_image)))
        cv2.imshow('disparity', disparity)

        print(max_dis)
        
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        
finally:
    pipe.stop()
