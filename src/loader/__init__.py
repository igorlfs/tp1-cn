import sys

from src.args import load_config_from_args
from src.loader.test import load_test_config

# Hack to load a default config if running a test
config = load_test_config() if "pytest" in sys.modules else load_config_from_args()
