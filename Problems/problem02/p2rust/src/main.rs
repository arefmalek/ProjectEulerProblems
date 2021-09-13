fn main() {
    let mut fib0 = 0;
    let mut fib1 = 1;

    let mut sum = 0;
    while fib1 < 4_000_000 {
        if fib1 % 2 == 0 {
            sum += fib1;
        }
        let temp = fib1;
        fib1 += fib0;
        fib0 = temp;
    }

    println!("{}", sum)
}
