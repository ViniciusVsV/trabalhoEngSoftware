from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração inicial
driver = webdriver.Chrome()

# Carregar a página inicial
driver.get("file:///C:/VsCode/Eng.%20Software%20I/trabalhoEngSoftware/Prototipo/index.html")  # Atualize o caminho para o arquivo local

def test_navegacao_secao():
    seções = ['usuarios', 'clientes', 'exercicios', 'fichas']
    for secao in seções:
        botao = driver.find_element(By.XPATH, f"//button[@onclick=\"showSection('{secao}')\"]")
        botao.click()
        time.sleep(1)
        assert driver.find_element(By.ID, secao).is_displayed(), f"Seção {secao} não está visível!"

def test_inserir_usuario():
    driver.find_element(By.XPATH, "//button[@onclick=\"showSection('usuarios')\"]").click()
    driver.find_element(By.XPATH, "//button[@onclick=\"showForm('formInserirUsuario')\"]").click()
    time.sleep(1)

    driver.find_element(By.ID, "nomeUsuario").send_keys("Teste Usuário")
    driver.find_element(By.ID, "nivelAcesso").send_keys("Administrador")
    driver.find_element(By.ID, "senhaUsuario").send_keys("senha123")
    driver.find_element(By.ID, "inserirUsuarioForm").submit()

    # Esperar pelo alerta
    time.sleep(1)
    
    # Lidar com o alerta
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    
    # Verificar se o alerta tinha a mensagem esperada
    assert alert_text == "Usuário inserido com sucesso!", f"Alerta inesperado: {alert_text}"

def test_consultar_usuario():
    driver.find_element(By.XPATH, "//button[@onclick=\"showSection('usuarios')\"]").click()
    driver.find_element(By.XPATH, "//button[@onclick=\"showForm('formConsultarUsuario')\"]").click()
    time.sleep(1)

    # Depuração: Verificar se o campo de consulta está presente
    try:
        consulta_nome_usuario = driver.find_element(By.ID, "consultaNomeUsuario")
    except Exception as e:
        print(f"Erro ao encontrar o campo de consulta de usuário: {e}")
        driver.quit()
        return

    consulta_nome_usuario.send_keys("Teste Usuário")
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarUsuario()\"]")
    except Exception as e:
        print(f"Erro ao encontrar o botão de consulta de usuário: {e}")
        driver.quit()
        return
    
    botao_consultar.click()
    time.sleep(1)

def test_inserir_cliente():
    driver.find_element(By.XPATH, "//button[@onclick=\"showSection('clientes')\"]").click()
    driver.find_element(By.XPATH, "//button[@onclick=\"showForm('formInserirCliente')\"]").click()
    time.sleep(1)

    driver.find_element(By.ID, "nomeCliente").send_keys("Teste Cliente")
    driver.find_element(By.ID, "dataNascimentoCliente").send_keys("20/10/2002")
    driver.find_element(By.ID, "enderecoCliente").send_keys("teste endereço")
    driver.find_element(By.ID, "telefoneCliente").send_keys("(31 98986-4176)")
    driver.find_element(By.ID, "emailCliente").send_keys("cliente@teste.com")
    driver.find_element(By.ID, "inserirClienteForm").submit()

    # Esperar pelo alerta
    time.sleep(1)
    
    # Lidar com o alerta
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    
    # Verificar se o alerta tinha a mensagem esperada
    assert alert_text == "Cliente inserido com sucesso!", f"Alerta inesperado: {alert_text}"

def test_consultar_cliente():
    driver.find_element(By.XPATH, "//button[@onclick=\"showSection('clientes')\"]").click()
    driver.find_element(By.XPATH, "//button[@onclick=\"showForm('formConsultarCliente')\"]").click()
    time.sleep(1)

    # Depuração: Verificar se o campo de consulta está presente
    try:
        consulta_nome_cliente = driver.find_element(By.ID, "consultaNomeCliente")
    except Exception as e:
        print(f"Erro ao encontrar o campo de consulta de cliente: {e}")
        driver.quit()
        return

    consulta_nome_cliente.send_keys("Teste Cliente")
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarCliente()\"]")
    except Exception as e:
        print(f"Erro ao encontrar o botão de consulta de cliente: {e}")
        driver.quit()
        return
    
    botao_consultar.click()
    time.sleep(1)

