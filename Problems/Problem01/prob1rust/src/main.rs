fn main() {
    let lower_bound: u32  = 1;
    let upper_bound: u32= 1000;

    let mut sum: u32 = 0;

    for val in lower_bound..upper_bound {
        if val % 5 == 0 {
            sum += val;
        } else if val % 3 == 0 {
            sum += val;
        }
    }

    println!("{}", sum);

}
