import numpy as np
import csv
import sys

sequence_f=[];correct_f=[];wrong_f=[]
label_sgen=[];label_snum=[];label_dgen=[];label_dnum=[]
label_svar=[];label_dvar=[];label_long=[];label_d=[]
score_correct=[];score_wrong=[];resultados=[];conta=[]

# python3 script resultados.txt eval_out.csv

with open(sys.argv[1]) as f:
    for line in f:
        aux=line.split(';');conta.append(len(aux))
        sequence_f.append(aux[0])
        correct_f.append(aux[1])
        wrong_f.append(aux[2])
        label_sgen.append(int(aux[3]))
        label_snum.append(int(aux[4]))
        label_dgen.append(int(aux[5]))
        label_dnum.append(int(aux[6]))
        label_svar.append(int(aux[7]))
        label_dvar.append(int(aux[8]))
        label_long.append(int(aux[9]))
        label_d.append(int(aux[10]))
        score_correct.append(float(aux[11]))
        score_wrong.append(float(aux[12]))
        resultados.append(int(str.strip(aux[13])))

sequence_f=np.array(sequence_f)
correct_f=np.array(correct_f)
wrong_f=np.array(wrong_f)
label_sgen=np.array(label_sgen)
label_snum=np.array(label_snum)
label_dgen=np.array(label_dgen)
label_dnum=np.array(label_dnum)
label_long=np.array(label_long)
label_d=np.array(label_d)
resultados=np.array(resultados)

m=int(168)
nadx=int(len(sequence_f)/m)
n=len(sequence_f)
adx=correct_f[np.arange(0,n,m)]

media_d0=[];media_d1=[]
media_sgen0=[];media_sgen1=[]
media_snum0=[];media_snum1=[]
media_long0=[];media_long1=[]
med_tot=[]

ind_d0=np.where(label_d==0)[0];ind_d1=np.where(label_d==1)[0]
ind_sgen0=np.where(label_sgen==0)[0];ind_sgen1=np.where(label_sgen==1)[0]
ind_snum0=np.where(label_snum==0)[0];ind_snum1=np.where(label_snum==1)[0]
ind_long0=np.where(label_long==0)[0];ind_long1=np.where(label_long==1)[0]

file=open(sys.argv[2] + "_gerais.csv", "w")
writer=csv.writer(file)
writer.writerow(['inf','nsents','avg_tot','nattr','attr','suj_masc','suj_fem','suj_sing','sux_pl','curta','longa'])

for i in np.arange(nadx):
    ind0=ind_d0[np.where((m*i<=ind_d0)&(ind_d0<m*(i+1)))]
    ind1=ind_d1[np.where((m*i<=ind_d1)&(ind_d1<m*(i+1)))]
    media_d0.append(np.mean(resultados[ind0]))
    media_d1.append(np.mean(resultados[ind1]))
#
    ind0=ind_sgen0[np.where((m*i<=ind_sgen0)&(ind_sgen0<m*(i+1)))]
    ind1=ind_sgen1[np.where((m*i<=ind_sgen1)&(ind_sgen1<m*(i+1)))]
    media_sgen0.append(np.mean(resultados[ind0]))
    media_sgen1.append(np.mean(resultados[ind1]))
#
    ind0=ind_snum0[np.where((m*i<=ind_snum0)&(ind_snum0<m*(i+1)))]
    ind1=ind_snum1[np.where((m*i<=ind_snum1)&(ind_snum1<m*(i+1)))]
    media_snum0.append(np.mean(resultados[ind0]))
    media_snum1.append(np.mean(resultados[ind1]))
#
    ind0=ind_long0[np.where((m*i<=ind_long0)&(ind_long0<m*(i+1)))]
    ind1=ind_long1[np.where((m*i<=ind_long1)&(ind_long1<m*(i+1)))]
    media_long0.append(np.mean(resultados[ind0]))
    media_long1.append(np.mean(resultados[ind1]))
#
    med_tot.append(np.mean(resultados[np.arange(m*i,m*(i+1),1)]))