def test_inserir_exercicio():
    driver.find_element(By.XPATH, "//button[@onclick=\"showSection('exercicios')\"]").click()
    driver.find_element(By.XPATH, "//button[@onclick=\"showForm('formInserirExercicio')\"]").click()
    time.sleep(1)

    driver.find_element(By.ID, "nomeExercicio").send_keys("Teste Exercício")
    driver.find_element(By.ID, "descricaoExercicio").send_keys("Descrição do exercício de teste")
    driver.find_element(By.ID, "efeitoExercicio").send_keys("Peito")
    driver.find_element(By.ID, "nivelExercicio").send_keys("Iniciante")
    driver.find_element(By.ID, "inserirExercicioForm").submit()

    # Esperar pelo alerta
    time.sleep(1)
    
    # Lidar com o alerta
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    
    # Verificar se o alerta tinha a mensagem esperada
    assert alert_text == "Exercício inserido com sucesso!", f"Alerta inesperado: {alert_text}"

def test_consultar_exercicio():
    driver.find_element(By.XPATH, "//button[@onclick=\"showSection('exercicios')\"]").click()
    driver.find_element(By.XPATH, "//button[@onclick=\"showForm('formConsultarExercicio')\"]").click()
    time.sleep(1)
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarExercicio()\"]")
    except Exception as e:
        print(f"Erro ao encontrar o botão de consulta de exercício: {e}")
        driver.quit()
        return
    
    botao_consultar.click()
    time.sleep(1)

def test_inserir_ficha():
    driver.find_element(By.XPATH, "//button[@onclick=\"showSection('fichas')\"]").click()
    driver.find_element(By.XPATH, "//button[@onclick=\"showForm('formInserirFicha')\"]").click()
    time.sleep(1)

    driver.find_element(By.ID, "clienteFicha").send_keys("Teste Cliente")
    driver.find_element(By.ID, "tipoTreinoFicha").send_keys("Personalizado")
    driver.find_element(By.ID, "dataInicioFicha").send_keys("20/05/2024")
    driver.find_element(By.ID, "objetivosFicha").send_keys("Ganho de massa")
    driver.find_element(By.ID, "exerciciosFicha").send_keys("Teste Exercício")
    driver.find_element(By.ID, "tipoPlanoFicha").send_keys("Avançado")
    driver.find_element(By.ID, "inserirFichaForm").submit()

    # Esperar pelo alerta
    time.sleep(1)
    
    # Lidar com o alerta
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    
    # Verificar se o alerta tinha a mensagem esperada
    assert alert_text == "Ficha de treino inserida com sucesso!", f"Alerta inesperado: {alert_text}"

def test_consultar_ficha():
    driver.find_element(By.XPATH, "//button[@onclick=\"showSection('fichas')\"]").click()
    driver.find_element(By.XPATH, "//button[@onclick=\"showForm('formConsultarFicha')\"]").click()
    time.sleep(1)

    # Depuração: Verificar se o campo de consulta está presente
    try:
        consulta_nome_ficha = driver.find_element(By.ID, "consultaClienteFicha")
    except Exception as e:
        print(f"Erro ao encontrar o campo de consulta de ficha: {e}")
        driver.quit()
        return

    consulta_nome_ficha.send_keys("Teste Ficha")
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarFicha()\"]")
    except Exception as e:
        print(f"Erro ao encontrar o botão de consulta de ficha: {e}")
        driver.quit()
        return
    
    botao_consultar.click()
    time.sleep(1)

# Executando os testes
try:
    test_navegacao_secao()
    test_inserir_usuario()
    test_consultar_usuario()
    test_inserir_cliente()
    test_consultar_cliente()
    test_inserir_exercicio()
    test_consultar_exercicio()
    test_inserir_ficha()
    test_consultar_ficha()
finally:
    # Fechando o navegador
    driver.quit()
