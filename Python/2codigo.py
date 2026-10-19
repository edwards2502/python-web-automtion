import pyautogui
import time
pyautogui.PAUSE=0.9
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(4)
pyautogui.click(x=905, y=378)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha muito muito muito dificilima")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("enter")

time.sleep(2)

import pandas
tabela = pandas.read_csv("produtos (1).csv")
print(tabela)
for linha in tabela.index:
    pyautogui.click(x=855, y=258)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])

    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(500)