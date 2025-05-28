import gender_guesser.detector as gender

detector = gender.Detector(case_sensitive=False)

def get_gender(name: str) -> str:
    g = detector.get_gender(name)
    if g in ('male', 'mostly_male'): return 'male'
    if g in ('female', 'mostly_female'): return 'female'
    return 'unknown' 