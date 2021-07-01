from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Permite que rode no background || Allows the script to run in the background

# from selenium.webdriver.chrome.options import Options   
# chrome_options = Options()
# chrome_options.headless = True
# nav = webdriver.Chrome(options=chrome_options)


#Escolha o browser ||  Choose your browser 
browser = webdriver.Chrome()

#Use isto para inserir o texto do seu post dentro do terminal || Use this line to write your post's text on the terminal
#post = input('insira o texto do post aqui: ')

#Insere aqui o site que se quer acessar || Insert here the website you want to acess
browser.get('https://www.linkedin.com')


#Aqui vai o seu log-in de usuario || Here's where you input your username 
browser.find_element_by_xpath('//*[@id="session_key"]').send_keys('Log-in/Username')

#E aqui a sua senha || And here your password
browser.find_element_by_xpath('//*[@id="session_password"]').send_keys('Senha || Password')

#Este é o click para entrar na conta. Tambem pode-se usar o .send_keys(Keys.ENTER) se preferir || Here is where click to log in. You could use .send_keys(Keys.ENTER) if you prefer
browser.find_element_by_xpath('//*[@id="main-content"]/section[1]/div[2]/form/button').click()
#browser.find_element_by_xpath('//*[@id="session_password"]').send_keys(Keys.ENTER)

#Para garantir que a pagina carregue e os elemento esteja la para ser encontrado, coloque o time.sleep() que faz o script esperar por deteminado tempo em segundos
#To garantee that the page is loaded and the elements found, put the script to sleep for some time in seconds with time.sleep()
# Exemplo || Example
#time.sleep(3)  -----> script espera 3 segundos antes de presseguir || script will wait for 3 seconds before proceeding

#Este click abre o espaço para inserir o texto do post || This click opens up the textbox so you can write your post
browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div/div/div/main/div[1]/div/div[1]/button').click()

#Finalmente o texto que você colocou é inserido na caixa do post || Finally your input is inserted in the textbox ready to be posted!
browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]').send_keys('Post text here || Texto do post aqui')


#Para que a postagem também seja automatizada, basta adicionar:  || To also automate the posting action itself, just add this line: 
#browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button').click()

#Para que o browser feche depois de rodar o script || To close the browser after the script has ended
#browser.quit()
