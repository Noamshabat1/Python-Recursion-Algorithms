#################################################################
# FILE : calculate_mathematical_expression
# WRITER : noam shabat , no.amshabat1 , 206515579
# EXERCISE : intro2cs2 ex7 2021
# DESCRIPTION: A simple search engine that crawl's the web.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED: stackoverflow.com
# NOTES: ...
#################################################################
"""Import Variable's:"""
from typing import List, Any

import ex7_helper as h


def mult(x: float, y: int) -> float:
    """
    this func is getting two numbers and checking the multiply of them.
    :param x: the first val that is being multiply.
    :param y: the second val that is being multiply.
    :return: the val of the multiplication.
    """
    if y == 0:
        return 0
    return h.add(x, mult(x, h.subtract_1(y)))


def is_even(n: int) -> bool:
    """
    checks if the num is even.
    :param n: the number being checked.
    :return: true if its even or false if the not even.
    """
    if n > 0:
        if n == 0:
            return True
        if n == 1:
            return False
        else:
            return is_even(h.subtract_1(h.subtract_1(n)))
    elif n == 0:
        return True
    else:
        if n <= -1:
            return False
        else:
            return is_even(int(h.add(n, 2)))


def log_mult(x: float, y: int) -> float:
    """
    this func is calculation the val of the two numbers in log complexity.
    :param x: the first val that is being multiply.
    :param y: the second val that is being multiply.
    :return: the val of the multiplication.
    """
    if y == 0:
        return 0
    if h.is_odd(y):
        return h.add(x, log_mult(h.add(x, x), h.divide_by_2(y)))
    else:
        return log_mult(h.add(x, x), h.divide_by_2(y))


def is_power(b: int, x: int) -> bool:
    """
    checking if a number is equal to an num in power of val b.
    :param b: power that is being checked.
    :param x: the num that we are checking about.
    :return: true if the val is the power of the desirable val.
    """
    if b == 0 and x != 0:
        return False
    else:
        return _helper_is_power(b, x, b)


def _helper_is_power(b: int, x: int, current_num: int) -> bool:
    """
    an help func for is_power def.
    :param b: power that is being checked.
    :param x: the num that we are checking about.
    :param current_num: the number that is under the examination for the
    roll of the number under the power of b.
    :return: true if the val is the power of the desirable val.
    """
    if current_num == x:
        return True
    if current_num > x:
        return False
    else:
        return _helper_is_power(b, x, int(log_mult(current_num, b)))


def reverse(s: str) -> str:
    """
    reverses the string.
    :param s: the string.
    :return: reversed string.
    """
    if len(s) <= 1:
        return s
    else:
        return _reverse_helper(s, "", len(s) - 1)


def _reverse_helper(s: str, new_s: str, index: int) -> str:
    """
    this func is helping us to do the reversed func.
    :param s: the string.
    :param new_s: reversed string.
    :param index: the index of the letter in the string.
    :return: reversed string.
    """
    if index == 0:
        return h.append_to_end(new_s, s[index])
    new_s = h.append_to_end(new_s, s[index])
    return _reverse_helper(s, new_s, index - 1)


def play_hanoi(Hanoi: Any, n: int, src: Any, dest: Any, temp: Any) -> Any:
    """
    this func is the code for the game Hanoi
    :param Hanoi: The file we run to play the game
    :param n: The number of discs for the game
    :param src: The pole where we remove the discs from
    :param dest: The pole that we want to move the discs to
    :param temp: The third pole of the game
    :return: None
    """
    if n >= 1:
        play_hanoi(Hanoi, n - 1, src, temp, dest)
        Hanoi.move(src, dest)
        play_hanoi(Hanoi, n - 1, temp, dest, src)


def number_of_ones(n: int) -> int:
    """
    count the numbers of times the figure 1 appeared in the number and the
    privies numbers.
    :param n: the number that we check.
    :return: the sum of the figure 1 appeared.
    """
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        count = _count_ones(n)
        return count + number_of_ones(n - 1)


def _count_ones(n: int) -> int:
    """
    a help func that counts the amount of times that 1 opened in the number.
    :param n: the cornet numbers
    :return: the count of one's.
    """
    count = 0
    if n == -1:
        return count + 1
    if n == 0:
        return count
    if n % 10 == 1:
        count += 1
    return count + _count_ones(n // 10)


def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    """
    this func is checking if two lists are the same.
    :param l1:the first list that we compare with.
    :param l2:the second list that we compare with.
    :return: true or false if the list's are the same.
    """
    if len(l1) == len(l2) == 0:
        return True
    if len(l1) != len(l2):
        return False
    if compare_1d_lists(l1[0], l2[0]):
        return compare_2d_lists(l1[1:], l2[1:])
    return False


def compare_1d_lists(l1: List[int], l2: List[int]) -> bool:
    """
    this func is compering the values of two list's.
    :param l1:the first list that we compere with.
    :param l2:the second list that we compere with.
    :return: true or false if the list's are the same.
    """
    if len(l1) == len(l2) == 0:
        return True
    if len(l1) != len(l2):
        return False
    if l1[0] == l2[0]:
        return compare_1d_lists(l1[1:], l2[1:])
    return False


def magic_list(n: int) -> List[Any]:
    """
    gives back the number of times that we are getting list of list's.
    :param n:the given number
    :return:list of list's as the given number.
    """
    if n == 0:
        return []
    if n == 1:
        return [[]]
    return magic_list(n - 1) + [magic_list(n - 1)]
