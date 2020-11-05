import java.io.BufferedReader;
import java.io.FileReader;

public class Problem8 {
    public static void main(String[] args) {
        
        String filename = "Problem8\\num.txt";

        try (BufferedReader bfr = new BufferedReader(new FileReader(filename))) {
            
            String line = bfr.readLine();

            

        } catch (Exception e) {
            e.printStackTrace();
            //TODO: handle exception
        }
    }
}