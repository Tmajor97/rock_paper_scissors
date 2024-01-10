import random 

def play():
    user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors :")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'Its a tie'
    
    #r > s, s > p, p > rr
    

    if is_win(user, computer):
        return 'You won'
    
    return 'You lost!'
        
def is_win(player,opponent):
    #retun true if player wins
    #r > s, s > p, p > r,
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')  or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False
    
    
print(play())