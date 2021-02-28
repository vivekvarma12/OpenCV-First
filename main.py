import cv2
import sys
#cs = sys.argv[1]
face = cv2.CascadeClassifier('haarcascade_face_detect.xml')
r = cv2.VideoCapture(0)
while True:
    ret, frm = r.read()
    fcs = face.detectMultiScale(frm,scaleFactor=2,minNeighbors=5,minSize=(30,30))
    for (x, y, w, h) in fcs:
        t = cv2.rectangle(frm, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.putText(t,'This is your face',(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.9, (36,255,12), 2)
    cv2.imshow("Detection",t)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
r.release()
cv2.destroyAllWindows()