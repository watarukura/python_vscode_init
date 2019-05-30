from src.fizz_buzz_plus import FizzBuzzPlus


def test_fizz_buzz():
    """a simple example to start you off"""
    fizz_or_buzz_or_other = FizzBuzzPlus()
    assert "Fizz" in fizz_or_buzz_or_other.answer(3)
    assert "Fizz" in fizz_or_buzz_or_other.answer(9)
    assert "Fizz" in fizz_or_buzz_or_other.answer(31)
    assert "Fizz" in fizz_or_buzz_or_other.answer(38)
    assert "Buzz" in fizz_or_buzz_or_other.answer(10)
    assert "Buzz" in fizz_or_buzz_or_other.answer(51)
    assert "Buzz" in fizz_or_buzz_or_other.answer(58)
    assert "7" in fizz_or_buzz_or_other.answer(7)
