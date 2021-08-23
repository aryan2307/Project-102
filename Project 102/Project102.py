import cv2
vid = cv2.VideoCapture(0)
result = True
while(result):
  ret, frame = vid.read()
  print(ret)
  cv2.imwrite("class102.png", frame)
  cv2.imshow('frame', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
vid.release()
cv2.destroyAllWindows()