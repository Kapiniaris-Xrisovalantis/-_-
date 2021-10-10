import random



#συναρτηση που αλλαζει τον αξιωματικο(Β) σε b αν απειλει την βασιλισσα
def fix_position(p):
	if p=="B":
        
		return "b"
	
	else:
		return p

#μετρητης για ποσες φορες απειληθηκε η βασιλισσα
cnt =0
for l in range(100):
    QUEEN=1
    BISHOP=1
    #τοποθετησε τα πιονια
    tmp=["0"]*(64-QUEEN-BISHOP)
    tmp+=["Q"]*QUEEN
    tmp+=["B"]*BISHOP
    #ανακατεψε τα
    random.shuffle(tmp)
    board=[]
    
    for i in range(8):
        board+=[tmp[8*i:8*i+8]]

    for i in range(8):
        for j in range(8):
            if board[i][j]=="Q":

                for k in range(8):
                    #κυρια διαγωνιος με κεντρο την βασιλισσα
                        if k!=i and k+j-i>=0 and k+j-i<8:
                            board[k][k+j-i]=fix_position(board[k][k+j-i])
                    #δευτερευουσα διαγωνιοσ με κεντρο την βασιλισσα        
                        if k!=i and -k+j+i>=0 and -k+j+i<8:
                            board[k][-k+i+j]= fix_position(board[k][-k+i+j])
                            
#αυξησε τον μετρητη αν βρεθει b μεσα στον πινακα
    for i in range(8):
        for j in range(8):
            if board[i][j]=="b":
                cnt+=1
                                       
    
print ("The Queen was threatened " ,cnt," times")