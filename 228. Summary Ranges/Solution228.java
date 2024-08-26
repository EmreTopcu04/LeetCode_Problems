
import java.util.ArrayList;
import java.util.List;

class Solution228 {
    public static List<String> summaryRanges(int[] nums, ArrayList<String> arrayList) {
        ArrayList<String> list = new ArrayList<>();
        int i = 0;
        while (i < nums.length) {
            int start = nums[i];
            while (i < nums.length - 1 && nums[i] + 1 == nums[i + 1]) {
                i++;
            }
            if (start != nums[i]) {
                list.add(start + "->" + nums[i]);
            } else {
                list.add(String.valueOf(nums[i]));
            }
            i++;
        }

        return list;

    }

    public static void main(String[] args) {
        int[] nums = { 0, 1, 2, 4, 5, 7 };
        System.out.println(summaryRanges(nums, new ArrayList<String>()));
    }
}