import random
n = int(input("有多少參賽者 : "))
players = list()
_rowList = list()
_result = list()
print("請依序輸入今天的參賽者")
for i in range(n):
    temp = input("第" + str(i+1) + "位參賽者 : ")
    players.append(temp)

for i in range(n):
    for j in range(i+1, n, 1):
        _rowList.append({"Player1": players[i], "Player2": players[j]})

temp = _rowList.copy()
while True:
    for i in range(len(_rowList)):
        if i == 0:
            _result.append(_rowList[i])
            continue
        
        ttcount = 0
        while(True):
            ttcount+=1
            if(ttcount == 50):
                print("Restart this program again")
                break
            rand_index = random.randint(0, len(temp)-1)
            if(len(temp)==0):
                break
            if(_result[i-1]["Player1"] != temp[rand_index]["Player1"] and _result[i-1]["Player2"] != temp[rand_index]["Player2"] and _result[i-1]["Player1"] != temp[rand_index]["Player2"] and _result[i-1]["Player2"] != temp[rand_index]["Player1"]):
                _result.append(temp[rand_index])
                temp.pop(rand_index)
                break
            else:
                continue

    print("\n---------------\n")
    for i in range(len(_result)):
        print("第" + str(i+1) + "場 : " + _result[i]["Player1"] + " vs. " + _result[i]["Player2"])
    
    _exit = input("輸入任何輸入以結束程式, 輸入re可以重新跑一次 : ")
    if(_exit.upper() != "RE"):
        break