from time import sleep
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while True:
            print(f'{TrafficLight.__color[i % 3]}')
            if i // 3 == 0:
                sleep(3)
            elif i // 2 == 1:
                sleep(5)
            else:
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()