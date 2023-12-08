def parse_music(music_string: str) -> List[int]:
    note_values = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    beats = []
    for note in notes:
        beats.append(note_values[note])
    return beats