import cv2

class cam(object):
    def __init__(self, source=None):
        self.video_source = cv2.VideoCapture(source)

    def sample_image(self):
        return self.video_source.read()
    
    def reset_cam(self, source=None):
        self.video_source.release()
        self.video_source = cv2.VideoCapture(source)
    
