#!usr/bin/env python
# Yk+1 = Yk + DeltaT * Fk

from functionParser.py import parse

def euler_simple(delta, yk, fk, t_value=""):
	yk1 = yk+delta*parse(fk, t_value)
	return