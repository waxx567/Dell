from twttr import shorten

def test_twttr():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"

# run pytest test_twttr.py