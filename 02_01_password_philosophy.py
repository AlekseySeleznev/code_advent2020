data = open('02_passwords.txt').readlines()

entry = data[]
print(entry)
for char in entry:
    print(char)

low_str = ""
high_str = ""
letter = ""
password = ""

state = "low"
for char in entry:
    #print(f"State: {state}, {char}")
    if state == "low":
        if char in "0123456789":
            low_str += char
        elif char == "-":
            state = "high"

    elif state =="high":
        if char in "0123456789":
            high_str += char
        elif char == " ":
            state = "letter"

    elif state == "letter":
        if char in "abcdefghijklmnopqrstuvwxyz":
            letter += char
        elif char == ":":
            state = "password"

    elif state == "password":
        if char in "abcdefghijklmnopqrstuvwxyz":
            password += char

#print(f"Low: {low_str}, High: {high_str}, Letter: {letter}, Password: {password}")