
import java.util.ArrayList;

class Solution56 {
    public static int[][] merge(int[][] intervals) {

        for (int i = 0; i < intervals.length; i++) {
            for (int j = 0; j < i; j++) {
                if (intervals[j][0] > intervals[i][0]) {
                    int[] temp = intervals[i];
                    intervals[i] = intervals[j];
                    intervals[j] = temp;
                }
            }
        }

        ArrayList<int[]> list = new ArrayList<>();

        for (int[] interval : intervals) {
            if (list.isEmpty() || list.get(list.size() - 1)[1] < interval[0]) {
                list.add(interval);
            } else {
                int[] arr = { list.get(list.size() - 1)[0], Math.max(list.get(list.size() - 1)[1], interval[1]) };
                list.set(list.size() - 1, arr);
            }
        }

        int[][] mergedIntervals = new int[list.size()][2];
        for (int i = 0; i < list.size(); i++) {
            mergedIntervals[i] = list.get(i);
        }

        return mergedIntervals;
    }

    public static void main(String[] args) {
        int[][] arr = { { 2, 6 }, { 1, 3 }, { 8, 10 }, { 15, 18 } };
        arr = merge(arr);

        for (int[] arr1 : arr) {
            System.out.print("[");
            for (int j = 0; j < arr[0].length; j++) {
                if (j == arr[0].length - 1) {
                    System.out.print(arr1[j]);
                } else {
                    System.out.print(arr1[j] + ",");
                }
            }
            System.out.print("],");
        }
    }
}