#
    writer.writerow([adx[i],m,med_tot[i],media_d0[i],media_d1[i],media_sgen0[i],media_sgen1[i],media_snum0[i],media_snum1[i],media_long0[i],media_long1[i]])
    
writer.writerow(['avg',m,np.mean(med_tot),np.mean(media_d0),np.mean(media_d1),np.mean(media_sgen0),np.mean(media_sgen1),np.mean(media_snum0),np.mean(media_snum1),np.mean(media_long0),np.mean(media_long1)])
file.close()

media_d0_snum0=[];media_d0_snum1=[]
media_d1_snum0=[];media_d1_snum1=[]
media_d0_sgen0=[];media_d0_sgen1=[]
media_d1_sgen0=[];media_d1_sgen1=[]
media_d1_dgen0=[];media_d1_dgen1=[]
media_d0_long0=[];media_d0_long1=[]
media_d1_long0=[];media_d1_long1=[]

ind_d0_snum0=np.where((label_d==0)&(label_snum==0))[0]
ind_d0_snum1=np.where((label_d==0)&(label_snum==1))[0]
ind_d1_snum0=np.where((label_d==1)&(label_snum==0))[0]
ind_d1_snum1=np.where((label_d==1)&(label_snum==1))[0]
ind_d0_sgen0=np.where((label_d==0)&(label_sgen==0))[0]
ind_d0_sgen1=np.where((label_d==0)&(label_sgen==1))[0]
ind_d1_sgen0=np.where((label_d==1)&(label_sgen==0))[0]
ind_d1_sgen1=np.where((label_d==1)&(label_sgen==1))[0]
ind_d1_dgen0=np.where((label_d==1)&(label_dgen==0))[0]
ind_d1_dgen1=np.where((label_d==1)&(label_dgen==1))[0]
ind_d0_long0=np.where((label_d==0)&(label_long==0))[0]
ind_d0_long1=np.where((label_d==0)&(label_long==1))[0]
ind_d1_long0=np.where((label_d==1)&(label_long==0))[0]
ind_d1_long1=np.where((label_d==1)&(label_long==1))[0]

file=open(sys.argv[2] + "_dist.csv", "w")
writer=csv.writer(file)
writer.writerow(['inf','nsents','nattr_suj_sing','nattr_suj_pl','attr_suj_sing','attr_suj_pl','nattr_suj_masc','nattr_suj_fem','attr_suj_masc','attr_suj_fem','attr_dist_masc','attr_dist_fem','nattr_curta','nattr_longa','attr_curta','attr_longa'])

for i in np.arange(nadx):
#
    ind0=ind_d0_snum0[np.where((m*i<=ind_d0_snum0)&(ind_d0_snum0<m*(i+1)))]
    ind1=ind_d0_snum1[np.where((m*i<=ind_d0_snum1)&(ind_d0_snum1<m*(i+1)))]
    media_d0_snum0.append(np.mean(resultados[ind0]))
    media_d0_snum1.append(np.mean(resultados[ind1]))
#
    ind0=ind_d1_snum0[np.where((m*i<=ind_d1_snum0)&(ind_d1_snum0<m*(i+1)))]
    ind1=ind_d1_snum1[np.where((m*i<=ind_d1_snum1)&(ind_d1_snum1<m*(i+1)))]
    media_d1_snum0.append(np.mean(resultados[ind0]))
    media_d1_snum1.append(np.mean(resultados[ind1]))
#
    ind0=ind_d0_sgen0[np.where((m*i<=ind_d0_sgen0)&(ind_d0_sgen0<m*(i+1)))]
    ind1=ind_d0_sgen1[np.where((m*i<=ind_d0_sgen1)&(ind_d0_sgen1<m*(i+1)))]
    media_d0_sgen0.append(np.mean(resultados[ind0]))
    media_d0_sgen1.append(np.mean(resultados[ind1]))
