import pytube

url = input("link: ")

youtube = pytube.YouTube(url)

video = youtube.streams.get_highest_resolution()

video.download()