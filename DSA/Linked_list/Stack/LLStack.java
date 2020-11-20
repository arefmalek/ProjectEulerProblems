public class LLStack {
    Node head;

    private class Node {
        Node link;
        int value;

        Node(int val) {
            this.value = val;
        }
    }

    public boolean isEmpty() {
        return head == null;
    }

    public void push(int value) {
        Node node = new Node(value);

        node.link = head;
        head = node;
    }

    public int pop() {
        int answer = 0;

        answer = head.value;
        head = head.link;

        return answer;
    }
}