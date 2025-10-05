from __future__ import annotations

from dataclasses import dataclass

from src.app.application.ports import CartRepo, Catalog
from src.app.domain.models import Cart, Cents, Item
from src.app.domain.rules import add_item, percent, subtotal, total


@dataclass(frozen=True)
class AddToCartCmd:
    cart_id: str
    sku: str


@dataclass(frozen=True)
class CartTotalsDto:
    subtotal: Cents
    discounted: Cents


def add_to_cart(repo: CartRepo, catalog: Catalog, cmd: AddToCartCmd) -> Cart:
    cart = repo.get(cmd.cart_id) or Cart(items=())
    item: Item | None = catalog.find(cmd.sku)
    if item is None:
        raise ValueError("Item not found in catalog")
    updated_cart = add_item(cart, item)
    repo.put(cmd.cart_id, updated_cart)
    return updated_cart


def compute_totals(cart: Cart, discount: float) -> CartTotalsDto:
    cart_subtotal = subtotal(cart)
    discount_func = percent(discount)
    cart_total = total(cart, discount_func)
    return CartTotalsDto(subtotal=cart_subtotal, discounted=cart_total)
