# ---------------- Task 1 ---------------------
class Counter:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Counter = {self.number}"

    def __add__(self, other):
        self.number += other
        return Counter(self.number)

    def __sub__(self, other):
        self.number -= other
        return Counter(self.number)

    def __int__(self):
        return self.number


new_counter = Counter(5)
new_counter += 3
print(new_counter)
new_counter -= 2
print(new_counter.__int__())


# ---------------- Task 2 ---------------------
import datetime


class Email:

    @staticmethod
    def _convert_date(other_date):
        return datetime.date(*map(int, other_date.split("-")))

    def __init__(self, e_from, e_to, thema, text, date):
        self.e_from = e_from
        self.e_to = e_to
        self.thema = thema
        self.text = text
        self.date = self._convert_date(date)

    def __str__(self):
        return f"Date: {self.date}\nFrom: {self.e_from}\nTo: {self.e_to}\nThema: {self.thema}\nText: {self.text}"

    def __len__(self):
        return len(self.text)

    def __hash__(self):
        return hash(self.e_from) + hash(self.e_to) + hash(self.thema) + hash(self.text) + hash(self.date)

    def __bool__(self):
        if self.text:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.date < self._convert_date(other):
            return True
        else:
            return False

    def __le__(self, other):
        if self.date <= self._convert_date(other):
            return True
        else:
            return False

    def __eq__(self, other):
        if self.date == self._convert_date(other):
            return True
        else:
            return False


email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.",
               "2022-05-10")
email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")

print(email1)
print("------------")
print(len(email2))
print(hash(email3))
print(bool(email1))
print(email2.date > email3.date)
