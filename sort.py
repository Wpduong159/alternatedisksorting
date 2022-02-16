# -*- coding: utf-8 -*-

# William Duong, Nathan Whatley
# CPSC 335-01
# 14 February 2022

# Code for sorting alternating light and dark disks

# Make some evenly-sized list with 2 distinct alternating characters [i.e. 01010101]
disks1 = []
benchmark = []


def makeLists(n):
	"""Generate the unsorted and sorted list"""
	for i in range(n):
		disks1.extend(['L', 'D'])
		benchmark.append('D')
	for i in range(n):
		benchmark.append('L')


def right():
	"""Traverse from left to right"""
	last = None
	for x in range(len(disks1)):
		# Check every 2 disks and swap if disk is dark and previous disk is light
		if disks1[x] == 'D' and last == 'L':
			disks1[x] = 'L'
			disks1[x-1] = 'D'
		last = disks1[x]


if __name__ == "__main__":
	"""Main function"""

	# Choose n for n light disks and n dark disks
	n = 5

	makeLists(n)

	print(disks1)

	while disks1 != benchmark:
		right()
		print(disks1)