import re
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#email e senha parta login
email = 'phd48397@eoopy.com'
senha = 'testelandix2021'

#texto a ser utilizado na busca
busca = 'landix'

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://github.com/")
driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a').click()
    
#Faz login no github
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
campo_busca.send_keys(Keys.ENTER)
sleep(1)

#Pega o menu para contagem do total na lista
list_menu = driver.find_elements_by_xpath("//a[@class='menu-item' or @class='menu-item selected']")

#Validação realizada através da comparação do 'Texto do Item do Menu' com o 'URL da página'
for i in range(len(list_menu)):        
    try:
        #Pega todos os elementos do menu inclusive o selecionado        
        list_menu = []
        list_menu = driver.find_elements_by_xpath("//a[@class='menu-item' or @class='menu-item selected']")
        sleep(1)        
        
        #Após a busca, a página carrega sem o URL da opção padrão do menu, portanto é necessário clicar 
        # na primeira opção e recarregar a página com o URL necessário para validação.
        list_menu[i].click()
                
        text_menu = re.sub('[^A-Za-z]', '', list_menu[i].text).upper()
        url = driver.current_url.split("type=",1)[1].upper()
        #print("Texto do Menu: " + text_menu)        
        #print("URL da página: " + url)      
                
        #Utilizado para clicar no próximo menu
        j = 0
        j = i + 1   

        #Poderia colocar qualquer outra ação aqui, mas devido a falta de tempo, 
        # irei apenas printar que a opção no menu lateral redireciona para o site correto.
        if text_menu == url:
            print('\nMenu ' + url + ' redireciona para o site correto')       
        else:
            print('Menu ' + url + ' NÃO redireciona para o site correto')       
                               
        #Como a página foi recarregada, é necessário recarregar os itens do menu
        list_menu = []
        list_menu = driver.find_elements_by_xpath("//a[@class='menu-item' or @class='menu-item selected']")
        sleep(1)

        #Proxima opção no menu 
        list_menu[j].click()
        sleep(1)
    except Exception as e:
        #Está ocorrendo uma exceção durante o try que não identifiquei
        #print(e)
        print('Não há mais opções no menu!')


driver.quit()

