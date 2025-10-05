from faker import Faker

from app.domain.models import Cents, Item

faker = Faker()


def build_item(sku: str | None, price: Cents | None) -> Item:
    if sku is None:
        sku = faker.uuid4()
    if price is None:
        price = Cents(faker.random_int(min=100, max=10000))
    return Item(sku=sku, price=price)


def build_items(num_items: int = 3) -> list[Item]:
    return [build_item(None, None) for _ in range(num_items)]


class TestCatalog:
    def __init__(self, items: dict[str, Item] | None = None) -> None:
        self._items: dict[str, Item] = items or {
            "book": Item(sku="book", price=Cents(1500)),
            "pen": Item(sku="pen", price=Cents(300)),
        }

    def find(self, sku: str) -> Item | None:
        return self._items.get(sku)


def build_catalog(items: dict[str, Item] | None = None) -> TestCatalog:
    return TestCatalog(items)
