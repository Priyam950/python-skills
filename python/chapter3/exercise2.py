# write a program to fill in a letter template given below with name and Data 
letter = '''
dear <|Name|>,
you are selected !
<|Date|>'''
print(letter.replace("<|Name|>","Sujal").replace("<|Date|>","25 jun 2024"))