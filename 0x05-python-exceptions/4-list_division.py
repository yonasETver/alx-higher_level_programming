#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("Type err")
            div = 0
        except ZeroDivisionError:
            print("Division by 0 err")
            div = 0
        except IndexError:
            print("Out of range err")
            div = 0
        finally:
            new_list.append(div)
    return new_list
