first_name = 'Blessed'
last_name = 'Henry'
print(first_name.capitalize()  + ' ' +  last_name.capitalize())

sentence = 'The church of jesus christ of latter day saints'
print(sentence.capitalize())
print(sentence.lower())
print(sentence.upper())
print(sentence.count('e'))

first_name = input('Enter your first name:')
last_name = input('Enter your last name:')

print('Hello,' + first_name +' ' + last_name)

first_name = 'Blessed'
last_name = 'Henry'


output = 'Hello, ' + first_name + ' ' + last_name
print(output)

output = 'Hello, {} {}'. format(first_name,last_name)
print(output)

output = 'Hello, {0} {1}'. format(first_name,last_name)
print(output)

output = f'Hello, {first_name} {last_name}'
print(output)
