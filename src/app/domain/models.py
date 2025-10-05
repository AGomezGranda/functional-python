from dataclasses import dataclass
from typing import NewType

Cents = NewType("Cents", int)


@dataclass(frozen=True, slots=True)
class Item:
    sku: str
    price: Cents


@dataclass(frozen=True, slots=True)
class Cart:
    items: tuple[Item, ...]
