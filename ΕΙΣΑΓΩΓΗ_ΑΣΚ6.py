import random



#function to change the B to b if the bishop theatens the queen
def fix_position(p):
	if p=="B":
        
		return "b"
	
	else:
		return p

#a counter to count how many times queen has been threatened
cnt =0
for l in range(100):
    QUEEN=1
    BISHOP=1
    #place the 2 pieces
    tmp=["0"]*(64-QUEEN-BISHOP)
    tmp+=["Q"]*QUEEN
    tmp+=["B"]*BISHOP
    #shuffle them
    random.shuffle(tmp)
    board=[]
    
    for i in range(8):
        board+=[tmp[8*i:8*i+8]]

    for i in range(8):
        for j in range(8):
            if board[i][j]=="Q":

                for k in range(8):
                    
                        if k!=i and k+j-i>=0 and k+j-i<8:
                            board[k][k+j-i]=fix_position(board[k][k+j-i])
                            
                        if k!=i and -k+j+i>=0 and -k+j+i<8:
                            board[k][-k+i+j]= fix_position(board[k][-k+i+j])
                            

    for i in range(8):
        for j in range(8):
            if board[i][j]=="b":
                cnt+=1
                                       
    
print ("The Queen was threatened " ,cnt," times")