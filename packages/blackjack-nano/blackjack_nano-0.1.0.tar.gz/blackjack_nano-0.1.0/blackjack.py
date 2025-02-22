#!/usr/bin/env python3

import argparse

def main():
	parser = argparse.ArgumentParser(description="A simple Blackjack game")
	parser.add_argument("--name", type=str, help="Your name")
	args = parser.parse_args()

	print(f"Hello, {args.name or 'World'}!")

if __name__ == "__main__":
	main()