#
    ind0=ind_d1_sgen0[np.where((m*i<=ind_d1_sgen0)&(ind_d1_sgen0<m*(i+1)))]
    ind1=ind_d1_sgen1[np.where((m*i<=ind_d1_sgen1)&(ind_d1_sgen1<m*(i+1)))]
    media_d1_sgen0.append(np.mean(resultados[ind0]))
    media_d1_sgen1.append(np.mean(resultados[ind1]))
#
    ind0=ind_d1_dgen0[np.where((m*i<=ind_d1_dgen0)&(ind_d1_dgen0<m*(i+1)))]
    ind1=ind_d1_dgen1[np.where((m*i<=ind_d1_dgen1)&(ind_d1_dgen1<m*(i+1)))]
    media_d1_dgen0.append(np.mean(resultados[ind0]))
    media_d1_dgen1.append(np.mean(resultados[ind1]))
#
    ind0=ind_d0_long0[np.where((m*i<=ind_d0_long0)&(ind_d0_long0<m*(i+1)))]
    ind1=ind_d0_long1[np.where((m*i<=ind_d0_long1)&(ind_d0_long1<m*(i+1)))]
    media_d0_long0.append(np.mean(resultados[ind0]))
    media_d0_long1.append(np.mean(resultados[ind1]))
#
    ind0=ind_d1_long0[np.where((m*i<=ind_d1_long0)&(ind_d1_long0<m*(i+1)))]
    ind1=ind_d1_long1[np.where((m*i<=ind_d1_long1)&(ind_d1_long1<m*(i+1)))]
    media_d1_long0.append(np.mean(resultados[ind0]))
    media_d1_long1.append(np.mean(resultados[ind1]))
#
    writer.writerow([adx[i],m,media_d0_snum0[i],media_d0_snum1[i],media_d1_snum0[i],media_d1_snum1[i],media_d0_sgen0[i],media_d0_sgen1[i],media_d1_sgen0[i],media_d1_sgen1[i],media_d1_dgen0[i],media_d1_dgen1[i],media_d0_long0[i],media_d0_long1[i],media_d1_long0[i],media_d1_long1[i]])

writer.writerow(['avg',m,np.mean(media_d0_snum0),np.mean(media_d0_snum1),np.mean(media_d1_snum0),np.mean(media_d1_snum1),np.mean(media_d0_sgen0),np.mean(media_d0_sgen1),np.mean(media_d1_sgen0),np.mean(media_d1_sgen1),np.mean(media_d1_dgen0),np.mean(media_d1_dgen1),np.mean(media_d0_long0),np.mean(media_d0_long1),np.mean(media_d1_long0),np.mean(media_d1_long1)])
file.close()

media_long0_snum0=[];media_long0_snum1=[]
media_long1_snum0=[];media_long1_snum1=[]
media_long0_sgen0=[];media_long0_sgen1=[]
media_long1_sgen0=[];media_long1_sgen1=[]
media_long0_d0=[];media_long0_d1=[]
media_long1_d0=[];media_long1_d1=[]

ind_long0_snum0=np.where((label_long==0)&(label_snum==0))[0]
ind_long0_snum1=np.where((label_long==0)&(label_snum==1))[0]
ind_long1_snum0=np.where((label_long==1)&(label_snum==0))[0]
ind_long1_snum1=np.where((label_long==1)&(label_snum==1))[0]
ind_long0_sgen0=np.where((label_long==0)&(label_sgen==0))[0]
ind_long0_sgen1=np.where((label_long==0)&(label_sgen==1))[0]
ind_long1_sgen0=np.where((label_long==1)&(label_sgen==0))[0]
ind_long1_sgen1=np.where((label_long==1)&(label_sgen==1))[0]
ind_long0_d0=np.where((label_d==0)&(label_long==0))[0]
ind_long0_d1=np.where((label_d==1)&(label_long==0))[0]
ind_long1_d0=np.where((label_d==0)&(label_long==1))[0]
ind_long1_d1=np.where((label_d==1)&(label_long==1))[0]

