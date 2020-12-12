'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]
'''
class Solution(object):
	def sortColors(self, arr):
		zero,one,two = 0,0,0
		for val in arr:
			if val==0:
				zero+=1
			elif val==1:
				one += 1
			else:
				two +=1
		for i in range(len(arr)):
			if zero!=0:
				arr[i]=0
				zero-=1
			elif zero==0 and one!=0:
				arr[i]=1
				one-=1
			elif zero==0 and one==0:
				arr[i]=2
				two-=1
		return arr
