import pyautogui
import time
import sys
import os

def send_whatsapp_message(phone_number, message, attachment_path):
    try:
        # Verificar se o arquivo de anexo existe
        if not os.path.isfile(attachment_path):
            raise FileNotFoundError(f"Attachment file does not exist: {attachment_path}")

        # Definir tempo de espera para garantir que a interface está carregada
        time.sleep(10)  # Ajuste o tempo conforme necessário

        # Pesquisa pelo número de telefone no WhatsApp Web
        pyautogui.click(x=206, y=155)  # Clique na barra de pesquisa (ajuste a posição conforme necessário)
        pyautogui.write(phone_number)
        pyautogui.press('enter')

        time.sleep(2)  # Aguarde a abertura da conversa

        # Digitar a mensagem
        pyautogui.write(message)
        
        # Anexar arquivo
        # Clique no botão de anexo
        pyautogui.click(x=533, y=684)  # Ajuste a posição conforme necessário
        time.sleep(1)  # Aguarde o menu de anexos abrir

        # Clique na opção "Documentos"
        pyautogui.click(x=616, y=424)  # Ajuste a posição conforme necessário para o botão "Documentos"
        time.sleep(1)  # Aguarde o diálogo de seleção de arquivos abrir

        # Digitar o caminho do arquivo no campo de entrada
        pyautogui.write(attachment_path)
        pyautogui.press('enter')
        time.sleep(1)  # Aguarde o arquivo carregar

        # Enviar a mensagem
        pyautogui.press('enter')

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    phone_number = sys.argv[1]
    message = sys.argv[2]
    attachment_path = "divulgacao.png"  # Usar o caminho do anexo passado ou o padrão
    #attachment_path = sys.argv[3] if len(sys.argv) > 3 else "divulgacao.png"  # Usar o caminho do anexo passado ou o padrão
    send_whatsapp_message(phone_number, message, attachment_path)
