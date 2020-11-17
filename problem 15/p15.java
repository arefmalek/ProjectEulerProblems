public class p15{
    public static void main(String[] args) {
        int size = 20;
        int[][] map = new int[size][size];
        for (int[] is : map) {
            for (int is2 : is) {
                System.out.print(is2);
            }
            System.out.println();
        }
    }
}