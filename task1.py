def search_word(element, my_list):
    if element in my_list:
        return True
    else:
        return False


print("Enter The Value")
value = input()
my_list1 = ['Lahore', 'Pakistan', 'Karachi', 'Peshawar', 'Quetta']
print(search_word(value, my_list1))



