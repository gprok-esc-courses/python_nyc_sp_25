from hangman import Game

game = Game()

game.user.read_user_name()
game.set_secret()

while True:
    print(game.get_secret_to_display())
    letter = game.user.ask_user_play()
    game.play(letter)
    print("Wrong", game.get_wrong_num())
    if game.is_hanged():
        print("HANGED")
        break 
    if game.secret_found():
        print(game.get_secret_to_display())
        print("FOUND")
        break
