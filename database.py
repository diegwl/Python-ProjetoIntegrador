import pandas as pd
import openpyxl


def del_xlsx():
    dados = pd.read_excel("Produtos.xlsx")
    df = pd.DataFrame(dados)
    df.drop()


def create_xlsx():
    d = {"Produto": [''], "Preço": ['']}
    dados = pd.DataFrame(data=d)
    dados.to_excel("Produtos.xlsx", index=False)


def del_csv():
    dados = pd.read_csv("Produtos.csv")
    df = pd.DataFrame(dados)
    df.drop()


def create_csv():
    d = {"Produto": [''], "Preço": ['']}
    dados = pd.DataFrame(data=d)
    dados.to_csv("Produtos.csv", index=False)


def exportar_xlsx(produto, preco):
    df = pd.read_excel("Produtos.xlsx")
    df.loc[len(df)] = [produto, preco]
    df.to_excel("Produtos.xlsx", index=False)


def exportar_csv(produto, preco):
    df = pd.read_csv("Produtos.csv")
    df.loc[len(df)] = [produto, preco]
    df.to_csv("Produtos.csv", index=False)
