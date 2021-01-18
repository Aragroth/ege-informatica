use std::fs::File;
use std::io::{BufRead, BufReader, Error, ErrorKind, Read};

struct Data {
    len: i32,
    size: i32,
    data: Vec<i32>,
}

fn read<R: Read>(io: R) -> Data {
    let mut buffer = BufReader::new(io);

    let mut first_line = String::new();
    buffer.read_line(&mut first_line).unwrap();

    let mut parts = first_line.split_whitespace().map(|s| s.parse::<i32>());
    let (len, size) = match (parts.next(), parts.next()) {
        (Some(Ok(a)), Some(Ok(b))) => (a, b),
        _ => panic!("error"),
    };

    Data {
        len,
        size,
        data: buffer
            .lines()
            .map(|line| {
                line.and_then(|v| v.parse().map_err(|e| Error::new(ErrorKind::InvalidData, e)))
            })
            .filter_map(Result::ok)
            .collect(),
    }
}

struct Elem {
    files: Vec<i32>,
    sum: i32
}

fn main() {
    let all = read(File::open("./26.txt").unwrap());
    let big_cargos = all.data.into_iter().filter_map(|i| {
        if 210 <= i && i <= 220 { Some(i) }
        else { None }
    }).collect::<Vec<_>>();
    
    
    let variants: Vec<Option<Elem>> = vec![None; big_cargos.iter().sum::<i32>() as usize];
    println!("{}", variants.len())
}
