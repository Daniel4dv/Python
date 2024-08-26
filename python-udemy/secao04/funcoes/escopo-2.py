x = 7

def escopo ():
    # global x 
    x= 10

    def escopo2():
        # x=15
        y=5
        print(x,y)
    
    escopo2()

escopo()
print(x)