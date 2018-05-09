command= input('Do you want to continue: Y/N')
while command != 'N':
    #Assignment 3 Qn 5
    file=input('Enter the file name: ')     #request for file name

    F=open(file,'r')        #open file

    print('%-15s%-17s%-15s'%('<last name>','<hourly wage>','<hours worked>'))       #print heading

    line = F.readline()     #read file
    while line != '':
        line = line.split('|')      #remove all |
        name=line[0]        #assign variables
        wage=line[1]
        hours=line[2]
        line = F.readline()
        print('%-15s%-18.1f%-8d'%(name,float(wage),int(hours)))     #print data on shell

    F.close()       #close file
    command= input('Do you want to continue: Y/N')
