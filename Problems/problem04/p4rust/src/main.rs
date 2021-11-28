fn largest_palindrome() -> i32 {
    let mut answer = 0; // very obviously the largest value here
    for i in 100..1000 {
        for j in i..1000 {
            let mut product = i * j;

            // check if product is palindrome
            let mut reversed = 0;

            while product != 0 {
                reversed *= 10;
                reversed += product % 10;
                product = (product / 10) as i32;
            }
            let product = i * j;
            if reversed == product && product > answer {
                answer = product;
            }
        }
    }
    return answer;
}

fn main() {
    let answer = largest_palindrome();
    println!("{}",answer);
}
