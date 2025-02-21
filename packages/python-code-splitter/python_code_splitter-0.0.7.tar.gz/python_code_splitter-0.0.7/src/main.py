import sys
from pathlib import Path

from src.code_splitter import CodeSplitter


def main():
    if len(sys.argv) != 2:
        print("Usage: python code_splitter.py path/to/models.py")
        sys.exit(1)
    CodeSplitter(original_file_path=Path(sys.argv[1])).execute()


if __name__ == "__main__":
    main()
