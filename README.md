# Functional Python with Hexagonal Architecture

A demonstration project showcasing **functional programming principles** combined with **Hexagonal Architecture** (Ports and Adapters) in Python.

## Project Goal

This project implements a simple shopping cart system following best practices:

- **Pure functions** for business logic
- **Immutable data structures** using frozen dataclasses
- **Dependency inversion** through Protocol interfaces
- **Type safety** with strict type checking (basedpyright)
- **Clean separation of concerns** across domain, application, and adapter layers

## Architecture

The project follows **Hexagonal Architecture** principles:

```
┌─────────────────────────────────────────────────────────┐
│                     Adapters Layer                      │
│  ┌─────────────────────────────────────────────────┐   │
│  │          Application Layer (Ports)              │   │
│  │  ┌───────────────────────────────────────────┐  │   │
│  │  │         Domain Layer (Core)               │  │   │
│  │  │  • Pure business logic (rules.py)         │  │   │
│  │  │  • Domain models (models.py)              │  │   │
│  │  │  • No external dependencies               │  │   │
│  │  └───────────────────────────────────────────┘  │   │
│  │  • Ports (Protocol interfaces)                  │   │
│  │  • Use cases orchestration                      │   │
│  └─────────────────────────────────────────────────┘   │
│  • Concrete implementations (in_memory_store.py)       │
│  • External integrations                               │
└─────────────────────────────────────────────────────────┘
```

### Project Structure

```
src/app/
├── domain/          # Core business logic (pure functions)
│   ├── models.py    # Immutable domain entities
│   └── rules.py     # Pure business rules
├── application/     # Application services
│   ├── ports.py     # Protocol interfaces (Ports)
│   └── use_cases.py # Use case orchestration
└── adapters/        # External implementations (Adapters)
    └── in_memory_store.py  # Concrete repository implementation

tests/
├── unit_tests/      # Unit tests for each layer
│   ├── domain/
│   ├── application/
│   └── adapters/
└── builders/        # Test data builders (Test Object pattern)
```

## Key Design Patterns

### 1. **Immutability**

All domain models use `@dataclass(frozen=True)` to prevent mutation:

```python
@dataclass(frozen=True, slots=True)
class Cart:
    items: tuple[Item, ...]  # Immutable tuple
```

### 2. **Pure Functions**

Domain rules are stateless and side-effect-free:

```python
def add_item(cart: Cart, item: Item) -> Cart:
    return Cart(items=(*cart.items, item))  # Returns new cart
```

### 3. **Type Safety**

Using `NewType` for semantic types and strict type checking:

```python
Cents = NewType("Cents", int)  # Price as cents to avoid float issues
```

### 4. **Dependency Inversion**

Application layer depends on abstractions ([`CartRepo`](src/app/application/ports.py), [`Catalog`](src/app/application/ports.py)), not concrete implementations:

```python
class CartRepo(Protocol):
    def get(self, cart_id: str) -> Cart | None: ...
    def put(self, cart_id: str, cart: Cart) -> None: ...
```

### 5. **Higher-Order Functions**

Functions that return functions for composable behavior:

```python
def percent(percent: float) -> Discount:
    def apply(price: Cents) -> Cents:
        return Cents(round(int(price) * (1.0 - percent / 100)))
    return apply
```

## Requirements

- **Python 3.13+**
- **uv** package manager

## Installation

```bash
# Install dependencies
uv sync
```

## Development Commands

The project includes a [Makefile](Makefile) with common development tasks:

```bash
# Run linter with auto-fix
make lint

# Format code
make format

# Run type checker
make typecheck

# Run all checks (lint, format, typecheck)
make all

# Clean Python cache files
make clean

# Run tests
uv run pytest tests/
```

## Running the Application

```bash
python main.py
```

This demonstrates:

1. Adding items to a cart using [`add_to_cart`](src/app/application/use_cases.py)
2. Computing totals with discounts using [`compute_totals`](src/app/application/use_cases.py)

## Testing

Tests are organized by architectural layer:

```bash
# Run all tests
uv run pytest

# Run specific layer tests
uv run pytest tests/unit_tests/domain/
uv run pytest tests/unit_tests/application/
uv run pytest tests/unit_tests/adapters/
```

## Code Quality Tools

- **Ruff**: Fast Python linter and formatter
- **Basedpyright**: Strict type checking (fork of Pyright)
- **pytest**: Testing framework with async support
