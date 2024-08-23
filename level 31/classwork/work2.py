#შექმენით ფუნქცია რომელიც ადიდებს მხოლოდ 1 ასოს,  გამიყენეთ სლაისინგი.



def single(text, capitalize):

    index = text.find(capitalize)
    

    before = text[:index]          
    char = text[index].upper()    
    after = text[index + 1:]      
    return before + char + after

text = "world"
capitalize = 'd'  
text = single(text, capitalize)
print(text)


