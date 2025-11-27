default:
  just --list

# Run tests
test *args:
    uv run pytest tests/ {{args}}

# Reset student implementation files to skeleton
clean:
    git checkout src/micrograd/engine.py src/micrograd/nn.py
