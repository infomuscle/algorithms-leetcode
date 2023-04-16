import java.util.HashMap;
import java.util.Map;

/**
 * 1. Two Sum
 * Runtime 82.14 Memory 85.32
 */
public class TwoSum {

    class Solution {
        public int[] twoSum(int[] nums, int target) {

            Map<Integer, Integer> counters = new HashMap<>();

            for (int i = 0; i < nums.length; i++) {
                if (counters.containsKey(nums[i])) {
                    return new int[]{i, counters.get(nums[i])};
                }
                counters.put(target - nums[i], i);
            }

            throw new RuntimeException("no answers");
        }
    }

    public static void main(String[] args) {

        int[] n1 = {2, 7, 11, 15};
        int t1 = 9;

        TwoSum twoSum = new TwoSum();
        Solution solution = twoSum.new Solution();

        solution.twoSum(n1, t1);
    }
}
