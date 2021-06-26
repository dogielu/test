steps=['Python','Git','Deap','AI']
def my_enumerate(iterable,start=0):
    count=start
    for element in iterable:
        yield count,element
        count+=1
for num,step in my_enumerate(steps,1):
    print('Step{} {}'.format(num,step))

for num,step in enumerate(steps,1):
    print('Step{} {}'.format(num,step))
