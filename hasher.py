import sys, hashlib, optparse
from optparse import OptionParser

#Variables
#md5_val = False
#sha1_val = False
#sha256_val = False


parser = OptionParser()

#Command Line options
parser.add_option("--md5", action="store_true", dest="md5_val", help="Use MD5 Algorithm", default=False)
parser.add_option("--sha1", action="store_true", dest="sha1_val", help="Use SHA1 Algorithm", default=False)
parser.add_option("--sha256", action="store_true", dest="sha256_val", help="Use SHA256 Algorithm", default=False)

(options, args) = parser.parse_args()


#Functions

def file_hash_md5(filename):
    h = hashlib.md5()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)
    return ("    MD5: "+h.hexdigest())

def file_hash_sha1(filename):
    h = hashlib.sha1()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)
    return ("    SHA1: "+h.hexdigest())    

def file_hash_sha256(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)
    return ("    SHA256: "+h.hexdigest())

def main():
    for file in sys.argv:
        if file != "hasher.py" and file != "hasher.exe" and file != "--md5" and file != "--sha1" and file != "--sha256":
            #Conditions

            #Compound Conditions
            if (options.md5_val == True and options.sha1_val == True):
                print("[+] File: "+file)
                print(file_hash_md5(file))
                print(file_hash_sha1(file))
            elif (options.md5_val == True and options.sha256_val == True):
                print("[+] File: "+file)
                print(file_hash_md5(file))
                print(file_hash_sha256(file))
            elif (options.sha1_val == True and options.sha256_val == True):
                print("[+] File: "+file)
                print(file_hash_sha1(file))
                print(file_hash_sha256(file))
            
            #Single Conditions
            elif (options.md5_val == True):
                print("[+] File: "+file)
                print(file_hash_md5(file))
            elif (options.sha1_val == True):
                print("[+] File: "+file)
                print(file_hash_sha1(file))
            elif (options.sha256_val == True):
                print("[+] File: "+file)
                print(file_hash_sha256(file))
            
            #Default
            else:
                print("[+] File: "+file)
                print(file_hash_md5(file))
                print(file_hash_sha1(file))
                print(file_hash_sha256(file))
                print("\n")
            print("\n\n")
        else:
            pass


#Main
if __name__ == "__main__":
    print("[+] File Hasher V1.0")
    print("\n")
    main()
