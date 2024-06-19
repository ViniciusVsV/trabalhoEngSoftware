from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração inicial
driver = webdriver.Chrome()

# Carregar a página inicial
driver.get("file:///C:/Users/vini1/OneDrive/%C3%81rea%20de%20Trabalho/engSoft/trabalhoEngSoftware/Prototipo/index.html")  # Atualize o caminho para o arquivo local

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
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarUsuario()\"]")
    except Exception as e:
        print(f"Erro ao encontrar o botão de consulta de usuário: {e}")
        driver.quit()
        return
    
    botao_consultar.click()
    time.sleep(1)

    # Verificar se há resultados da consulta
    try:
        resultado_consulta = driver.find_element(By.ID, "resultadoConsultaUsuario")
        usuarios_encontrados = resultado_consulta.find_elements(By.CLASS_NAME, "expandable")
        
        if usuarios_encontrados:
            # Clicar no primeiro usuário encontrado para expandir os detalhes
            usuarios_encontrados[0].click()
            time.sleep(1)

            # Verificar se os detalhes estão visíveis
            detalhes_usuario = driver.find_element(By.ID, "usuario0")
            if not detalhes_usuario.is_displayed():
                print("Erro: Detalhes do usuário não estão visíveis após clicar para expandir.")
            else:
                print("Sucesso: Detalhes do usuário estão visíveis.")
                time.sleep(2)

            # Editar o usuário
            try:
                botao_editar = detalhes_usuario.find_element(By.XPATH, ".//button[contains(text(), 'Editar')]")
                botao_editar.click()
                time.sleep(1)
                # Interagir com os prompts (deve-se modificar para sua automação específica de prompts)
                driver.switch_to.alert.send_keys("Teste Editar")
                driver.switch_to.alert.accept()
                time.sleep(1)
                driver.switch_to.alert.send_keys("Administrador")
                driver.switch_to.alert.accept()
                time.sleep(1)
                driver.switch_to.alert.send_keys("Teste Senha Nova")
                driver.switch_to.alert.accept()
                time.sleep(1)
                print("Sucesso: Usuário editado.")

            except Exception as e:
                print(f"Erro ao editar o usuário: {e}")
        else:
            print("Nenhum usuário encontrado na consulta.")
    except Exception as e:
        print(f"ERRO -1")

    #Pesquisar novamente o usuário editado
    # Depuração: Verificar se o campo de consulta está presente
    try:
        consulta_nome_usuario = driver.find_element(By.ID, "consultaNomeUsuario")
    except Exception as e:
        print(f"ERRO 0{e}")
        driver.quit()
        return
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarUsuario()\"]")
    except Exception as e:
        print(f"ERRO 1")
        driver.quit()
        return
    
    botao_consultar.click()
    time.sleep(1)

    resultado_consulta = driver.find_element(By.ID, "resultadoConsultaUsuario")
    usuarios_encontrados = resultado_consulta.find_elements(By.CLASS_NAME, "expandable")
    
    if usuarios_encontrados:
        # Clicar no primeiro usuário encontrado para expandir os detalhes
        usuarios_encontrados[0].click()
        time.sleep(2)

    # Remover o usuário
    try:
        # Re-localizar o botão de remoção para evitar "stale element reference"
        botao_remover = driver.find_element(By.XPATH, "//div[@id='usuario0']//button[contains(text(), 'Remover')]")
        botao_remover.click()
        time.sleep(1)
        print("Sucesso: Usuário removido.")
    except Exception as e:
        print(f"Erro ao remover o usuário: {e}")

    #Pesquisar novamente o usuário Removido
    # Depuração: Verificar se o campo de consulta está presente
    try:
        consulta_nome_usuario = driver.find_element(By.ID, "consultaNomeUsuario")
    except Exception as e:
        print(f"Erro ao encontrar o campo de consulta de usuário: {e}")
        driver.quit()
        return
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarUsuario()\"]")
    except Exception as e:
        print(f"Erro ao encontrar o botão de consulta de usuário: {e}")
        driver.quit()
        return
    
    botao_consultar.click()
    time.sleep(3)

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
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarCliente()\"]")
    except Exception as e:
        print(f"Erro ao encontrar o botão de consulta de cliente: {e}")
        driver.quit()
        return
    
    botao_consultar.click()
    time.sleep(1)

    # Verificar se há resultados da consulta
    try:
        resultado_consulta = driver.find_element(By.ID, "resultadoConsultaCliente")
        clientes_encontrados = resultado_consulta.find_elements(By.CLASS_NAME, "expandable")
        
        if clientes_encontrados:
            # Clicar no primeiro cliente encontrado para expandir os detalhes
            clientes_encontrados[0].click()
            time.sleep(1)

            # Verificar se os detalhes estão visíveis
            detalhes_cliente = driver.find_element(By.ID, "cliente0")
            if not detalhes_cliente.is_displayed():
                print("Erro: Detalhes do cliente não estão visíveis após clicar para expandir.")
            else:
                print("Sucesso: Detalhes do cliente estão visíveis.")
                time.sleep(2)

                # Editar o cliente
                try:
                    botao_editar = detalhes_cliente.find_element(By.XPATH, ".//button[contains(text(), 'Editar')]")
                    botao_editar.click()
                    time.sleep(1)
                    # Interagir com os prompts (deve-se modificar para sua automação específica de prompts)
                    driver.switch_to.alert.send_keys("Teste Editar Nome Cliente")
                    driver.switch_to.alert.accept()
                    time.sleep(1)
                    driver.switch_to.alert.accept()
                    time.sleep(1)
                    driver.switch_to.alert.accept()
                    time.sleep(1)
                    driver.switch_to.alert.accept()
                    time.sleep(1)
                    driver.switch_to.alert.accept()
                    time.sleep(1)
                    driver.switch_to.alert.accept()
                    time.sleep(1)
                    driver.switch_to.alert.accept()
                    time.sleep(1)
                    print("Sucesso: cliente editado.")

                except Exception as e:
                    print(f"Erro ao editar o cliente: {e}")
        else:
            print("Nenhum cliente encontrado na consulta.")
    except Exception as e:
        print(f"ERRO -1")

    #Pesquisar novamente o cliente editado
    # Depuração: Verificar se o campo de consulta está presente
    try:
        consulta_nome_cliente = driver.find_element(By.ID, "consultaNomeCliente")
    except Exception as e:
        print(f"ERRO 0")
        driver.quit()
        return
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarCliente()\"]")
    except Exception as e:
        print(f"ERRO 1")
        driver.quit()
        return
    
    botao_consultar.click()
    time.sleep(1)

    resultado_consulta = driver.find_element(By.ID, "resultadoConsultaCliente")
    clientes_encontrados = resultado_consulta.find_elements(By.CLASS_NAME, "expandable")
    
    if clientes_encontrados:
        # Clicar no primeiro cliente encontrado para expandir os detalhes
        clientes_encontrados[0].click()
        time.sleep(2)

    # Remover o cliente
    try:
        # Re-localizar o botão de remoção para evitar "stale element reference"
        botao_remover = driver.find_element(By.XPATH, "//div[@id='cliente0']//button[contains(text(), 'Remover')]")
        botao_remover.click()
        time.sleep(1)
        print("Sucesso: cliente removido.")
    except Exception as e:
        print(f"Erro ao remover o cliente: {e}")

    #Pesquisar novamente o cliente Removido
    # Depuração: Verificar se o campo de consulta está presente
    try:
        consulta_nome_cliente = driver.find_element(By.ID, "consultaNomeCliente")
    except Exception as e:
        print(f"Erro ao encontrar o campo de consulta de cliente: {e}")
        driver.quit()
        return
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarCliente()\"]")
    except Exception as e:
        print(f"ERRO SEILAKKK")
        driver.quit()
        return

    botao_consultar.click()
    time.sleep(3)

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

    # Verificar se há resultados da consulta
    try:
        resultado_consulta = driver.find_element(By.ID, "resultadoConsultaExercicio")
        exercicios_encontrados = resultado_consulta.find_elements(By.CLASS_NAME, "expandable")
        
        if exercicios_encontrados:
            # Clicar no primeiro exercício encontrado para expandir os detalhes
            exercicios_encontrados[0].click()
            time.sleep(1)

            # Verificar se os detalhes estão visíveis
            detalhes_exercicio = driver.find_element(By.ID, "exercicio0")
            if not detalhes_exercicio.is_displayed():
                print("Erro: Detalhes do exercício não estão visíveis após clicar para expandir.")
            else:
                print("Sucesso: Detalhes do exercício estão visíveis.")
                time.sleep(2)

            
            # Editar o exercicio
            try:
                botao_editar = detalhes_exercicio.find_element(By.XPATH, ".//button[contains(text(), 'Editar')]")
                botao_editar.click()
                time.sleep(1)
                # Interagir com os prompts (deve-se modificar para sua automação específica de prompts)
                driver.switch_to.alert.send_keys("Teste Editar Nome Exercício")
                driver.switch_to.alert.accept()
                time.sleep(1)
                driver.switch_to.alert.accept()
                time.sleep(1)
                driver.switch_to.alert.accept()
                time.sleep(1)
                driver.switch_to.alert.accept()
                time.sleep(1)
                print("Sucesso: exercicio editado.")

            except Exception as e:
                print(f"Erro ao editar o exercicio: {e}")
        else:
            print("Nenhum exercicio encontrado na consulta.")
    except Exception as e:
        print(f"ERRO -1")

    #Pesquisar novamente o exercicio editado
    # Depuração: Verificar se o campo de consulta está presente
    try:
        consulta_nome_exercicio = driver.find_element(By.ID, "consultaNomeExercicio")
    except Exception as e:
        print(f"ERRO 0")
        driver.quit()
        return
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarExercicio()\"]")
    except Exception as e:
        print(f"ERRO 1")
        driver.quit()
        return
    
    botao_consultar.click()
    time.sleep(1)

    resultado_consulta = driver.find_element(By.ID, "resultadoConsultaExercicio")
    exercicios_encontrados = resultado_consulta.find_elements(By.CLASS_NAME, "expandable")
    
    if exercicios_encontrados:
        # Clicar no primeiro exercicio encontrado para expandir os detalhes
        exercicios_encontrados[0].click()
        time.sleep(2)

    # Remover o exercicio
    try:
        # Re-localizar o botão de remoção para evitar "stale element reference"
        botao_remover = driver.find_element(By.XPATH, "//div[@id='exercicio0']//button[contains(text(), 'Remover')]")
        botao_remover.click()
        time.sleep(1)
        print("Sucesso: exercicio removido.")
    except Exception as e:
        print(f"Erro ao remover o exercicio: {e}")

    #Pesquisar novamente o exercicio Removido
    # Depuração: Verificar se o campo de consulta está presente
    try:
        consulta_nome_exercicio = driver.find_element(By.ID, "consultaNomeExercicio")
    except Exception as e:
        print(f"Erro ao encontrar o campo de consulta de exercicio: {e}")
        driver.quit()
        return
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarExercicio()\"]")
    except Exception as e:
        print(f"ERRO SEILAKKK")
        driver.quit()
        return

    botao_consultar.click()
    time.sleep(3)

