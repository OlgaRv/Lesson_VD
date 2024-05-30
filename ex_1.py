import tkinter
import time
import random

window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

colors = ('blue3', 'brown', 'black', 'blue violet', 'blue4', 'chartreuse', 'coral1')
r = random.randint(0, 400)  # случайные значения для координаты центра окружности
x = r  # переменная центра окружности
y = r  # переменная центра окружности

for color, R in enumerate(range(150, 181, 5)):
    canvas.create_oval(x - R, y - R, x + R, y + R, outline=colors[color])
    canvas.update()  # обновление - запуск нового круга
    time.sleep(0.05)  # пауза перед новым кругом

window.mainloop()