def encontrar_pesos(request):
  
  '''Gera uma determinada quantidade de pesos aleatórios retirados de uma distribuição uniforme com limite máximo
  de 0.89 e limite mínimo de 0.1 utilizando a função random.uniform do Numpy, realiza a análise da filtragem dos estudantes
  geradas por este peso qunado aplicado à Média Ponderada da Nota Normalizada destes estudantes (cujas informações se 
  encontram no arquivo 'colunas_p.csv') e testa se a filtragem se encaixa nas condições definidas pelo parâmetro limites
  cujo formato é ['NMaxAprovados','PctAprovadosPCurso','PctMinAMaisPretos','PctMinAmaisHomens','PctMinAMaisEPub].
  Tanto o parâmetro limites e a quantidade de pesos testados são passados a função através do parâmetro 'request'
  recebido a partir da chamada à API, filtra os pesos cujas análises se encaixam e os retorna, junto com a qtd de
  pesos testados, a quantidade de pesos que foram encontrados e os limites que foram usados para filtragem
  em formato json.
  é executado utilizando o Google Cloud Functions(ferramenta de criação de micro-serviços sem servidor dedicado que permite o 
  A função é executada sempre que recebe um gatilho HTTP (A url é acessada) e retorna seus valores em formato json à página html da   url.'''
  
  from numpy import array,dot,where,append,zeros,seterr,repeat
  from numpy.random import uniform
  import pandas as pd
  from flask import jsonify
  qtd=request.args.get('qtd_pesos')
  limites_str=request.args.get('limites')
  limites_formato=['NMaxAprovados','PctAprovadosPCurso','PctMinAMaisPretos','PctMinAmaisHomens','PctMinAMaisEPub']
  try:
    qtd_i=int(qtd)
  except:
    return jsonify({'Erro 001':'O Valor Fornecido para qtd_pesos não é um número inteiro.'})
  try:
    limites_arr=array([float(i) for i in limites_str.replace('[','').replace(']','').split(',')])
  except:
    return jsonify({'Erro 002':f'O Valor Fornecido para limites não é do tipo {limites_formato}'})
  pesos_arrs=uniform(0.1,0.9,(qtd_i,5))
  n_it=len(pesos_arrs)
  p_fail,results,peso_data_arrs=array([-1,-1,-1,-1,-1]),zeros([n_it,5]),zeros([n_it,16])
  colunas_p=pd.read_csv('colunas_p.csv').set_index('matrícula')
  notas_arr=pd.read_csv('notas_df.csv').set_index('matrícula').to_numpy()
  psum=repeat(pesos_arr.sum(axis=1).reshape((qtd_i,1)),500,axis=1)
  for i in range(n_it):
    mp=dot(notas_arr,pesos_arrs[i])/psum[i]
    l_appr=(dot(array([10,10,10,10,10]),pesos_arrs[i])/psum[i][0])*0.8
    colunas_p['Mp']=mp
    colunas_p_arr=colunas_p.to_numpy()
    appr,nappr=colunas_p_arr[where(colunas_p_arr[:,-1]>=l_appr)],colunas_p_arr[where(colunas_p_arr[:,-1]<l_appr)]
    cp={3:(1,2,3,4,5,6,7,8,9),4:(1,2),5:(1,2),1:(1,2)}
    apprfilt=array([len(appr[where(appr[:,k]==a)]) for k in cp.keys() for a in cp[k]])
    naoapprfilt=array([len(nappr[where(nappr[:,k]==a)]) for k in cp.keys() for a in cp[k]])
    total=apprfilt+naoapprfilt
    seterr(invalid='ignore')
    peso_data_arrs[i]=append(array((len(appr))),apprfilt/total)
  for i in range(n_it):
    cond1= peso_data_arrs[i][0]<=limites_arr[0]
    cond2= all(peso_data_arrs[i][1:10]>=limites_arr[1])
    cond3= (peso_data_arrs[i][11]-peso_data_arrs[i][10])>=limites_arr[2]
    cond4= (peso_data_arrs[i][12]-peso_data_arrs[i][13])>=limites_arr[3]
    cond5= (peso_data_arrs[i][14]-peso_data_arrs[i][15])>=limites_arr[4]
    if all(array([cond1,cond2,cond3,cond4,cond5])):
        results[i]=pesos_arrs[i]
    else:
        results[i]=p_fail
  results_strs=[str(i) for i in results if sum(i)!=-5]
  pesos_str=',\n'.join(results_strs)
  p_encontrado=str(len(results_strs))
  lim=', '.join(['{}:{}'.format(i,a) for i,a in zip(limites_formato,[str(i) for i in limites_arr])])
  response=(jsonify( {'mensagem':'Teste Finalizado',
                      "pesos":pesos_str,
                      "pesos_encontrados":p_encontrado,
                      "limites":lim,
                      'qtd_pesos_testados':qtd}),200)
  return response
