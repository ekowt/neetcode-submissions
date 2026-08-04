class Solution {
    public boolean hasDuplicate(int[] nums) {
 
        HashSet<Integer> set = new HashSet<>();

        for(int i = 0; i<nums.length; i++)
        {
            if(!set.contains(nums[i]))
            {
                set.add(nums[i]);
            }
            else if(set.contains(nums[i]))
            {
                return true;
            }
        }

        return false;
    }
}
