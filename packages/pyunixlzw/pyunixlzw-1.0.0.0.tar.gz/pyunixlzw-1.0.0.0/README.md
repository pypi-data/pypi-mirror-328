# pyunixlzw
**pyunixlzw** is a "pure" python3 implementation of the Unix compress/uncompress tool.

## Usage
pyunixlzw comes with access to both a module and a script that serves as a semi-replacement for `(N)compress`.

### Module
```python
>>> import pyunixlzw
>>> print(pyunixlzw.compress(b'aaaaaaaaaa'))
b'\x1f\x9d\x90a\x02\n\x1c\x08'
>>> print(pyunixlzw.decompress(b'\x1f\x9d\x90a\x02\n\x1c\x08'))
b'aaaaaaaaaa'
```

### Script
```bash
$ pyunixlzw -h
usage: pyunixlzw [-h] [-d] [-c] [-b MAXBITS] [-f] [-v] [-V] file

A pure-Python3 implementation of UNIX compress and decompress.

positional arguments:
  file

options:
  -h, --help            show this help message and exit
  -d, --decompress      If given, decompression is done instead.
  -c, --stdout          Write output on stdout, don't remove original.
  -b, --maxbits MAXBITS
                        Parameter limits the max number of bits/code.
  -f, --force           Forces output file to be generated, even if one already exists, and even if no space is saved
                        by compressing.
  -v, --stats           Write compression statistics.
  -V, --version         Output version and author.
$ 
```

## Installation
```bash
pip install pyunixlzw
```

# WARNING
The compression function attempts to mirror `(N)compress` as close as possible, but there are times that a file compressed with `compress` ***will not match*** the output of a file compressed with `pyunixlzw`. This is due to logic that determines when to output a CLEAR code, which I was unable to replicate in my script. 

These mismatched files can still be handled with both `(N)compress` and `pyunixlzw`; the primary difference is that `(N)compress` offers a much better compression ratio in much more efficient logic. 

If anyone is able to integrate the CLEAR code logic, feel free to submit a note or pull request replacing the `check_clear` function contents in `compress.py` with the logic required to match. 
