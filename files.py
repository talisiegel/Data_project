# writingfiles.py
# Save this file, edit the three TODOs

from pathlib import Path
'''
=== QUICK LESSON: Files in 60 seconds ===

A file lives on disk. Python can open files to read or write.

Modes you need now:
  - 'w' : write mode. Creates a new file or replaces an existing file.
  - 'a' : append mode. Opens file and adds text to the end (keeps existing content).
  - 'r' : read mode. Read the file content.

Always use:
  with open(path, mode, encoding='utf-8') as f:
      ... use f.read() or f.write(...) ...
This guarantees the file is closed when you're done.

We will practice three tiny functions:
  - save_message(path, msg)    -> overwrite/create file with msg
  - append_message(path, msg)  -> add msg on a new line to end of file
  - load_message(path)         -> read and return entire file text

After you edit the TODOs, run this script. It will test your functions automatically.
'''

print(LESSON)

# ---------- Student TODOs: implement these three functions ----------
# You will replace the 'pass' in each one with code that uses 'with open(...)'

def save_message(path, msg):
    
    with open(path, "w", endcoding="utf-8") as f:
        f.write(msg)
 


def append_message(path, msg):
    """
    Add msg to the end of the file at `path`.
    Each appended message should be on its own line.
    If the file does not exist, append should create it.
    Example: append_message("note.txt", "more")
    After this, the file note.txt should include lines added earlier plus "more"
    """
    # TODO: open the file in append mode and write msg (with a newline)
    pass


def load_message(path):
    """
    Read the whole file and return it as a string.
    If the file does not exist, return an empty string.
    Example: load_message("note.txt") -> "first line\nsecond line"
    """
    # TODO: open the file in read mode and return its contents
    pass

