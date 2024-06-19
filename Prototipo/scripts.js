function showSection(sectionId) {
    document.querySelectorAll('section').forEach(section => {
        section.classList.add('hidden');
    });
    document.getElementById(sectionId).classList.remove('hidden');
}

function showForm(formId) {
    document.querySelectorAll('.form-container').forEach(form => {
        form.classList.add('hidden');
    });
    document.getElementById(formId).classList.remove('hidden');
}

function inserirUsuario() {
    const nome = document.getElementById('nomeUsuario').value;
    const nivelAcesso = document.getElementById('nivelAcesso').value;
    const senha = document.getElementById('senhaUsuario').value;

    let usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];
    usuarios.push({ nome, nivelAcesso, senha });
    localStorage.setItem('usuarios', JSON.stringify(usuarios));

    alert('Usuário inserido com sucesso!');
    document.getElementById('inserirUsuarioForm').reset();
}

function consultarUsuario() {
    const nome = document.getElementById('consultaNomeUsuario').value.toLowerCase();
    const nivelAcesso = document.getElementById('consultaNivelAcesso').value;

    let usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];
    let resultados = usuarios.filter(usuario => {
        return (nome === "" || usuario.nome.toLowerCase().includes(nome)) &&
               (nivelAcesso === "" || usuario.nivelAcesso === nivelAcesso);
    });

    let resultadoHtml = "<h4>Resultados da Consulta:</h4>";
    if (resultados.length > 0) {
        resultadoHtml += "<ul>";
        resultados.forEach((usuario, index) => {
            resultadoHtml += `<li class="expandable" onclick="toggleDetails('usuario${index}')">${usuario.nome} - ${usuario.nivelAcesso}</li>
            <div id="usuario${index}" class="details hidden">
                <p>Nome: ${usuario.nome}</p>
                <p>Nível de Acesso: ${usuario.nivelAcesso}</p>
                <p>Senha: ${usuario.senha}</p>
                <button onclick="editarUsuario(${index})">Editar</button>
                <button onclick="removerUsuario(${index})">Remover</button>
            </div>`;
        });
        resultadoHtml += "</ul>";
    } else {
        resultadoHtml += "<p>Nenhum usuário encontrado.</p>";
    }

    document.getElementById('resultadoConsultaUsuario').innerHTML = resultadoHtml;
}

function editarUsuario(index) {
    const usuarios = JSON.parse(localStorage.getItem('usuarios'));
    const usuario = usuarios[index];

    const nome = prompt('Nome:', usuario.nome);
    const nivelAcesso = prompt('Nível de Acesso:', usuario.nivelAcesso);
    const senha = prompt('Senha:', usuario.senha);

    if (nome && nivelAcesso && senha) {
        usuarios[index] = { nome, nivelAcesso, senha };
        localStorage.setItem('usuarios', JSON.stringify(usuarios));
        consultarUsuario();
    }
}

function removerUsuario(index) {
    const usuarios = JSON.parse(localStorage.getItem('usuarios'));
    usuarios.splice(index, 1);
    localStorage.setItem('usuarios', JSON.stringify(usuarios));
    consultarUsuario();
}

function inserirCliente() {
    const nome = document.getElementById('nomeCliente').value;
    const dataNascimento = document.getElementById('dataNascimentoCliente').value;
    const endereco = document.getElementById('enderecoCliente').value;
    const telefone = document.getElementById('telefoneCliente').value;
    const email = document.getElementById('emailCliente').value;
    const tipoPlano = document.getElementById('tipoPlanoCliente').value;
    const status = document.getElementById('statusCliente').value;

    let clientes = JSON.parse(localStorage.getItem('clientes')) || [];
    clientes.push({ nome, dataNascimento, endereco, telefone, email, tipoPlano, status });
    localStorage.setItem('clientes', JSON.stringify(clientes));

    alert('Cliente inserido com sucesso!');
    document.getElementById('inserirClienteForm').reset();
}

