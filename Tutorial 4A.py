#Tutorial 4A Qn 1
'''
#request for inputs
games = int(input('Enter the number of games: '))
player = int(input('Enter the number of players: '))

#assume arrays
names = [''] * player
points = [0] * player
for num in range(player):
    points[num] = [0]*games
average = [0] * player
total = [0] * games

#initialise constants
Sum = 0
s = 0

#process data
for numP in range(player):
    names[numP] = input('\nEnter name of player ' + str(numP + 1) + ': ')
    for numG in range(games):
        points[numP][numG] = int(input('Enter score of game ' + str(numG + 1) + ': '))
        s += points[numP][numG]
    ave = s/games
    average[numP] = ave     

print('%-6s%-6s%-6s%-6s%-6s%-6s'%('Name','G1','G2','G3','G4','Average Score'))
for numP in range(player):
    print('%-6s'%(names[numP]),end='')
    for numG in range(games):
        print('%-6d'%(points[numP][numG]), end='')
    print(average[numP])    

'''

#Tutorial 4A Qn 2
'''
#request inputs
numStocks = int(input('Enter the total number of stocks: '))
numDays = int(input('Enter the number of days: '))

#assume arrays
names = [''] * numStocks
prices = [0] * numStocks
for num in range(numStocks):
    prices[num]=[0]*numDays
    
for stock in range(numStocks):
    names[stock] = input('\nEnter the name of stock ' + str(stock+1) +': ')
    for day in range (numDays):
        prices[stock][day] = float(input('Enter the price of stock on day ' +str(day+1)+ ': '))
        
    maxprice = prices[stock][0]
    minprice = prices[stock][0]
    maxday = 1
    minday = 1
    for day in range(1,numDays):
        if prices[stock][day] > maxprice:
            maxprice = prices[stock][day]
            maxday = day + 1
            
        if prices[stock][day] < minprice:
            minprice = prices[stock][day]
            minday = day + 1
    print(names[stock])
    print("The maximum price is",maxprice,'on day',maxday)
    print("The minimum price is",minprice,'on day',minday)
            
'''

