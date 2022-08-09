"""
Input	    Directory View	    report.txt
.	 	                        .html
                                - - - index.html
                                .js
                                - - - index.js
                                .pptx
                                - - - demo.pptx
                                .py
                                - - - program.py
                                - - - python.py
                                .txt
                                - - - log.txt
                                - - - notes.txt
"""
from os import walk

### Directory tree generator with dirpath, dirnames, filenames:
#for root, dirs, files in walk("."):
#    print(root)
#    print(dirs)
#    print(files)

result = {}
for _, _, files in walk("."):
    for file in files:
        ext = file.split(".")[-1]
        if ext not in result:
            result[ext] = []
        result[ext].append(file)

with open("./result.txt", "w") as output_file:
    for ext, files in sorted(result.items(), key = lambda x: x[0]):
        output_file.write("." + ext + "\n")
        for file in files:
            output_file.write(f"- - - {file}\n")