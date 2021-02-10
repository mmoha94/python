def Mohit(tool,arz):
    mo = 2 * ( tool + arz)
    return mo
def Masahat(tool,arz):
    ms = tool * arz
    return ms

tool = int(input("Enter Tool:"))
arz  = int(input("Enter Arz :"))
print ("Mohit:" , Mohit(tool,arz) )
print ("Masahat:" , Masahat(tool,arz) )