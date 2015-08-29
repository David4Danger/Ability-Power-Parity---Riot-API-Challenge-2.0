import json

#Open anywhere from 1-10 json files at a time, depending on your memory limit.
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\BR.json') as data_file:
        BR511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\EUNE.json') as data_file:
        EUNE511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\EUW.json') as data_file:
        EUW511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\KR.json') as data_file:
        KR511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\LAN.json') as data_file:
        LAN511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\LAS.json') as data_file:
        LAS511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\NA.json') as data_file:
        NA511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\OCE.json') as data_file:
        OCE511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\RU.json') as data_file:
        RU511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\TR.json') as data_file:
        TR511N = json.load(data_file)
        
def itemcount(regiontry): #set argument as the region you're processing
        archw = 0 #if you import more than one json at a time, put them in a list and set the argument as said list
        archl = 0 #then add an additional for loop to process said list.
        archc = 0
        roaw = 0
        roal = 0
        roac = 0        
        rabadonw = 0 #amount of rabadon wins
        rabadonl = 0 #amount of rabadon losses
        rabadonc = 0 #total rabadon count (w + l)
        nashorw = 0
        nashorl = 0
        nashorc = 0
        rylaiw = 0
        rylail = 0
        rylaic = 0
        voidw = 0
        voidl = 0
        voidc = 0
        lianw = 0
        lianl = 0
        lianc = 0
        zhonw = 0
        zhonl = 0
        zhonc = 0
        morelw = 0
        morell = 0
        morelc = 0
        athenew = 0
        athenel = 0
        athenec = 0
        ludenw = 0
        ludenl = 0
        ludenc = 0
        wotaw = 0
        wotal = 0
        wotac = 0
        
        for key, value in regiontry.items(): #for loop to process the dictionaries in each json
                team1 = regiontry[key]['participants'][:5] #split teams apart to tell if item won or lost
                team1wl = regiontry[key]['teams'][0]['winner']
                team2 = regiontry[key]['participants'][5:]
                team2wl = regiontry[key]['teams'][1]['winner']
                
                for pack in team1:
                        for summoner in pack: #finds all items in each summoner's inventory
                                item1 = pack['stats']['item0']
                                item2 = pack['stats']['item1']
                                item3 = pack['stats']['item2']
                                item4 = pack['stats']['item3']
                                item5 = pack['stats']['item4']
                                item6 = pack['stats']['item5']
                                itemset = [item1, item2, item3, item4, item5, item6]
                                
                        if 3089 in itemset and team1wl == True: #each statement checks if __ item is in the inventory and if they won
                                rabadonw += 1 #adds 1 to a win and count variables
                                rabadonc += 1
                        elif 3089 in itemset and team1wl == False:
                                rabadonl += 1 #adds 1 to a loss and count variable
                                rabadonc += 1
                                
                        if 3003 in itemset and team1wl == True:
                                archw += 1
                                archc += 1
                        elif 3003 in itemset and team1wl == False:
                                archl += 1
                                archc += 1
                        
                        if 3040 in itemset and team1wl == True: #seraphs is archangel's, has different ID
                                archw += 1
                                archc += 1
                        elif 3040 in itemset and team1wl == False:
                                archl += 1
                                archc += 1
                                
                        if 3027 in itemset and team1wl == True:
                                roaw += 1
                                roac += 1
                        elif 3027 in itemset and team1wl == False:
                                roal += 1
                                roac += 1         

                        if 3115 in itemset and team1wl == True:
                                nashorw += 1
                                nashorc += 1
                        elif 3115 in itemset and team1wl == False:
                                nashorl += 1
                                nashorc += 1
                                
                        if 3116 in itemset and team1wl == True:
                                rylaiw += 1
                                rylaic += 1
                        elif 3116 in itemset and team1wl == False:
                                rylail += 1
                                rylaic += 1        
                                
                        if 3135 in itemset and team1wl == True:
                                voidw += 1
                                voidc += 1
                        elif 3135 in itemset and team1wl == False:
                                voidl += 1
                                voidc += 1        
                                
                        if 3151 in itemset and team1wl == True:
                                lianw += 1
                                lianc += 1
                        elif 3151 in itemset and team1wl == False:
                                lianl += 1
                                lianc += 1          
                                
                        if 3157 in itemset and team1wl == True:
                                zhonw += 1
                                zhonc += 1
                        elif 3157 in itemset and team1wl == False:
                                zhonl += 1
                                zhonc += 1    
                                
                        if 3165 in itemset and team1wl == True:
                                morelw += 1
                                morelc += 1
                        elif 3165 in itemset and team1wl == False:
                                morell += 1
                                morelc += 1      
                                
                        if 3174 in itemset and team1wl == True:
                                athenew += 1
                                athenec += 1
                        elif 3174 in itemset and team1wl == False:
                                athenel += 1
                                athenec += 1                  
                                
                        if 3285 in itemset and team1wl == True:
                                ludenw += 1
                                ludenc += 1
                        elif 3285 in itemset and team1wl == False:
                                ludenl += 1
                                ludenc += 1                    
                                
                        if 3152 in itemset and team1wl == True:
                                wotaw += 1
                                wotac += 1
                        elif 3152 in itemset and team1wl == False:
                                wotal += 1
                                wotac += 1
                
                for pack in team2: #does the same as above, but for the 5 summoners on team 2
                        for summoner in pack:
                                item1 = pack['stats']['item0']
                                item2 = pack['stats']['item1']
                                item3 = pack['stats']['item2']
                                item4 = pack['stats']['item3']
                                item5 = pack['stats']['item4']
                                item6 = pack['stats']['item5']
                                itemset = [item1, item2, item3, item4, item5, item6]
                                
                        if 3089 in itemset and team2wl == True:
                                rabadonw += 1
                                rabadonc += 1
                        elif 3089 in itemset and team2wl == False:
                                rabadonl += 1
                                rabadonc += 1
                                        
                        if 3003 in itemset and team2wl == True:
                                archw += 1
                                archc += 1
                        elif 3003 in itemset and team2wl == False:
                                archl += 1
                                archc += 1
                                
                        if 3040 in itemset and team2wl == True:
                                archw += 1
                                archc += 1
                        elif 3040 in itemset and team2wl == False:
                                archl += 1
                                archc += 1
                                
                        if 3027 in itemset and team2wl == True:
                                roaw += 1
                                roac += 1
                        elif 3027 in itemset and team2wl == False:
                                roal += 1
                                roac += 1         
                                                        
                        if 3115 in itemset and team2wl == True:
                                nashorw += 1
                                nashorc += 1
                        elif 3115 in itemset and team2wl == False:
                                nashorl += 1
                                nashorc += 1
                                                                
                        if 3116 in itemset and team2wl == True:
                                rylaiw += 1
                                rylaic += 1
                        elif 3116 in itemset and team2wl == False:
                                rylail += 1
                                rylaic += 1        
                                
                        if 3135 in itemset and team2wl == True:
                                voidw += 1
                                voidc += 1
                        elif 3135 in itemset and team2wl == False:
                                voidl += 1
                                voidc += 1        
                                
                        if 3151 in itemset and team2wl == True:
                                lianw += 1
                                lianc += 1
                        elif 3151 in itemset and team2wl == False:
                                lianl += 1
                                lianc += 1          
                                
                        if 3157 in itemset and team2wl == True:
                                zhonw += 1
                                zhonc += 1
                        elif 3157 in itemset and team2wl == False:
                                zhonl += 1
                                zhonc += 1    
                                
                        if 3165 in itemset and team2wl == True:
                                morelw += 1
                                morelc += 1
                        elif 3165 in itemset and team2wl == False:
                                morell += 1
                                morelc += 1      
                                
                        if 3174 in itemset and team2wl == True:
                                athenew += 1
                                athenec += 1
                        elif 3174 in itemset and team2wl == False:
                                athenel += 1
                                athenec += 1                  
                                
                        if 3285 in itemset and team2wl == True:
                                ludenw += 1
                                ludenc += 1
                        elif 3285 in itemset and team2wl == False:
                                ludenl += 1
                                ludenc += 1
                                
                        if 3152 in itemset and team2wl == True:
                                wotaw += 1
                                wotac += 1
                        elif 3152 in itemset and team2wl == False:
                                wotal += 1
                                wotac += 1                        
                                
        print('arch') #prints out the item we're identifying followed by 3 numbers
        print(archw) #the items wins
        print(archl) #the items losses
        print(archc) #the items total count
        print('roa')
        print(roaw)
        print(roal)
        print(roac)
        print('rabadon')
        print(rabadonw)
        print(rabadonl)
        print(rabadonc)
        print('nashor')
        print(nashorw)
        print(nashorl)
        print(nashorc)
        print('rylai')
        print(rylaiw)
        print(rylail)
        print(rylaic)
        print('void')
        print(voidw)
        print(voidl)
        print(voidc)
        print('liandry')
        print(lianw)
        print(lianl)
        print(lianc)
        print('zhonyas')
        print(zhonw)
        print(zhonl)
        print(zhonc)
        print('morello')
        print(morelw)
        print(morell)
        print(morelc)
        print('athene')
        print(athenew)
        print(athenel)
        print(athenec)
        print('luden')
        print(ludenw)
        print(ludenl)
        print(ludenc)
        
#An alternative solution to finding total count that would present a slightly shorter runtime would to simply add
#the total wins and losses together once the final item wins and losses had been calculated.