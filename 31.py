# a + 2b + 5c + 10d + 20e + 50f + 100g = 200
# where a,b,c,d,e,f,g can be any integer solution.

possible = 1
coins = [1,2,5,10,20,50,100]
coins.reverse() # Go from the largest one
goal = 200

def recurrsion(index,value):
    global possible
    
    if index < len(coins):
        coin = coins[index]

        for i in range(0, int(goal/coin)+1):
            _value = value + i * coin
            if _value < goal:
                recurrsion(index + 1,_value)
            elif _value == goal: 
                possible += 1
            else:
                return
    else:
        if value == goal:
            possible += 1
        return

recurrsion(0,0)
print(possible)