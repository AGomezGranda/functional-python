from typing import override

from src.app.application.ports import CartRepo
from src.app.domain.models import Cart


class InMemoryCartRepo(CartRepo):
    def __init__(self) -> None:
        self._store: dict[str, Cart] = {}

    @override
    def get(self, cart_id: str) -> Cart | None:
        return self._store.get(cart_id)

    @override
    def put(self, cart_id: str, cart: Cart) -> None:
        self._store[cart_id] = cart
