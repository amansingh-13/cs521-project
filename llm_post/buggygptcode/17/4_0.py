def parse_music(music_string: str) -> List[int]:
    beats = []
    es = music_string.split()
    for e in es:
        if e == 'o':
            beats.append(4)
        elif e == 'o|':
            beats.append(2)
        elif e == '.|':
            beats.append(1)
    return beats