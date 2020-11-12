import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Problem8 {
    public static void main(String[] args) {
        
        String filename = "Problem8\\num.txt";
        String doc = "";
        
        try (BufferedReader bfr = new BufferedReader(new FileReader(filename))) {
            
            String line = bfr.readLine();

            while(line != null) {
                doc += line;
                line = bfr.readLine();
            }
        } catch (Exception e) {
            e.printStackTrace();
            //TODO: handle exception
        }

        char[] pog = doc.toCharArray();
        int[] yes = new int[pog.length];


        for (int i = 0; i < yes.length; i++) {
            yes[i] = Character.getNumericValue(pog[i]);
        }


        long max = 0;
        for (int i = 0; i < yes.length - 12; i++) {
            int[] temp = Arrays.copyOfRange(yes, i, i + 13);

            long prod = 1;
            for (int j : temp) {
                prod *= j;
            }
            if (prod > max) {
                max = prod;
            }
        }

        System.out.println(max);
    }
}