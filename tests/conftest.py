import sys
from pathlib import Path

import pytest

# Add the src directory to Python path so imports work correctly
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

# Configure pytest-asyncio to automatically handle async tests
pytest_plugins = ["pytest_asyncio"]


# Configure asyncio mode
def pytest_configure(config: pytest.Config) -> None:
    config.option.asyncio_mode = "auto"
