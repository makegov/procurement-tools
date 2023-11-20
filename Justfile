clean:
    rm -rf dist/*
    rm -rf .pytest_cache
    find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf


publish:
    @poetry build
    @poetry publish
