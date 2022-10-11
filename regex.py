import re

with open('regex_test.txt') as file:
    hw_data = file.read()
    print(hw_data)

new_names = re.compile(r"""
    ^(?P<first_name>[A-Z]\w*)\s?
    (?P<middle_name>[A-Za-z]+)?\s?
    (?P<last_name>[A-Z]\w*)$
""", re.M|re.X)

my_list = new_names.match(hw_data)
print(my_list)



for match in new_names.finditer(hw_data):
    if match.group('first_name'):
        print('='*50)
        first_name = match.group('first_name')
        middle_name = match.group('middle_name')
        last_name = match.group('last_name')


        print(f"{first_name} {middle_name} {last_name}")
    else:
        print('None')
    # if match:
    #     print(match.group(1))
    # else:
    #     print("-1")