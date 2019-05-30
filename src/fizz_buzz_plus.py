class FizzBuzzPlus:
    @staticmethod
    def answer(number: int) -> str:
        text = ""
        if number % 3 == 0:
            text += "Fizz"
        if number % 5 == 0:
            text += "Buzz"
        if "3" in str(number):
            text += "Fizz"
        if "5" in str(number):
            text += "Buzz"
        if text == "":
            text = str(number)
        return text


if __name__ == "__main__":
    fizz_or_buzz_or_other = FizzBuzzPlus()
    for i in range(1, 101):
        print(fizz_or_buzz_or_other.answer(i))
