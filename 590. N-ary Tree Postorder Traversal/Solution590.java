import java.util.ArrayList;
import java.util.List;

class Node {
    public int val;
    public List<Node> children;

    public Node() {
    }

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};

class Solution590 {

    public static List<Integer> postorder(Node root) {
        ArrayList<Integer> list = new ArrayList<>();
        if (root == null) {
            return list;
        }

        dfs(root, list);

        return list;

    }

    private static void dfs(Node root, ArrayList<Integer> list) {

        for (Node node : root.children) {
            dfs(node, list);
        }
        list.add(root.val);

    }

    public static void main(String[] args) {

    }
}
