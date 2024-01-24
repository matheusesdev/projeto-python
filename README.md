# Minicurso de Python - OneBitCode

## Descrição

Este repositório contém o código e os materiais do Minicurso de Python fornecido pela OneBitCode. O curso abordou tópicos como importação de dados, manipulação de dados, criação de gráfico e envio de e-mail utilizando SMTPLIB.

## Conteúdo do Curso

1. **Importação de Dados**: 
- Análise do Estudo de Caso
- Instalação Python
- Configuração Python
- Importação de Dados com o Pandas

2. **Manipulação de Dados**:  
- Selecionando Colunas de um Dataframe
- Gerando Tabela Pivô
- Exportando Tabela Pivô em Excel
- Lendo planilhas com Openpyxl
- Manipulando linhas e colunas em planilha
- Criando gráficos em planilhas

3. **Criando Gráfico e Envio de E-mail**: 
- Incluindo fórmulas para totalizar vendas por fabricantes
- Configuração de um app para manipular e-mails do Gmail por aplicações terceiras
- Envio de E-mail com anexo utilizando SmtpLib
- Considerações Gerais - Estudo de Caso

## Modo de Uso e Configuração
1: **Instalação de Dependências**:
Certifique-se de ter as dependências necessárias instaladas. Você pode instalar as dependências executando o seguinte comando:

```bash
pip install -r requirements.txt
```

**Nota: Este projeto requer Python 3.6 ou superior.**

2: **Importação de Dados**
No arquivo import_data.py, o código realiza a importação de dados a partir de um arquivo Excel. Execute o seguinte comando para visualizar os dados:

```bash	
python import_data.py
```

3: **Manipulação de Dados e Criação de Tabela Pivô**
Os arquivos pivot_table.py, sheet_ready.py, e add_chart.py trabalham com a manipulação de dados e criação de uma tabela pivô com gráfico.

Execute os seguintes comandos sequencialmente:

```bash
python pivot_table.py
python sheet_ready.py
python add_chart.py
```

4: **Incluindo Fórmulas na Planilha**
O arquivo formulas.py adiciona fórmulas à planilha, calculando a soma das vendas para cada fabricante. Execute o seguinte comando:

```bash
python formulas.py
```

5: **Envio de E-mail com Anexo**
O arquivo email.py é responsável pelo envio do e-mail com a planilha anexada. Certifique-se de ter configurado o arquivo senha com a senha do remetente.

Execute o seguinte comando:
```bash
python email.py
```
Lembre-se de substituir os valores no código de email.py pelos seus próprios dados de e-mail.
