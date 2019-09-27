from pathlib import Path

import pytest
from typing import Dict


@pytest.fixture(scope="session")
def config() -> Dict:
    """ Any test config values to be used """
    from yaml import safe_load

    config_path: Path = Path(__file__).parent / "config.yml"
    if not config_path.is_file():
        return {}
    with config_path.open() as fp:
        return safe_load(fp)
