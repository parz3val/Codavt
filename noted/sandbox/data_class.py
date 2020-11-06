# dataclasses
# Dataclasses provide a decorator and afucntions for automatically
# addingg generated special methods such as __init__ and ___repr__
# for user classes
# vars are annoated with PEP 526 type hints
# complete docs link: https://docs.python.org/3/library/dataclasses.html?highlight=dunder


from dataclasses import dataclass, InitVar
from typing import Any


@dataclass(init=True, repr=True)
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


# Among other things the decorator will add __init__

# Options for the decorators
# @dataclasses.dataclass
# init = True/False - can set it to generate init or not
# repr = True/False
# eq = True/False, compares class like tuple of its fields
# order = False, compares class like tuple of its fields: in order
# unsafe_hash = False , does the __hash__ according to the
# definitions in the __eq__ and whther frozen is true or false
# __hash__ calls hash(), which returns the value of obj
# frozen = False
# Dataclass will not implicitly add __hash__() unless its safe to do so.
# the way of adding __hash__ in any case is to mark the unsafe_hash flag True

"""
Three different ways of using the dataclass
@dataclass
class C:
    ...

@dataclass()
class C:
    ...

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class C:

"""
product = InventoryItem(name="Crocs", unit_price=50, quantity_on_hand=40)

print(repr(product))


class A:
    a: int
    b: int = 0


class C:
    d: float
    e: str

# Init only vars
# These are fields defined in the class which are pseudo-field
# They are only used in the init

@dataclass
class F:
    g: int
    h: int = None
    i = InitVar[int]

    def __post__init__(self, i):
        if self.g is not None and self.h is not None:
            self.h = i + self.g

k = F(g=4, h=5)

print(k.h)

"""
Immutability: We can turn dataclass into immutable python objects 
by passing frozen = True to the dataclass() decorator
"""

@dataclass
class sbs:
    x: Any = 5.0
    y: int = 0

@dataclass(frozen=True)
class sbi:
    x: int = 100
    y: int = 150

sbs_obj = sbs(x=10, y=10)
sbi_obj = sbi(x=50, y=60)

# try and mutate the values
sbs_obj.x = 105.00
sbi_obj.x = 110

print(repr(sbs_obj))
# print(repr(sbi_obj)) There will be frozen instance error.