def test_inserir_ficha():
    # Atualizar a página
    driver.refresh()

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

    # Verificar se há resultados da consulta
    try:
        resultado_consulta = driver.find_element(By.ID, "resultadoConsultaFicha")
        fichas_encontrados = resultado_consulta.find_elements(By.CLASS_NAME, "expandable")
        
        if fichas_encontrados:
            # Clicar no primeiro ficha encontrado para expandir os detalhes
            fichas_encontrados[0].click()
            time.sleep(1)

            # Verificar se os detalhes estão visíveis
            detalhes_ficha = driver.find_element(By.ID, "ficha0")
            if not detalhes_ficha.is_displayed():
                print("Erro: Detalhes do ficha não estão visíveis após clicar para expandir.")
            else:
                print("Sucesso: Detalhes do ficha estão visíveis.")
                time.sleep(2)
            
            # Editar o ficha
            try:
                botao_editar = detalhes_ficha.find_element(By.XPATH, ".//button[contains(text(), 'Editar')]")
                botao_editar.click()
                time.sleep(1)
                # Interagir com os prompts (deve-se modificar para sua automação específica de prompts)
                driver.switch_to.alert.send_keys("Teste Editar Nome ficha")
                driver.switch_to.alert.accept()
                time.sleep(1)
                driver.switch_to.alert.accept()
                time.sleep(1)
                driver.switch_to.alert.accept()
                time.sleep(1)
                driver.switch_to.alert.accept()
                time.sleep(1)
                driver.switch_to.alert.accept()
                time.sleep(1)
                driver.switch_to.alert.accept()
                time.sleep(1)
                print("Sucesso: ficha editado.")

            except Exception as e:
                print(f"Erro ao editar o ficha: {e}")
        else:
            print("Nenhum ficha encontrado na consulta.")
    except Exception as e:
        print(f"ERRO -1")

    #Pesquisar novamente o ficha editado
    # Depuração: Verificar se o campo de consulta está presente
    try:
        consulta_nome_ficha = driver.find_element(By.ID, "consultaClienteFicha")
    except Exception as e:
        print(f"ERRO 0")
        driver.quit()
        return
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarFicha()\"]")
    except Exception as e:
        print(f"ERRO 1")
        driver.quit()
        return
    
    botao_consultar.click()
    time.sleep(1)

    resultado_consulta = driver.find_element(By.ID, "resultadoConsultaFicha")
    fichas_encontrados = resultado_consulta.find_elements(By.CLASS_NAME, "expandable")
    
    if fichas_encontrados:
        # Clicar no primeiro ficha encontrado para expandir os detalhes
        fichas_encontrados[0].click()
        time.sleep(2)

    # Remover o ficha
    try:
        # Re-localizar o botão de remoção para evitar "stale element reference"
        botao_remover = driver.find_element(By.XPATH, "//div[@id='ficha0']//button[contains(text(), 'Remover')]")
        botao_remover.click()
        time.sleep(1)
        print("Sucesso: ficha removido.")
    except Exception as e:
        print(f"Erro ao remover o ficha: {e}")

    #Pesquisar novamente o ficha Removido
    # Depuração: Verificar se o campo de consulta está presente
    try:
        consulta_nome_ficha = driver.find_element(By.ID, "consultaClienteFicha")
    except Exception as e:
        print(f"Erro ao encontrar o campo de consulta de ficha: {e}")
        driver.quit()
        return
    
    # Depuração: Verificar se o botão de consulta está presente
    try:
        botao_consultar = driver.find_element(By.XPATH, "//button[@onclick=\"consultarFicha()\"]")
    except Exception as e:
        print(f"ERRO SEILAKKK")
        driver.quit()
        return

    botao_consultar.click()
    time.sleep(3)

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
