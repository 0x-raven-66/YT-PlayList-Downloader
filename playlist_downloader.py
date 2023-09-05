from pytube import Playlist
import os

# getting the link from user
print("-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-\n|=>  script to download youtube playlist  <=|\n-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-÷-")
url = str(input(" Enter Youtube PlayList url : "))
play = Playlist(url)

# show playlist information
print(f"\n  title   => {play.title}")
print(f"  number  => {play.length} videos")
print(f"  channel => {play.owner} ")

# create folder to download videos in
path = fr"D:\downloaded_PlayList\{play.title}"
if not os.path.exists(path):
    os.makedirs(path)

# download the videos
print("\n waiting to start downloading...")
i = 1
for video in play.videos:
    video = video.streams
    video = video.get_highest_resolution()
    print(f" video  {i} : downloading...")
    video.download(path)
    i = i + 1
print("\nplaylist downloaded successfully")
