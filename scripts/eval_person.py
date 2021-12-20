import numpy as np
import csv
import sys

# python3 script input output

sequence_f=[];correct_f=[];wrong_f=[]
label_long=[];label_pos=[];label_temp=[]
label_pers=[];label_inf=[];ncorrect_f=[];nwrong_f=[]
score_correct=[];score_wrong=[];resultados=[]

with open(sys.argv[1]) as f:
    for line in f:
        aux=np.array(line.split(';'))
        sequence_f.append(aux[0])
        ncorrect_f.append(int(aux[1]));ncorrect=int(aux[1])
        nwrong_f.append(int(aux[2]));nwrong=int(aux[2])
        m1=3+ncorrect;m2=3+ncorrect+nwrong
        correct_f.append(aux[np.arange(3,m1,1)].tolist())
        wrong_f.append(aux[np.arange(m1,m2,1)].tolist())
        label_long.append(int(aux[m2]))
        label_pos.append(int(aux[m2+1]))
        label_temp.append(int(aux[m2+2]))
        label_pers.append(int(aux[m2+3]))
        label_inf.append(int(aux[m2+4]))
        n1=m2+5+ncorrect;n2=m2+5+ncorrect+nwrong
        score_correct.append(aux[np.arange(m2+5,n1,1)].tolist())
        score_wrong.append(aux[np.arange(n1,n2,1)].tolist())
        resultados.append(int(str.strip(aux[n2])))

sequence_f=np.array(sequence_f)
label_long=np.array(label_long)
label_pos=np.array(label_pos)
label_temp=np.array(label_temp)
label_pers=np.array(label_pers)
label_inf=np.array(label_inf)
resultados=np.array(resultados)

media_long0=[];media_long1=[]
media_pos0=[];media_pos1=[]
media_temp0=[];media_temp1=[]
media_pers0=[];media_pers1=[]
media_inf1=[];media_inf2=[];media_inf4=[]
med_tot=[]

ind_long0=np.where(label_long==0)[0]
ind_long1=np.where(label_long==1)[0]
ind_pos0=np.where(label_pos==0)[0]
ind_pos1=np.where(label_pos==1)[0]
ind_temp0=np.where(label_temp==0)[0]
ind_temp1=np.where(label_temp==1)[0]
ind_pers0=np.where(label_pers==0)[0]
ind_pers1=np.where(label_pers==1)[0]
ind_inf1=np.where(label_inf==1)[0]  
ind_inf2=np.where(label_inf==2)[0]
ind_inf4=np.where(label_inf==4)[0]  

if np.sum(label_inf==3)==0:
    m=int(48)
    n=len(resultados)
    ncont=int(n/64)
    contextos=sequence_f[np.arange(0,n,m)]

    file=open(sys.argv[2], "w")
    writer=csv.writer(file)
    writer.writerow(['count','nsents','avg_tot','curta','longa','posterior','anterior','past','fut','primeira','terceira','inf_segunda_sing','inf_primeira_pl','inf_terceira_pl'])

    for i in np.arange(ncont):

        ind0=ind_long0[np.where((m*i<=ind_long0)&(ind_long0<m*(i+1)))]
        ind1=ind_long1[np.where((m*i<=ind_long1)&(ind_long1<m*(i+1)))]
        media_long0.append(np.mean(resultados[ind0]))
        media_long1.append(np.mean(resultados[ind1]))

        ind0=ind_pos0[np.where((m*i<=ind_pos0)&(ind_pos0<m*(i+1)))]
        ind1=ind_pos1[np.where((m*i<=ind_pos1)&(ind_pos1<m*(i+1)))]
        media_pos0.append(np.mean(resultados[ind0]))
        media_pos1.append(np.mean(resultados[ind1]))

        ind0=ind_temp0[np.where((m*i<=ind_temp0)&(ind_temp0<m*(i+1)))]
        ind1=ind_temp1[np.where((m*i<=ind_temp1)&(ind_temp1<m*(i+1)))]
        media_temp0.append(np.mean(resultados[ind0]))
        media_temp1.append(np.mean(resultados[ind1]))

        ind0=ind_pers0[np.where((m*i<=ind_pers0)&(ind_pers0<m*(i+1)))]
        ind1=ind_pers1[np.where((m*i<=ind_pers1)&(ind_pers1<m*(i+1)))]
        media_pers0.append(np.mean(resultados[ind0]))
        media_pers1.append(np.mean(resultados[ind1]))

        ind1=ind_inf1[np.where((m*i<=ind_inf1)&(ind_inf1<m*(i+1)))]
        ind2=ind_inf2[np.where((m*i<=ind_inf2)&(ind_inf2<m*(i+1)))]
        ind4=ind_inf4[np.where((m*i<=ind_inf4)&(ind_inf4<m*(i+1)))]
        media_inf1.append(np.mean(resultados[ind1]))
        media_inf2.append(np.mean(resultados[ind2]))
        media_inf4.append(np.mean(resultados[ind4]))

        med_tot.append(np.mean(resultados[np.arange(m*i,m*(i+1),1)]))

        writer.writerow([contextos[i],m,med_tot[i],media_long0[i],media_long1[i],media_pos0[i],media_pos1[i],media_temp0[i],media_temp1[i],media_pers0[i],media_pers1[i],media_inf1[i],media_inf2[i],media_inf4[i]])

    writer.writerow(['medias',m,np.mean(med_tot),np.mean(media_long0),np.mean(media_long1),np.mean(media_pos0),np.mean(media_pos1),np.mean(media_temp0),np.mean(media_temp1),np.mean(media_pers0),np.mean(media_pers1),np.mean(media_inf1),np.mean(media_inf2),np.mean(media_inf4)])
    file.close()

    med_tot.append(np.mean(resultados[np.arange(m*i,m*(i+1),1)]))
