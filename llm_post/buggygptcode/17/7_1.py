def parse_music(music_string: str) -> List[int]:
    beats = []

    # Split the music string into individual es
    es = music_string.split()

    # Loop through each e and determine the number of beats it lasts
    for e in es:
        if e == 'o':
            beats.append(4)
        elif e == 'o|':
            beats.append(2)
        elif e == '.|':
            beats.append(1)

    return beats