# posicao.py

import pyautogui
import time

def print_position():
    print("Posicione o cursor onde deseja capturar a coordenada e pressione 'Enter'.")
    while True:
        try:
            # Captura a posição do mouse quando a tecla Enter é pressionada
            input("Pressione 'Enter' para capturar a posição...")
            x, y = pyautogui.position()
            print(f"Posição capturada: X={x}, Y={y}")
        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário.")
            break

if __name__ == "__main__":
    print("Script para capturar coordenadas do mouse.")
    print_position()
