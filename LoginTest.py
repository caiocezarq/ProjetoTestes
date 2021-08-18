from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#email e senha parta testar login, somente o primeiro é verdadeiro
emails = ['phd48397@eoopy.com', 'teste@teste.com', '']
senhas = ['testelandix2021', 'teste', '']

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
#print("Titulo da página é", driver.title)
#print("URL da página é", driver.current_url)

for i in range(len(emails)):
    driver.get("https://github.com/")
    driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a').click()
    
    campo_email = driver.find_element_by_xpath('//*[@id="login_field"]')
    campo_senha = driver.find_element_by_xpath('//*[@id="password"]')
    sleep(1)
    campo_email.send_keys(emails[i])
    campo_senha.send_keys(senhas[i])
    driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()
    sleep(1)
    
    try:
        if(driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary/span[2]')):
            #se o menu dropdown existe, então fez login com sucesso
            status_login = 'Login do usuário: ' + emails[i] + ' feito com sucesso!'
            
            #clica no menu dropdown
            driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary/span[2]').click()               
            sleep(1)

            #clica no menu Sign Out
            driver.find_element_by_xpath("//button[@class='dropdown-item dropdown-signout']").click()
    except NoSuchElementException:
        status_login = 'Login do usuário: ' + emails[i] + ' NÃO realizado!'        
    print(status_login)

driver.quit()

