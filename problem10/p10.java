
public class p10 {
	public static void main(String[] args) {
		System.out.println(processing(2_000_000));
	}

	public static long processing(int limit) {

		long sum = 0;
		
		int[] blist = new int[limit];

		//cool lessons: think about all parts of an algorithm:
		//how it works is nice but also how each part 
		//plays into the solution because that allows implementation
		
		for (int i = 2; i < limit; i++) {
			if (blist[i] == 0) {
				sum += i;

				if (i < Math.sqrt(limit) + 1) {
					for (int j = i*i; j < limit; j += i) {
						blist[j] = 1;
					}
				}
				
			}
		}

		return sum;
	}
}