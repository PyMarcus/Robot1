import pyautogui
import time
import threading

class Robot1():
    """
    Bot star github
    """
    def __init__(self, start):
        self.start = start

    def bot(self):
        time.sleep(0.5)
        x, y = pyautogui.size()
        center = (x/2, y/2)
        where = pyautogui.position(837, 248)
        time.sleep(1)
        pyautogui.click(where)
        value = True
        while value:
            photo = 'foto.png'
            pyautogui.moveTo(center)
            screen = pyautogui.locateCenterOnScreen(photo)
            threading.Thread(target=pyautogui.locateCenterOnScreen).start()
            pyautogui.click(screen)


if __name__ == '__main__':
    time.sleep(1)
    print("Olá")
    time.sleep(1)
    print("Abra o github")
    time.sleep(1)
    print("Deixe a janela aberta ao executar o robô")
    choice = str(input("executar? (s/n): ")).lower()
    time.sleep(1)
    if choice == 's':
        robo = Robot1(choice)
        robo.bot()
    else:
        print("Tchau")
