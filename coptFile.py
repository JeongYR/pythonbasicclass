butter_size = 1024

with open('bts_movie.mp4','rb') as source:
    with open('bts_movie2.mp4', 'wb') as copy:
        while True:
            butter = source.read(butter_size)
            if not butter:
                break
            copy.write(butter)

print("Finish")
