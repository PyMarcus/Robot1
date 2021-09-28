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
    vetor = ["Olá", "Abra o github", "Deixe a janela aberta ao executar o robô"]
    for n in range(3):
        time.sleep(1)
        print(vetor[n])
    choice = str(input("executar? (s/n): ")).lower()
    time.sleep(1)
    if choice == 's':
        robo = Robot1(choice)
        robo.bot()
    else:
        print("Tchau")
