def parse_music(music_string: str) -> List[int]:
    beats = []
    for e in music_string.split():
        if e == 'o':
            beats.append(4)
        elif e == 'o|':
            beats.append(2)
        elif e == '.|':
            beats.append(1)
    return beats