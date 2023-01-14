from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import os
os.system("cls")

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico)
 
def click(xpath):
    navegador.find_element('xpath',xpath).click()
def escreva(xpath, texto):
    navegador.find_element('xpath',xpath).send_keys(texto)
def ler(html):
    text = navegador.get_attribute(html)
    print(text)
    
def init():# Localizar o local do site com xpath
    url = ("https://escola1.info/FTESM")
    navegador.get(url)
    # Realizar login
    escreva("/html/body/form/div[6]/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input",login)
    escreva("/html/body/form/div[6]/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[4]/input",senha)
    click("/html/body/form/div[6]/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[5]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a")
    navegador.get("https://escola1.info/site/Servicos/Essencial/Boletim/DirecionarUsuarioBoletim.asp")
    x = input("oi")


init()