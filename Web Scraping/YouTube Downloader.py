from pytube import YouTube

link = input('Please enter the video\'s link:> ')
video = YouTube(link)

print(type(video))
# print(video.title)

print(video.description)
print(video.ratings, video.views)

print(video.streams)

for stream in video.streams:
    print(stream)

video.streams.get_lowest_resolution().download(
    output_path='/Users/hendy/Desktop/classes')
