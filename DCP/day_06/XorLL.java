public class XorLL {
    private class Node{
        Node xor;
        int val;
    }

    Node head;
    Node tail;

    public boolean isEmpty() {
        return head == null;
    }

    public void add(int val) {
        Node node = new Node();
        node.val = val;

        if (isEmpty()) {
            head = tail = node;
        }
        else {
            tail.xor = dereference_pointer(tail.hashCode() ^ node.hashCode());
            tail = node;
        }
    }

    public Node dereference_pointer(int input) {
        System.out.println("ligma boy");
        return head;
    }
}
