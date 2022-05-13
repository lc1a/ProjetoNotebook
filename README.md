
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
>> - *n_vms* = Quantidade de chamadas simultâneas que se deseja realizar à API, sendo que cada uma será executada em uma MV diferente no ambiente do Google Cloud.
>
>> *FiltragemKMeans*
>>
>>**Parâmetros de Inicialização**
>>
>> - *pesos_arr* = Array do Numpy de pesos para as 5 colunas principais (Que será passado para a classe NovosPesos)
>>
>> - *n_subcjts* = número de subconjuntos pré-determinado para o modelo do algoritmo KMeans.
>>
>> - *tol* = (Opcional) tolerância do modelo da instância que por padrão tem valor igual a 10.
>>
>>Classe que tem como função criar um Modelo do algortimo de clustering KMeans, implmentado pela biblioteca scikit-learn, a partir dos parâmtros de
>>inicialização fornecidos e treiná-lo utilizando as 500 Médias Ponderadas das Notas Normalizadas dos Estudantes quando se utiliza na fórmula os pesos
>>fornecidos no parâmtro *pesos_arr*. Após o treino oferece métodos para:
>>
>> - Classificar Novos estudantes a partir de suas Médias Ponderadas utilizando o modelo,
>> 
>> - Plotar um gráfico de dispersão da renda dos estudantes noeixo x e a Média Ponderada destes no eixo y no qual a cor do ponto que representa oestudante
>>   depende de qual subconjunto o estudante pertence, com o intuito de visualizar graficamente a Filtragem e divisão feita pelo modelo.
>>   
>> - Realizar uma análise das porcentagens de aprovação para estudantes pertencentes a todos os diferentes subconjuntos definidos pelo valor específico de
>>   uma das 5 colunas primárias, (Considerando os aprovados como sendo o Subconjunto encontrado pelo modelo no qual a Média da Mp dos estudantes é máxima),
>>   e comparar esta análise com a mesma análise feita para o peso utilizado quando os aprovados são considerados como aqueles com Média Ponderada maior que
>>   8.
>>   
### Módulo Gerente
>
>**Classes:**
>>*HistoricoSolicitacoes*
>> - Classe que tem como função armazenar novas solicitações, ler e editar
>>   um arquivo .csv de nome "historico_s.csv" no diretório local do usuário especificado pelo parâmetro "dir_arq_csv".
>>   
>> - Caso um arquivo .csv com este nome não exista no diretório local especificado pelo usuário, um novo será criado. 
>> 
>> - Caso já exista a instância abrirá este arquivo como uma tabela do pandas e cada edição feita utilizando a instância
>>   terá impacto no arquivo .csv já existente.
>
>>*InformarEstudante*
>>
>>Classe que possui todas as informações necessárias,
>>de um estudante individual, para:
>>
>> Caso a solicitação do estudante seja deferida:
>>
>> - defenir o notebook que será comprado, o seu preço e sua data de entrega prevista, utilizando:
>>   - A informação sobre o curso do estudante para definir o modelo do notebook;
>>   - A biblioteca 'selenium' para acessar o site da Dell, encontrar o modelo do notebook ,
>>     coletar o preço do modelo, inserir o cep do estudante na página de 'Data de entrega estimada' e
>>     coletar a data de entrega estimada para o cep inserido.
>>           
>> - Criar uma mensagem personalizada sobre as informações da solicitação com o nome,ra,notebook que será recebido,
>>   e data de entrega estimada deste para ser enviada ao estudante. Utilizando a biblioteca 'email' inclusa no python.
>>        
>> - Enviar um e-mail para o e-mail do estudante fornecido a partir da conta 'projetonotebookcdia@gmail.com' com a mensagem
>>   personalizada criada. Utilizando a biblioteca 'smtp' e 'ssl' inclusas no python.
>>        
>> Caso a solicitação do estudante não seja deferida:
>>      
>> - Criar uma mensagem personalizada sobre as informações da solicitação com o nome e ra
>>   para ser enviada ao estudante. Utilizando a biblioteca 'email' inclusa no python.
>>        
>> - Enviar um e-mail para o e-mail do estudante fornecido a partir da conta 'projetonotebookcdia@gmail.com' com a mensagem
>>   personalizada criada neste caso informando sobre o não deferimento. 
>>   Utilizando a biblioteca 'smtp' e 'ssl' inclusas no python.
>>        
>>**Parâmetros de incialização de uma instância:**
>>    
>> - *navweb* = Navegador que será utilizado pela bilbioteca 'selenium' para realizar o WebScraping em forma de string
>>    
>> - *info_estudantes* = dicionário contendo informações do estudante cujo formato é:
>>
>>   - **'NOME'**: Nome do Estudante,
>>   - **'RA'**: RA do Estudante,
>>   - **'COD_CURSO'**: Código do Curso do Estudante,
>>   - **'CEP'**: CEP do Estudante,
>>   - **'EMAIL'**: Email do Estudante
>>     
>> - *deferido* = Valor booleano (True ou False) indicando se a solicitação do aluno foi deferida ou não.
>
### Módulo ProcessoAutomatizado
>
>**Classes:**
>>*ProcessarEstudante*
>>
>>Classe que tem como função agregar todos os processos realizados pelas classes do módulo Analista e do módulo Gerente e, a partir das informações de
>>um estudante individual:
>> - classificar sua solicitação como deferida ou não, 
>> - encontrar o notebook que lhe será fornecido caso seja aprovado, seu preço e a data estimada de entrega para o cep do estudante,
>> - criar uma mensagem de e-mail personalizada para o estudante contendo informações sobre sua solicitação,
>> - enviar a mensagem criada para o estudante,
>> - adiconar as informações da solicitação do estudante em um arquivo .csv que serve como histórico de solicitações.
>>    
>>**Parâmetros de Inicialização:**
>> - *i_e* = dicionário contendo as informações necessárias do estudante para o processamento, que tem formato:
>>     - **'nome'**: Nome do Estudante,
>>     - **'ra'**: RA do Estudante,
>>     - **'cod_curso'**: Código do Curso do Estudante,
>>     - **'cep'**: CEP do Estudante,
>>     - **'email'**: Email Estudante,
>>     - **'renda'**: Renda familiar mensal do Estudante,
>>     - **'escola'**: Código Referente a Escola do Estudante,
>>     - **'motivação'**: Motivação do Estudante,
>>     - **'cor'**: Código da cor do Estudante,
>>     - **'sexo'**: Código do Sexo do Estudante
>>   
>> - *dir_arq_csv* = diretório local para salvar .csv referente ao histórico das solicitações.
>>   
>> - *filtkmeans* = Instância da classe ProjetoNotebook.Analista.FiltragemKMeans.
>
