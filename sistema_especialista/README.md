# **Sistema Especialista para Inferência de Sugestões de Refeições**

## 📝 Resumo

O repósitorio mostra o protótipo de Sistema Especialista (SE) projetado para auxiliar na tomada de decisão sobre o preparo de refeições. O problema central abordado é a seleção de pratos sob as restrições de tempo de preparo e disponibilidade de ingredientes. Utilizando a linguagem Python, a biblioteca `Experta` como motor de inferência e `Tkinter` para a interface gráfica, o sistema implementa uma base de conhecimento com regras hierárquicas para mapear as entradas do usuário a um conjunto de sugestões de receitas. O artefato de software resultante demonstra a viabilidade do paradigma de sistemas baseados em regras para resolver problemas práticos de recomendação, ao mesmo tempo que evidencia as limitações de uma base de conhecimento estática e acoplada à lógica.

**Palavras-chave:** Sistema Especialista, Motor de Inferência, Base de Conhecimento, Python, Experta, Tomada de Decisão.

---

### 📜 Índice

1. [Introdução](#-1-introdução)
2. [Metodologia](#2-metodologia)
3. [Implementação Técnica](#-3-implementação-técnica)
4. [Guia de Utilizacao](#4-guia-de-utilizacao)
5. [Conclusão e Trabalhos Futuros](#-5-conclusão-e-trabalhos-futuros)
6. [Autor](#-6-autor)

---

### 🎯 1. Introdução

A seleção de uma refeição para preparo é um problema de tomada de decisão comum, frequentemente sujeito a um conjunto de restrições dinâmicas. Os fatores nesse processo são o tempo disponível e os ingredientes à disposição do indivíduo.

O objetivo deste projeto foi desenvolver um protótipo de software, na forma de um Sistema Especialista, que formaliza o processo de decisão e oferece sugestões lógicas e contextualizadas ao usuário. A aplicação visa servir como uma ferramenta de apoio, trazendo o conhecimento sobre combinações de pratos em uma base de regras.

### 2. Metodologia

A abordagem adotada para a solução do problema foi o desenvolvimento de um sistema baseado em regras, um paradigma clássico de Inteligência Artificial.

#### 2.1. Representação do Conhecimento

O conhecimento do domínio foi modelado através de Fatos (`Facts`) e Regras (`Rules`), utilizando as abstrações fornecidas pela biblioteca `Experta`.

- **Fatos:** Representam as unidades de informação declaradas pelo usuário. Foram definidas duas classes de fatos:

  - `Tempo`: Uma estrutura que armazena a disponibilidade de tempo do usuário em três níveis discretos: `pouco`, `medio` e `muito`.
  - `Ingrediente`: Uma estrutura que armazena a disponibilidade dos ingredientes primários: `frango`, `carne` e `macarrao`.

- **Motor de Inferência:** O sistema utiliza o motor de inferência _forward-chaining_ da biblioteca `Experta`. A partir de um conjunto inicial de fatos declarados pela interface, o motor avalia la base de regras e ativa ("dispara") todas as regras cujas condições são satisfeitas, adicionando os resultados a uma lista de conclusões.

#### 2.2. Arquitetura da Base de Regras

A base de conhecimento foi estruturada de forma hierárquica. O `Tempo` funciona como o critério primário de filtragem, definindo o escopo das receitas possíveis. Subsequentemente, as regras avaliam as combinações de `Ingredientes` para refinar a busca.

A base de regras é composta por um conjunto de regras distintas, cada uma mapeando uma combinação específica de fatos `Tempo` e `Ingrediente` a um ou mais resultados. A lógica de sugestão para combinações de ingredientes é cumulativa; por exemplo, a regra para `Frango + Carne` inclui as sugestões individuais de ambos, além de pratos que os combinam.

### 2.3 Hierarquia das Regras

A lógica é organizada hierarquicamente para abranger todas as combinações possíveis:

``` bash
Tempo
├── Pouco
│   ├── Frango
│   │   └── Resultado: "Bife de frango ou Frango grelhado"
│   │
│   ├── Carne
│   │   └── Resultado: "Bife de carne"
│   │
│   ├── Macarrão
│   │   └── Resultado: "Macarrão ao alho e óleo"
│   │
│   ├── Frango + Carne
│   │   └── Resultado: "Bife de frango e carne grelhada /
│   │                   Bife de frango /
│   │                   Bife de carne"
│   │
│   ├── Frango + Macarrão
│   │   └── Resultado: "Frango grelhado com macarrão /
│   │                   Macarrão ao alho e óleo /
│   │                   Bife de frango"
│   │
│   ├── Carne + Macarrão
│   │   └── Resultado: "Bife de carne com macarrão /
│   │                   Bife de carne /
│   │                   Macarrão ao alho e óleo"
│   │
│   └── Frango + Carne + Macarrão
│       └── Resultado: "Frango e carne com macarrão /
│                       Bife de frango /
│                       Bife de carne /
│                       Macarrão ao alho e óleo"
│
├── Médio
│   ├── Frango
│   │   └── Resultado: "Strogonoff de frango / Frango grelhado"
│   │
│   ├── Carne
│   │   └── Resultado: "Carne assada ou ensopado rápido / Bife de carne"
│   │
│   ├── Macarrão
│   │   └── Resultado: "Macarrão ao creme de leite / Macarrão ao alho e óleo"
│   │
│   └── Combinações (Frango + Carne, Frango + Macarrão, etc.)
│       └── Resultado: combinações hierárquicas de pratos intermediários
│
└── Muito
    ├── Frango
    │   └── Resultado: "Frango assado ou Frango recheado /
    │                   Strogonoff de frango"
    │
    ├── Carne
    │   └── Resultado: "Carne assada elaborada /
    │                   Carne assada ou ensopado rápido"
    │
    ├── Macarrão
    │   └── Resultado: "Macarrão especial com molho elaborado /
    │                   Macarrão ao creme de leite"
    │
    └── Combinações (Frango + Carne, Frango + Macarrão, etc.)
        └── Resultado: combinações hierárquicas de pratos elaborados
```

---

### 💻 3. Implementação Técnica

Desenvolvido com as seguintes tecnologias:

- **Linguagem de Programação:** Python 3.x.
- **Motor de Inferência:** A classe `Sugestao`, que herda de `KnowledgeEngine` da biblioteca `Experta`, encapsula toda a base de regras do sistema.
- **Interface Gráfica (GUI):** Construída com a biblioteca `Tkinter`. A interface permite ao usuário declarar os fatos iniciais através de widgets `TRadiobutton` para a seleção de tempo e `TCheckbutton` para os ingredientes. Um `TButton` inicia o processo de inferência, e os resultados são exibidos dinamicamente como uma lista de `Label` clicáveis, que acionam a abertura de links de receitas via `webbrowser`.

### 4. Guia de Utilizacao

#### 4.1. Pré-requisitos

- Python 3.6 ou superior.

#### 4.2. Instalação

1. **Clone o repositório:**

    ```sh
    git clone [https://github.com/joaokrv/SERefeicao](https://github.com/joaokrv/SERefeicao)
    cd SERefeicao
    ```

2. **Instale as dependências:**
    Recomenda-se criar um ambiente virtual. O projeto depende da biblioteca `experta`.

    ```sh
    pip install experta
    ```

#### 4.3. Execução

Para iniciar a aplicação, execute o script principal a partir do terminal:

```sh
python main.py
```

A interface será aberta. Interaja com os widgets para selecionar suas opções e clique em "Verificar seleção" para obter as sugestões.

### 🔬 5. Conclusão e Trabalhos Futuros

Este projeto demonstrou com sucesso a aplicação de técnicas de sistemas especialistas para resolver um problema de decisão cotidiano. O protótipo é funcional e a arquitetura inicial é válida para o escopo definido.

Como evolução, o plano maior é **desacoplar os dados da lógica**. Envolvendo a migração da base de conhecimento para uma estrutura de dados externa (como um arquivo JSON, CSV ou um banco de dados) e a refatoração do motor de inferência para utilizar uma única regra genérica, que iteraria sobre essa base de dados para encontrar correspondências.

### 👨‍💻 6. Autor

- João Victor Oliveira de Carvalho
