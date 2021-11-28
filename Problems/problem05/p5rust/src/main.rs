fn sieve(i32: limit) -> Vec<i32> {
    // sieve's algorithm
    let mut answer = Vec::new();
    let numbers = [true; limit];

    for i in 2..limit {
        if numbers[i] {
            answer.push(i);
            for j in (i*i..number).step_by(i) {
                numbers[j] = false;
            }
        }
    }

    return answer;
}

fn smallest_multiple(i32: upper_limit) -> i32 {
    // get the primes (guarantee to be there)



    return 0;
}

fn main() {
    println!("Hello, world!");
    let var = sieve(10);
    println!("{}", var);
}
