import java.io.BufferedReader;
import java.io.FileReader;
import java.math.BigInteger;

public class p13 {
    public static void main(String[] args) {
        
        BigInteger sum = new BigInteger("0");

        try (BufferedReader bfr = new BufferedReader(new FileReader("problem13\\number.txt"))) {
            String line = bfr.readLine();
            
            while (line != null) {
                BigInteger parsed = new BigInteger(line);
                sum = sum.add(parsed);

                line = bfr.readLine();
            }            
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println(sum.toString().substring(0, 10));
    }
}
