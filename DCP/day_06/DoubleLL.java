import javax.management.RuntimeErrorException;

public class DoubleLL {

    private class Node{
        Node prevNode;
        Node nextNode;
        int value;

        Node(int value) {
            this.value = value;
            size++;
        }
    }

    Node head;
    Node tail;
    int size = 0;

    private boolean isEmpty() {
        return (head == null);
    }

    public void add(int value) {
        Node node = new Node(value);

        if (isEmpty()) head = tail = node;
        else {
            tail.nextNode = node;
            node.prevNode = tail;
            tail = node;
        }
    }

    public Node get(int index) {
        if (index >= size) return null;
        //optimize?
        Node temp = head;
        for (int i = 0; i < index; i++) {
            temp = temp.nextNode;
        }
        return temp;
        
    }

    public static void main(String[] args) {
        DoubleLL dll = new DoubleLL();

        dll.add(1);
        dll.add(4);

    }
}
