import numpy as np
from tkinter import  messagebox,Tk
import pygame
import board_to_file
import im_show
from create_board import *
import board_interface
import one_thread_per_box
import two_thread_per_box
import matplotlib.pyplot as plt
solver_5={"runtime":0,"adimsayisi":0}
solver_10={"runtime":0,"adimsayisi":0}

if __name__=="__main__":
    root = Tk()
    root.overrideredirect(1)
    root.withdraw()
    messagebox.showinfo("Sudoku Çözüm","5 thread ile sudoku çözümüne başlanıyor")
    first=one_thread_per_box.start()
    solver_5["runtime"]=first["runtime"]
    solver_5["adimsayisi"] = first["adimsayisi"]
    board_interface.init_pygame()
    board_interface.draw_square(create_array_board())

    FPSCLOCK = pygame.time.Clock()
    for i in board_to_file.pickle_to_board():
        board_interface.update_numbers(i[0],i[1],i[2])
        board_interface.update()
        pygame.event.get()
    board_interface.wait()
    messagebox.showinfo("Sudoku Çözüm","10 thread ile sudoku çözümüne başlanıyor")
    second=two_thread_per_box.start()
    solver_10["runtime"]=second["runtime"]
    solver_10["adimsayisi"] = second["adimsayisi"]
    board_interface.init_pygame()
    board_interface.draw_square(create_array_board())
    FPSCLOCK = pygame.time.Clock()
    for i in board_to_file.pickle_to_board():
        board_interface.update_numbers(i[0], i[1], i[2])
        board_interface.update()
        pygame.event.get()
    board_interface.wait()
    messagebox.showinfo("Sudoku Çözüm","İki yöntem zaman-Bulunan çözüm grafiği")
    point_5_1=[0,0]
    point_5_2=[solver_5["runtime"],solver_5["adimsayisi"]]
    point_10_1=[0,0]
    point_10_2 = [solver_10["runtime"], solver_10["adimsayisi"]]
    x1_val=[point_5_1[0],point_5_2[0]]
    y1_val=[point_5_1[1],point_5_2[1]]
    x2_val = [point_10_1[0], point_10_2[0]]
    y2_val = [point_10_1[1], point_10_2[1]]
    plt.plot(x1_val,y1_val,'b',label="5 thread")
    plt.plot(x2_val,y2_val,'r',label="10 thread")
    plt.xticks(np.arange(0,0.8,0.05))
    plt.legend(loc="best")

    plt.ylabel("Adım Sayısı")
    plt.xlabel("Zaman")
    plt.savefig("plot.png")
    im_show.show()
