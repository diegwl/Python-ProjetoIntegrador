from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from database import *


class Web:
    def __init__(self):
        self.site = "https://diegwl.github.io/Web-ProjetoIntegrador/views/products.html"
        self.map = {
            'produto': {
                'xpath': '/html/body/main/div/section/a[&&]/div/div[2]/h3[1]'
            },
            'preco': {
                'xpath': '/html/body/main/div/section/a[&&]/div/div[2]/h3[2]'
            }
        }

    def webscraping(self):
        opcao = int(input("Deseja exportar as informações para qual tipo de arquivo?\n1 - .xlsx\n2 - .csv\n"))
        self.driver = webdriver.Chrome()
        self.driver.get(self.site)
        sleep(2)
        i = 1
        if opcao == 1:
            try:
                del_xlsx()
            except:
                pass
            create_xlsx()
            while True:
                try:
                    self.produto = self.driver.find_element(By.XPATH,
                                                            self.map['produto']['xpath'].replace('&&', f'{i}')).text
                    self.preco = self.driver.find_element(By.XPATH,
                                                          self.map['preco']['xpath'].replace('&&', f'{i}')).text
                    exportar_xlsx(self.produto, self.preco)
                    i += 1
                except:
                    break
        elif opcao == 2:
            try:
                del_csv()
            except:
                pass
            create_csv()
            while True:
                try:
                    self.produto = self.driver.find_element(By.XPATH,
                                                            self.map['produto']['xpath'].replace('&&', f'{i}')).text
                    self.preco = self.driver.find_element(By.XPATH,
                                                          self.map['preco']['xpath'].replace('&&', f'{i}')).text
                    exportar_csv(self.produto, self.preco)
                    i += 1
                except:
                    break
        else:
            print("Erro")
