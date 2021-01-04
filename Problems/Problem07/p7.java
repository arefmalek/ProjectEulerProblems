import java.util.ArrayList;

public class p7 {
	public static void main(String[] args) {
		//find out later

		System.out.println(processing(10_001));
	}

	public static boolean is_Prime(int input) {
		
		if (input % 2 == 0) return false;

		for (int i = 3; i < input/2 + 1; i += 2) {
			if (input % i == 0) return false;
		}

		return true;
	}

	public static int processing(int limit) {

		ArrayList<Integer> aye = new ArrayList<Integer>();

		aye.add(2);
		int i = 2;

		while (aye.size() < limit) {
			if (is_Prime(i)) {
				aye.add(i);
			}
			i++;
		}

		return aye.get(aye.size() - 1);
	}
}