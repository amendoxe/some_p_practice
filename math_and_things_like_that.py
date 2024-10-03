"""Random module"""
import random


def main():
    """just playing with random and lists"""
    my_list = [1, 2, 3, 4]
    print(appending_a_bunch(my_list, 3))


def appending_a_bunch(lists, times):
    '''Append a random number on the lists, times times'''

    for i in range(times):
        lists.append(random.randint(0, 9))
    return lists


main()
