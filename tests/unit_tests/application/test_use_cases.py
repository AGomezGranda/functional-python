from app.adapters.in_memory_store import InMemoryCartRepo
from app.application.use_cases import AddToCartCmd, add_to_cart, compute_totals
from app.domain.models import Cents
from tests.builders.models import build_catalog


async def test_add_to_cart() -> None:
    repo = InMemoryCartRepo()
    catalog = build_catalog(None)
    new_cart = add_to_cart(
        repo, catalog, AddToCartCmd(cart_id="cart1", sku="book")
    )
    assert len(new_cart.items) == 1
    assert new_cart.items[0].sku == "book"
    assert new_cart.items[0].price == Cents(1500)


async def test_compute_totals() -> None:
    repo = InMemoryCartRepo()
    catalog = build_catalog(None)
    new_cart = add_to_cart(
        repo, catalog, AddToCartCmd(cart_id="cart1", sku="book")
    )
    totals = compute_totals(new_cart, discount=10.0)
    assert totals.subtotal == Cents(1500)
    assert totals.discounted == Cents(1350)
