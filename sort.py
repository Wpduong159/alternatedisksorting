# -*- coding: utf-8 -*-

# William Duong, Nathan Whatley
# CPSC 335-01
# 14 February 2022

def disksSorted():
	"""Checks to see if light disks are to the left \
	   and dark disks are to the right"""
	benchmark = [0, 0, 0, 0, 1, 1, 1, 1]

	return True if disks2 == benchmark else False



def swap(x, y):
	"""Swaps two given elements in a list"""
	disks2[x], disks2[y] = disks2[y], disks2[x]



# Make some evenly-sized list with 2 distinct alternating characters [i.e. 01010101]
disks1 = [0, 1, 0, 1, 0, 1, 0, 1]
disks2 = [0, 1, 0, 1, 0, 1, 0, 1]



if __name__ == "__main__":
	"""Main function"""

	condition = False

	while (condition == False):
		for x in range(len(disks1)):
			print(disks2)
			if (disks1[x] == 0 and disks1[x+1] == 1):
				swap(x, x+1)
			else:
				pass
		condition = disksSorted()

print(disks2)
