"""
Input	                                                        Output
C:\Internal\training-internal\Template.pptx	                    File name: Template
                                                                File extension: pptx
C:\Projects\Data-Structures\LinkedList.cs	                    File name: LinkedList
                                                                File extension: cs
"""
path = input().split("\\")
file = path[-1]

file_extension = file.split(".")
print(f"File name: {file_extension[0]}\nFile extension: {file_extension[1]}")