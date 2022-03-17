# -*- coding: utf-8 -*-
from utils import load_random_word
from Player import Player
from basic_word import BasicWord

def main():
    game_is_on = True

    main_word = load_random_word()
    word = main_word.word
    word_count = main_word.get_words()

    print("Введите имя игрока")
    user_name = input()
    print(f"Привет, {user_name}\nСоставьте {word_count} слов из слова {str.title(word)}\n"
          f"Слова должны быть не короче 3 букв\n"
          f"Чтобы закончить игру, угадайте все слова или напишите 'стоп'\n"
          f"Поехали, ваше первое слово?")
    player = Player(user_name)
    while game_is_on:

        answer = input()
        if answer == "стоп" or answer == 'stop':
            print("игра завершена!")
            print(f"вы угадали {player.count_words()} слов")
            break
        if player.count_words() == word_count:
            print("слова закончились, игра завершена!")
            print(f"вы угадали {player.count_words()} слов")
            break

        if main_word.is_correct(answer):
            player.add_word(answer)
            print("Верно")
        else:
            print("Неверно")


main()









