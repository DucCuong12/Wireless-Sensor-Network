def crossover1(indd1,indd2):
    new=[]
    for i in range(len(indd1)):
        if indd1[i]==indd2[i]:
            new.append(indd1[i])
        else:
            ft1= list_indi[tuple(indd1)]
            ft2= list_indi[tuple(indd2)]
            ft12 = ft1+ft2
            if random.random() <  (ft1/(ft1+ft2)):
                new.append(indd1[i])
            else:
                new.append(indd2[i])
    return new
            
def mutate1(ind1,m_m):
    ind2 = copy.deepcopy(ind1)
    m_mm = copy.deepcopy(m_m)
    if check(ind2):
        for i in range(1,len(ind2)):
            if ind2[i]==0:
                if random.random()<m_mm:
                    m_mm -= 1/(2*len(ind1))
                    ind2[i]=1
    else:
        for i in range(1,len(ind2)):
            if ind2[i]==1:
                if random.random()<m_m:
                    ind2[i]=0
                    m_mm -=1/(2*len(ind1))
    return ind2