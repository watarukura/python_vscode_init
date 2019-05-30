class FizzBuzzPlus:
    @staticmethod
    def answer(number: int) -> str:
        text = ""
        if number % 3 == 0:
            text += "Fizz"
        if number % 5 == 0:
            text += "Buzz"
        if str(number).find("3") > -1:
            text += "Fizz"
        if str(number).find("5") > -1:
            text += "Buzz"
        if text == "":
            text = str(number)
        return text


if __name__ == "__main__":
    fizz_or_buzz_or_other = FizzBuzzPlus()
    for i in range(1, 101):
        print(fizz_or_buzz_or_other.answer(i))
