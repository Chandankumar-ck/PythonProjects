#...........youtube video/audio Downloader .............

from pytube import YouTube
link = input(str("enter/paste your youtube video link:"))
youtube_1 = YouTube(link)
#download in all format both video/audio. we can change here according to our requirement for only Audio or only Video.
# for download only Audio we can use this 👇👇

# videos = youtube_1.streams.filter(only_audio=True) 

# for download only Audio we can use this 👇👇

# videos = youtube_1.streams.filter(only_video=True)
videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
  print(i)
strm = int(input("enter the Sl. No. which format you want to download: "))
videos[strm].download()
print("your file downloaded sucessfully")