file=open(sys.argv[2] + "_long.csv", "w")
writer=csv.writer(file)
writer.writerow(['inf','nsents','curta_suj_sing','curta_suj_pl','longa_suj_sing','longa_suj_pl','curta_suj_masc','curta_suj_fem','longa_suj_masc','longa_suj_fem','curta_nattr','curta_attr','longa_nattr','longa_attr'])

for i in np.arange(nadx):
#
    ind0=ind_long0_snum0[np.where((m*i<=ind_long0_snum0)&(ind_long0_snum0<m*(i+1)))]
    ind1=ind_long0_snum1[np.where((m*i<=ind_long0_snum1)&(ind_long0_snum1<m*(i+1)))]
    media_long0_snum0.append(np.mean(resultados[ind0]))
    media_long0_snum1.append(np.mean(resultados[ind1]))
#
    ind0=ind_long1_snum0[np.where((m*i<=ind_long1_snum0)&(ind_long1_snum0<m*(i+1)))]
    ind1=ind_long1_snum1[np.where((m*i<=ind_long1_snum1)&(ind_long1_snum1<m*(i+1)))]
    media_long1_snum0.append(np.mean(resultados[ind0]))
    media_long1_snum1.append(np.mean(resultados[ind1]))
#
    ind0=ind_long0_sgen0[np.where((m*i<=ind_long0_sgen0)&(ind_long0_sgen0<m*(i+1)))]
    ind1=ind_long0_sgen1[np.where((m*i<=ind_long0_sgen1)&(ind_long0_sgen1<m*(i+1)))]
    media_long0_sgen0.append(np.mean(resultados[ind0]))
    media_long0_sgen1.append(np.mean(resultados[ind1]))
#
    ind0=ind_long1_sgen0[np.where((m*i<=ind_long1_sgen0)&(ind_long1_sgen0<m*(i+1)))]
    ind1=ind_long1_sgen1[np.where((m*i<=ind_long1_sgen1)&(ind_long1_sgen1<m*(i+1)))]
    media_long1_sgen0.append(np.mean(resultados[ind0]))
    media_long1_sgen1.append(np.mean(resultados[ind1]))
#
    ind0=ind_long0_d0[np.where((m*i<=ind_long0_d0)&(ind_long0_d0<m*(i+1)))]
    ind1=ind_long0_d1[np.where((m*i<=ind_long0_d1)&(ind_long0_d1<m*(i+1)))]
    media_long0_d0.append(np.mean(resultados[ind0]))
    media_long0_d1.append(np.mean(resultados[ind1]))
#
    ind0=ind_long1_d0[np.where((m*i<=ind_long1_d0)&(ind_long1_d0<m*(i+1)))]
    ind1=ind_long1_d1[np.where((m*i<=ind_long1_d1)&(ind_long1_d1<m*(i+1)))]
    media_long1_d0.append(np.mean(resultados[ind0]))
    media_long1_d1.append(np.mean(resultados[ind1]))
#
    writer.writerow([adx[i],m,media_long0_snum0[i],media_long0_snum1[i],media_long1_snum0[i],media_long1_snum1[i],media_long0_sgen0[i],media_long0_sgen1[i],media_long1_sgen0[i],media_long1_sgen1[i],media_long0_d0[i],media_long0_d1[i],media_long1_d0[i],media_long1_d1[i]])

writer.writerow(['avg',m,np.mean(media_long0_snum0),np.mean(media_long0_snum1),np.mean(media_long1_snum0),np.mean(media_long1_snum1),np.mean(media_long0_sgen0),np.mean(media_long0_sgen1),np.mean(media_long1_sgen0),np.mean(media_long1_sgen1),np.mean(media_long0_d0),np.mean(media_long0_d1),np.mean(media_long1_d0),np.mean(media_long1_d1)])
file.close()

media_long0_d0_snum0=[];media_long0_d0_snum1=[]
media_long1_d0_snum0=[];media_long1_d0_snum1=[]
media_long0_d1_snum0=[];media_long0_d1_snum1=[]
media_long1_d1_snum0=[];media_long1_d1_snum1=[]
media_long0_d0_sgen0=[];media_long0_d0_sgen1=[]
media_long1_d0_sgen0=[];media_long1_d0_sgen1=[]
media_long0_d1_sgen0=[];media_long0_d1_sgen1=[]
media_long1_d1_sgen0=[];media_long1_d1_sgen1=[]

