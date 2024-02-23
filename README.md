# Python-Venv-SENAI
Repositório criado para as aulas de ambiente virtual do SENAI.


## Instruções para executar

1° Coloque o arquivo de texto no diretório que você gostaria de armazenar.

2° Use o CMD para encontrar o caminho onde o arquivo está.

3° Crie uma variável de ambiente usando o comando $env:DATA_PATH = 'caminho-do-arquivo' no prompt do PC ou do ambiente. Ela só durará enquanto o prompt estiver aberto. Também é possível utilizar o SETX DATA_PATH 'caminho-do-arquivo' para criar uma variável de ambiente permanente.

4° Use o arquivo requirements.txt para baixar os requisitos utilizando o comando pip install -r requirements.txt

5° Se for usar um ambiente virtual, ative-o com o comando .\< nome-do-ambiente >\Scripts\activate. 
Obs: Caso não conseguir executar o comando por estar em uma rede com certas configurações de segurança, use o comando Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass para liberar as alterações.

6° Execute o arquivo python no ambiente através do prompt de comando usando o comando py -m data_analysis

7° Os gráficos se abrirão automaticamente.