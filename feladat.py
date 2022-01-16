import random

while True:
    gameMode = 0    # 0 -> bot;  1 -> 2 player
    choosed = 0
    
    while choosed == 0:
        print("----------------------------------------------------------------------------")
        print("Válaszd ki az ellenfeled!")
        print("Ha AI ellen szertnél játszani akkor írd be, hogy AI")
        print("Ha BARÁTOD ellen szertnél játszani akkor írd be, hogy barat")
        changeGameMode = str(input("Választásod: ").strip()).lower()
        print("----------------------------------------------------------------------------")
        
        if changeGameMode == "ai":
            gameMode = 0
            choosed = 1
        elif changeGameMode == "barat":
            gameMode = 1
            choosed = 1
    
    
    if gameMode == 0:
        mutatsz = 0
    
        while mutatsz == 0:
            print("----------------------------------------------------------------------------")
            print("Mit fogsz mutatni?")
            print("Ha követ írd be, hogy kovet")
            print("Ha papírt írd be, hogy papirt")
            print("Ha ollót írd be, hogy ollot")
            player = input("Mit választasz (kovet, papirt, ollot)?: ")
            print("----------------------------------------------------------------------------")
    
            if player == "kovet":
                player = "ko"
                mutatsz = 1
            elif player == "papirt":
                player = "papir"
                mutatsz = 1
            elif player == "ollot":
                player = "ollo"
                mutatsz = 1
    
    
        ai = random.randint(1,3)
    
        if ai == 1:
            ai = "ko"
        elif ai == 2:
            ai = "papir"
        else:
            ai = "ollo"
    
    
    
        if player == "ko" and ai == "papir":
            print("----------------------------------------------------------------------------")
            print("Játékos:", player, "| AI:", ai)
            print("Játékos veszített")
            print("----------------------------------------------------------------------------")
    
        elif player == "ko" and ai == "ollo":
        
            print("----------------------------------------------------------------------------")
            print("Játékos:", player, "| AI:", ai)
            print("Játékos nyert")
            print("----------------------------------------------------------------------------")
    
        elif player == "papir" and ai == "ollo":
        
            print("----------------------------------------------------------------------------")
            print("Játékos:", player, "| AI:", ai)
            print("Játékos veszített")
            print("----------------------------------------------------------------------------")
    
        elif player == "papir" and ai == "ko":
        
            print("----------------------------------------------------------------------------")
            print("Játékos:", player, "| AI:", ai)
            print("Játékos nyert")
            print("----------------------------------------------------------------------------")
    
        elif player == "ollo" and ai == "papir":
        
            print("----------------------------------------------------------------------------")
            print("Játékos:", player, "| AI:", ai)
            print("Játékos nyert")
            print("----------------------------------------------------------------------------")
    
        elif player == "ollo" and ai == "ko":
        
            print("----------------------------------------------------------------------------")
            print("Játékos:", player, "| AI:", ai)
            print("Játékos veszített")
            print("----------------------------------------------------------------------------")
    
        else:
        
            print("----------------------------------------------------------------------------")
            print("Játékos:", player, "| AI:", ai)
            print("döntetlen")
            print("----------------------------------------------------------------------------")
    
    else:
        mutatsz = 0
    
        while mutatsz == 0:
            print("----------------------------------------------------------------------------")
            print("Első játékos...")
            print("Mit fogsz mutatni?")
            print("Ha követ írd be, hogy kovet")
            print("Ha papírt írd be, hogy papirt")
            print("Ha ollót írd be, hogy ollot")
            player1 = input("Mit választasz (kovet, papirt, ollot)?: ")
            print("----------------------------------------------------------------------------")
    
            if player1 == "kovet":
                player1 = "ko"
                mutatsz = 1
            elif player1 == "papirt":
                player1 = "papir"
                mutatsz = 1
            elif player1 == "ollot":
                player1 = "ollo"
                mutatsz = 1
    
        while mutatsz == 1:
            print("----------------------------------------------------------------------------")
            print("Második játékos...")
            print("Mit fogsz mutatni?")
            print("Ha követ írd be, hogy kovet")
            print("Ha papírt írd be, hogy papirt")
            print("Ha ollót írd be, hogy ollot")
            player2 = input("Mit választasz (kovet, papirt, ollot)?: ")
            print("----------------------------------------------------------------------------")
    
            if player2 == "kovet":
                player2 = "ko"
                mutatsz = 2
            elif player2 == "papirt":
                player2 = "papir"
                mutatsz = 2
            elif player2 == "ollot":
                player2 = "ollo"
                mutatsz = 2
    
        if player1 == "ko" and player2 == "papir":
            print("----------------------------------------------------------------------------")
            print("Első játékos:", player1, "| Második játékos:", player2)
            print("Második játékos nyert!")
            print("----------------------------------------------------------------------------")
    
        elif player1 == "ko" and player2 == "ollo":
        
            print("----------------------------------------------------------------------------")
            print("Első játékos:", player1, "| Második játékos:", player2)
            print("Első játékos nyert!")
            print("----------------------------------------------------------------------------")
    
        elif player1 == "papir" and player2 == "ollo":
        
            print("----------------------------------------------------------------------------")
            print("Első játékos:", player1, "| Második játékos:", player2)
            print("Második játékos nyert!")
            print("----------------------------------------------------------------------------")
    
        elif player1 == "papir" and player2 == "ko":
        
            print("----------------------------------------------------------------------------")
            print("Első játékos:", player1, "| Második játékos:", player2)
            print("Első játékos nyert!")
            print("----------------------------------------------------------------------------")
    
        elif player1 == "ollo" and player2 == "papir":
        
            print("----------------------------------------------------------------------------")
            print("Első játékos:", player1, "| Második játékos:", player2)
            print("Első játékos nyert!")
            print("----------------------------------------------------------------------------")
    
        elif player1 == "ollo" and player2 == "ko":
        
            print("----------------------------------------------------------------------------")
            print("Első játékos:", player1, "| Második játékos:", player2)
            print("Második játékos nyert!")
            print("----------------------------------------------------------------------------")
    
        else:
        
            print("----------------------------------------------------------------------------")
            print("Első játékos:", player1, "| Második játékos:", player2)
            print("Döntetlen!")
            print("----------------------------------------------------------------------------")
    
    