clean:
    @rm -rf dist/*
    @rm -rf .pytest_cache
    @rm -rf .ruff_cache
    @find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
    @echo "🧹 Cleaned built scripts and caches"

publish:
    @poetry build
    @poetry publish