function consultarCliente() {
    const nome = document.getElementById('consultaNomeCliente').value.toLowerCase();
    const tipoPlano = document.getElementById('consultaTipoPlanoCliente').value;
    const status = document.getElementById('consultaStatusCliente').value;

    let clientes = JSON.parse(localStorage.getItem('clientes')) || [];
    let resultados = clientes.filter(cliente => {
        return (nome === "" || cliente.nome.toLowerCase().includes(nome)) &&
               (tipoPlano === "" || cliente.tipoPlano === tipoPlano) &&
               (status === "" || cliente.status === status);
    });

    let resultadoHtml = "<h4>Resultados da Consulta:</h4>";
    if (resultados.length > 0) {
        resultadoHtml += "<ul>";
        resultados.forEach((cliente, index) => {
            resultadoHtml += `<li class="expandable" onclick="toggleDetails('cliente${index}')">${cliente.nome} - ${cliente.tipoPlano} - ${cliente.status}</li>
            <div id="cliente${index}" class="details hidden">
                <p>Nome: ${cliente.nome}</p>
                <p>Data de Nascimento: ${cliente.dataNascimento}</p>
                <p>Endereço: ${cliente.endereco}</p>
                <p>Telefone: ${cliente.telefone}</p>
                <p>Email: ${cliente.email}</p>
                <p>Tipo de Plano: ${cliente.tipoPlano}</p>
                <p>Status: ${cliente.status}</p>
                <button onclick="editarCliente(${index})">Editar</button>
                <button onclick="removerCliente(${index})">Remover</button>
            </div>`;
        });
        resultadoHtml += "</ul>";
    } else {
        resultadoHtml += "<p>Nenhum cliente encontrado.</p>";
    }

    document.getElementById('resultadoConsultaCliente').innerHTML = resultadoHtml;
}

function editarCliente(index) {
    const clientes = JSON.parse(localStorage.getItem('clientes'));
    const cliente = clientes[index];

    const nome = prompt('Nome:', cliente.nome);
    const dataNascimento = prompt('Data de Nascimento:', cliente.dataNascimento);
    const endereco = prompt('Endereço:', cliente.endereco);
    const telefone = prompt('Telefone:', cliente.telefone);
    const email = prompt('Email:', cliente.email);
    const tipoPlano = prompt('Tipo de Plano:', cliente.tipoPlano);
    const status = prompt('Status:', cliente.status);

    if (nome && dataNascimento && endereco && telefone && email && tipoPlano && status) {
        clientes[index] = { nome, dataNascimento, endereco, telefone, email, tipoPlano, status };
        localStorage.setItem('clientes', JSON.stringify(clientes));
        consultarCliente();
    }
}

function removerCliente(index) {
    const clientes = JSON.parse(localStorage.getItem('clientes'));
    clientes.splice(index, 1);
    localStorage.setItem('clientes', JSON.stringify(clientes));
    consultarCliente();
}

function inserirExercicio() {
    const nome = document.getElementById('nomeExercicio').value;
    const descricao = document.getElementById('descricaoExercicio').value;
    const efeito = Array.from(document.getElementById('efeitoExercicio').selectedOptions).map(option => option.value);
    const nivel = document.getElementById('nivelExercicio').value;

    let exercicios = JSON.parse(localStorage.getItem('exercicios')) || [];
    exercicios.push({ nome, descricao, efeito, nivel });
    localStorage.setItem('exercicios', JSON.stringify(exercicios));

    alert('Exercício inserido com sucesso!');
    document.getElementById('inserirExercicioForm').reset();
}

