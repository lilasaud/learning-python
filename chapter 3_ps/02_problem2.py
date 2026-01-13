letter = ''' Dear <|Name|>,
            you are selected!  
             <|Date|>'''
print(letter.replace("<|Name|>", "lila").replace("<|date|>","24 september 2050"))