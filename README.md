# Project Title

Malware analysis tools used alongside "Practical Malware Analysis: The Hands-on Guide to Dissecting Malicious Software" Book by Andrew Honig and Michael Sikorski. Some are custom written but most are straight from the book.


### Installing

A step by step series of examples that tell you how to download the repo

Use command line git or download with a browser


* Using Git

Navigate to the directory where the repo will be cloned and then use
```
git clone https://github.com/rptucker/analysisTools.git
```
Move into the directory to access the tools and installers

## Tools
* [Dependecy Walker](http://www.dependencywalker.com/) - A utility that scans any 32-bit or 64-bit Windows module (exe, dll, ocx, sys, etc.) and builds a hierarchical tree diagram of all dependent modules
* hasher.py - A script written by me to compute file hashes, it currently supports MD5, SHA1, and SHA256
* hasher - The compiled binary of hasher.py
* [PEBrowse Professional](http://www.smidgeonsoft.prohosting.com/pebrowse-pro-file-viewer.html) - a static-analysis tool and disassembler for Win32/Win64 executables and Microsoft .NET assemblies. 
* [PEiD](https://www.aldeid.com/wiki/PEiD) - detects most common packers, cryptors and compilers for PE files, however support was discontinued since April 2011
* [PEview](https://www.aldeid.com/wiki/PEView) - Used for viewing the PE file header
* [reshacker_setup.exe](http://www.angusj.com/resourcehacker/#download) - Resource Hacker™ has been designed to be the complete resource editing tool: compiling, viewing, decompiling and recompiling resources for both 32bit and 64bit Windows executables.
* [strings.exe](https://docs.microsoft.com/en-us/sysinternals/downloads/strings) - It scans the file you pass it for UNICODE (or ASCII) strings of a default length of 3 or more UNICODE (or ASCII) characters
* [Sysinternals Suite](https://docs.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite) - the individual troubleshooting tools and help files from Microsoft
## Acknowledgments

* The stackoverflow community
* My dog
