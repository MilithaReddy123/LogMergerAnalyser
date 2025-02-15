#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging

def main():
	os.makedirs("logs/msg/", exist_ok=True)
	#logging.basicConfig(filename='logs/msg/log_manage.txt', format='%(asctime)s -[%(pathname)s - %(lineno)d] - %(levelname)-8s %(message)s', filemode= 'a')
	#logger = logging.getLogger()
	#logger.setLevel(logging.INFO)
	#logging.info("A main file")
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logapp.settings')
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
