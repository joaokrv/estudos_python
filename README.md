# Estudos Python — Inteligência Artificial

## Sobre
Este repositório reúne exercícios e pequenas implementações em Python feitas durante os estudos da disciplina de Inteligência Artificial na faculdade. O objetivo é manter um histórico organizado das atividades, facilitar a reprodução dos experimentos e apoiar o versionamento dos códigos usados nas entregas.

## Estrutura geral
Os arquivos e pastas seguem um formato por atividade para facilitar navegação. Exemplos:

- `Ativdade_05-09/` — atividade sobre Perceptron (exemplo mínimo em `main.py`).
- `...` — outras atividades e exercícios organizados por pasta.

Mantenha cada atividade dentro de uma pasta própria com um `README.md` explicando o exercício e um arquivo principal (`main.py`, `notebook.ipynb`, etc.).

## Exemplo: atividade Perceptron
Na pasta `Ativdade_05-09/` há um exemplo simples com as funções `perceptron_input` e `perceptron_output`. Consulte `Ativdade_05-09/README.md` para a explicação detalhada da atividade, respostas às perguntas conceituais e instruções de execução.

## Como executar os exemplos
Recomenda-se usar Python 3.8+ e um ambiente virtual.

No PowerShell (Windows):

```pwsh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
# Para rodar um exemplo específico (ex.: perceptron):
python Ativdade_05-09/main.py
```

No bash/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python Ativdade_05/09/main.py
```

Observação: muitos exemplos deste repositório não dependem de bibliotecas externas; se adicionar dependências, inclua um `requirements.txt` na pasta correspondente.

## Boas práticas para commits e versionamento
- Faça commits pequenos e com mensagens descritivas.
- Crie um repositório remoto (GitHub/GitLab) por atividade ou um repositório monolítico com pastas por atividade.
- Inclua um `README.md` em cada pasta de atividade com: objetivo, explicação conceitual, como executar e resultados esperados.

Passos rápidos para versionar:

```pwsh
git init
git add .
git commit -m "Adiciona atividade X"
git remote add origin <URL_DO_REPOSITORIO>
git push -u origin main
```

## Sugestões de workflow para estudos de IA
- Documente hipóteses e resultados no `README.md` da atividade.
- Use notebooks (`.ipynb`) para análises experimentais e gráficos.
- Adicione pequenos testes ou scripts de verificação para garantir que os exemplos executem sem erros.

## Próximos passos recomendados
- Implementar o algoritmo de treinamento do Perceptron e testar com os conjuntos AND/OR/XOR.
- Criar notebooks com visualizações das fronteiras de decisão (matplotlib).
- Adicionar um `requirements.txt` e scripts `run_examples.py` para automatizar execuções.

## Contribuições
Este repositório é pessoal (estudos). Se quiser organizar colaborações, indique no `README.md` de cada atividade como contribuir (issues/prs).

## Licença
MIT
