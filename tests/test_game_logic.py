from logic_utils import check_guess


def test_guess_too_low():
    # secret=50, guess=30 → outcome should be "Too Low"
    outcome, message = check_guess(30, 50)
    assert outcome == "Too Low"


def test_guess_too_high():
    # secret=50, guess=70 → outcome should be "Too High"
    outcome, message = check_guess(70, 50)
    assert outcome == "Too High"


def test_winning_guess():
    # secret=50, guess=50 → outcome should be "Win"
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
