import glob
import os
import os 
import re
import shutil
hex_file = ""
tag = "1.0.0"
os.mkdir("./hex-files")
def renameHexFile(fileRegex,releaseType):
    new_file = re.findall(f"^(.*?)\.{fileRegex}",file)[0]
    new_file = f"{new_file}_{releaseType}_{tag}.hex"
    shutil.copyfile(os.path.join(dirpath,file), f"./hex-files/{new_file}")
for dirpath, dirnames, filenames in os.walk("./"):
    for file in filenames:
        if "hex" in file:
            print(file,dirpath)
            '''if os.path.join("Release","") in dirpath:
                renameHexFile("hex","release")
            elif os.path.join("Debug","") in dirpath:
                renameHexFile("hex","debug")
            elif os.path.join("pro","production") in dirpath:
                renameHexFile("X","pro")
            elif os.path.join("free","production") in dirpath:
                renameHexFile("X","free")
            else:
                pass'''
            if "Release" in dirpath:
                renameHexFile("hex","release")
            elif "Debug" in dirpath:
                renameHexFile("hex","debug")
            elif os.path.join("pro","production") in dirpath:
                renameHexFile("X","pro")
            elif os.path.join("free","production") in dirpath:
                renameHexFile("X","free")
            else:
                pass
shutil.make_archive("hex-files","zip","./hex-files")