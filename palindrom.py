i = 0

def palindromeStrings(word):
    panList = []
    for i in range(len(word)):
         spread(word, i, i, panList)
         spread(word, i, i+1, panList)
    
    panList.sort()
    return panList

def spread(given, low, high, panList):
    while(low >= 0 and high < len(given) and given[low]==given[high]):
        if(low!=high):
            panList.append(given[low:high+1])
        low = low - 1
        high = high + 1
   
        




def main():
    global i
    check = []
    while True:   
        try:
            line = input()
            if line:
                check.append(line)
            else:
                if(i==0):
                    break
                    #i = i + 1
                    #continue
                else:
                    break
              
            
        except:
            
            break
    
    
    for i in check:
        
        pList = palindromeStrings(i)
        
        pList = list(dict.fromkeys(pList))
        
        for k in pList:
            print(k)
            
        print()

    print()




if __name__ == "__main__":
    main()