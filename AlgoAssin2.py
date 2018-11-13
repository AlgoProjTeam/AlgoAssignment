# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:51:53 2018

@author: Kripa
"""

import matplotlib.pyplot as plt
import random

class nd(object):
    def __init__(self, adjacentnd):
        self.adjacentnd=[];
        self.EdgesNo=0;

def begin():
    global i;
    global tDegree;
    i=1;
    LNode.append(nd(i));
    i=i+1;
    LNode[0].adjacentnd.append(LNode[0]);
    LNode[0].EdgesNo=1;
    tDegree=1;
    ProbabilityBirth.append(1);
    ProbabilityDeath.append(1);
    
def Birthnd(ndSelect):
    global i;
    global tDegree;
    nd1=nd(i);
    LNode.append(nd1);
    nd1.adjacentnd.append(ndSelect);
    nd1.EdgesNo=1;        
    ndSelect.adjacentnd.append(nd1);
    ndSelect.EdgesNo=(ndSelect.EdgesNo)+1; 
    i=i+1;
    tDegree=tDegree+2;    
    NodesNo=len(LNode);
    for k in range (len(LNode)):
        ProbabilityBirth.append((LNode[k].EdgesNo)/(tDegree));
        ProbabilityDeath.append((NodesNo-(LNode[k].EdgesNo))/((NodesNo**2)-(tDegree)));
    
def Deathnd(SelNode):
    global tDegree;
    pos=LNode.index(SelNode);
    LNode.remove(SelNode);
    tDegree=tDegree-len(SelNode.adjacentnd);
    length=len(LNode);
    if pos>0:
        for j in range (length):
            if SelNode in LNode[j].adjacentnd:
                LNode[j].adjacentnd.remove(SelNode);
                LNode[j].EdgesNo=(LNode[j].EdgesNo)-1;
                tDegree=tDegree-1;
        NodesNo=len(LNode);
        if NodesNo==1:
            ProbabilityDeath.append(1);
        else:
            for k in range (len(LNode)):
                ProbabilityBirth.append((LNode[k].EdgesNo)/(tDegree));
                ProbabilityDeath.append((NodesNo-(LNode[k].EdgesNo))/((NodesNo**2)-(tDegree)));
         
def CumProbability():  
    Cumulative_BirthProb=0;
    for k in range (len(ProbabilityBirth)):
        Cumulative_BirthProb=Cumulative_BirthProb+ProbabilityBirth[k];
        CumBirthProbability.append(Cumulative_BirthProb);
    y=random.randint(0, 10);
    y=y/10;
    for k in range (len(CumBirthProbability)):
        if CumBirthProbability[k]>=y:
            nd=LNode[k];
            return nd;
LNode=[];
ProbabilityBirth=[];
ProbabilityDeath=[];
begin();
StepsNo=[];
NodeNo=[];
EdgeNo=[];
CumBirthProbability=[];

for j in range (5000):
    x=random.randint(0, 10);
    x=x/10;    
    if x<=0.6:    
        SelNode=CumProbability();         
        ProbabilityBirth=[];
        ProbabilityDeath=[];
        Birthnd(SelNode);
    else:
        MaxiPos=ProbabilityDeath.index(max(ProbabilityDeath));
        SelNode=LNode[MaxiPos];
        ProbabilityBirth=[];
        ProbabilityDeath=[];
        Deathnd(SelNode);
    length=len(LNode);
    if length==0:
        begin();
    StepsNo.append(j);
    NodeNo.append(len(LNode));
    EdgeNo.append(tDegree);

           
LNode=[];
ProbabilityBirth=[];
ProbabilityDeath=[];
begin();
StepsNo1=[];
NodeNo1=[];
EdgeNo1=[];
CumBirthProbability=[]; 
for j in range (5000):
    x=random.randint(0, 10);
    x=x/10;
    if x<=0.75:
        SelNode=CumProbability();            
        ProbabilityBirth=[];
        ProbabilityDeath=[];
        Birthnd(SelNode);
    else:
        MaxiPos=ProbabilityDeath.index(max(ProbabilityDeath));
        SelNode=LNode[MaxiPos];
        ProbabilityBirth=[];
        ProbabilityDeath=[];
        Deathnd(SelNode);
    length=len(LNode);
    if length==0:
        begin();
    StepsNo1.append(j);
    NodeNo1.append(len(LNode));
    EdgeNo1.append(tDegree);

LNode=[];
ProbabilityBirth=[];
ProbabilityDeath=[];
begin();
StepsNo2=[];
NodeNo2=[];
EdgeNo2=[];
CumBirthProbability=[];
for j in range (5000):
    x=random.randint(0, 10);
    x=x/10;   
    if x<=0.85:
        SelNode=CumProbability();            
        ProbabilityBirth=[];
        ProbabilityDeath=[];
        Birthnd(SelNode);
    else:
        MaxiPos=ProbabilityDeath.index(max(ProbabilityDeath));
        SelNode=LNode[MaxiPos];
        ProbabilityBirth=[];
        ProbabilityDeath=[];
        Deathnd(SelNode);
    length=len(LNode);
    if length==0:
        begin();
    StepsNo2.append(j);
    NodeNo2.append(len(LNode));
    EdgeNo2.append(tDegree);
    
    

plt.plot(StepsNo,NodeNo,color='green')
plt.scatter([1010,1810,2810,4010], [680,1100,1800,2550], color='darkgreen', marker='^')
plt.plot(StepsNo1,NodeNo1,color='red')
plt.scatter([1000,1800,2800,4000], [500,900,1300,1900], color='darkgreen', marker='D')
plt.plot(StepsNo2,NodeNo2,color='blue')
plt.scatter([1050,1850,2850,4050], [330,500,650,1000], color='darkgreen', marker='P')
plt.xlabel('t- Time steps')
plt.ylabel('E[n]- Number of nodes')
plt.title('Figure 1')
plt.show()

plt.plot(StepsNo,EdgeNo)
plt.scatter([1000,1800,2800,4000], [1300,2400,3800 ,5050], color='darkgreen', marker='^')
plt.plot(StepsNo1,EdgeNo1)
plt.scatter([1000,1800,2800,4000], [1000,1800,2800,3800], color='darkgreen', marker='D')
plt.plot(StepsNo2,EdgeNo2)
plt.scatter([1000,1800,2800,4000], [530,800,1250,2000], color='darkgreen', marker='P')
plt.xlabel('t- Time steps')
plt.ylabel('E[m]- Number of edges')
plt.title('Figure 2')
plt.show()

ListP=[];
ListK=[];
ListAk=[];
m=len(LNode);
P=0;

NodeNo_kdegree=0;
for k in range (1,100):
    for l in range (len(LNode)):
        if LNode[l].EdgesNo == k:
            NodeNo_kdegree=NodeNo_kdegree + 1;
#            ak=NodeNo_kdegree**(-1-((2*0.8)/((2*0.8)-1)));
    P= (P + (NodeNo_kdegree/m));
    P1=(100-P)/100
    ListP.append(P1);
    ListK.append(k);
#    ListAk.append(ak);

plt.plot(ListK,ListP)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('k')
plt.ylabel("P'(k)")
plt.title('Figure 3')
plt.show()