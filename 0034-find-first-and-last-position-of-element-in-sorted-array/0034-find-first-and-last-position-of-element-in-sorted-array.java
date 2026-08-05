class Solution {
    public int[] searchRange(int[] nums, int target) {
        /*int first=-1;//two pointer at start and end first start with starting if it finds then index and second starts from  ends if it finds then index 
        int last=-1;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==target){
                first=i;
                break;
            }
        }
        for(int i=nums.length-1;i>=0;i--){
            if(nums[i]==target){
                last=i;
                break;
            }
        }
        return new int[]{first,last};*/
        
        int first = findBound(nums, target, true);
        if (first == -1) return new int[]{-1, -1};
        int last = findBound(nums, target, false);
        return new int[]{first, last};
    }

    private int findBound(int[] nums, int target, boolean findFirst) {
        int lo = 0, hi = nums.length - 1;
        int result = -1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;

            if (nums[mid] == target) {
                result = mid; // found a match, remember it

                if (findFirst) {
                    hi = mid - 1; // keep searching LEFT for an earlier one
                } else {
                    lo = mid + 1; // keep searching RIGHT for a later one
                }
            } else if (nums[mid] < target) {
                lo = mid + 1; // target is further right
            } else {
                hi = mid - 1; // target is further left
            }
        }

        return result;
    }
}
    
