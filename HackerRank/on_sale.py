#!/usr/bin/python

if __name__ == "__main__":
    fruits = ["banana", "apple", "pineapple", "oranges"]
    on_sale = ["banana", "apple", "tomatoes"]

    print("All: ", set(on_sale) | set(fruits))
    print("On Sale: ", set(on_sale) & set(fruits))
    print("Others on Sale: ", set(on_sale) - set(fruits))
