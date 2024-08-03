from pytubefix import YouTube

# YouTube video URL'si
url = 'https://www.youtube.com/watch?v=9bZkp7q19f0'  # Kendi URL'nizi buraya ekleyin
yt = YouTube(url)

# Tüm çözünürlük seçeneklerini listeleyin
resolutions = [s.resolution for s in yt.streams.filter(file_extension='mp4') if s.resolution]

# Çözünürlük seçeneklerini yazdırın
print("Mevcut çözünürlük seçenekleri:", resolutions)