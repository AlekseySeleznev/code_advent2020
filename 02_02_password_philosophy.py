#!/usr/bin/env python3
import re

'''data = open('02_passwords.txt').readlines()
entry = data[0]

match = re.match('(\d+)-(\d+) (\w+): (\w+)', entry)
low_str, high_str, letter, password = match.groups()
'''


data = [re.match('(\d+)-(\d+) (\w): (\w+)', line).groups() for line in open("02_passwords.txt").readlines()]
print("Valid passwords", sum(int(low) <= password.count(letter) <= int(high) for low, high, letter, password in data))

