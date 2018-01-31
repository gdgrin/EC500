import subprocess,os

def image_rename():
    i=0
    directory = "photos"
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            os.rename(directory + "/" + filename, directory + "/" + str(i) + ".jpg")
            i+=1
    return

image_rename()

fps = 1
subprocess.call(["ffmpeg","-y","-r",str(fps),"-i", "photos/%d.jpg","-vcodec","mpeg4", "-qscale","5", "-r", str(fps), "video.avi"])