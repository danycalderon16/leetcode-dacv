
class Solution:
	def search(self, nums, target):
		left = 0
		right = len(nums) - 1
		while left <= right:
			if nums[left] == target or nums[right] == target:
				return True

			piv = (left+right)//2

			if nums[left] == nums[piv]:
				left +=1
				continue

			if nums[piv] == target:
				return True
			
			if nums[left] < nums[piv] and nums[piv] < nums[right]:#sorted
				if target < nums[piv]:
					right -= 1
				else:
					left += 1
			else:#rotated
				if nums[left] < nums[piv]: #sorted left
					if target < nums[piv]:
						right -= 1
					else:
						left += 1
				else:	#sorted right
					if target > nums[piv]:
						left += 1
					else:
						right -= 1
		return False


if __name__ == "__main__":
    bs = Solution()
    print(bs.search([0 ,0, 1, 1, 2, 0], 2))
#   print(bs.search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18],0))
