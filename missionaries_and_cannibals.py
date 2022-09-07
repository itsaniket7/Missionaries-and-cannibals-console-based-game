print("Cannibals and Missionaries puzzle...\n\n")
print("Starting From Left Side of River:")
print("😁😁😁👿👿👿\t\t\t\t No one");
min = 0
lc = 3
lm = 3
direct = True
rc = 0
rm = 0

def check(tc, tm, llc, llm, rrc, rrm, d):
    if(d):
        llc = llc - tc
        llm = llm - tm
        rrc = rrc + tc
        rrm = rrm + tm
    else:
        rrc = rrc - tc
        rrm = rrm - tm
        llc = llc + tc
        llm = llm + tm

    print("\n\nChecking for:\nLeft cannibals: "+str(llc)+"\n"+"Left missionaries: "+str(llm)+"\nRight cannibals: "+str(rrc)+"\nRight missionaries: "+str(rrm)+"\n\n")

    if((rrc > rrm) and rrm != 0):
        return False
       
    elif (llc > llm) and llm != 0:
        return False
    else:
        return True



while True:
    min = min+1
    if(rc == 3 and rm == 3):
        print("Iterations required: "+str(min))
        print("Sucessfully passed!");
        break
    else:
        while(True):
            tc = int(input("Enter cannibals to travel(0/1/2): "))
            tm = int(input("Enter missionaries to travel(0/1/2): "))
            if((tc+tm) > 2 or tc+tm < 1):
                print("Boat can carry at least one and at most 2 people. please give input again!\n\n")
            elif(direct and (lc < tc or lm < tm)):
                print("No of cannibals or missionaries is greater than the total available on left\n\n")
            elif(not direct and (rc < tc or rm < tm)):
                print("No of cannibals or missionaries is greater than the total available on right\n\n")
    
            else:
                break;
        
        
        if(check(tc, tm, lc, lm, rc, rm, direct)):
            if(direct):
                print("At right Side:")
                direct = False
                lc = lc - tc
                lm = lm - tm
                rc = rc + tc
                rm = rm + tm
            else:
                print("At left side:")
                direct = True
                lc = lc + tc
                lm = lm + tm
                rc = rc - tc
                rm = rm - tm
            
            tempc = lc
            tempm = lm
            
            while tempc > 0:
                tempc = tempc - 1
                print("👿",end="")
            while tempm > 0:
                tempm = tempm - 1
                print("😁",end="")
            print("\t\t\t\t", end="")
            
            tempc = rc
            tempm = rm
            while tempc > 0:
                tempc = tempc - 1
                print("👿",end="")
            while tempm > 0:
                tempm = tempm - 1
                print("😁",end="")
            print("\t")
            
            
                
            
        else:
            print("You Failed!!")
            break
