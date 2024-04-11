"""clear
By Al Sweigart al@inventwithpython.com
Special thanks to David George for allowing me to use the Clear name on PyPI.

A cross-platform Python module that provides a clear() function which clears the terminal. That's all.

This function clears the terminal screen by printing an ascii code, works on all systems and an even simpler 1 liner

This module exists as a simpler alternative to defining this function on your own."""

__version__ = '2.0.1'

def clear():
	"""Simple clear function"""
	print("\33c")
