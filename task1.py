def search_word(x, my_list):
    for y in my_list:
        if y == x:
            return 1
        else:
            return 0


print("Enter The Value")
value = input()
my_list1 = ['Lahore', 'Pakistan', 'Karachi', 'Peshawar', 'Quetta']
if search_word(value, my_list1):
    print("True")
else:
    print("False")


