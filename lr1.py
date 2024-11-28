import tkinter as tk
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

def calculate_digital_differential_analyzer(start_x, start_y, end_x, end_y):
    image = Image.new('RGB', (1000, 500),  (255, 255, 255))
    draw = ImageDraw.Draw(image)
    delta_x = end_x - start_x
    delta_y = end_y - start_y
    steps = max(abs(delta_x), abs(delta_y))
    for i in range(steps + 1):
        current_x = start_x + delta_x * i // steps
        current_y = start_y + delta_y * i // steps
        draw.point((current_x, current_y), fill=(255, 0, 0))
    return np.array(image)

def brezenhem_algorithm(start_x, start_y, end_x, end_y):
    image = Image.new('RGB', (1000, 500),  (255, 255, 255))
    draw = ImageDraw.Draw(image)
    delta_x = end_x - start_x
    delta_y = end_y - start_y
    t = 0
    while t <= 1:
        current_x = start_x + t * delta_x
        current_y = start_y + t * delta_y
        draw.point((int(current_x), int(current_y)), fill=(255, 0, 0))
        t += 0.001
    return np.array(image)

def integer_brezenhem_algorithm(start_x, start_y, end_x, end_y):
    image = Image.new('RGB', (1000, 500), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    delta_x = abs(end_x - start_x)
    delta_y = abs(end_y - start_y)
    step_x = 1 if start_x < end_x else -1
    step_y = 1 if start_y < end_y else -1
    error = delta_x - delta_y
    while True:
        if start_x == end_x and start_y == end_y:
            break
        draw.point((start_x, start_y), fill=(255, 0, 0))
        error_term = error
        if error_term > -delta_y:
            error -= delta_y
            start_x += step_x
        if error_term < delta_x:
            error += delta_x
            start_y += step_y
    return np.array(image)
class LinePlot:
    def __init__(self, root):
        self.root = root
        self.root.title("Алгоритмы")
        self.create_widgets()

    def create_widgets(self):
        self.label_x1 = tk.Label(self.root, text="x1:")
        self.label_x1.grid(row=0, column=0)
        self.entry_x1 = tk.Entry(self.root)
        self.entry_x1.grid(row=0, column=1)

        self.label_y1 = tk.Label(self.root, text="y1:")
        self.label_y1.grid(row=0, column=2)
        self.entry_y1 = tk.Entry(self.root)
        self.entry_y1.grid(row=0, column=3)

        self.label_x2 = tk.Label(self.root, text="x2:")
        self.label_x2.grid(row=1, column=0)
        self.entry_x2 = tk.Entry(self.root)
        self.entry_x2.grid(row=1, column=1)

        self.label_y2 = tk.Label(self.root, text="y2:")
        self.label_y2.grid(row=1, column=2)
        self.entry_y2 = tk.Entry(self.root)
        self.entry_y2.grid(row=1, column=3)

        self.button_plot = tk.Button(self.root, text="Построить", command=self.plot)
        self.button_plot.grid(row=2, column=0, columnspan=4)

        self.figure, self.axis = plt.subplots()
        self.axis.set_title("Алгоритмы")
        self.axis.set_axis_off()
        self.buttons = [plt.Button(plt.axes([0.1, 0.05, 0.2, 0.075]), 'ЦДА'), plt.Button(plt.axes([0.35, 0.05, 0.2, 0.075]), 'Брезенхем'), plt.Button(plt.axes([0.6, 0.05, 0.3, 0.075]), 'Целочисл. Брезенхем')]
        self.buttons[0].on_clicked(self.plot_digital_differential_analyzer)
        self.buttons[1].on_clicked(self.plot_brezenhem_algorithm)
        self.buttons[2].on_clicked(self.plot_integer_brezenhem_algorithm)

    def plot(self):
        self.start_x = int(self.entry_x1.get())
        self.start_y = int(self.entry_y1.get())
        self.end_x = int(self.entry_x2.get())
        self.end_y = int(self.entry_y2.get())
        self.axis.clear()
        plt.show(block=False)
        self.axis.imshow(calculate_digital_differential_analyzer(self.start_x, self.start_y, self.end_x, self.end_y))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.axis.set_title("Алгоритм ЦДА")

    def plot_digital_differential_analyzer(self, event):
        self.axis.clear()
        plt.show(block=False)
        self.axis.imshow(calculate_digital_differential_analyzer(self.start_x, self.start_y, self.end_x, self.end_y))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.axis.set_title("Алгоритм ЦДА")

    def plot_brezenhem_algorithm(self, event):
        self.axis.clear()
        plt.show(block=False)
        self.axis.imshow(brezenhem_algorithm(self.start_x, self.start_y, self.end_x, self.end_y))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.axis.set_title("Алгоритм Брезенхема")

    def plot_integer_brezenhem_algorithm(self, event):
        self.axis.clear()
        plt.show(block=False)
        self.axis.imshow(integer_brezenhem_algorithm(self.start_x, self.start_y, self.end_x, self.end_y))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.axis.set_title("Целочисленный алгоритм Брезенхема")

def main():
    root = tk.Tk()
    line_plot = LinePlot(root)
    root.mainloop()

if __name__ == "__main__":
    main()