function consultarExercicio() {
    const nome = document.getElementById('consultaNomeExercicio').value.toLowerCase();
    const efeito = Array.from(document.getElementById('consultaEfeitoExercicio').selectedOptions).map(option => option.value);
    const nivel = document.getElementById('consultaNivelExercicio').value;

    let exercicios = JSON.parse(localStorage.getItem('exercicios')) || [];
    let resultados = exercicios.filter(exercicio => {
        return (nome === "" || exercicio.nome.toLowerCase().includes(nome)) &&
               (efeito.length === 0 || efeito.some(e => exercicio.efeito.includes(e))) &&
               (nivel === "" || exercicio.nivel === nivel);
    });

    let resultadoHtml = "<h4>Resultados da Consulta:</h4>";
    if (resultados.length > 0) {
        resultadoHtml += "<ul>";
        resultados.forEach((exercicio, index) => {
            resultadoHtml += `<li class="expandable" onclick="toggleDetails('exercicio${index}')">${exercicio.nome} - ${exercicio.efeito.join(', ')} - ${exercicio.nivel}</li>
            <div id="exercicio${index}" class="details hidden">
                <p>Nome: ${exercicio.nome}</p>
                <p>Descrição: ${exercicio.descricao}</p>
                <p>Efeito: ${exercicio.efeito.join(', ')}</p>
                <p>Nível: ${exercicio.nivel}</p>
                <button onclick="editarExercicio(${index})">Editar</button>
                <button onclick="removerExercicio(${index})">Remover</button>
            </div>`;
        });
        resultadoHtml += "</ul>";
    } else {
        resultadoHtml += "<p>Nenhum exercício encontrado.</p>";
    }

    document.getElementById('resultadoConsultaExercicio').innerHTML = resultadoHtml;
}

function editarExercicio(index) {
    const exercicios = JSON.parse(localStorage.getItem('exercicios'));
    const exercicio = exercicios[index];

    const nome = prompt('Nome:', exercicio.nome);
    const descricao = prompt('Descrição:', exercicio.descricao);
    const efeito = prompt('Efeito (separar por vírgulas):', exercicio.efeito.join(', ')).split(',').map(e => e.trim());
    const nivel = prompt('Nível:', exercicio.nivel);

    if (nome && descricao && efeito.length > 0 && nivel) {
        exercicios[index] = { nome, descricao, efeito, nivel };
        localStorage.setItem('exercicios', JSON.stringify(exercicios));
        consultarExercicio();
    }
}

function removerExercicio(index) {
    const exercicios = JSON.parse(localStorage.getItem('exercicios'));
    exercicios.splice(index, 1);
    localStorage.setItem('exercicios', JSON.stringify(exercicios));
    consultarExercicio();
}

function inserirFicha() {
    // Obtenha os valores do formulário
    const clienteFicha = document.getElementById('clienteFicha').value;
    const tipoTreinoFicha = document.getElementById('tipoTreinoFicha').value;
    const dataInicioFicha = document.getElementById('dataInicioFicha').value;
    const objetivosFicha = document.getElementById('objetivosFicha').value;
    const exerciciosFicha = Array.from(document.getElementById('exerciciosFicha').selectedOptions).map(option => option.value);
    const tipoPlanoFicha = document.getElementById('tipoPlanoFicha').value;

    // Crie um objeto de ficha de treino
    const ficha = {
        cliente: clienteFicha,
        tipoTreino: tipoTreinoFicha,
        dataInicio: dataInicioFicha,
        objetivos: objetivosFicha,
        exercicios: exerciciosFicha,
        tipoPlano: tipoPlanoFicha
    };

    // Obtenha as fichas do localStorage
    let fichas = JSON.parse(localStorage.getItem('fichas')) || [];

    // Adicione a nova ficha à lista
    fichas.push(ficha);

    // Salve a lista atualizada no localStorage
    localStorage.setItem('fichas', JSON.stringify(fichas));

    // Mostre uma mensagem de sucesso ou atualize a interface conforme necessário
    alert('Ficha de treino inserida com sucesso!');

    // Limpe o formulário
    document.getElementById('inserirFichaForm').reset();

    // Esconda o formulário após a inserção
    document.getElementById('formInserirFicha').classList.add('hidden');
}


