import org.graalvm.compiler.graph.Node;

public class LinkedListV2 {
    private Node head;
    private Node tail;
    private int size;

    private class Node {
        String value;
        Node link;

        Node(String value) {
            this.value = value;
            size++;
        }
    }

    LinkedListV2() {
        head = tail = null;
        size = 0;
    }

    public void add(String val) {
        Node node = new Node(val);
        //this next line for edge case for creating first Node
        if (head == null) head = node;

        //dodges first 
        if (tail != null) tail.link = node;
        tail = node;
    }
    
    public String[] toArray() {
        String[] array = new String[size];
        int i = 0;
        Node node = head;
        while (node != null) {
            array[i++] = node.value; //note how the loop increments i for us
            node = node.link;
        }

        return array;
    }
}