ind_long0_d0_snum0=np.where((label_d==0)&(label_long==0)&(label_snum==0))[0]
ind_long0_d0_snum1=np.where((label_d==0)&(label_long==0)&(label_snum==1))[0]
ind_long1_d0_snum0=np.where((label_d==0)&(label_long==1)&(label_snum==0))[0]
ind_long1_d0_snum1=np.where((label_d==0)&(label_long==1)&(label_snum==1))[0]
ind_long0_d1_snum0=np.where((label_d==1)&(label_long==0)&(label_snum==0))[0]
ind_long0_d1_snum1=np.where((label_d==1)&(label_long==0)&(label_snum==1))[0]
ind_long1_d1_snum0=np.where((label_d==1)&(label_long==1)&(label_snum==0))[0]
ind_long1_d1_snum1=np.where((label_d==1)&(label_long==1)&(label_snum==1))[0]
ind_long0_d0_sgen0=np.where((label_d==0)&(label_long==0)&(label_sgen==0))[0]
ind_long0_d0_sgen1=np.where((label_d==0)&(label_long==0)&(label_sgen==1))[0]
ind_long1_d0_sgen0=np.where((label_d==0)&(label_long==1)&(label_sgen==0))[0]
ind_long1_d0_sgen1=np.where((label_d==0)&(label_long==1)&(label_sgen==1))[0]
ind_long0_d1_sgen0=np.where((label_d==1)&(label_long==0)&(label_sgen==0))[0]
ind_long0_d1_sgen1=np.where((label_d==1)&(label_long==0)&(label_sgen==1))[0]
ind_long1_d1_sgen0=np.where((label_d==1)&(label_long==1)&(label_sgen==0))[0]
ind_long1_d1_sgen1=np.where((label_d==1)&(label_long==1)&(label_sgen==1))[0]

file=open(sys.argv[2] + "_concretas.csv", "w")
writer=csv.writer(file)
writer.writerow(['inf','nsents','curta_nattr_suj_sing','curta_nattr_suj_pl','longa_nattr_suj_sing','longa_nattr_suj_pl','curta_attr_suj_sing','curta_attr_suj_pl','longa_attr_suj_sing','longa_attr_suj_pl','curta_nattr_suj_masc','curta_nattr_suj_fem','longa_nattr_suj_masc','longa_nattr_suj_fem','curta_attr_suj_masc','curta_attr_suj_fem','longa_attr_suj_masc','longa_attr_suj_fem'])

for i in np.arange(nadx):
    ind0=ind_long0_d0_snum0[np.where((m*i<=ind_long0_d0_snum0)&(ind_long0_d0_snum0<m*(i+1)))]
    ind1=ind_long0_d0_snum1[np.where((m*i<=ind_long0_d0_snum1)&(ind_long0_d0_snum1<m*(i+1)))]
    media_long0_d0_snum0.append(np.mean(resultados[ind0]))
    media_long0_d0_snum1.append(np.mean(resultados[ind1]))

    ind0=ind_long1_d0_snum0[np.where((m*i<=ind_long1_d0_snum0)&(ind_long1_d0_snum0<m*(i+1)))]
    ind1=ind_long1_d0_snum1[np.where((m*i<=ind_long1_d0_snum1)&(ind_long1_d0_snum1<m*(i+1)))]
    media_long1_d0_snum0.append(np.mean(resultados[ind0]))
    media_long1_d0_snum1.append(np.mean(resultados[ind1]))
#
    ind0=ind_long0_d1_snum0[np.where((m*i<=ind_long0_d1_snum0)&(ind_long0_d1_snum0<m*(i+1)))]
    ind1=ind_long0_d1_snum1[np.where((m*i<=ind_long0_d1_snum1)&(ind_long0_d1_snum1<m*(i+1)))]
    media_long0_d1_snum0.append(np.mean(resultados[ind0]))
    media_long0_d1_snum1.append(np.mean(resultados[ind1]))
