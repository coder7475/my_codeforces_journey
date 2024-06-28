use std::io;

fn main() {
  let stdin = io::stdin();
  let mut input = String::new();

  let _ = stdin.read_line(&mut input);

  // number of watermelon
  let num: i32 = input.trim().parse().unwrap(); // replace i32 with your desired integer type

  // Logic
  if num % 2 == 0 && num > 2 {
    println!("YES");
  } else {
    println!("NO")
  }
}