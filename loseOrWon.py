from random import choice
import time
import os
from envparse import env
from termcolor import cprint

env.read_envfile('money.env')
capital = int(os.getenv('CAPITAL'))
slots = list(range(1, 31))


def starting():
    global slots
    global capital
    stavka = int(input('Укажите ставку: '))
    from_ = int(input(f'Выберите диапазон чисел на которую хотите поставить ставку:(диапазон не должен превышать {slots[-11]})\n'
                      f'От: '))
    to = int(input(f'До: '))
    winning_number = choice(slots)
    gamer_choice = list(range(from_, to))
    if gamer_choice[-1] > 30:
        cprint('Недопустимый формат', "red")
        starting()

    if winning_number in gamer_choice:
        if len(gamer_choice) < 4:
            stavka *= 10
        elif len(gamer_choice) > 3 and len(gamer_choice) < 11:
            stavka *= 3
        elif len(gamer_choice) > 10 and len(gamer_choice) < 21:
            stavka *= 1.2
        elif len(gamer_choice) > 21:
            cprint('Диапазон не должен превышать 20!!!', "red")
            starting()
        cprint('Поздравляем, вы угадали!', "yellow")
        capital += stavka
    else:
        cprint('К сожалению, вы не угадали', "magenta")
        capital -= stavka
    time.sleep(1)
    play_round()



def play_round():
    choice = input('Если хотите повторить игру- нажмите 1\n'
                   'Чтобы покинуть игру- нажмите 0\n'
                   '>? ')
    if choice == '1':
        starting()
    elif choice == '0':
        gameover()


def gameover():
    cprint(f'Хорошая игра, ваш баланс состваляет: {capital} долларов', "blue", "on_grey")

