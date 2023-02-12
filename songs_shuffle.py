import random

song_list = []

print(f"If you are done, you can simply type 'done'")

while True:
    song = input("Insert Your Song: ").title().strip()
    if song == "Done":
        break
    song_list.append(song)

random.shuffle(song_list)

for i, song in enumerate(song_list,1):
    if song != "Done":
        print(i,"-",song)