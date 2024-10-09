from um import count
import pytest


def test_um_case():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2


def test_um_in_space():
    assert count("so um yeah") == 1


def test_um_surrounded():
    assert count("hello, um, world") == 1
    assert count("um?") == 1


def test_um_in_word():
    assert count("yummy consumption") == 0


if __name__ == "__main__":
    main()