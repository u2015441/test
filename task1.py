def search_word(element, my_list):
    if element in my_list:
        return True
    else:
        return False


print("Enter The Value")
value = input()
f = open("list.txt", "rt")
my_list1 = [words for lines in f for words in lines.split()]
print(search_word(value, my_list1))
