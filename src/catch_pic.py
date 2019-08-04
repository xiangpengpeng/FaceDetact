import cv2
import sys
import time
from PIL import Image

def CatchPICFromVideo(window_name, camera_idx, catch_pic_num, path_name):
    cv2.namedWindow(window_name)
    cap = cv2.VideoCapture(camera_idx)
    classfier = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    color = (0, 255, 0)
    num = 0
    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break

        time.sleep(0.2)

        img_name = '%s/%d.jpg'%(path_name, num)
        image = frame
        cv2.imwrite(img_name, image)
        num += 1

        if num > catch_pic_num: break

        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage:%s camera_id face_num_max path_name\r\n" % (sys.argv[0]))
    else:
        CatchPICFromVideo("截取人脸", 0, 1000, '../pictures/noface')
