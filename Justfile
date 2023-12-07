clean:
    @rm -rf dist/*
    @rm -rf .pytest_cache
    @rm -rf .ruff_cache
    @rm -rf docs/_build/*
    @find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
    @echo "🧹 Cleaned built scripts and caches"

docs:
    @just clean
    @cd docs && make html
    @python -m http.server -d docs/_build/html

publish:
    @poetry build
    @poetry publish

test:
    @tox
