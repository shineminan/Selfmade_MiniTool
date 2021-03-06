import pytube as p

playlsiturl = "https://youtube.com/playlist?list=PLQqbdnAgoRmZBp0GklnKNIvr2dn1GyYcS"
saveto = "E:\Video\eCloud"




urls = p.Playlist(playlsiturl)

a = urls[0]
p.YouTube(a).streams.first().download(saveto)
print("Complete!")