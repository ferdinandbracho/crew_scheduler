.PHONY: setup demo

# Default target when you just type 'make'
help:
	@echo "Available commands:"
	@echo "  make setup    - Set up the development environment"
	@echo "  make demo     - Run the solar scheduler demo"

# Set up the development environment
setup:
	@echo "Setting up the development environment..."
	@if ! command -v uv >/dev/null 2>&1; then \
		echo "Installing uv..."; \
		curl -sSf https://astral.sh/uv/install.sh | sh; \
	else \
		echo "uv is already installed"; \
	fi
	uv pip install -e .

# Run the demo
run:
	@echo "Running the solar scheduler demo..."
	uv run python -m solar_scheduler.cli

# Alias for run
demo: run
