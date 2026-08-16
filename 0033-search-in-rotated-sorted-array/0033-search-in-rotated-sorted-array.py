class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            
            # LEFT HALF IS SORTED
            # Check if nums[lo] <= nums[mid] (left portion is in sorted order)
            elif nums[lo] <= nums[mid]:
                
                # Check if target is in the sorted LEFT range [lo, mid]
                # Use <= on BOTH sides to include boundary values
                if nums[lo] <= target <= nums[mid]:
                    # Target is in left half, search left
                    hi = mid - 1
                else:
                    # Target is NOT in left half, must be in right half
                    lo = mid + 1
            
            # RIGHT HALF IS SORTED
            else:
                
                # Check if target is in the sorted RIGHT range [mid, hi]
                # Use <= on BOTH sides to include boundary values
                if nums[mid] <= target <= nums[hi]:
                    # Target is in right half, search right
                    lo = mid + 1
                else:
                    # Target is NOT in right half, must be in left half
                    hi = mid - 1
        
        # Target not found
        return -1