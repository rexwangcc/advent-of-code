use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;


fn main() {
    let res = solution("inputs.txt", 2020);
    println!("{:?}", res);
}

fn solution(filename: &str, target: i32) -> i32 {
    // Read inputs
    let f = File::open(filename).unwrap();
    let f = BufReader::new(f);

    // Create a lookup map and result
    let mut set:HashSet<i32> = HashSet::new();
    let mut res = 0;

    for line in f.lines() {
        // convert to int32
        let curr = line.unwrap().parse::<i32>().unwrap();
        let complement = target - curr;

        if set.contains(&complement) {
            res = curr * complement;
            break;
        } else {
            set.insert(curr);
        }
    }
    // return the result
    res
}
