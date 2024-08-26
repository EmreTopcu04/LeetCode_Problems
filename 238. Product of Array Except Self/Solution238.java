class Solution238 {
    public static int[] productExceptSelf(int[] nums) {

        int[] result = new int[nums.length];
        int[] leftArray = new int[nums.length];
        int[] rightArray = new int[nums.length];
        int leftSide = 1;
        int rightSide = 1;
        for (int i = 0; i < nums.length; i++) {

            int j = nums.length - 1 - i;
            leftArray[i] = leftSide;
            rightArray[j] = rightSide;
            leftSide *= nums[i];
            rightSide *= nums[j];
        }

        for (int i = 0; i < result.length; i++) {
            result[i] = leftArray[i] * rightArray[i];
        }
        return result;

    }

    public static void main(String[] args) {
        int[] nums = { 1, 2, 3, 4 };
        int[] solution = productExceptSelf(nums);
        for (int i = 0; i < solution.length; i++) {
            System.out.print(solution[i] + " ");
        }
    }
}
