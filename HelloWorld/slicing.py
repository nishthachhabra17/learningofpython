letters = 'abcdefghijklmnopqrstuvwxyz'

print(letters[0:15])
print(letters[:18])
print(letters[21:])
print(letters[:13] + letters[13:])

print(letters[-26:15])
print(letters[3:-12])
print(letters[:-18])
print(letters[-21:])
print(letters[:-13] + letters[-13:])
print(letters[0:25:5])  #start,step,stop

numbers = "7,345 224:456;549"
seperators = numbers[1::4]
print(seperators)

