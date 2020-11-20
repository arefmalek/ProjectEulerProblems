import javax.management.RuntimeErrorException;

public class LLQueue {
    Node head;
    Node tail;

    private class Node {
        int value;
        Node link;
    }

    public boolean isEmpty() {
        return head == null;
    }

    public void add(int value) {
        //fucking idiot we add to the end 
        //not beginning
        Node node = new Node();
        node.value = value;

        if (isEmpty()) head = tail = node;
        else {
            //tail is the one added to
            //so we can preserve FIFO
            tail.link = node;
            tail = node;
        }
    }

    public int remove() {
        int temp = head.value;
        head = head.link;

        if (isEmpty()) tail = null;

        return temp;        
    }

    public int peek() {
        return head.value;
    }
}