from termcolor import colored
from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']
    __timer = [7, 2, 10]

    def running(self):
        for i in (0, 1, 2, 1, 0):
            print(colored('\r' + self.__color[i], color=self.__color[i]), end='')
            sleep(self.__timer[i])


t = TrafficLight()
t.running()
