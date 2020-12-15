import java.util.ArrayList;
import java.util.List;

/**
 * 38. Count and Say
 * Runtime 26.21 Memory 19.05
 */
public class CountAndSay {


    class Solution {

        public String countAndSay(int n) {

            if (n == 1) {
                return "1";
            }

            String base = countAndSay(n - 1);

            List<String> digits = new ArrayList<String>();
            StringBuffer digit = new StringBuffer();

            for (int i = 0; i < base.length(); i++) {
                if (i == 0) {
                    digit.append(base.charAt(i));
                    continue;
                }

                if (base.charAt(i) != digit.charAt(0)) {
                    digits.add(digit.toString());
                    digit = new StringBuffer();
                }
                digit.append(base.charAt(i));
            }
            digits.add(digit.toString());

            StringBuffer result = new StringBuffer();
            for (String d : digits) {
                String s = Integer.toString(d.length()) + d.charAt(0);
                result.append(s);
            }

            return result.toString();
        }

    }

    public static void main(String[] args) {
        CountAndSay c = new CountAndSay();
        Solution sol = c.new Solution();

        System.out.println(sol.countAndSay(4));

    }
}
