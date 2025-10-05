.PHONY: lint format typecheck all clean help

# Default target
all: lint format typecheck

# Run ruff linter with auto-fix
lint:
	uv run ruff check --fix src tests

# Run ruff formatter
format:
	uv run ruff format src tests

# Run type checker
typecheck:
	uv run basedpyright src tests

# Clean Python cache files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

# Show available targets
help:
	@echo "Available targets:"
	@echo "  lint      - Run ruff linter with auto-fix"
	@echo "  format    - Run ruff formatter"
	@echo "  typecheck - Run basedpyright type checker"
	@echo "  all       - Run lint, format, and typecheck"
	@echo "  clean     - Remove Python cache files"
	@echo "  help      - Show this help message"