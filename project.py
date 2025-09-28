# NUMBER GUESSING GAME
import random
class Player:
    print("HELLO GAMER...!!!")
    def __init__(self,name):
        self.name=name
        self.score=35
        print("HELLO GAMER...")
        print("Rules of game:\n1. There are 3 levels\n2. Each level has different difficulty\n3. There are limited chances only")
        print("\nClick '0' for exiting the game\n")

    def play_level(self,max_Num,chances):
        num = random.randint(1, max_Num)
        for i in range(chances): 
            choice = int(input(f"Enter your choice (1-{max_Num}): "))

            if choice == num:
                print("You WIN this level...")
                return True
            elif choice < num:
                print("Try Big Number")
                print("Total lives left:", chances - (i+1))
                self.score -= 1
            else:
                print("Try Small Number")
                print("Total lives left:", chances - (i+1))
                self.score -= 1
        print("YOU LOST!!!")
        print("To try again press 1 ")
        num=int(input("Enter the number : "))
        if(num==1): self.replay()
        else:
            return False

    def play(self):
            print("Press 1 for start : ")
            n=int(input("Enter here  : "))
            if n==0:
                self.Exit()
            if self.play_level(10,4):
                print("Get Ready for level 2 ")
            else:
                self.Exit()
            if self.play_level(100,9):
                print("Get Ready for next level ")
            else:
                self.Exit()
            if self.play_level(1000,9):
                print("YOU WIN !!!")

            print("TOTAL SCORE : ",self.score)
            return self.score

    def replay(self):
        print("Restarting the level...")
        return self.play()

    def Exit(self):
        print("THANKYOU FOR PLAYING...PLEASE VISIT AGAIN")
        exit()


if __name__=="__main__":
    scores = [] 

    name = input("Player Name : ")
    Player_name=Player(name)
    final_score=Player_name.play()

    with open("project1.csv", "a") as file: 
        file.write(f"{name},{final_score},35\n")

    with open("project1.csv", "r") as file:
        for line in file:
            player, score, total = line.strip().split(",")
            scores.append((player, int(score)))
    scores.sort(key=lambda x: x[1], reverse=True)
    print("Top Scores:")
    for i, (player, score) in enumerate(scores[:5], 1):
        print(f"{i}. {player} - {score}")
    exit()
