#filter() in higher order funcion check even odd
def chkevenodd(n):
    if n%2==0:
        return True
lst=[12,24,33,57,98,19]
output_list=list(filter(chkevenodd,lst))
print(output_list)

