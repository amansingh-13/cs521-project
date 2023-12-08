def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1}
    es = music_string.split()
    return [durations[e] for e in es]