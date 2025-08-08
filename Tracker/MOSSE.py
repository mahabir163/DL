import cv2

tracker_type = "mosse"
tracker = cv2.legacy.TrackerMOSSE_create()

video = cv2.VideoCapture(0)

ret,frame = video.read()
if not ret:
    print("Faild")
    exit()

bbox = cv2.selectROI("Select Obj",frame,fromCenter=False,showCrosshair=True)
cv2.destroyWindow("Select Obj")

tracker.init(frame,bbox)

while True:
    ret,frame = video.read()

    if not ret:
        break

    sucess,bbox = tracker.update(frame)

    if sucess:
        x,y,w,h = [int(v) for v in bbox]
        cv2.rectangle(frame,(x,y),(x+w,x+h),(0,255,0),2,1)
        cv2.putText(frame,"Tracking",(x,y-10),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.6,(0,255,0),2)
    else:
        cv2.putText(frame,"Lost",(50,80),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,255),2)
    
    cv2.imshow("Object Tracking",frame)

    key = cv2.waitKey(30) & 0xFF

    if key == 27:
        break
    
video.release()
cv2.destroyAllWindows()