from transformers import AutoModelWithLMHead, AutoTokenizer
import torch
import numpy as np
import sys

# python3 script dataset.txt output.txt model_name

model_name = sys.argv[3] # path or name ('bert-base-multilingual-cased')
tokenizer=AutoTokenizer.from_pretrained(model_name,add_prefix_space=True)
model = AutoModelWithLMHead.from_pretrained(model_name)

sequence_f=[];correct_f=[];wrong_f=[]
label_sgen=[];label_snum=[];label_dgen=[];label_dnum=[]
label_svar=[];label_dvar=[];label_long=[];label_d=[]

with open(sys.argv[1]) as f:
    for line in f:
        aux=line.split(';')
        sequence_f.append(aux[0])
        correct_f.append(aux[1])
        wrong_f.append(aux[2])
        label_sgen.append(aux[3])
        label_snum.append(aux[4])
        label_dgen.append(aux[5])
        label_dnum.append(aux[6])
        label_svar.append(aux[7])
        label_dvar.append(aux[8])
        label_long.append(aux[9])
        label_d.append(str.strip(aux[10]))

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

    ids_correct=tokenizer.encode(correct_f[i],return_tensors="pt")[0][1]
    score_correct_i=mask_logits[0][ids_correct]
    score_correct_i=score_correct_i.detach().item()
    ids_wrong=tokenizer.encode(wrong_f[i],return_tensors="pt")[0][1]
    score_wrong_i=mask_logits[0][ids_wrong]
    score_wrong_i=score_wrong_i.detach().item()

    score_correct.append(str(score_correct_i))
    score_wrong.append(str(score_wrong_i))
    if score_correct_i>score_wrong_i:
        resultados.append(str(1))
    elif score_correct_i<=score_wrong_i:
        resultados.append(str(0))

    print(i)

with open(sys.argv[2], "x") as f:
    for i in ind:
        aux=(sequence_f[i],correct_f[i],wrong_f[i],label_sgen[i],
             label_snum[i],label_dgen[i],label_dnum[i],label_svar[i],
             label_dvar[i],label_long[i],label_d[i],score_correct[i],score_wrong[i],resultados[i])
        aux2=';'.join(aux)
        _=f.write(aux2+"\n")
