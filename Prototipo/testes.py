from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Configurar o driver do navegador (ex: Chrome)
driver = webdriver.Chrome()

# Abrir o arquivo HTML
driver.get("file:///C:/Users/vini1/OneDrive/%C3%81rea%20de%20Trabalho/engSoft/trabalhoEngSoftware/Prototipo/index.html")  # Ajuste o caminho para o seu arquivo HTML

# Função para testar a inserção de um usuário
def test_inserir_usuario(nome, nivel_acesso, senha):
    driver.find_element(By.XPATH, "//button[text()='Usuários']").click()
    driver.find_element(By.XPATH, "//button[text()='Inserir Usuário']").click()
    time.sleep(1)
    driver.find_element(By.ID, "nomeUsuario").send_keys(nome)
    Select(driver.find_element(By.ID, "nivelAcesso")).select_by_visible_text(nivel_acesso)
    driver.find_element(By.ID, "senhaUsuario").send_keys(senha)
    driver.find_element(By.XPATH, "//form[@id='inserirUsuarioForm']//button[@type='submit']").click()

# Função para testar a consulta de um usuário
def test_consultar_usuario(nome, nivel_acesso):
    driver.find_element(By.XPATH, "//button[text()='Usuários']").click()
    driver.find_element(By.XPATH, "//button[text()='Consultar Usuário']").click()
    time.sleep(1)
    driver.find_element(By.ID, "consultaNomeUsuario").send_keys(nome)
    Select(driver.find_element(By.ID, "consultaNivelAcesso")).select_by_visible_text(nivel_acesso)
    driver.find_element(By.XPATH, "//form[@id='consultarUsuarioForm']//button[text()='Consultar']").click()
    time.sleep(5)

# Função para testar a inserção de um cliente
def test_inserir_cliente(nome, data_nascimento, endereco, telefone, email, tipo_plano, status):
    driver.find_element(By.XPATH, "//button[text()='Clientes']").click()
    driver.find_element(By.XPATH, "//button[text()='Inserir Cliente']").click()
    time.sleep(1)
    driver.find_element(By.ID, "nomeCliente").send_keys(nome)
    driver.find_element(By.ID, "dataNascimentoCliente").send_keys(data_nascimento)
    driver.find_element(By.ID, "enderecoCliente").send_keys(endereco)
    driver.find_element(By.ID, "telefoneCliente").send_keys(telefone)
    driver.find_element(By.ID, "emailCliente").send_keys(email)
    Select(driver.find_element(By.ID, "tipoPlanoCliente")).select_by_visible_text(tipo_plano)
    Select(driver.find_element(By.ID, "statusCliente")).select_by_visible_text(status)
    driver.find_element(By.XPATH, "//form[@id='inserirClienteForm']//button[@type='submit']").click()

# Função para testar a consulta de um cliente
def test_consultar_cliente(nome, tipo_plano, status):
    driver.find_element(By.XPATH, "//button[text()='Clientes']").click()
    driver.find_element(By.XPATH, "//button[text()='Consultar Cliente']").click()
    time.sleep(1)
    driver.find_element(By.ID, "consultaNomeCliente").send_keys(nome)
    Select(driver.find_element(By.ID, "consultaTipoPlanoCliente")).select_by_visible_text(tipo_plano)
    Select(driver.find_element(By.ID, "consultaStatusCliente")).select_by_visible_text(status)
    driver.find_element(By.XPATH, "//form[@id='consultarClienteForm']//button[text()='Consultar']").click()
    time.sleep(5)

# Função para testar a alteração de um usuário
def test_alterar_usuario(nome_original, novo_nome, novo_nivel_acesso, nova_senha):
    # Consultar o usuário original
    driver.find_element(By.XPATH, "//button[text()='Usuários']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Consultar Usuário']").click()
    time.sleep(1)
    driver.find_element(By.ID, "consultaNomeUsuario").send_keys(nome_original)
    time.sleep(1)
    driver.find_element(By.XPATH, "//form[@id='consultarUsuarioForm']//button[text()='Consultar']").click()
    time.sleep(1)
    
    # Supondo que o resultado da consulta exiba um botão 'Alterar' ao lado do usuário encontrado
    alterar_button = driver.find_element(By.XPATH, f"//td[text()='{nome_original}']/following-sibling::td/button[text()='Alterar']")
    alterar_button.click()
    time.sleep(1)

    # Alterar os campos do usuário
    nome_field = driver.find_element(By.ID, "nomeUsuario")
    nome_field.clear()
    nome_field.send_keys(novo_nome)
    time.sleep(1)
    
    nivel_acesso_select = Select(driver.find_element(By.ID, "nivelAcesso"))
    nivel_acesso_select.select_by_visible_text(novo_nivel_acesso)
    time.sleep(1)
    
    senha_field = driver.find_element(By.ID, "senhaUsuario")
    senha_field.clear()
    senha_field.send_keys(nova_senha)
    time.sleep(5)
    
    # Submeter o formulário alterado
    driver.find_element(By.XPATH, "//form[@id='inserirUsuarioForm']//button[@type='submit']").click()
    time.sleep(1)

# Função para testar a exclusão de um usuário
def test_excluir_usuario(nome, nivel_acesso):
    test_consultar_usuario(nome, nivel_acesso)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Remover']").click()

# Função para testar a alteração de um cliente
def test_alterar_cliente(nome_original, novo_nome, nova_data_nascimento, novo_endereco, novo_telefone, novo_email, novo_tipo_plano, novo_status):
    test_consultar_cliente(nome_original, "", "")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Alterar']").click()
    time.sleep(1)
    driver.find_element(By.ID, "nomeCliente").clear()
    driver.find_element(By.ID, "nomeCliente").send_keys(novo_nome)
    driver.find_element(By.ID, "dataNascimentoCliente").clear()
    driver.find_element(By.ID, "dataNascimentoCliente").send_keys(nova_data_nascimento)
    driver.find_element(By.ID, "enderecoCliente").clear()
    driver.find_element(By.ID, "enderecoCliente").send_keys(novo_endereco)
    driver.find_element(By.ID, "telefoneCliente").clear()
    driver.find_element(By.ID, "telefoneCliente").send_keys(novo_telefone)
    driver.find_element(By.ID, "emailCliente").clear()
    driver.find_element(By.ID, "emailCliente").send_keys(novo_email)
    Select(driver.find_element(By.ID, "tipoPlanoCliente")).select_by_visible_text(novo_tipo_plano)
    Select(driver.find_element(By.ID, "statusCliente")).select_by_visible_text(novo_status)
    driver.find_element(By.XPATH, "//form[@id='inserirClienteForm']//button[@type='submit']").click()

# Função para testar a exclusão de um cliente
def test_excluir_cliente(nome, tipo_plano, status):
    test_consultar_cliente(nome, tipo_plano, status)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Remover']").click()

# Chamar as funções de teste
test_inserir_usuario("João", "Administrador", "senha123")
test_consultar_usuario("João", "Administrador")
##test_alterar_usuario("João", "João Silva", "Treinador", "novaSenha123")
##test_excluir_usuario("João Silva", "Treinador")

test_inserir_cliente("Maria", "1990-01-01", "Rua A", "(11) 98765-4321", "maria@example.com", "Premium", "Ativo")
test_consultar_cliente("Maria", "Premium", "Ativo")
##test_alterar_cliente("Maria", "Maria Silva", "1990-01-01", "Rua B", "(11) 98765-0000", "maria.silva@example.com", "Avançado", "Inativo")
##test_excluir_cliente("Maria Silva", "Avançado", "Inativo")

# Fechar o navegador após os testes
driver.quit()
