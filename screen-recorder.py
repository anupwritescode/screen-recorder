# importing the required packages
import pyautogui
import cv2
import numpy as np
import ctypes

width = ctypes.windll.user32.GetSystemMetrics(0)
height = ctypes.windll.user32.GetSystemMetrics(1)

# Specify resolution
resolution = (width, height)

codec = cv2.VideoWriter_fourcc(*"mp4v")

filename = "Recording.mp4"

fps = 20.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot()

    frame = np.array(img)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    out.write(frame)
    
    cv2.imshow('Live', frame)
    
    if cv2.waitKey(50) == ord('q'):
        break        

out.release()

cv2.destroyAllWindows()
