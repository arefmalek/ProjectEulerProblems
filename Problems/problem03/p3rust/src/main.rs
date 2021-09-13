fn main() {
    let upper_bound: i32 = 13195;

    let loop_lim = (upper_bound / 2 as i32) + 1;

    let a = vec![1; loop_lim];

    for i in 2..=loop_lim {
        if a[i] == 1 && upper_bound % i == 0 {
            // divisible
            for factor in (i..=loop_lim).step_by(2) {
                a[factor] = 0;
            }
        }
    }

}
