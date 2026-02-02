import random
n = random.randint(1, 100)
print("###### Guess the exact num to win the game #####")

lives = 5

while lives > 0:
    g_num = int(input(f"You have {lives} lives. Guess a number (1-100)-->> "))

    if g_num < 1 or g_num > 100:
        print("Please enter a num between 1-100")
        continue

    if g_num == n:
        print(f"You won the game! The number was {n}.")
        break
    
    else:
        lives -= 1
        if g_num > n:
            print(f"{g_num} is too HIGH,you have {lives} left")
        else:
            print(f"{g_num} is too LOW,you have {lives} left")

if lives == 0:
    print(f"You lost! The correct number was {n}.")
            
    
        
        
    