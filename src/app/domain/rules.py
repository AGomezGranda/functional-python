from collections.abc import Callable

from src.app.domain.models import Cart, Cents, Item

Discount = Callable[[Cents], Cents]


def percent(percent: float) -> Discount:
    def apply(price: Cents) -> Cents:
        return Cents(round(int(price) * (1.0 - percent / 100)))

    return apply


def add_item(cart: Cart, item: Item) -> Cart:
    return Cart(items=(*cart.items, item))


def subtotal(cart: Cart) -> Cents:
    return Cents(sum(int(item.price) for item in cart.items))


def total(cart: Cart, discount: Discount) -> Cents:
    return Cents(sum(discount(item.price) for item in cart.items))
