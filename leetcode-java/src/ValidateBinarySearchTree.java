import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class ValidateBinarySearchTree {

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }


    class Solution {
        public boolean isValidBST(TreeNode root) {

            Stack<TreeNode> stack = new Stack<>();
            stack.add(root);

            List<TreeNode> visited = new ArrayList<>();
            while (!stack.isEmpty()) {
                TreeNode node = stack.pop();

                if (node.left == null && node.right == null) {
                    visited.add(node);
                }

                if (node.left != null && node.right == null) {
                    if (visited.contains(node.left)) {
                        visited.add(node);
                    } else {
                        stack.add(node);
                        stack.add(node.left);
                    }
                }

                if (node.left == null && node.right != null) {
                    visited.add(node);
                    stack.add(node.right);
                }

                if (node.left != null && node.right != null) {
                    if (visited.contains(node.left)) {
                        visited.add(node);
                        stack.add(node.right);
                    } else {
                        stack.add(node);
                        stack.add(node.left);
                    }
                }
            }

            for (int i = 0; i < visited.size() - 1; i++) {
                if (visited.get(i).val >= visited.get(i + 1).val) {
                    return false;
                }
            }

            return true;
        }
    }

    public static void main(String[] args) {


    }
}
