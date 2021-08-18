import re
import sys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#email e senha para login
email = 'phd48397@eoopy.com'
senha = 'testelandix2021'

#texto a ser utilizado na busca
busca = 'landix'

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://github.com/")
driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a').click()
    
#faz login no github
campo_email = driver.find_element_by_xpath('//*[@id="login_field"]')
campo_senha = driver.find_element_by_xpath('//*[@id="password"]')
sleep(1)
campo_email.send_keys(email)
campo_senha.send_keys(senha)

driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()
sleep(1)

#Faz a busca pelo repositorio
campo_busca = driver.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div/form/label/input[1]')
campo_busca.send_keys(busca)
sleep(1)
campo_busca.send_keys(Keys.ENTER)
sleep(1)

#Armazena a quantidade de respositorios em "repository results"
repositorios = re.sub('[^0-9]', '', driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/div[1]/h3').text)
print ('Busca: ' + busca + ' / Número de repositorios: ' + repositorios)

lista_rep_qtd = 0
for i in range(sys.maxsize**10):
    try:
        if(driver.find_element_by_xpath(".//a[@class='next_page']")):
            #Na ultima pagina o botão vira um span, portanto não vai existir mais
            sleep(1)

            #Lista de repositorio listados na pagina
            lista_rep = []
            lista_rep = driver.find_elements_by_xpath("//li[@class='repo-list-item hx_hit-repo d-flex flex-justify-start py-4 public source']")
            lista_rep_qtd = len(lista_rep) + lista_rep_qtd
            
            sleep(1)
            #Muda de pagina            
            driver.find_element_by_xpath(".//a[@class='next_page']").click()
    except NoSuchElementException:
        print('Total de ' + str(lista_rep_qtd) + ' em ' + str(i) + ' pagina(s)')
        break

if int(lista_rep_qtd) == int(repositorios):
    print('Número de repositorios listados nas paginas é igual ao numero de repositorios encontrados')
else:
    print('Número de repositorios listados NÃO é igual')

driver.quit()

