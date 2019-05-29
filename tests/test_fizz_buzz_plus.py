from src.fizz_buzz_plus import FizzBuzzPlus


def test_fizz_buzz():
    """a simple example to start you off"""
    fizz_or_buzz_or_other = FizzBuzzPlus()
    assert fizz_or_buzz_or_other.answer(3).find('Fizz') > -1
    assert fizz_or_buzz_or_other.answer(9).find('Fizz') > -1
    assert fizz_or_buzz_or_other.answer(31).find('Fizz') > -1
    assert fizz_or_buzz_or_other.answer(38).find('Fizz') > -1
    assert fizz_or_buzz_or_other.answer(10).find('Buzz') > -1
    assert fizz_or_buzz_or_other.answer(51).find('Buzz') > -1
    assert fizz_or_buzz_or_other.answer(58).find('Buzz') > -1
    assert fizz_or_buzz_or_other.answer(7) == '7'
