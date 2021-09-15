fn main() {
    let upper_bound: i64 = 600851475143;

    let loop_lim = ((upper_bound as f64).sqrt() as i64) + 1;

    let mut a = vec![1; loop_lim as usize];

    let mut answer = 0;
    for i in 2..loop_lim {
        if a[i as usize] == 1 && upper_bound % i == 0 {
            // divisible
            answer = i;
            for factor in (i..loop_lim).step_by(i as usize) {
                a[factor as usize] = 0;
            }
        }
    }

    println!("{}", answer)

}
