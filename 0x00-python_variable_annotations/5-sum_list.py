#!/usr/bin/env python3
'''
5-sum_list.py
'''
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    # return reduce(lambda acc, item: acc + item, input_list, 0)
    return sum(input_list)
