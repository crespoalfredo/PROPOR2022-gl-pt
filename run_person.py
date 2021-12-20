from transformers import AutoModelWithLMHead, AutoTokenizer
import torch
import numpy as np
import sys

# Modify
modelpath = "bert-base-multilingual-cased"
tokenizer=AutoTokenizer.from_pretrained(modelpath,add_prefix_space=True)
model = AutoModelWithLMHead.from_pretrained(modelpath)

sequence_f=[];correct_f=[];wrong_f=[]
label_long=[];label_pos=[];label_temp=[]
label_pers=[];label_inf=[];ncorrect_f=[];nwrong_f=[]

# Modify dataset
datapath = "person.txt"
with open(datapath) as f:
    for line in f:
        aux=np.array(line.split(';'))
        sequence_f.append(aux[0])
        ncorrect_f.append(int(aux[1]));ncorrect=int(aux[1])
        nwrong_f.append(int(aux[2]));nwrong=int(aux[2])
        m1=3+ncorrect;m2=3+ncorrect+nwrong
        correct_f.append(aux[np.arange(3,m1,1)].tolist())
        wrong_f.append(aux[np.arange(m1,m2,1)].tolist())
        label_long.append(aux[m2])
        label_pos.append(aux[m2+1])
        label_temp.append(aux[m2+2])
        label_pers.append(aux[m2+3])
        label_inf.append(str.strip(aux[m2+4]))

n=len(sequence_f)
ind=np.arange(n)

if len(tokenizer.encode('*'))!=3:
    print('ERROR')
    sys.exit()

mask_data_set=tokenizer.encode('*',return_tensors="pt")[0][1]
resultados=[];score_correct=[];score_wrong=[]

for i in ind:
    sequence=sequence_f[i]
    ids_sequence=tokenizer.encode(sequence,return_tensors="pt")
    mask_ind=torch.where(ids_sequence[0]==mask_data_set)[0]
    ids_sequence[0][mask_ind]=tokenizer.mask_token_id

    logits=model(ids_sequence).logits
    mask_logits=logits[0][mask_ind]
    mask_logits=torch.softmax(mask_logits,dim=1)

    score_correct_i_list=[];score_wrong_i_list=[]

    for j in np.arange(0,ncorrect_f[i],1):
        ids_correct=tokenizer.encode(correct_f[i][j],return_tensors="pt")[0][1]
        score_correct_i=mask_logits[0][ids_correct]
        score_correct_i=score_correct_i.detach().item()
        score_correct_i_list.append(score_correct_i)

    for j in np.arange(0,nwrong_f[i],1):
        ids_wrong=tokenizer.encode(wrong_f[i][j],return_tensors="pt")[0][1]
        score_wrong_i=mask_logits[0][ids_wrong]
        score_wrong_i=score_wrong_i.detach().item()
        score_wrong_i_list.append(score_wrong_i)
   
    score_correct.append(score_correct_i_list)
    score_wrong.append(score_wrong_i_list)
    if np.sum(score_correct_i_list)>np.sum(score_wrong_i_list):
        resultados.append(str(1))
    elif np.sum(score_correct_i_list)<=np.sum(score_wrong_i_list):
        resultados.append(str(0))

    print(i)

outputfile = "output.txt"
with open(outputfile,"x") as f:
    for i in ind:
        l=[sequence_f[i]]
        ncorrect=ncorrect_f[i]
        l.append(str(ncorrect))
        nwrong=nwrong_f[i]
        l.append(str(nwrong))
        for j in np.arange(ncorrect):
            l.append(correct_f[i][j])
        for j in np.arange(nwrong):
            l.append(wrong_f[i][j])
        l.append(label_long[i])
        l.append(label_pos[i])  
        l.append(label_temp[i])
        l.append(label_pers[i])
        l.append(label_inf[i])
        for j in np.arange(ncorrect):
            l.append(str(score_correct[i][j]))
        for j in np.arange(nwrong):
            l.append(str(score_wrong[i][j]))
        l.append(resultados[i])
        aux=tuple(l)
        aux2=';'.join(aux)
        _=f.write(aux2+"\n")
