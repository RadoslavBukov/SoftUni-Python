"""
Input	                            Output
kiwi orange banana apple	        kiwi
                                    orange
                                    banana

pizza cake pasta chips	            cake
"""
input_version = input().split(" ")

even_word_list = [x for x in input_version if len(x) % 2 == 0]

print(*even_word_list,sep='\n')