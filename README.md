
# ProjetoNotebook-Trabalho Acadêmico

### Autor: Lucas Almeida

### Email: ra00319146@pucsp.edu.br

**Repositório criado com o intuito de facilitar a organização, atualização, controle de versão e correção de erros do código da biblioteca *ProjetoNotebook*
criada para a resolução da questão do *Tema Hipotético Acquisição de Bens*, projeto acadêmico da PUC-SP, Faculdade FEI, Curso Ciência de Dados e Inteligência
Artificial, Turma CDIA-MA1. Projeto iniciado em Abril de 2022.**

# Descrição da Biblioteca:

### Módulo Analista:

> **Define classes para o processamento, visualização e classificação dos dados presentes no arquivo .tsv em ProjetoNotebook/ProjetoNotebook/Dados/estudantes-pucsp.tsv**

> **Define classe para a realizar chamadas simultâneas, e organizar os resultados obtidos destas, à API implementada utilizando o Google Cloud Functions que possui gatilho HTTP e executa, com escalonamento automático gerenciado pela infraestrututa da Google, a função localizada no arquivo ProjetoNotebook/CodigoAPI/main.py. Tem como propósito encontrar um conjunto de 5 pesos que , quando aplicados à média ponderada das notas normalizadas definidas, geram uma filtragem dos dados dos estudantes que obedece a determinados limites fornecidos.**

