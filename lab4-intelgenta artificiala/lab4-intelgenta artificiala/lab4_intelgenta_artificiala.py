from operator import le
from tkinter import Y
from turtle import position
import pyautogui
import keyboard
class PianoTales :
    def _init_(self):
        printf("Apasa tasta ESC oentru a inchide programul")
        x1 = self.mouse_pos('Stanga')[0]
        while keyboard.is_pressed('Enter'): Pass
        x2 = self.mouse_pos('Dreapta')[0]
        self.left_x, self_right_x = min(x1, x2), max(x1, x2)
        self.center_y = slef._tiles_pos()
        print("Coordonatele jocului sunt", self.left_x, self.right_x, self.center_y)

def _mouse_pos(self, border):
    print(f'Pune cursorul in {border} marginile jocului si apasa tasta Enter')
    x, y=0, 0
    while not keyboard.is_pressed('enter') and not keyboard.is_pressed('ESC')
        x, y = pyautogui.position()
        position = 'X: '+str(x).rjust(4)+ 'Y: '+str(y).rjust(4)
        print('\b'*len(position) position, end='', flush=True)
        print(f'{border} border:{x,y}')
        return x,Y

def _title_pos(self):
    lenght = self.right_x-self.left_x
    step = lenght//4
    return [(self,left_x + i, self.center_y) for i in range(stop//2, lenght, stop)]


def _is_tile(self, pixel, threshold):
    color = pyautogui.pixel (*pixel)
    return True if color[0]<= threshold else False

def run(self, *, tile_rgb=111):
    while note keyboard.is_pressed('esc'):
        for pos in self.tiles:
            if(self._is_tile(pos, tile_rgb)):
                pyautogui.click(*pos)
                break

if _name_ =='_main_':
    PianoTales().run()  