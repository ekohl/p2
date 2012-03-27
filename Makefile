PYTHON=/usr/bin/env python

check:
	$(PYTHON) -m unittest discover --start-directory tests
