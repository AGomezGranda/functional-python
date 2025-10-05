from src.app.application.use_cases import AddToCartCmd, add_to_cart, compute_totals
from src.app.adapters.in_memory_store import InMemoryCartRepo
from src.app.domain.models import Cents, Item

class StaticCatalog:
    def __init__(self) -> None:
        self._items: dict[str, Item] = {
            "book": Item(sku="book", price=Cents(1500)),
            "pen": Item(sku="pen", price=Cents(300)),
            "notebook": Item(sku="notebook", price=Cents(800)),
            "eraser": Item(sku="eraser", price=Cents(100)),
        }

    def find(self, sku: str) -> Item | None:
        return self._items.get(sku)

def main():
    repo = InMemoryCartRepo()
    catalog = StaticCatalog()

    cart = add_to_cart(repo, catalog, AddToCartCmd(cart_id="1", sku="book"))
    print(f"New cart after adding item: {cart}")
    totals = compute_totals(cart, discount=10.0)
    print(f"Computed totals: {totals}")


if __name__ == "__main__":
    main()
