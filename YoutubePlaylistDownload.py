import pytube as p
import subprocess
import os

playlsiturl = "https://youtube.com/playlist?list=PLQqbdnAgoRmZBp0GklnKNIvr2dn1GyYcS"
saveto = "E:\Video\eCloud"

webm_path = saveto + "\Webms"
audio_path = saveto + "\Audios"
output_path = "E:\Video\eCloud\Videos"


urls = p.Playlist(playlsiturl)
l = len(urls)

video = urls[0]
i = 1

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

    string = "ffmpeg -i " + audio_rename + " -i " + webm_rename +  " -c copy " + output_path + "\\name" + "_(" + str(i) + ").mkv"
    subprocess.run(string)
    print("Episode "+str(i)+"/"+str(l) +" finished!")

print("ALL DONE!")