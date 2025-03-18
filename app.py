import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('Bot Excel.xlsx')
vendas_pg = workbook['Planilha1']

for linha in vendas_pg.iter_rows(min_row=2):
    print(linha[0].value)
    print(linha[1].value)
    print(linha[2].value)
    print(linha[3].value)