#
    ind0=ind_long1_d1_snum0[np.where((m*i<=ind_long1_d1_snum0)&(ind_long1_d1_snum0<m*(i+1)))]
    ind1=ind_long1_d1_snum1[np.where((m*i<=ind_long1_d1_snum1)&(ind_long1_d1_snum1<m*(i+1)))]
    media_long1_d1_snum0.append(np.mean(resultados[ind0]))
    media_long1_d1_snum1.append(np.mean(resultados[ind1]))
#
    ind0=ind_long0_d0_sgen0[np.where((m*i<=ind_long0_d0_sgen0)&(ind_long0_d0_sgen0<m*(i+1)))]
    ind1=ind_long0_d0_sgen1[np.where((m*i<=ind_long0_d0_sgen1)&(ind_long0_d0_sgen1<m*(i+1)))]
    media_long0_d0_sgen0.append(np.mean(resultados[ind0]))
    media_long0_d0_sgen1.append(np.mean(resultados[ind1]))
#
    ind0=ind_long1_d0_sgen0[np.where((m*i<=ind_long1_d0_sgen0)&(ind_long1_d0_sgen0<m*(i+1)))]
    ind1=ind_long1_d0_sgen1[np.where((m*i<=ind_long1_d0_sgen1)&(ind_long1_d0_sgen1<m*(i+1)))]
    media_long1_d0_sgen0.append(np.mean(resultados[ind0]))
    media_long1_d0_sgen1.append(np.mean(resultados[ind1]))
#
    ind0=ind_long0_d1_sgen0[np.where((m*i<=ind_long0_d1_sgen0)&(ind_long0_d1_sgen0<m*(i+1)))]
    ind1=ind_long0_d1_sgen1[np.where((m*i<=ind_long0_d1_sgen1)&(ind_long0_d1_sgen1<m*(i+1)))]
    media_long0_d1_sgen0.append(np.mean(resultados[ind0]))
    media_long0_d1_sgen1.append(np.mean(resultados[ind1]))
#
    ind0=ind_long1_d1_sgen0[np.where((m*i<=ind_long1_d1_sgen0)&(ind_long1_d1_sgen0<m*(i+1)))]
    ind1=ind_long1_d1_sgen1[np.where((m*i<=ind_long1_d1_sgen1)&(ind_long1_d1_sgen1<m*(i+1)))]
    media_long1_d1_sgen0.append(np.mean(resultados[ind0]))
    media_long1_d1_sgen1.append(np.mean(resultados[ind1]))
#
    writer.writerow([adx[i],m,media_long0_d0_snum0[i],media_long0_d0_snum1[i],media_long1_d0_snum0[i],media_long1_d0_snum1[i],media_long0_d1_snum0[i],media_long0_d1_snum1[i],media_long1_d1_snum0[i],media_long1_d1_snum1[i],media_long0_d0_sgen0[i],media_long0_d0_sgen1[i],media_long1_d0_sgen0[i],media_long1_d0_sgen1[i],media_long0_d1_sgen0[i],media_long0_d1_sgen1[i],media_long1_d1_sgen0[i],media_long1_d1_sgen1[i]])

writer.writerow([adx[i],m,np.mean(media_long0_d0_snum0),np.mean(media_long0_d0_snum1),np.mean(media_long1_d0_snum0),np.mean(media_long1_d0_snum1),np.mean(media_long0_d1_snum0),np.mean(media_long0_d1_snum1),np.mean(media_long1_d1_snum0),np.mean(media_long1_d1_snum1),np.mean(media_long0_d0_sgen0),np.mean(media_long0_d0_sgen1),np.mean(media_long1_d0_sgen0),np.mean(media_long1_d0_sgen1),np.mean(media_long0_d1_sgen0),np.mean(media_long0_d1_sgen1),np.mean(media_long1_d1_sgen0),np.mean(media_long1_d1_sgen1)])
file.close()
