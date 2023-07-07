#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings_produccion' if os.environ.get(
        'DJANGO_DEBUG') == 'False' else 'djangoProject.settings')
    os.environ.setdefault('DJANGO_DEBUG', 'False' if os.environ.get('DJANGO_DEBUG') == 'False' else 'True')
    # os.environ.setdefault("DATABASE_URL", f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
