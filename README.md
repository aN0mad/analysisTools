# Project Title

Malware analysis tools used alongside "Practical Malware Analysis: The Hands-on Guide to Dissecting Malicious Software" Book by Andrew Honig and Michael Sikorski. Some are custom written but most are straight from their book.


### Installing

A step by step series of examples that tell you how to download the repo

Use command line git or download with a browser


*Using Git

Navigate to the directory where the repo will be cloned and then use
```
git clone https://github.com/rptucker/analysisTools.git
```
Move into the directory to access the tools and installers

## Tools
* [Dependecy Walker](http://www.dependencywalker.com/) - A utility that scans any 32-bit or 64-bit Windows module (exe, dll, ocx, sys, etc.) and builds a hierarchical tree diagram of all dependent modules
* hasher.py - A script written by me to compute file hashes, it currently supports MD5, SHA1, and SHA256
* hasher - The compiled binary of hasher.py
* [PIeD](https://www.aldeid.com/wiki/PEiD) - detects most common packers, cryptors and compilers for PE files, however support was discontinued since April 2011
* [strings.exe](https://docs.microsoft.com/en-us/sysinternals/downloads/strings) - It scans the file you pass it for UNICODE (or ASCII) strings of a default length of 3 or more UNICODE (or ASCII) characters

## Acknowledgments

* The stackoverflow community
* My dog
