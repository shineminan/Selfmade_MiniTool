import pytube as p
import subprocess
from playsound import playsound
import os
import time
""""
pytube upgrading line:
pip install pytube -U
"""

saveto = "E:\Video\eCloud"
webm_path = saveto + "\Webms"
audio_path = saveto + "\Audios"
output_path = "E:\Video\eCloud\Videos"
playlisttext = "playlist"

def singlevidoedownload(url, videoname, mode, i=0):
    a = p.YouTube(url)
    t1 = time.perf_counter()

    if i == 0:  # single video download
        print("Webm started downloading!")
    else:  #single download in a playlist
        print("Episode " + str(i) + "/" + str(l) + " webm started downloading!")

    webm = a.streams.filter(file_extension='webm').order_by('resolution').desc().first().download(webm_path) #.filter(resolution="1080p")
    webm_rename = webm_path + "\\YouJustDownloaded.webm"
    os.rename(webm, webm_rename)
    print("Webm downloaded! And Audio start downloading!")

    audio = a.streams.filter(only_audio=True).order_by('abr').desc().first().download(audio_path)
    audio_rename = audio_path + "\\YouJustDownloaded.webm"
    os.rename(audio, audio_rename)
    print("Audio downloaded! Start combine!")

    t2 = time.perf_counter()
    min, sec = divmod(t2 - t1, 60)
    if i == 0:  # single video download
        originalname = audio.replace("E:\\Video\\eCloud\\Audios\\", "").replace(".webm", "")
        print("DONE! " + str(int(min)) + " Min " + str(int(sec)) + " Sec used And the original video title is: " + originalname)
        playsound("./AudioFile/cartoon_mallets_rise_up_fast_2_steps.mp3")
    else:  #single download in a playlist
        print("Episode " + str(i) + "/" + str(l) + " finished! " + str(int(min)) + " Min " + str(int(sec)) + " Sec used")
        playsound("./AudioFile/cartoon_bubble_pop.mp3")

    string = "ffmpeg -i " + audio_rename + " -i " + webm_rename + " -c copy " + output_path + "\\" + str(videoname) + "_(" + '{0:03}'.format(int(mode))  + ").mkv"
    subprocess.run(string)
    os.remove(webm_rename)
    os.remove(audio_rename)

def playlistdownload(urls,episodelist, videoname, mode):
    a = time.perf_counter()
    for i in episodelist: # i is the episode number, i-1 is the episode index
        singlevidoedownload(urls[i-1], videoname, mode, i)
        singledlname = output_path + "\\" + str(videoname) + "_(" + '{0:03}'.format(int(mode))  + ").mkv"
        playlistepisodename = output_path + "\\" + str(name) + "_(" + '{0:03}'.format(i) + ").mkv"
        os.rename(singledlname, playlistepisodename)
    b = time.perf_counter()
    min, sec = divmod(b - a, 60)
    print("ALL DONE! Totally " + str(int(min)) + " Min " + str(int(sec)) + " Sec used")
    playsound("./AudioFile/cartoon_mallets_rise_up_fast_2_steps.mp3")

infoinput= input("Paste your URL, the name of episodes and download mode here separated by a coma: ") #0 is reverse, 1 is normal
givenurl, name, mode = (infoinput.split(","))
if playlisttext in givenurl:
    videourls = p.Playlist(givenurl)
    l = len(videourls)
    if int(mode) == 0:
        urls = list(videourls)[::-1]
    else:
        urls = list(videourls)
    data = input("Which episodes you want to download? Input ike: (0-1000), (2-8), (0-8), (2-1000), (2,4,6,8) ->: ")
    # name = input("What is the name of the episode? : ")
    if "-" in data:
        a, b = (int(s) for s in data.split("-") if s.isdigit())
        episodelist = [x for x in range(max(a, 1), min(b, l)+1)]
    elif "," in data:
        inputlist = [int(s) for s in data.split(",") if s.isdigit()]
        episodelist = [x for x in inputlist if 0 < x <= l]
    else:
        print("Duck you, totally wrong input!!!")
    print("It is a playlist, will take a long time to download all these episodes: ", episodelist)
    print("." * 200)
    playlistdownload(urls, episodelist, name, mode)
else:
    print("Just one video, will be finished soon")
    singlevidoedownload(givenurl, name, mode)

"""
https://youtube.com/playlist?list=PLGMn_M1Fmi2g2XPvx0SbfYymVzO6Z-dOh,你是我的荣耀,1
https://youtube.com/playlist?list=PLooD8l3FSd6k3wj5BVSqOhDP7mpHhnn8m,玉楼春,1
https://youtube.com/playlist?list=PLQqbdnAgoRma3HwiHsunjZXP0v-ChTiHV,乔家的儿女,1
https://youtube.com/playlist?list=PLATwx1z00Hsd_6Awul8IzE7QOPuqpKfDy,玫瑰行者,1
https://youtube.com/playlist?list=PL9yRf-Ghij3ZjLtoV6iCqP9klbD9BGgly,扫黑风暴,0
https://youtube.com/playlist?list=PLhnjbkseqMET-exRbvVoA29AMTIHeELwj,双镜,0
"""