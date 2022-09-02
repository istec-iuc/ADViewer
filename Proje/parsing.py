from ldap_con import *
from itertools import chain


def parse (lst: list) -> list :
    try:
        temp = [_.split(",")[::-1] if i == 0 else [_.split(",")[0]] for i , _ in enumerate(lst)]
        temp = [*chain.from_iterable(temp)]
        temp.pop(0)
        return temp
    except:
        raise ValueError("Can't return the expected output type")






