use std::path::Path;
use std::mem;
use std::string::String;
use rand::Rng;

const WIDTH:usize = 768;
const HEIGHT:usize = 768;
const CS:usize = 256-1;
const CE:usize = 512;

fn main() {
    let img = random_merge_plus();
    
    save_image(img, &String::from("image.png"));
}

fn random_bg() -> Vec<Vec<Vec<u8>>> {
    let mut img: Vec<Vec<Vec<u8>>> = vec![vec![vec![0; 3]; WIDTH]; HEIGHT];
    for i in 1..HEIGHT {
        for j in 1..WIDTH {
            let t1:u8 = (img[i-1][j-1][0] as i16 + rand::thread_rng().gen_range(-10..=10)) as u8;
            let t2:u8 = (img[i-1][j-1][1] as i16 + rand::thread_rng().gen_range(-10..=10)) as u8;
            let t3:u8 = (img[i-1][j-1][2] as i16 + rand::thread_rng().gen_range(-10..=10)) as u8;
            img[i][j] = vec![t1, t2, t3];
        }
    }
    img
}

fn save_image(img: Vec<Vec<Vec<u8>>>, name: &str) {
    let mut img2: Vec<u8> = vec![0; WIDTH*HEIGHT*3];
    
    for i in 0..HEIGHT {
        for j in 0..WIDTH {
            for k in 0..3 {
                img2[i*WIDTH*3 + j*3 + k] = img[i][j][k];
            }
        }
    }
    
    image::save_buffer(&Path::new(name), &img2, WIDTH as u32, HEIGHT as u32, image::ColorType::Rgb8);
}

fn random() -> Vec<Vec<Vec<u8>>> {
    let mut img = random_bg();
    for i in CS..CE {
        for j in CS..CE {
            img[i][j] = vec![rand::thread_rng().gen_range(0..=255), rand::thread_rng().gen_range(0..=255), rand::thread_rng().gen_range(0..=255)]
        }
    }
    img
}

fn random_bp() -> Vec<Vec<Vec<u8>>> {
    let mut img = random_bg();
    for i in (CS..CE).step_by(8) {
        for j in (CS..CE).step_by(8) {
            let r = rand::thread_rng().gen_range(0..=255);
            let g = rand::thread_rng().gen_range(0..=255);
            let b = rand::thread_rng().gen_range(0..=255);
            for k in i..i+8 {
                for l in j..j+8 {
                    img[k][l] = vec![r, g, b];
                }
            }
        }
    }
    img
}

fn random_merge() -> Vec<Vec<Vec<u8>>> {
    let mut img = random_bg();
    for i in CS..CE {
        for j in CS..CE {
            img[i][j] = vec![(img[i-1][j][0].wrapping_add(img[i][j-1][0]))/2, (img[i-1][j][1].wrapping_add(img[i][j-1][1]))/2, (img[i-1][j][2].wrapping_add(img[i][j-1][2]))/2];
        }
    }
    img
}

fn random_merge_bp() -> Vec<Vec<Vec<u8>>> {
    let mut img = random_bg();
    for i in (CS..CE).step_by(8) {
        for j in (CS..CE).step_by(8) {
            let r = (img[i-1][j][0].wrapping_add(img[i][j-1][0]))/2;
            let g = (img[i-1][j][1].wrapping_add(img[i][j-1][1]))/2;
            let b = (img[i-1][j][2].wrapping_add(img[i][j-1][2]))/2;
            for k in i..i+8 {
                for l in j..j+8 {
                    img[k][l] = vec![r, g, b];
                }
            }
        }
    }
    img
}

fn random_merge_plus() -> Vec<Vec<Vec<u8>>> {
    let mut img = random_bg();
    let mut lb = rand::thread_rng().gen_range(0..=100);
    let mut rb = rand::thread_rng().gen_range(0..=100);
    if lb > rb {
        mem::swap(&mut lb, &mut rb);
    }
    if lb == rb {
        rb += 1;
    }

    for i in CS..CE {
        for j in CS..CE {
            let add = rand::thread_rng().gen_range(lb..=rb);
            img[i][j] = vec![((img[i-1][j][0].wrapping_add(img[i][j-1][0]))/2).wrapping_add(add), ((img[i-1][j][1].wrapping_add(img[i][j-1][1]))/2).wrapping_add(add), ((img[i-1][j][2].wrapping_add(img[i][j-1][2]))/2).wrapping_add(add)];
        }
    }
    img
}
