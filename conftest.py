import sys
from pathlib import Path

# Add the src directory to Python path so imports work correctly
src_path = Path(__file__).parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))
