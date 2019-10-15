
def simple_table():
        #Title
    print("\nSimple Punnett Square Generator:\nPlease enter parent genotypes below, put a space between each letter\ne.g. H h\n\n")

    #Input functions
    x, y = input("Parent 1 Genotype: ").split()
    z,q = input("Parent 2 Genotype: ").split()
    
    #Margin calculation

    if len(z) > len(q) :
        marginL = len(z)
        qmarginl = len(z)-len(q)
        zmarginl = 0

    else :
        marginL = len(q)
        zmarginl = len(q)-len(z)
        qmarginl = 0

    m = 0
    margin = ""
    while m < marginL:
        margin = margin + " "
        m+= 1

    m1 = 0
    zmargin = ""
    qmargin = ""
    while m1 < zmarginl: 
        zmargin = zmargin + " "
        m1+=1
    m2 = 0
    while m2 < qmarginl:
        qmargin = qmargin + " "
        m2+= 1

    #var declaration
    val1 = x+z
    val2 = y+z
    val3 = x+q
    val4 = y+q

    #length comparison
    varlst = [len(val1)+ len(val2), len(val3) + len(val4)]
    topval = max(varlst) 

    #gap write 
    gap = topval/4
    spaces = ""
    f = 0
    while f < gap:
        spaces = spaces + " "
        f+=1
    totspace = f*4


    # total line length comparison and write

    totalwidth = (zmarginl + len(z) + 3 + totspace + topval -1) *.8974
    totalwidth2 = (qmarginl + len(q) + 3 + totspace + topval - 1) *.8974

    if totalwidth< totalwidth2 :
        totalwidth = totalwidth2

    topline = ""
    s = 0
    while s < totalwidth:
        topline = topline + "-"
        s+=1



    #Individual box spacing adjustments
    if (len(val1)< len(val3)):
        diff1 = len(val3)-len(val1)
        e = 0
        while e< diff1:
            val1 = val1 + " "
            e+= 1
    if(len(val3)< len(val1)):
        diff2 = len(val1)- len(val3)
        e = 0
        while e< diff2:
            val3 = val3 + " "
            e+=1
    if(len(val2)< len(val4)):
        diff3 = len(val4)- len(val2)
        e1 = 0
        while e1< diff3:
            val2 = val2 + " "
            e1+=1
    if(len(val4)< len(val2)):
        diff4 = len(val2)- len(val4)
        e1 = 0
        while e1<diff4:
            val4= val4 + " "
            e1 += 1



    #table print
    print("\n" + margin + " " + spaces + x + spaces + spaces + " " + y)
    print(margin + topline)
    print(zmargin + z + "|" + spaces + val1 + spaces + "|" + spaces + val2 + spaces+ "|")
    print(margin + topline)
    print(qmargin + q + "|" + spaces+ val3 +spaces + "|"+ spaces+ val4 + spaces+ "|")
    print(margin + topline)


    #percentage reporting

    #split function definition
    def split(x):
        return list(x)

    varlst1 = [val1, val2, val3, val4]
    varlst2 = [split(val1), split(val2), split(val3), split(val4)]

    #compare function definition
    def compare(lst1, lst2):
        for i in lst1:
            if(i not in lst2 ):
                return False
            else:
                for i in lst2:
                    if(i not in lst1):
                        return False
        
        return True


    #ratio dictionary declaration
    perc = {'box1': 0, 'box2': 0, 'box3': 0, 'box4': 0}

    #main comparison function. This function compares the allele combinations to each other, while incrementally increasing starting values 
    #so values aren't compared to themselves or to each other multiple times. It then adds to the ratio dictionary values if two values are 
    #found to be equivalent
    b = 0
    startval = 1
    for i in varlst1:
        k = varlst2[b]
        for i in range(startval, len(varlst2)):
            j = varlst2[i]
            if len(j) == len(k):
                if (compare(j, k)== True):
                    if(b == 0):
                        perc['box1']+= 1
                        perc['box'+ str(i+1)] += 1
                    else:
                        perc['box'+ str(i+1)] += 1
                        perc['box' + str(b + 1)] += 1
            
        b+=1
        startval +=1

    #ratio list declaration- this takes the definition values of the ratio dictionary and writes them to a list so they can be evaluated.
    ratios = []
    for i in perc:
        ratios.append(perc[i])

    #Percentages print and evaluation: this section then checks to see what ratio is presented by the data, and prints the respective
    #percentages
    print("Percentages: ")
    if(ratios == [1, 0, 0, 1]):
        print(str(varlst1[0]) + ": "+ "50%")
        print(str(varlst1[1])+ ": " + "25%")
        print(str(varlst1[2])+ ": " + "25%")
    if (ratios == [0, 1, 1, 0]):
        print(str(varlst1[1]) + ": "+ "50%")
        print(str(varlst1[0])+ ": " + "25%")
        print(str(varlst1[3])+ ": " + "25%")
    if(ratios == [1, 1, 1, 1]):
        if(varlst1[0] != varlst1[3]):
            print(str(varlst1[0]) + ": "+ "50%")
            print(str(varlst1[3]) + ": "+ "50%")
        else:
            print(str(varlst1[0]) + ": "+ "50%")
            print(str(varlst1[1]) + ": "+ "50%")

    if(ratios == [3, 3, 3, 3]):
        print(str(varlst1[0]) + ": "+ "100%")
    if(ratios == [0, 0, 0, 0]):
        print(str(varlst1[0]) + ": "+ "25%")
        print(str(varlst1[1])+ ": " + "25%")
        print(str(varlst1[2])+ ": " + "25%")
        print(str(varlst1[3])+ ": " + "25%")

