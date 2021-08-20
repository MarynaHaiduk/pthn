def create_shopping_list():
    shopping_list = []
    item = 0

    while True:
        item = input("Enter shopping list item: ")
        if item == "exit":
            break
        else:
            shopping_list.append(item)
    for i in range(0, len(shopping_list)):
        print(i + 1, shopping_list[i])


if __name__ == '__main__':
    create_shopping_list()
