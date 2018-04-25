#1D array
'''
names = [''] * 3        #['','','']  #assuming an array of strings
print (names)       #'original'

#input name and store in array
for i in range (3):
    names[i] = input('Enter name: ')

print(names)        #'final'
'''

#2D array
'''
numStuds = 3
numTests = 2

scores = [0]*numStuds   #[0,0,0] --> 0 is standard integer when using an array of int
for stud in range (0,numStuds):
    scores[stud] = [0]*numTests     #[[0,0],[0,0],[0,0]]

print(scores)    
'''

#input scores and store in array,scores
for stud in range(0,numStuds):
    print('\nStudent',stud+1)
    for test in range(0,numTests):
        scores[stud][test] = int(input('Enter marks for test',str(test+1)+': ')

print()
print(scores)
                                 
#output scores from array
for stud in range(0,numStuds):
    print('\nstudents',stud+1)
    for test in range(0,numTests):
        print'Test ' + str(test+1)+': ' + str(scores[stud][test]),end='  ')
    print()    
