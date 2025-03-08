from time import sleep
import pyautogui as pg
import pandas as pd

pg.PAUSE = 0.5

pg.press('win')
pg.write('chrome')
pg.press('enter')

sleep(3)
pg.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login') #   Site da empresa
pg.press('enter')

sleep(3)
pg.click(x=480, y=408)

pg.PAUSE = 0.3

#   LOGIN
pg.write('empresa@gmail.com')
pg.press('tab')
pg.write('123456789')
pg.press('tab')
pg.press('enter')

sleep(5)
pg.press('enter')

tabela = pd.read_csv('produtos.csv') # Nome da tabela

for linha in tabela.index:

    pg.click(x=471, y=287)

    codigo = tabela.loc[linha, 'codigo']
    pg.write(codigo)
    pg.press('tab')

    pg.write(str(tabela.loc[linha, 'marca']))
    pg.press('tab')

    pg.write(str(tabela.loc[linha, 'tipo']))
    pg.press('tab')

    pg.write(str(tabela.loc[linha, 'categoria']))
    pg.press('tab')

    pg.write(str(tabela.loc[linha, 'preco_unitario']))
    pg.press('tab')

    pg.write(str(tabela.loc[linha, 'custo']))
    pg.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pg.write(obs)
    pg.press('tab')

    pg.press('enter')

    pg.scroll(5000)
    