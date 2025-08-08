import cv2

#define the tracker
tracker_type = "csrt"
tracker = cv2.legacy.TrackerCSRT_create()

#Load the video from file or webcam
video = cv2.VideoCapture(0)   #Use O for webcame and replace with video.mp4

#Read the first frame
ret,frame = video.read()
if not ret:
    print("Failed to read the video")
    exit()

#Make bbox on top of the image
bbox = cv2.selectROI("Select Object",frame,fromCenter=False,showCrosshair=True)
cv2.destroyWindow("Select Object")

#Initilize the tracker with the first frame and selected bbox
tracker.init(frame,bbox)

while True:
    ret,frame = video.read()
    if not ret:
        break

    #Update tracker
    success, bbox = tracker.update(frame)

    #Draw bbox
    if success:
        x,y,w,h = [int(v) for v in bbox]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2,1)
        cv2.putText(frame,"Tracking",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
    else:
        cv2.putText(frame,"Lost",(50,80),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,255),2)

    #Display result
    cv2.imshow("Object Tracking", frame)

    #Exit with ESC
    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()