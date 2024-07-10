calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    string_lenght = len(string)
    string_up = string.upper()
    string_low = string.lower()
    count_calls()
    return string_lenght, string_up, string_low


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [element_of_list.lower() for element_of_list in list_to_search]
    if string in list_to_search:
        return True
    else:
        return False


print(string_info('start'))
print(string_info('stay tuned!'))
print(string_info('no fear'))
print(is_contains('bro', ['Brother', 'robot', 'brOck'])) # Urban ~ urBAN
print(is_contains('sis', ['SiSters', 'sin', 'solo', 'metamorphosis', 'SIS'])) # No matches
print(calls)