def complex_table():
    print("\nTwo-gene Punnett Square Generator:\nPlease enter parent genotypes below, put a space between each letter\ne.g. H h J j\n\n")

    #Input functions
    x, y, x1, y1 = input("Parent 1 Genotype: ").split()
    z,q, z1, q1 = input("Parent 2 Genotype: ").split()

    #Side margin adjustments
    val1 = z+z1
    val2 = z+q1
    val3 = q+z1
    val4 = q+q1
    mlist = [len(val1), len(val2), len(val3), len(val4)]
    marginl = max(mlist)
    margin1 = ""
    margin2 = ""
    margin3 = ""
    margin4 = ""
    if(len(val1) < marginl):
        i = 0
        diff1 = marginl - len(val1)
        while i < diff1:
            margin1 += " "
            i+= 1
    if(len(val2)< marginl):
        i = 0
        diff2 = marginl - len(val2)
        while i < diff2:
            margin2 += " "
            i+= 1
    if(len(val3)< marginl):
        i = 0
        diff3 = marginl - len(val3)
        while i < diff3:
            margin3 += " "
            i+= 1
    if (len(val4)< marginl):
        i = 0
        diff4 = marginl -len(val4)
        while i< diff4:
            margin4+= " "
            i+=1

    #Topline margin adjustment
    A1, B1, C1, D1 = x+x1,x+y1, y+x1, y+y1     
    topmargin = ''
    n3 = 0
    while n3 < marginl:
        topmargin += " "
        n3+= 1
    

    #Box margin adjustment
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P = x+z+x1+z1, x+z+y1+z1, y+z+x1+z1, y+z+y1+z1, x+z+x1+q1, x+z+y1+q1, y+z+x1+q1, y+z+y1+q1, x+q+x1+z1, x+q+y1+z1, y+q+x1+z1, y+q+y1+z1, x+q+x1+q1, x+q+y1+q1, y+q+x1+q1, y+q+y1+q1   
    comp_var_list_len = [len(A), len(B), len(C), len(D), len(E), len(F), len(G), len(H), len(I), len(J), len(K), len(L), len(M), len(N), len(O), len(P), len(A1), len(B1), len(C1), len(D1)]
    top_len = max(comp_var_list_len)
    comp_var_list = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P, A1,B1,C1,D1]
   
    for i in range(len(comp_var_list)):
        global sidevar 
        global string1
        global string2
        sidevar = True
        diff = top_len - comp_var_list_len[i]
        n = 0
        string1= ' '
        string2 = ' '
        while n < diff:
            if (sidevar):
                string1 = string1 + ' '
                sidevar = False
            else:
                string2 = string2 + ' '
                sidevar = True
            n += 1
        comp_var_list[i] = string1 + comp_var_list[i] + string2
        
        
    #line length adjustments
    total_length = ((top_len + 2) * 4) + 4
    n1 = 0
    line = ''
    while n1 < marginl:
        line += ' '
        n1+=1
    n2 = 0
    while n2< total_length:
        line = line + '-'
        n2+=1
   

    #Complex Table print
    
    print("\n" +topmargin + " "+ comp_var_list[16] + " "+ comp_var_list[17] + " "+ comp_var_list[18] + " "+ comp_var_list[19])
    print(line)
    print(margin1 + z+z1 + "|" + comp_var_list[0] +"|"+comp_var_list[1] + "|"+  comp_var_list[2]  + "|" + comp_var_list[3] + "|")
    print(line)
    print(margin2 + z+ q1 + "|"+ comp_var_list[4]+ "|"+ comp_var_list[5]+ "|"+ comp_var_list[6]+ "|"+ comp_var_list[7]+ "|")
    print(line)
    print(margin3+ q+z1 + "|"+ comp_var_list[8]+ "|"+ comp_var_list[9]+ "|"+ comp_var_list[10]+ "|"+ comp_var_list[11]+ "|")
    print(line)
    print(margin4 + q+q1 + "|"+comp_var_list[12]+ "|"+comp_var_list[13]+ "|"+ comp_var_list[14]+ "|"+ comp_var_list[15]+ "|")
    print(line)

    
    #Compare function
    def compare(lst1, lst2):
        for i in lst1:
            if(i not in lst2 ):
                return False
            else:
                for i in lst2:
                    if(i not in lst1):
                        return False
        
        return True
    #split function definition
    def split(x):
        return list(x)

    #Compare process
    comp_varlst = [A, B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]
    comp_varlst_split = split(comp_varlst)
    perc2 = {'box1': 0, 'box2': 0, 'box3': 0, 'box4': 0, 'box5':0, 'box6': 0,'box7': 0,'box8': 0,'box9': 0,'box10': 0,'box11': 0,'box12': 0,'box13': 0,'box14': 0,'box15': 0,'box16': 0,}
    b = 0
    startval = 1
    for i in comp_varlst:
        k = comp_varlst_split[b]
        for i in range(startval, len(comp_varlst_split)):
            j = comp_varlst_split[i]
            if len(j) == len(k):
                if (compare(j, k)== True):
                    if(b == 0):
                        perc2['box1']+= 1
                        perc2['box'+ str(i+1)] += 1
                    else:
                        perc2['box'+ str(i+1)] += 1
                        perc2['box' + str(b + 1)] += 1
            
        b+=1
        startval +=1
    ratios = []
    for i in perc2:
        ratios.append(perc2[i])
    print(ratios)

    if(ratios == [15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15]):
        print("Percentages:\n"+ A+ ": 100%")
 #Title

def startMenu():

    print("\nPunnett Square Generator:\nTo select a simple punnett square, please type '1' below.\nTo select a two-gene punnett square, please type'2' below.")
    select = input("Selection: ")
    if select == '1':
        simple_table()
    elif select == '2':
        complex_table()
    else :
        print("\nSorry, that input is not recognized. Please try again.")
        startMenu()

startMenu()

            






        
