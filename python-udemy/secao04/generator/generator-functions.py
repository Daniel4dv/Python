# toda funcao com um yield é uma generator function

def generator(n=0,fim=10):
   while True:
       yield n
       n+=1

       if n> fim:
           return

gen = generator()

for n in gen:
    print(n)