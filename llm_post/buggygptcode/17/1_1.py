def parse_music(music_string: str) -> List[int]:
    es = music_string.split()
    durations = []
    for e in es:
        if e == 'o':
            durations.append(4)
        elif e == 'o|':
            durations.append(2)
        elif e == '.|':
            durations.append(1)
    return durations

print(parse_music('o o| .| o| o| .| .| .| .| o o'))