from time import sleep

class TrafficLight:
    __color = ['Зеленый', 'Желтый', 'Красный']

    def running(self):
        k = 0
        while k < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[k]}')
            if k == 0:
                sleep(7)
            elif k == 1:
                sleep(5)
            elif k == 2:
                sleep(3)
            k += 1


TrafficLight = TrafficLight()
TrafficLight.running()
