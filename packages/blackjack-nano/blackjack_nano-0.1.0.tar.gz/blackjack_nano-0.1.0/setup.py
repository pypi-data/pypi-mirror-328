from setuptools import setup

setup(
	name="blackjack_nano",
	version="0.1.0",
	py_modules=["blackjack"],
	entry_points={
		"console_scripts": ["blackjack=blackjack:main"]
	},
)
