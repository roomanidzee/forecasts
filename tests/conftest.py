from pathlib import Path

def pytest_unconfigure(config):
    file_path = Path(__file__).parent / Path("resources") / Path("test.db")
    file_path.unlink()

