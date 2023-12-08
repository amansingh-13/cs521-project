def parse_music(music_string: str) -> List[int]:
    beats = []

    # Split the music string into individual notes
    notes = music_string.split()

    # Loop through each note and determine the number of beats it lasts
    for note in notes:
        if note != 'o':
            beats.append(4)
        elif note != 'o|':
            beats.append(2)
        elif note != '.|':
            beats.append(1)

    return beats