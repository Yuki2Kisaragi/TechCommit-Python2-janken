import random

def input_number():
    while 1:
        print("最初はグー、じゃんけん…")
        card = int(float(input("（グー 1, チョキ 2, パー 3）")))
        if card <1 or card > 3:
            print("1～3の正数を入力してください")
        else:
            return card


card = {1: "rock", 2: "scissors", 3: "paper"}



for i in range(3):
    Your_card = input_number()
    Computer_card = random.randint(1, 3)

    if Your_card == 1 and Computer_card == 2:  # You:rock, COMP:scissors
        print(card[Your_card])
        print(card[Computer_card])
        print("You Win!")
        break
    elif Your_card == 1 and Computer_card == 3:  # You:rock,COMP:paper
        print(card[Your_card])
        print(card[Computer_card])
        print("You Lose!")
        break
    elif Your_card == 3 and Computer_card == 1:  # You:paper,COMP:rock
        print(card[Your_card])
        print(card[Computer_card])
        print("You Win!")
        break
    elif Your_card == 3 and Computer_card == 2:  # You:paper ,COMP:scissors
        print(card[Your_card])
        print(card[Computer_card])
        print("You Lose!")
        break
    elif Your_card == 2 and Computer_card == 1:  # You:scissors ,COMP:rock
        print(card[Your_card])
        print(card[Computer_card])
        print("You Lose!")
        break
    elif Your_card == 3 and Computer_card == 2:  # You:scissors ,COMP:paper
        print(card[Your_card])
        print(card[Computer_card])
        print("You Win!")
        break
    else:  # EVEN
        print(card[Your_card])
        print(card[Computer_card])
        print("あいこで")



