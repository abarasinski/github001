"""Liczy iloczyn podanych argumentów."""

import sys

if len(sys.argv) < 2:  # sys.argv[0] = iloczyn.py
    print("Musisz podać co najmniej jedną liczbę .")
else:
    wyrazenie = "*".join(sys.argv[1:])
    print(wyrazenie, "=", eval(wyrazenie))
