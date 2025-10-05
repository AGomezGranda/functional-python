from app.domain.models import Cart, Cents
from app.domain.rules import add_item, percent, subtotal, total
from tests.builders.models import build_item


async def test_add_item() -> None:
    cart = Cart(items=())
    item = build_item(sku="1", price=Cents(100))
    cart = add_item(cart, item)

    assert len(cart.items) == 1
    assert cart.items[0] == item


async def test_subtotal() -> None:
    cart = Cart(items=())
    item1 = build_item(sku="1", price=Cents(100))
    item2 = build_item(sku="2", price=Cents(200))
    cart = add_item(cart, item1)
    cart = add_item(cart, item2)

    assert subtotal(cart) == Cents(300)


async def test_subtotal_empty_cart() -> None:
    cart = Cart(items=())
    assert subtotal(cart) == Cents(0)


async def test_total() -> None:
    cart = Cart(items=())
    item1 = build_item(sku="1", price=Cents(100))
    item2 = build_item(sku="2", price=Cents(200))
    cart = add_item(cart, item1)
    cart = add_item(cart, item2)
    d = percent(10)
    assert total(cart, d) == Cents(270)


async def test_total_empty_cart() -> None:
    cart = Cart(items=())
    discount = percent(10)
    assert total(cart, discount) == Cents(0)
