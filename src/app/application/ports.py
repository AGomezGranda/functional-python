from typing import Protocol

from src.app.domain.models import Cart, Item


class CartRepo(Protocol):
    def get(self, cart_id: str) -> Cart | None: ...
    def put(self, cart_id: str, cart: Cart) -> None: ...


class Catalog(Protocol):
    def find(self, sku: str) -> Item | None: ...
