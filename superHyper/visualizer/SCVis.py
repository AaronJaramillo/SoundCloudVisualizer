
#import scipy.io.wavfile, numpy, sys, subprocess
import soundcloud
#import urllib.request
import youtube_dl
import os
import traceback

# def make_savepath(title, savedir):
#     return os.path.join(savedir, "%s.mp3" % (title))

def fetch(url):
    # create directory
    savedir = "visualizer/media/"
    if not os.path.exists(savedir):
        os.makedirs(savedir)



    options = {
        'format':'bestaudio/best',
        'extractaudio': True,
        'audioformat': "mp3",
        'outtmpl': '%(id)s',
        'noplaylist': True,}
    ydl = youtube_dl.YoutubeDL(options)

    with ydl:

            ydl.download([url])

            savedir = 'visualizer/media/'

            print("Downloading...")

            # download video
            try:
                result = ydl.extract_info(url, download=True)

                # for i in result :
                #     print(i)

                #filename = make_savepath(result['title'], savedir)

                #filename =  result['title'] + ".mp3"

                filename = "visualizer/media/TEMPSONG.mp3"

                os.rename(result['id'], filename)
                print("Downloaded and converted successfully!")

            except Exception as e:
                print("Can't download audio! %s\n" % traceback.format_exc())

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None
    return_val = fetch(arg)