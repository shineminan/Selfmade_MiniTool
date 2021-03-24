import pytube as p
import subprocess
from playsound import playsound
import os
import time

saveto = "E:\Video\eCloud"
webm_path = saveto + "\Webms"
audio_path = saveto + "\Audios"
output_path = "E:\Video\eCloud\Videos"

def playlistdownload(urls,episodelist):
    for i in episodelist: # i is the episode number
        episodeindex = i - 1
        a = p.YouTube(urls[episodeindex])

        t1 = time.perf_counter()
        print("Episode " + str(i) + " webm started downloading!")
        webm = a.streams.filter(file_extension='webm').order_by('resolution').desc().first().download(webm_path)
        print("Episode "+str(i)+" webm downloaded!")
        webm_rename = webm_path + "\\name" + "_(" + str(i) + ").webm"
        os.rename(webm, webm_rename)

        audio = a.streams.filter(only_audio=True).order_by('abr').desc().first().download(audio_path)
        print("Episode "+str(i)+" audio downloaded!")
        audio_rename = audio_path + "\\name" + "_(" + str(i) + ").webm"
        os.rename(audio, audio_rename)

        if i < 10:
            string = "ffmpeg -i " + audio_rename + " -i " + webm_rename + " -c copy " + output_path + "\\name" + "_(0" + str(i) + ").mkv"
        else:
            string = "ffmpeg -i " + audio_rename + " -i " + webm_rename +  " -c copy " + output_path + "\\name" + "_(" + str(i) + ").mkv"

        subprocess.run(string)
        t2 = time.perf_counter()
        min, sec = divmod(t2-t1, 60)
        print("Episode "+str(i)+"/"+str(l) +" finished! " + str(int(min)) + "Min" + str(int(sec)) + "Sec used")
        playsound("./AudioFile/cartoon_bubble_pop.mp3")
        os.remove(webm_rename)
        os.remove(audio_rename)

def singlevidoedownload(url):
    a = p.YouTube(url)

    t1 = time.perf_counter()
    print("Webm started downloading!")
    webm = a.streams.filter(file_extension='webm').order_by('resolution').desc().first().download(webm_path)
    print("Webm downloaded!")
    webm_rename = webm_path + "\\YouJustDownloaded.webm"
    os.rename(webm, webm_rename)


    audio = a.streams.filter(only_audio=True).order_by('abr').desc().first().download(audio_path)
    print("Audio downloaded!")
    audio_rename = audio_path + "\\YouJustDownloaded.webm"
    os.rename(audio, audio_rename)

    string = "ffmpeg -i " + audio_rename + " -i " + webm_rename + " -c copy " + output_path + "\\SingleVideoYouJustDownloaded" + ".mkv"
    subprocess.run(string)
    t2 = time.perf_counter()
    min, sec = divmod(t2 - t1, 60)

    os.remove(webm_rename)
    os.remove(audio_rename)
    thename = audio.replace("E:\\Video\\eCloud\\Audios\\", "").replace(".webm", "")
    print("DONE! " + str(int(min)) + "Min" + str(int(sec)) + "Sec used And the original video title is: " + thename)
    playsound("./AudioFile/cartoon_mallets_rise_up_fast_2_steps.mp3")

playlisttext = "playlist"
givenurl = input("Paste your URL here:")
if playlisttext in givenurl:
    urls = p.Playlist(givenurl)
    l = len(urls)

    data = input("Which episodes you want to download? Input ike: (0-1000), (2-8), (0-8), (2-1000),(2,4,6,8) -> ")
    if "-" in data:
        mid = data.index("-")
        startepisode = max(int(data[:mid]), 1)
        endepisode = min(int(data[mid+1:]), l)
        episodelist = [x for x in range(startepisode,endepisode+1)]
        print(episodelist)
    elif "," in data:
        inputlist = [int(s) for s in data.split(",") if s.isdigit()]
        episodelist = [x for x in inputlist if 0 < x <= l]
        if len(episodelist) < inputlist:
            print("Hey, some episode(s) are out of range, but I wont tell which, hehe ")
    else:
        print("Duck you, totally wrong input!!!")

    a = time.perf_counter()
    print("It is a playlist, will take a long time to download all")
    playlistdownload(urls, episodelist)
    b = time.perf_counter()
    min, sec = divmod(b - a, 60)
    print("ALL DONE! Totally "+ str(min) + "Min" + str(sec) + "Sec used")
    playsound("./AudioFile/cartoon_mallets_rise_up_fast_2_steps.mp3")
else:
    print("Just one video, will be finished soon")
    singlevidoedownload(givenurl)