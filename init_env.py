from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parent
ENV_EXAMPLE = ROOT / ".env.example"
ENV_FILE = ROOT / ".env"

if not ENV_EXAMPLE.exists():
    print(".env.example not found in project root")
    sys.exit(1)

if ENV_FILE.exists():
    print(".env already exists. Nothing to do.")
    sys.exit(0)

shutil.copy(ENV_EXAMPLE, ENV_FILE)
print(".env created successfully from .env.example")
print("Edit .env if needed, then run your tests")