elif np.sum(label_inf==3)!=0:
    m=int(64)
    n=len(resultados)
    ncont=int(n/64)
    contextos=sequence_f[np.arange(0,n,m)]

    media_inf3=[]
    ind_inf3=np.where(label_inf==3)[0]

    file=open(sys.argv[2], "w")
    writer=csv.writer(file)
    writer.writerow(['count','nsents','avg_tot','curta','longa','posterior','anterior','past','fut','primeira','terceira','inf_segunda_sing','inf_primeira_pl','inf_segunda_pl','inf_terceira_pl'])

    for i in np.arange(ncont):
        ind0=ind_long0[np.where((m*i<=ind_long0)&(ind_long0<m*(i+1)))]
        ind1=ind_long1[np.where((m*i<=ind_long1)&(ind_long1<m*(i+1)))]
        media_long0.append(np.mean(resultados[ind0]))
        media_long1.append(np.mean(resultados[ind1]))

        ind0=ind_pos0[np.where((m*i<=ind_pos0)&(ind_pos0<m*(i+1)))]
        ind1=ind_pos1[np.where((m*i<=ind_pos1)&(ind_pos1<m*(i+1)))]
        media_pos0.append(np.mean(resultados[ind0]))
        media_pos1.append(np.mean(resultados[ind1]))

        ind0=ind_temp0[np.where((m*i<=ind_temp0)&(ind_temp0<m*(i+1)))]
        ind1=ind_temp1[np.where((m*i<=ind_temp1)&(ind_temp1<m*(i+1)))]
        media_temp0.append(np.mean(resultados[ind0]))
        media_temp1.append(np.mean(resultados[ind1]))

        ind0=ind_pers0[np.where((m*i<=ind_pers0)&(ind_pers0<m*(i+1)))]
        ind1=ind_pers1[np.where((m*i<=ind_pers1)&(ind_pers1<m*(i+1)))]
        media_pers0.append(np.mean(resultados[ind0]))
        media_pers1.append(np.mean(resultados[ind1]))

        ind1=ind_inf1[np.where((m*i<=ind_inf1)&(ind_inf1<m*(i+1)))]
        ind2=ind_inf2[np.where((m*i<=ind_inf2)&(ind_inf2<m*(i+1)))]
        ind3=ind_inf3[np.where((m*i<=ind_inf3)&(ind_inf3<m*(i+1)))]
        ind4=ind_inf4[np.where((m*i<=ind_inf4)&(ind_inf4<m*(i+1)))]
        media_inf1.append(np.mean(resultados[ind1]))
        media_inf2.append(np.mean(resultados[ind2]))
        media_inf3.append(np.mean(resultados[ind3]))
        media_inf4.append(np.mean(resultados[ind4]))

        med_tot.append(np.mean(resultados[np.arange(m*i,m*(i+1),1)]))

        writer.writerow([contextos[i],m,med_tot[i],media_long0[i],media_long1[i],media_pos0[i],media_pos1[i],media_temp0[i],media_temp1[i],media_pers0[i],media_pers1[i],media_inf1[i],media_inf2[i],media_inf3[i],media_inf4[i]])

    writer.writerow(['avg',m,np.mean(med_tot),np.mean(media_long0),np.mean(media_long1),np.mean(media_pos0),np.mean(media_pos1),np.mean(media_temp0),np.mean(media_temp1),np.mean(media_pers0),np.mean(media_pers1),np.mean(media_inf1),np.mean(media_inf2),np.mean(media_inf3),np.mean(media_inf4)])
    file.close()
