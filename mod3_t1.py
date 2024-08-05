calls = 0


def count_calls():
    global calls
    calls += 1
    return


def string_info(string):
    count_calls()
    info = (len(string), string.upper(), string.lower())
    return info


def is_contains(string, list_to_search):
    global list1
    count_calls()
    for list1 in list_to_search:
        if string.lower() in list1.lower():
            return True
    else:
        if not string.lower() in list1.lower():
            return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
