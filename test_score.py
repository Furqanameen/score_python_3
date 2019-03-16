import os

from score import get_answer

def test_score():
    answers=get_answer(os.path.join("img","answered-sheet-photo.jpg"))
    assert  answers[0]==['A','C','C','E','N/A','N/A','A','N/A','N/A','N/A']
