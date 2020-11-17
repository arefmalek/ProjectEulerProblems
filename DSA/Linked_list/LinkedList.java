public class LinkedList{
    private Node head;
    private int size;

    private class Node {
        String value;
        Node link;

        Node (String value) {
            this.value = value;
            size++;
        }
    }

    //constructor
    public LinkedList() {
        head = null;
        size = 0;
    }

    //add method
    public void add(String value) {
        Node node = new Node(value);
        node.link = head;
        head = node;
    }

    //toArray() method
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

    //getSize() method
    public int getSize() {
        return size;
        // //lol
        // int answer = 0;
        // Node node = head;
        // while (node != null) {
        //     answer++;
        //     node = node.link;
        // }

        // return answer;
    }
}