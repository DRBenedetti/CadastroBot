# CadastroBot

## Descrição

CadastroBot é um script em Python que automatiza o processo de cadastramento de produtos em um sistema web. Utilizando as bibliotecas `pyautogui` e `pandas`, o programa acessa um site de login, insere as credenciais e cadastra os produtos listados em um arquivo CSV.

## Requisitos

Antes de executar o script, certifique-se de ter os seguintes requisitos instalados:

- Python 3.12.7
- Bibliotecas necessárias (instale com o comando abaixo):
  ```sh
  pip install pyautogui pandas
  ```

## Como Usar

1. Certifique-se de que o arquivo `produtos.csv` está na mesma pasta do script e está formatado corretamente.
2. Execute o script com:
   ```sh
   python CadastroBot.py
   ```
3. O programa abrirá o navegador, acessará o sistema de login e iniciará o cadastramento automático.

## Estrutura do Arquivo CSV

O arquivo `produtos.csv` está incluído no repositório para testes e deve conter as seguintes colunas:

O arquivo `produtos.csv` deve conter as seguintes colunas:

- `codigo`
- `marca`
- `tipo`
- `categoria`
- `preco_unitario`
- `custo`
- `obs` (opcional)

## Observação

- O script utiliza coordenadas fixas do mouse para clicar nos campos do site. Certifique-se de que a resolução da tela e o layout do site estejam compatíveis.
- Caso precise ajustar as coordenadas, utilize o seguinte código para descobrir a posição do mouse:
  ```python
  import pyautogui as pg
  print(pg.position())
  ```

## Autor

Criado por Diogo Benedetti.

