import cv2, time

video=cv2.VideoCapture(0)
# video2=cv2.VideoCapture("Dont Look Deeper 101 Alpha.mkv")

a=1

while True:
    a=a+1
    check, frame = video.read()
    # print(check)
    # print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # time.sleep(3)   # just wait 3 seconds 
    cv2.imshow("Capturing",gray)
    key=cv2.waitKey(50)
    if key==ord('q'):
        break

print(a)

video.release()

cv2.destroyAllWindows()