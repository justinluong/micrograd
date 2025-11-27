default:
  just --list

# Run tests
test *args:
    uv run pytest tests/ {{args}}

# Delete student implementation files
reset:
    rm -f src/micrograd/engine.py src/micrograd/nn.py
