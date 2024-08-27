# This is just a simple way to use SDelete on files and folders from the conetext menu.

## What is SDelete
  SDelete is a part of Sysinternals which deletes files/folders so they are unrecoverable.
  
  ### How does it delete so the files/folders are unrecoverable
    Usually when you delete a file it's just removed from a list which stores where everything starts and how long they are. If someone wants to recover a file after they deleted it they can use many program which can recover files.
    SDelete doesn't just delete the entry, but first writes random data over the file/folder so even if someone knows where the file/folder was there'll be rubbish data, which can't even be recovered by advanced recovery techniques.
    In the release I set 10 passes (the data will be overwritten 10 times by random data) which is pleanty, I read that 3 letter agencies use 7 usually.

## How to use it from src
  ### Requiments:
    Rust (cargo) installed
    Python installed for the automatic setup script which just puts things in their proper place automatically, but I'll explain how to do that manually. The script only uses core libs (no need for installing additional libs)

  ### Almost fully automatic process:
    1. Open a terminal in the "setupScriptPy" dir, run the python file (python main.py)
    2. Run the registry file in the "registry" dir
  
  ### Manual process:
    1. Open a terminal in the main dir ("RustSDelete") and run "cargo build --release"
    2. Make a dir in the "C:/" called "RustSDelete" and copy or move the "RustSDelete.exe" from the "RustSDelete/target/release" dir to there.
    3. Make a dir in the "C:/" called "SDelete" and extract the zip from the "RustSDelete/SDelete" to there.
    4. Run the registry file in the "RustSDelete/registry" dir

  Try it (right click on files/folders in the file explorer and find "RustSDelete" in the context menu and click it) on files/folders you don't need or copy files and try it on thoes, if there're any issues report them or solve them I guess...
  You can delete multiple file/folder (s) by just selecting multiple by dragging or using shift or ctrl
