use std::fs::File;
use std::io::Write;
use std::path::Path;
use rand::Rng;

const WIDTH:usize = 768;
const HEIGHT:usize = 768;
const CS:usize = 256;
const CE:usize = 512;

fn main() {
    let img = random_bg();
    
    
    let mut img2: Vec<u8> = vec![0; WIDTH*HEIGHT*3];
    
    for i in 0..HEIGHT {
        for j in 0..WIDTH {
            for k in 0..3 {
                img2[i*WIDTH*3 + j*3 + k] = img[i][j][k];
            }
        }
    }

    image::save_buffer(&Path::new("image.png"), &img2, WIDTH as u32, HEIGHT as u32, image::ColorType::Rgb8);
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
    return img;
}


/*
fn random(img: Vec<Vec<Vec<u8>>>) -> Vec<Vec<Vec<u8>>> {
    for i in CS..CE {
        for j in CS..CE {
            img[i][j] = vec![rand::thread_rng().gen_range(0..=255), rand::thread_rng().gen_range(0..=255), rand::thread_rng().gen_range(0..=255)]
        }
    }
}

*/