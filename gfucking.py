import pytube

link = input("""

DieNock's Made it !

indirilecek video,playlist linkini giriniz :
""")

yt = pytube.YouTube(link)

stream = yt.streams.first()
finished = stream.download()
print("Yükleme tamamlandı")
