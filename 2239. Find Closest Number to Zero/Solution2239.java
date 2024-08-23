class Solution2239 {

    public static int findClosestNumber(int[] nums) {
        boolean containSameButPositive = false;
        int closest = nums[0];
        for (int i = 0; i < nums.length; i++) {

            if (Math.abs(nums[i]) < Math.abs(closest))
                closest = nums[i];
        }

        for (int i : nums) {

            if (i == -closest) {
                containSameButPositive = true;
                break;
            }
        }

        if (closest < 0 && containSameButPositive) {
            return ((int) Math.abs(closest));
        } else {
            return (int) closest;
        }

    }
}

public static void main(String[] args) {
    int[] nums = { 2, 3, -1, -4, 2 };
    System.out.println(Solution2239.findClosestNumber(nums));
}
