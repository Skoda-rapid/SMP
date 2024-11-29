
from lab_9.src.facade import RunnerFacade
from shared.constants.global_variables import labs_menu
from shared.logger import Logger


def main():
    Logger.log("Лабораторна 9 запущена")
    
    facade = RunnerFacade()
    while True:
        facade.show_menu(labs_menu)
        choice = int(input("Оберіть лабораторну роботу: "))
        if choice == 0:
            break
        facade.run_lab(choice)