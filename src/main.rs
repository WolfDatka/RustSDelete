#![windows_subsystem = "windows"]

use std::env::args;
use std::process::Command;

fn main() {
    let args: Vec<String> = args().collect();

    let exe_path = "C:/RustSDelete/SDelete/sdelete.exe";
    let args = ["-p", "10", "-s", "-nobanner", &args[1]];

    Command::new(exe_path)
        .args(args)
        .output()
        .expect("Failed to execute process");
}
