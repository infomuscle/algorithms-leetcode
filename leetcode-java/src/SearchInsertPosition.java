/**
 * 35. Search Insert Position
 * Runtime 100 Memory 98.49
 */
public class SearchInsertPosition {

    class Solution {
        public int searchInsert(int[] nums, int target) {

            int answer = 0;

            for (int i = 0; i < nums.length; i++) {
                if (nums[i] < target) {
                    answer += 1;
                } else {
                    break;
                }
            }

            return answer;
        }
    }

    public static void main(String[] args) {

        Solution sol = new SearchInsertPosition().new Solution();

        int[] n1 = {1, 3, 5, 6};
        int t1 = 5;
        int t2 = 2;
        int t3 = 7;
        int t4 = 0;

        int[] n2 = {1};
        int t5 = 0;

        System.out.println(sol.searchInsert(n1, t1));
        System.out.println(sol.searchInsert(n1, t2));
        System.out.println(sol.searchInsert(n1, t3));
        System.out.println(sol.searchInsert(n1, t4));
        System.out.println(sol.searchInsert(n2, t5));
    }
}
