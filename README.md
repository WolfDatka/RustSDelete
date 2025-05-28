# This is just a simple way to utalize SDelete on files and folders using the conetext menu. (Windows only)
    (I made this because I thought there isn't a GUI for it, but I recently heard that there actually is, so you may want to try that first)

# !!! Be avare that this only works on HDDs and will reduce the lifespan of SSDs somewhat significantly !!!

## What is SDelete
SDelete is a part of Sysinternals, which deletes files/folders so they are unrecoverable.
  
### How does it delete so that the files/folders are unrecoverable
Usually when you delete a file it's just removed from a list, which stores where that file starts, or what the folder contains (keep in mind that this is hugely oversimplified). If someone wants to recover a file after it's been deleted, there are many programs, which can recover files.

SDelete doesn't just delete the entry, but first writes random data over the file/folder so even if someone knows where the file/folder was there'll be rubbish data there, which can't even be recovered by advanced recovery techniques.
    In the release I set 10 passes (the data will be overwritten 10 times by random bytes) which is VERY overkill, 3 passes should be pleanty.

## How to use it from src
### Requiments:
Rust (cargo) installed

Python installed for the automatic setup script which just puts things in their proper place automatically, but I'll explain how to do that manually. The script only uses core libs (no need for installing additional libs)

### Almost fully automatic process:
1. Open a terminal in the "setupScriptPy" dir, run the python file (python main.py)
2. Run the registry file in the "registry" dir
  
### Manual process:
1. Open a terminal in the main dir ("RustSDelete") and run "cargo build --release"
2. Make a dir in the "C:" called "RustSDelete"
3. Copy or move the "RustSDelete.exe" from the "RustSDelete/target/release" dir -> to the "RustSDelete" at "C:"
4. Make a dir in the "C:/RustSDelete" dir, called "SDelete" and extract the contents of the zip from the "RustSDelete/SDelete" to there
5. Run the registry file in the "RustSDelete/registry" dir

Try it (right click on files/folders in the file explorer and find "RustSDelete" in the context menu and click it) on files/folders you don't need or copy files and try it on thoes, if there're any issues report them or solve them I guess...

You can delete multiple file/folder (s) by just selecting multiple by dragging or using shift or ctrl

!!! BE VERY CAREFUL, WHAT YOU DELETE IS JUST ABOUT AS UNRECOVERABLE AS THEY CAN BE !!!
