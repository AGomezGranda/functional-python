from app.adapters.in_memory_store import InMemoryCartRepo
from app.domain.models import Cart


async def test_empty_store_get() -> None:
    store = InMemoryCartRepo()
    cart = store.get("non-existing-id")
    assert cart is None


async def test_store_put() -> None:
    store = InMemoryCartRepo()
    cart = Cart(items=())
    store.put("existing-id", cart)
    retrieved_cart = store.get("existing-id")
    assert retrieved_cart == cart
    assert retrieved_cart is not None
