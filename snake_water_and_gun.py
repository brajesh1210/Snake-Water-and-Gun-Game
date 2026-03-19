import random

def play_game():
    # Dictionary to map user inputs to full names
    choices = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}
    
    user_score = 0
    comp_score = 0
    total_rounds = 5
    
    print("Welcome to Snake, Water, Gun Game!")
    print(f"Let's play {total_rounds} rounds.\n")
    
    for round_num in range(1, total_rounds + 1):
        print(f"--- Round {round_num} ---")
        
        # 1. Get User Input
        user_input = input("Choose (s)nake, (w)ater, or (g)un: ").lower()
        
        if user_input not in choices:
            print("Invalid input! Please enter 's', 'w', or 'g'.\n")
            continue
            
        # 2. Get Computer Input
        comp_input = random.choice(['s', 'w', 'g'])
        
        print(f"You chose: {choices[user_input]}")
        print(f"Computer chose: {choices[comp_input]}")
        
        # 3. Determine the Winner
        if user_input == comp_input:
            print("Result: It's a Tie!\n")
            
        elif (user_input == 's' and comp_input == 'w') or \
             (user_input == 'w' and comp_input == 'g') or \
             (user_input == 'g' and comp_input == 's'):
            print("Result: You win this round!\n")
            user_score += 1
            
        else:
            print("Result: Computer wins this round!\n")
            comp_score += 1
            
    # 4. Final Score and Outcome
    print("=== Game Over ===")
    print(f"Final Score -> You: {user_score} | Computer: {comp_score}")
    
    if user_score > comp_score:
        print("Congratulations! You won the game! 🎉")
    elif comp_score > user_score:
        print("Computer wins the game! Better luck next time. 💻")
    else:
        print("The game ended in a draw! 🤝")

# Run the game
if __name__ == "__main__":
    play_game()