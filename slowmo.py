import picamera
import time
import webbrowser
from subprocess import call

camera = picamera.PiCamera()

#Set resolution to 640*480 to allow 90fps capture
camera.resolution=(640,480)
#The camera here is upside-down
camera.vflip = True
#Set frame-rate
camera.framerate=(90)

#identify the output file
url = 'test1.mp4'


while(True):
    print "RECORDING"
    camera.start_preview()
    #camera.annotate_text = "GO!!!"
    camera.start_recording('test1.h264')
    camera.wait_recording(5)
    camera.stop_recording()
    camera.stop_preview()
    print "WAIT"
    call(["rm","test1.mp4"])
    call(["MP4Box", "-add", "test1.h264", "test1.mp4"])
    webbrowser.open(url,new=0,autoraise=True)
    time.sleep(22)
