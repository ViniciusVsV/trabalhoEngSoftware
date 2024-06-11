// Arrays para armazenar os dados
let clientes = [];
let usuarios = [];

// Função para mostrar seções
function showSection(sectionId) {
    document.querySelectorAll('section').forEach(section => {
        section.classList.add('hidden');
    });
    document.getElementById(sectionId).classList.remove('hidden');
}

// Função para mostrar formulários
function showForm(formId) {
    document.querySelectorAll('.form-container').forEach(form => {
        form.classList.add('hidden');
    });
    document.getElementById(formId).classList.remove('hidden');
}

// Função para inserir usuário
function inserirUsuario() {
    const nome = document.getElementById('nomeUsuario').value;
    const nivelAcesso = document.getElementById('nivelAcesso').value;
    const senha = document.getElementById('senhaUsuario').value;

    const novoUsuario = { nome, nivelAcesso, senha };
    usuarios.push(novoUsuario);
    exibirUsuarios();
    limparFormulario('inserirUsuarioForm');
}

// Função para exibir usuários
function exibirUsuarios() {
    const resultadoContainer = document.getElementById('resultadoConsultaUsuario');
    resultadoContainer.innerHTML = usuarios.map((usuario, index) => `
        <div>
            <span>${usuario.nome}</span> - <span>${usuario.nivelAcesso}</span>
            <button onclick="alterarUsuario(${index})">Alterar</button>
            <button onclick="removerUsuario(${index})">Remover</button>
        </div>
    `).join('');
}

// Função para consultar usuários
function consultarUsuario() {
    const nome = document.getElementById('consultaNomeUsuario').value;
    const nivelAcesso = document.getElementById('consultaNivelAcesso').value;

    const resultadoFiltrado = usuarios.filter(usuario => {
        return (!nome || usuario.nome.includes(nome)) &&
               (!nivelAcesso || usuario.nivelAcesso === nivelAcesso);
    });

    const resultadoContainer = document.getElementById('resultadoConsultaUsuario');
    resultadoContainer.innerHTML = resultadoFiltrado.map((usuario, index) => `
        <div>
            <span>${usuario.nome}</span> - <span>${usuario.nivelAcesso}</span>
            <button onclick="alterarUsuario(${index})">Alterar</button>
            <button onclick="removerUsuario(${index})">Remover</button>
        </div>
    `).join('');
}

// Função para alterar usuário
function alterarUsuario(index) {
    const usuario = usuarios[index];
    document.getElementById('nomeUsuario').value = usuario.nome;
    document.getElementById('nivelAcesso').value = usuario.nivelAcesso;
    document.getElementById('senhaUsuario').value = usuario.senha;

    document.getElementById('inserirUsuarioForm').onsubmit = function() {
        usuario.nome = document.getElementById('nomeUsuario').value;
        usuario.nivelAcesso = document.getElementById('nivelAcesso').value;
        usuario.senha = document.getElementById('senhaUsuario').value;

        exibirUsuarios();
        limparFormulario('inserirUsuarioForm');
        return false;
    };

    showForm('formInserirUsuario');
}

// Função para remover usuário
function removerUsuario(index) {
    usuarios.splice(index, 1);
    exibirUsuarios();
}

// Função para inserir cliente
function inserirCliente() {
    const nome = document.getElementById('nomeCliente').value;
    const dataNascimento = document.getElementById('dataNascimentoCliente').value;
    const endereco = document.getElementById('enderecoCliente').value;
    const telefone = document.getElementById('telefoneCliente').value;
    const email = document.getElementById('emailCliente').value;
    const tipoPlano = document.getElementById('tipoPlanoCliente').value;
    const status = document.getElementById('statusCliente').value;

    const novoCliente = { nome, dataNascimento, endereco, telefone, email, tipoPlano, status };
    clientes.push(novoCliente);
    exibirClientes();
    limparFormulario('inserirClienteForm');
}

// Função para exibir clientes
function exibirClientes() {
    const resultadoContainer = document.getElementById('resultadoConsultaCliente');
    resultadoContainer.innerHTML = clientes.map((cliente, index) => `
        <div>
            <span>${cliente.nome}</span> - <span>${cliente.status}</span>
            <span>${cliente.telefone}</span> - <span>${cliente.email}</span>
            <span>${cliente.endereco}</span> - <span>${cliente.tipoPlano}</span>
            <button onclick="alterarCliente(${index})">Alterar</button>
            <button onclick="removerCliente(${index})">Remover</button>
        </div>
    `).join('');
}

// Função para consultar clientes
function consultarCliente() {
    const nome = document.getElementById('consultaNomeCliente').value;
    const tipoPlano = document.getElementById('consultaTipoPlanoCliente').value;
    const status = document.getElementById('consultaStatusCliente').value;

    const resultadoFiltrado = clientes.filter(cliente => {
        return (!nome || cliente.nome.includes(nome)) &&
               (!tipoPlano || cliente.tipoPlano === tipoPlano) &&
               (!status || cliente.status === status);
    });

    const resultadoContainer = document.getElementById('resultadoConsultaCliente');
    resultadoContainer.innerHTML = resultadoFiltrado.map((cliente, index) => `
        <div>
            <span>${cliente.nome}</span> - <span>${cliente.status}</span>
            <span>${cliente.telefone}</span> - <span>${cliente.email}</span>
            <span>${cliente.endereco}</span> - <span>${cliente.tipoPlano}</span>
            <button onclick="alterarCliente(${index})">Alterar</button>
            <button onclick="removerCliente(${index})">Remover</button>
        </div>
    `).join('');
}

// Função para alterar cliente
function alterarCliente(index) {
    const cliente = clientes[index];
    document.getElementById('nomeCliente').value = cliente.nome;
    document.getElementById('dataNascimentoCliente').value = cliente.dataNascimento;
    document.getElementById('enderecoCliente').value = cliente.endereco;
    document.getElementById('telefoneCliente').value = cliente.telefone;
    document.getElementById('emailCliente').value = cliente.email;
    document.getElementById('tipoPlanoCliente').value = cliente.tipoPlano;
    document.getElementById('statusCliente').value = cliente.status;

    document.getElementById('inserirClienteForm').onsubmit = function() {
        cliente.nome = document.getElementById('nomeCliente').value;
        cliente.dataNascimento = document.getElementById('dataNascimentoCliente').value;
        cliente.endereco = document.getElementById('enderecoCliente').value;
        cliente.telefone = document.getElementById('telefoneCliente').value;
        cliente.email = document.getElementById('emailCliente').value;
        cliente.tipoPlano = document.getElementById('tipoPlanoCliente').value;
        cliente.status = document.getElementById('statusCliente').value;

        exibirClientes();
        limparFormulario('inserirClienteForm');
        return false;
    };

    showForm('formInserirCliente');
}

// Função para remover cliente
function removerCliente(index) {
    clientes.splice(index, 1);
    exibirClientes();
}

// Função para limpar o formulário
function limparFormulario(formId) {
    document.getElementById(formId).reset();
}
