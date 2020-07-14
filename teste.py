import json
import csv

dt_geracao = []
hh_geracao = []
ano_eleicao = []
cd_tipo_eleicao = []
nm_tipo_eleicao = []
cd_eleicao = []
ds_eleicao = []
dt_eleicao = []
sg_uf = []
sg_ue = []
nm_ue = []
sq_candidato = []
nr_ordem_candidato = []
cd_tipo_bem_candidato = []
ds_bem_candidato = []
vr_bem_candidato = []
dt_ultima_atualizacao = []
hh_ultima_atualizacao = []
j = 0
linha = []

record_list = []
print("Teste Python 2.7")
with open("/home/henrique/Documents/Desenvolvimento/Python/Lambda/bem_candidato_2018_MG.csv", encoding="iso-8859-1") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
       dt_geracao.insert(j,row[0])
       hh_geracao.insert(j,row[1])
       ano_eleicao.insert(j,row[2])
       cd_tipo_eleicao.insert(j,row[3])
       nm_tipo_eleicao.insert(j,row[4])
       cd_eleicao.insert(j,row[5])
       ds_eleicao.insert(j,row[6])
       dt_eleicao.insert(j,row[7])
       sg_uf.insert(j,row[8])
       sg_ue.insert(j,row[9])
       nm_ue.insert(j,row[10])
       sq_candidato.insert(j,row[11])
       nr_ordem_candidato.insert(j,row[12])
       cd_tipo_bem_candidato.insert(j,row[13])
       ds_bem_candidato.insert(j,row[14])
       vr_bem_candidato.insert(j,row[15])
       dt_ultima_atualizacao.insert(j,row[16])
       hh_ultima_atualizacao.insert(j,row[17]) 
       j = j + 1 

print("Testando")
print(sq_candidato[0])
print(sq_candidato[1])
print(sq_candidato[2])