from art import logo      # Importing Blackjack art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Gives random card."""     # Random card choosing function 
    card = random.choice(cards)
    return card

def calculate_score(cards):        # Score calculation function
    """Calculates scores from given cards."""     
    if sum(cards) == 21 and len(cards) == 2:    # Checking for blackjack. 0 means blackjack 
        return 0
    if 11 in cards and sum(cards) > 21: # Checking for ace 
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare(user_score, computer_score):   # Score comparison function 
    """Compares user and computer scores."""    # Expaining the functions
    if user_score == computer_score:
        return "Draw."
    elif user_score == 0:
        return "Blackjack ! You win."
    elif computer_score == 0:
        return "Blackjack ! Computer wins."
    elif user_score > 21:
        return "You Bust. Computer wins."
    elif computer_score > 21:
        return "Computer Bust. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "Computer win."

def blackjack():     # Game function 
    """Blackjack game function."""
    is_game_over = False
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):         # Giving 2 cards to user and computer 
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)    # Calculating scores 
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")     # Showing users hand and users score and computers first card
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:  # Checking for blackjack for both players and if user is over 21 points 
            is_game_over = True
        else:
            new_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()    # Asking user to draw a card or pass. 
            print("----------------------------------------------------")       # Printing this for better reading
            if new_card == "y":   
                user_cards.append(deal_card())   # If user draws a card this will add a new card to users cards   
                user_score = calculate_score(user_cards)     # Recalculating scores 
                computer_score = calculate_score(computer_cards)
            else:
                is_game_over = True 
    while computer_score != 0 and computer_score < 17:  # Computer draws cards and recalculating computer scores
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand {user_cards}, final score: {user_score}") # Showing user and computer final cards and scores  
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score=user_score, computer_score=computer_score)) # Comparing user and computer scores and determining the winner
    print("----------------------------------------------------")       # Printing this for better reading

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":   # Asking user to play the game or not 
    blackjack()


