#working
import numpy as np
import cv2
#window,mac
#from PIL import  ImageGrab
#linux
import pyscreeenshot as ImageGrab

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1366, 768))

while True:
    img = ImageGrab.grab()
    img_np = np.array(img)

    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    cv2.imshow("Screen", frame)
    out.write(frame)

    if cv2.waitkey(1) == 27:
        break

out.release()

cv2.destroyAllWindows()

