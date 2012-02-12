#!usr/bin/env python
from math import sin, asin, cos, acos, atan, tan, factorial

def parse(function, t_value):
	replaces = {
				"sen(":"sin(", 
				"arcsen(":"asin(",
				"arccos(":"acos(",
				"tg(":"tan(",
				"arctg(":"atan(",
	}

	model = "result=function"
	model = model.replace("function",function)
	model = model.replace("T",t_value)
	for old, new in replaces:
		model = model.replace(old, new)
	model = parse_factorial(model)
	exec model
	return result

def parse_factorial(function):
	while function.find("!") > -1:
		value = find_factorial(function, factorial)
		old = "value!"
		old = old.replace("value",value)
		f_factorial = "factorial(value)"
		f_factorial = f_factorial.replace("value",value)
		function = function.replace(old,f_factorial)
	return function

def find_factorial(function, factorial_index):
	value = function[0,factorial_index-1]
	while !value.isnumeric():
		value = value[1:]
	return value