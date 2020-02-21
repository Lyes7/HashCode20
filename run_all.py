titles=['a_example','b_read_on','c_incunabula','d_tough_choices','e_so_many_books','f_libraries_of_the_world']
for t in titles:
    title=t+'.txt'
    f=open(title,'r')
    a=f.read().split("\n")
    BLD=list(map(int, a[0].split())) #bld => Book Library DeadLine
    scores=list(map(int, a[1].split()))
    libs,taked,outputs=[],[],[]
    DDL=int(BLD[2])
    for i in range(2,int(BLD[1])*2+1,2):
        lib={
            "id":(i//2)-1,
            "NTM":list(map(int, a[i].split())), #NTM = NbrBook TimeForSignup MaxPerDay
            "id_book":list(map(int, a[i+1].split()))
        }
        libs.append(lib)

    lst=sorted(libs,key=lambda k:k["NTM"][1])
    nbrLib=0

    for i in lst:
        DDL-=i["NTM"][1]
        if DDL<=0 :
            break
        else:
            bk=sorted(i["id_book"],reverse=True)
            line,shop,day,idx,isEmpt=[],[],0,0,True
            while(bk and day<DDL):
                b=bk.pop(0)
                if b not in taked:
                    isEmpt = False
                    taked.append(b)
                    shop.append(b)
                    idx+=1
                if idx==i["NTM"][2]:
                    day+=1
                    idx=0
            if not isEmpt:
                nbrLib+=1
                line=[i["id"],shop]
                outputs.append(line)

    title='result_'+title
    outFile=open(title,"w")
    outFile.write(str(nbrLib)+'\n')
    for i in outputs:
        outFile.write(str(i[0])+' '+str(len(i[1]))+'\n')      
        for s in i[1]:
            outFile.write(str(s)+' ')
        outFile.write('\n')
    outFile.close()
    f.close()
            