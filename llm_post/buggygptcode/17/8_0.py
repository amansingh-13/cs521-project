def parse_music(music_string: str) -> List[int]:
    e_values = {'o': 4, 'o|': 2, '.|': 1}
    es = music_string.split()
    beats = []
    for e in es:
        beats.append(e_values[e])
    return beats