function consultarFicha() {
    const clienteConsulta = document.getElementById('consultaClienteFicha').value;

    // Obtenha as fichas do localStorage
    const fichas = JSON.parse(localStorage.getItem('fichas')) || [];

    // Filtre as fichas pelo cliente selecionado
    const fichasFiltradas = clienteConsulta ? fichas.filter(ficha => ficha.cliente === clienteConsulta) : fichas;

    // Exiba as fichas filtradas
    const resultadoConsultaFicha = document.getElementById('resultadoConsultaFicha');
    resultadoConsultaFicha.innerHTML = '';

    if (fichasFiltradas.length === 0) {
        resultadoConsultaFicha.innerHTML = '<p>Nenhuma ficha encontrada.</p>';
    } else {
        let resultadoHtml = "<h4>Resultados da Consulta:</h4>";
        if (fichasFiltradas.length > 0) {
            resultadoHtml += "<ul>";
            fichasFiltradas.forEach((ficha, index) => {
                resultadoHtml += `<li class="expandable" onclick="toggleDetails('ficha${index}')">${ficha.cliente} - ${ficha.tipoTreino}</li>
                <div id="ficha${index}" class="details hidden">
                    <p>Cliente: ${ficha.cliente}</p>
                    <p>Tipo de Treino: ${ficha.tipoTreino}</p>
                    <p>Data de Início: ${ficha.dataInicio}</p>
                    <p>Objetivos: ${ficha.objetivos}</p>
                    <p>Exercícios: ${ficha.exercicios.join(', ')}</p>
                    <p>Tipo de Plano: ${ficha.tipoPlano}</p>
                    <button onclick="editarFicha(${index})">Editar</button>
                    <button onclick="removerFicha(${index})">Remover</button>
                </div>`;
            });
            resultadoHtml += "</ul>";
        } else {
            resultadoHtml += "<p>Nenhuma ficha encontrada.</p>";
        }

        resultadoConsultaFicha.innerHTML = resultadoHtml;
    }
}

function editarFicha(index) {
    const fichas = JSON.parse(localStorage.getItem('fichas'));
    const ficha = fichas[index];

    const cliente = prompt('Cliente:', ficha.cliente);
    const tipoTreino = prompt('Tipo de Treino:', ficha.tipoTreino);
    const dataInicio = prompt('Data de Início:', ficha.dataInicio);
    const objetivos = prompt('Objetivos:', ficha.objetivos);
    const exercicios = prompt('Exercícios:', ficha.exercicios.join(', ')).split(',').map(e => e.trim());
    const tipoPlano = prompt('Tipo de Plano:', ficha.tipoPlano);

    if (cliente && tipoTreino && dataInicio && objetivos && exercicios && tipoPlano) {
        fichas[index] = { cliente, tipoTreino, dataInicio, objetivos, exercicios, tipoPlano };
        localStorage.setItem('fichas', JSON.stringify(fichas));
        consultarFicha();
    }
}

function removerFicha(index) {
    const fichas = JSON.parse(localStorage.getItem('fichas'));
    fichas.splice(index, 1);
    localStorage.setItem('fichas', JSON.stringify(fichas));
    consultarFicha();
}

function toggleDetails(elementId) {
    const element = document.getElementById(elementId);
    element.classList.toggle('hidden');
}

document.addEventListener('DOMContentLoaded', () => {
    const clienteFichaSelect = document.getElementById('clienteFicha');
    const consultaClienteFichaSelect = document.getElementById('consultaClienteFicha');
    const exerciciosFichaSelect = document.getElementById('exerciciosFicha');

    let clientes = JSON.parse(localStorage.getItem('clientes')) || [];
    clientes.forEach(cliente => {
        const option = document.createElement('option');
        option.value = cliente.nome;
        option.textContent = cliente.nome;
        clienteFichaSelect.appendChild(option);

        const consultaOption = document.createElement('option');
        consultaOption.value = cliente.nome;
        consultaOption.textContent = cliente.nome;
        consultaClienteFichaSelect.appendChild(consultaOption);
    });

    let exercicios = JSON.parse(localStorage.getItem('exercicios')) || [];
    exercicios.forEach(exercicio => {
        const option = document.createElement('option');
        option.value = exercicio.nome;
        option.textContent = exercicio.nome;
        exerciciosFichaSelect.appendChild(option);
    });
});