>**Classes**:
>
>> *AgrupamentoCondicional*
>>- Utilizada para armazenar e modificar funções que atuam sobre os dados de cada estudante e retornam um indicador de Subconjunto para a tabela especificada.
>>- Recebe como parâmetro de inicialização opcional Ano e Mês para a busca do Salário Mínimo Vigente no período fornecido.
>>- Caso Não fornecido o parâmetro de Inicialização utiliza o módulo datetime do Python para obter o ano e mês locais da Máquina que executa o código.
>
>> *ModificarDados*
>> - Utilizada para armazenar funções que realizam operações sobre os dados originais e retornam análises pertinentes em formato pronto para a criação de gráficos
>> - Possui também funções para agrupar estudantes em subconjuntos a partir de colunas pré-determinadas para facilitar a visualização gráfica das informações
>> - Ao ser chamada inicializa uma Instância da Classe AgrupamentoCondicional, Logo aceita o mesmo parâmetro opcional desta e realiza as operações que envolvem a classificação dos estudantes em classes sociais utilizando o valor do salário mínimo obtido através da função SMWeb
>
>> *PlotarGraficos*
>> - Utiliza os dados gerados pela classe ModificarDados para facilitar a visualização destes através da Criação de Gráficos utilizando a Biblioteca de Plotagem Matplotlib, armazena funções as quais cada uma realiza a criação de um ou mais gráficos diferente e os salva como um arquivo .jpg no diretório especificado na chamada da função. Aceita o mesmo parâmetro opcional da classe AgrupamentoCondicional Pois inicializa, através da classe ModificarDados, uma instância desta.
>> 
>>   Gráficos Gerados:
>> - Histograma da Renda da tabela armazenada na variável TABESTUDANTES (Tabela Original)
>> - Gráfico de Dispersão da Renda em Escala Logaritmica com Linhas Horizontais Representando o Limite de Renda de cada Classe Social
>> - Mesmo Gráfico de Dispersão porém com linhas horizontais representando a Média das rendas com e sem Outliers, os desvios padrões , coeficientes de variações para cada um destes conjuntos e a Mediana do Conjunto com Outliers
>> - Conjunto de Gráficos de Barras Horizontais no qual cada gráfico mostra uma distribuição dos valores de uma determinada coluna na tabela e as porcentagens destes valores em relação ao total
>
>> *NotasNormalizadas*
>> - tem como propósito Armazenar as funções que alteram os valores das cinco Colunas Primárias Pré-Determinadas,Para cada estudante, com o valor da NotaNormalizada (calculada a partir deste valor) das respectivas colunas.
>> - Aceita mesmo parâmetro opcional da classe AgrupamentoCondicional para a Busca do Salário Mínimo Vigente Pois instancia uma classe desta.
>> - Define o método Criar para cada Instância que retorna uma Tabela de Notas dos estudantes utilizando a tabela na variável COLUNASP (Tabela das colunas primárias pré-determinadas) e o Salário Mínimo Encontrado pela Instância da classe AgrupamentoCondicional.
>> 
>>Critérios:
>>
>>Colunas Principais:
>>- **Renda**
>>- **Escola**
>>- **Motivação**
>>- **Curso**
>>- **Cor**
>>
>>Pesos Reguladores das Colunas Principais:
>>- **P_r**
>>- **P_e**
>>- **P_m**
>>- **P_cur**
>>- **P_c**
>>
>>Média Ponderada:
>>- **Mp = (P_r x RN + P_e x EN + P_m x MN + P_cur x CurN + P_c x CN) / (P_r+P_e+P_m+P_cur+P_c)**
>>- Com: **Mp pertercente a [0,10]**
>>
>>Tal que:
>>- **RN=Nota Normalizada da Renda**
>>- **EN=Nota Normalizada da Escola**
>>- **MN=Nota Normalizada da Motivação**
>>- **CurN=Nota Normalizada do Curso**
>>- **CN=Nota Normalizada da Cor**
>
>> *NovosPesos*
>> - Classe criada com a finalidade de realizar análises separadas sobre como diferentes pesos da Média Ponderada aplicados sobre
as notas normalizadas dos estudantes influenciam no processo de aprovação ou rejeição destes no processo. Desta forma facilitando
o entendimento humano dos perfis dos estudantes aprovados, ou não , resultantes da aplicação dos pesos passados como parâmetros,
além de permitir a checagem manual da frequência de estudantes aprovados ou rejeitados pertencentes a um subgrupo do total.
Desta forma cada instância da classe inicializada para um array de pesos específicos representa as análises ,unicas, citadas
para o array de pesos fornecidos.
>>- Consta também com um método para a criação de um gráfico de rede interativo cujos vértices são os Termos gerados pela multiplicação das notas normalizadas de um estudante qualquer pelo peso da sua respectiva coluna, permitindo assim a análise de quais colunas primárias mais estão influenciando na filtragem dos estudantes.
>>- O método permite a plotagem dos termos de um estudante único, uma lista de estudantes (Referenciados por uma string que corresponde ao seu RA) ou uma média feita para os termos dos estudantes presentes em 4 Subgrupos
>>
>>Subgrupos:
>>
>>- (Aprovados-80% da Mp Máxima)
>>- (Entre 70% e 80% da Mp Máxima)
>>- (Entre 40% e 70% da Mp Máxima)
>>- (Menor que 40% da Mp Máxima)
>>
>>- As plotagens destas médias representa o perfil de um estudante mediano em relação à sua nota de Mp de cada um destes Subconjuntos e tem como finalidade facilitar a observação de quais colunas primárias alteradas pelos pesos mais influenciam no processo de filtragem dos estudantes.
>
>>*GeradorPesos*
>> - Classe que tem como funcionalidade ajustar os parâmetros de geração aleatória de pesos utilizando valores
Aleatórios de uma distribuição Uniforme adquirida pela função do Numpy Numpy.random.uniform().
>> - Retorna Um Array do Numpy de formato [qtd,5] no qual cada linha representa um Array de Pesos Aleatórios Diferentes, sendo que o valor mínimo para qualquer elemento de qualquer um dos arrays é pmin e o valor máximo e pmax. A quantidade de arrays de Pesos Aleatórios geradas é controlada pelo parâmetro qtd que controla o formato do array gerado.
>> - O array retornado é guardado em um atributo da instância de classe iniciada chamado pesos_possiveis
>> - Classe não explicitada no módulo por estar presente na implementação da API
>
>>*TestePeso*
>> - Classe que contém somente uma função de inicialização a qual tem como parâmetro um array de pesos e a partir deste retorna
um outro array de formato (16,1) contendo as análises realizadas da filtragem dos estudantes resultante da utilização destes
pesos como os pesos da Média Ponderada das Notas Normalizadas dos estudantes.
>> - Incluida no Módulo somente como forma de verificação dos resultados obtidos através da chamada da API, já que estas análises estão incorporadas na função 'encontrar_pesos' do arquivo 'main.py' na Implementação da API.
>
>>*TestarPesoAPI*
>> - Classe utilizada para fazer múltiplas chamadas simultâneas à API de testagem dos pesos, para acelerar a busca pelos pesos filtrados, utilizando a função ThreadPoolExecutor do Módulo concurrent.features do Python ; Lidar com erros retornados pela API e formatar as múltiplas respostas bem-sucedidas em uma resposta unificada correspondente à agregação de todas as respostas obtidas
paralelamente.
>>
>>**Parâmetros de Inicialização:**
>> - *pesos_por_vm* = Quantidade de Pesos que se deseja testar por chamada da API, que executa em uma única MV no ambiente do Google Cloud.
>> - *limites* = Array de Condições das filtragens realizadas dos estudantes quando o peso que está sendo testado é usado como peso da Média Ponderada das Notas Normalizadas. Passado para a chamada da API em forma de parâmetro na URL.
>> 
>>  *Formato Array Limites* : (**NMaxAprovados**,**PctAprovadosPCurso**,**PctMinAMaisPretos**,**PctMinAmaisHomens**,**PctMinAMaisEPub**)
>> - *n_vms* = Quantidade de chamadas simultâneas que se deseja realizar à API, sendo que cada uma será executada em uma MV diferente no ambiente do Google Cloud.
