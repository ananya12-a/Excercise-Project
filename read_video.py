import cv2
import numpy as np

def printt():
    print("Hello World")
    return

#printt()

def read_video(link):
    cap = cv2.VideoCapture(link)
    print ("read")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.imshow('frame', gray)
            # & 0xFF is required for a 64-bit system
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
print("Enter the link of the video")
#zoom_0 (1).mp4
link = input()
#read_video(link)

def read_video_red(link):
    cap = cv2.VideoCapture(link)
    print ("read")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_red = np.array([169, 100, 100]) #[161, 155, 84]
            upper_red = np.array([189, 255, 255]) #[179, 255, 255]
            mask = cv2.inRange(color, lower_red, upper_red)
            res = cv2.bitwise_and(frame,frame, mask= mask)
            cv2.imshow('frame', mask)
            LUV = cv2.cvtColor(res, cv2.COLOR_BGR2LUV)
            edges = cv2.Canny(LUV, 10, 100)
            contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            print("Number of Contours is: " + str(len(contours)))
            print(contours)
            print(hierarchy)
            cv2.imshow('Contours', image)
            cv2.waitKey(0)
            # & 0xFF is required for a 64-bit system
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

#def get_cordinates()
read_video_red(link)
#cvtColor()

#video1: IMG_4229.mov
#video2: IMG_4230.mov
#video3: IMG_4231.mov