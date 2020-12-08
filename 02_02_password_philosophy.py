#!/usr/bin/env python3
import re

#-----------------------------------
#An EXAMPLE of using re module
#-----------------------------------
'''data = open('02_passwords.txt').readlines()
entry = data[0]

match = re.match('(\d+)-(\d+) (\w+): (\w+)', entry)
low_str, high_str, letter, password = match.groups()
'''

#-----------------------------------
#SOLUTION #1 FOR 1st part of 2nd Day
#-----------------------------------
'''
data = [re.match('(\d+)-(\d+) (\w): (\w+)', line).groups() for line in open("02_passwords.txt").readlines()]
print("Valid passwords", sum(int(low) <= password.count(letter) <= int(high) for low, high, letter, password in data))'''

#SOLUTION #2 for 1st part of 2nd Day


#-----------------------------------
#SOLUTION #2 FOR 1st part of 2nd Day
#-----------------------------------
'''pattern = re.compile('(?P<low>\d+)-(?P<high>\d+) (?P<letter>\w): (?P<password>\w+)', entry)
print(pattern.match(entry).groupdict())'''

#class Password:
class PasswordGeneralError():
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class PasswordFormatError(PasswordGeneralError):
    pass

class Password:
    pattern = re.compile("(?P<low>\d+)-(?P<high>\d+) (?P<letter>\w): (?P<password>\w+)", entry)


class PasswordFileParseError(PasswordGeneralError):
    def __init__(self, message, line):
        self.message = f"{message} on line {line}"
        super().__init__(self.message)

class PasswordChecker:
    def __init__(self, file):
        self.file = file

    def count_valid(self) -> int:
        total = 0
        with open(self.file) as file:
            for idx, line in enumerate(file):
                try:
                    valid = self.validate(line)
                except PasswordFormatError as err:
                    raise PaswordFileParseError("Could not validate", idx) from err
            total += int(valid)
        return total

    @staticmethod
    def validate(line) -> bool:
        return Password(line).is_valid()

checker = PasswordChecker("02_passwords.txt")
print("Number valid", checker.count_valid())
