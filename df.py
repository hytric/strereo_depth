import cv2
import numpy as np

dis = np.random.rand(100, 1000)
disparity = np.array(dis, dtype=np.float32) # 여기서 변환
rows, columns = disparity.shape
temp = np.ones(shape=(1,rows), dtype=np.float32)
line = (temp @ disparity).argmax()
cv2.line(disparity,(line, 0), (line, rows), (255, 255, 0), thickness=10, lineType=cv2.LINE_AA)
cv2.imshow('disparity', disparity)
cv2.waitKey(0)
cv2.destroyAllWindows()