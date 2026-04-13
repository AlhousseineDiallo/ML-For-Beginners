from pathlib import Path

PROJ_ROOT: Path = Path('__file__').resolve().parents[0]
REGRESSION_DIR = PROJ_ROOT / '2-Regression'
REGRESSION_DATA_DIR = REGRESSION_DIR / 'data'
CLASSIFICATION_DIR = PROJ_ROOT / '4-Classification'
CLASSIFICATION_DATA_DIR = CLASSIFICATION_DIR / 'data'


if __name__ == "__main__":
    print(PROJ_ROOT)
    print(REGRESSION_DIR)
    print(REGRESSION_DATA_DIR)