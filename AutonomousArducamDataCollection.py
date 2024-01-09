import time
import threading
from picamera2 import Picamera2, Preview


class Camera(object):
    # frame_reader = None
    cam = None
    _value_lock = None

    # previewer = None

    def __init__(self, width=640, height=360):
        self._value_lock = threading.Lock()
        self.open_camera(width, height)

    def open_camera(self, width=640, height=360, framerate=30):
        self.cam = Picamera2()
        self.cam.configure(self.cam.create_preview_configuration(main={"size": (width, height)}, buffer_count=4))
        # self.cam.start_preview(Preview.QTGL)
        # self.cam.start()

    def getFrame(self, a_wait: bool = True):
        with self._value_lock:
            return self.cam.capture_array(wait=a_wait)

    def start_preview(self, a_preview: bool = False):
        if a_preview == True:
            self.cam.start_preview(Preview.QTGL)
        else:
            self.cam.start_preview()
        self.cam.start()

    def stop_preview(self):
        self.cam.stop_preview()
        self.cam.stop()

    def close(self):
        self.cam.close()

    def takeImage(self, imgString):
        capture_config = camera.cam.create_still_configuration()
        self.cam.switch_mode_and_capture_file(capture_config, imgString)


def getImgString(num):
    return "image" + num + ".jpg"


if __name__ == "__main__":
    camera = Camera()
    camera.start_preview(True)

    t_end = time.time() + 60 * 10 * 60
    i = 0
    while time.time() < t_end:
        time.sleep(60)
        camera.takeImage(getImgString(i))
        i = i+1

    camera.stop_preview()
    camera.close()
