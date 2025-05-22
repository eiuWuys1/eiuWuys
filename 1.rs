fn main() {
    let (mut a, mut b) = (0, 1);
    for _ in 0..10 {
        println!("{}", a);
        let temp = a;
        a = b;
        b = temp + b;
    }
}
