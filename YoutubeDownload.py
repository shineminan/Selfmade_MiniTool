import pytube as p
import subprocess
from playsound import playsound
import os

saveto = "E:\Video\eCloud"
webm_path = saveto + "\Webms"
audio_path = saveto + "\Audios"
output_path = "E:\Video\eCloud\Videos"

def playlistdownload(url):
    urls = p.Playlist(url)
    l = len(urls)
    for x in range(l):
        a = p.YouTube(urls[x])
        i = x + 1

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
        print("Episode "+str(i)+"/"+str(l) +" finished!")
        os.remove(webm_rename)
        os.remove(audio_rename)
        playsound("./AudioFile/cartoon_bubble_pop.mp3")

    print("ALL DONE!")
    playsound("./AudioFile/cartoon_mallets_rise_up_fast_2_steps.mp3")


def singlevidoedownload(url):
    a = p.YouTube(url)

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

    os.remove(webm_rename)
    os.remove(audio_rename)
    thename = audio.replace("E:\\Video\\eCloud\\Audios\\", "").replace(".webm", "")
    print("DONE! And the original video title is: " + thename)
    playsound("./AudioFile/cartoon_mallets_rise_up_fast_2_steps.mp3")

playlisttext = "playlist"
givenurl = input("Paste your URL here:")
if playlisttext in givenurl:
    print("It is a playlist, will take a long time to download all")
    playlistdownload(givenurl)
else:
    print("Just one video, will be finished soon")
    singlevidoedownload(givenurl)