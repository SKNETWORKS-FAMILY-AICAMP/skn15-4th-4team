#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django가 설치되어 있어야 합니다. pip install django 실행해 주세요."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
