import pytube

print("Give URL:")
url = input()

pytube.YouTube(url).streams.get_highest_resolution().download('../Video')
