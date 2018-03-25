import cv2
a = 1
co = 0
if  a !=0:
    vidcap1 = cv2.VideoCapture("/scratch/anuj.rathore/cvit_vid/VID_20180320_201516.mp4")
    vidcap2 = cv2.VideoCapture("/scratch/anuj.rathore/cvit_vid/VID_20180320_201516.mp4")
    success,frame1 = vidcap1.read()
    success,frame2 = vidcap2.read()
    success,frame2 = vidcap2.read()
    
    while success:
        success,frame1 = vidcap1.read()
        success,frame2 = vidcap2.read()
        print frame1.shape
        print frame2.shape
        co +=1
        print co
