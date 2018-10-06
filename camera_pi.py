import cv2

class Camera(object):
    def __init__(self):
        if cv2.__version__.startswith('2'):
            PROP_FRAME_WIDTH = cv2.cv.CV_CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
        elif cv2.__version__.startswith('3'):
            PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT

        self.video = cv2.VideoCapture(0)
        #self.video = cv2.VideoCapture(1)
        #self.video.set(PROP_FRAME_WIDTH, 640)
        #self.video.set(PROP_FRAME_HEIGHT, 480)
        self.video.set(PROP_FRAME_WIDTH, 320)
        self.video.set(PROP_FRAME_HEIGHT, 240)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tostring()
    def get_frame2(self):
        success, image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, jpeg = cv2.imencode('.jpg', gray)
        return jpeg.tostring()
    def get_frame3(self):
        success, image = self.video.read()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        ret, jpeg = cv2.imencode('.jpg', hsv)
        return jpeg.tostring()
    def get_frame4(self):
        success, image = self.video.read()
        Sobel = cv2.Sobel(image, -1, 1, 1, ksize=5) 
        ret, jpeg = cv2.imencode('.jpg', Sobel)
        return jpeg.tostring()
    def get_frame5(self):
        success, image = self.video.read()
        Bilateral = cv2.bilateralFilter(image, 9, 75, 75)
        ret, jpeg = cv2.imencode('.jpg', Bilateral)
        return jpeg.tostring()
    def get_frame6(self):
        success, image = self.video.read()
        ret,threshold=cv2.threshold(image, 125, 255, cv2.THRESH_BINARY)
        ret, jpeg = cv2.imencode('.jpg', threshold)
        return jpeg.tostring()
