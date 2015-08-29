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
        
def avgwinloss(regiontry): #set argument as the region you're processing
        archw = 0 #counter of the average length of won games
        archl = 0 #counter of the average length of lost games
        archwc = 0 #counter of how many games item is in (won)
        archlc = 0 #counter of how many games item is in (lost)
        roaw = 0 #counter of the average length of won games
        roal = 0
        roawc = 0
        roalc = 0
        rabadonw = 0
        rabadonl = 0 
        rabadonwc = 0
        rabadonlc = 0
        nashorw = 0
        nashorl = 0
        nashorwc = 0
        nashorlc = 0
        rylaiw = 0
        rylail = 0
        rylaiwc = 0
        rylailc = 0
        voidw = 0
        voidl = 0
        voidwc = 0
        voidlc = 0
        lianw = 0
        lianl = 0
        lianwc = 0
        lianlc = 0
        zhonw = 0
        zhonl = 0
        zhonwc = 0
        zhonlc = 0
        morelw = 0
        morell = 0
        morelwc = 0
        morellc = 0 #looked at this too quick and thought it said 'morello' lol
        athenew = 0
        athenel = 0
        athenewc = 0
        athenelc = 0
        ludenw = 0
        ludenl = 0
        ludenwc = 0
        ludenlc = 0
        wotaw = 0
        wotal = 0
        wotawc = 0
        wotalc = 0
        
        for key, value in regiontry.items(): #for loop to process the dictionaries in each json
                team1 = regiontry[key]['participants'][:5] #split teams apart to tell if item won or lost
                team1wl = regiontry[key]['teams'][0]['winner']
                team2 = regiontry[key]['participants'][5:]
                team2wl = regiontry[key]['teams'][1]['winner']
                length = regiontry[key]['matchDuration']/100 #riot api returns no decimal, eg 3155 = 31.55 minutes
                
                for pack in team1: #split teams since 1 wins and other loses
                        for summoner in pack: #finds all items in each summoner's inventory
                                item1 = pack['stats']['item0']
                                item2 = pack['stats']['item1']
                                item3 = pack['stats']['item2']
                                item4 = pack['stats']['item3']
                                item5 = pack['stats']['item4']
                                item6 = pack['stats']['item5']
                                itemset = [item1, item2, item3, item4, item5, item6]
                                
                        if 3089 in itemset and team1wl == True: #item from item.json
                                rabadonw += length
                                rabadonwc += 1
                        elif 3089 in itemset and team1wl == False:
                                rabadonl += length
                                rabadonlc +=1
                                
                        if 3003 in itemset and team1wl == True:
                                archw += length
                                archwc += 1
                        elif 3003 in itemset and team1wl == False:
                                archl += length
                                archlc += 1
                        
                        if 3040 in itemset and team1wl == True: #seraphs is arch
                                archw += length
                                archwc += 1
                        elif 3040 in itemset and team1wl == False:
                                archl += length
                                archlc += 1
                                
                        if 3027 in itemset and team1wl == True:
                                roaw += length
                                roawc += 1
                        elif 3027 in itemset and team1wl == False:
                                roal += length
                                roalc += 1         

                        if 3115 in itemset and team1wl == True:
                                nashorw += length
                                nashorwc += 1
                        elif 3115 in itemset and team1wl == False:
                                nashorl += length
                                nashorlc += 1
                                
                        if 3116 in itemset and team1wl == True:
                                rylaiw += length
                                rylaiwc += 1
                        elif 3116 in itemset and team1wl == False:
                                rylail += length
                                rylailc += 1        
                                
                        if 3135 in itemset and team1wl == True:
                                voidw += length
                                voidwc += 1
                        elif 3135 in itemset and team1wl == False:
                                voidl += length
                                voidlc += 1        
                                
                        if 3151 in itemset and team1wl == True:
                                lianw += length
                                lianwc += 1
                        elif 3151 in itemset and team1wl == False:
                                lianl += length
                                lianlc += 1          
                                
                        if 3157 in itemset and team1wl == True:
                                zhonw += length
                                zhonwc += 1
                        elif 3157 in itemset and team1wl == False:
                                zhonl += length
                                zhonlc += 1    
                                
                        if 3165 in itemset and team1wl == True:
                                morelw += length
                                morelwc += 1
                        elif 3165 in itemset and team1wl == False:
                                morell += length
                                morellc += 1      
                                
                        if 3174 in itemset and team1wl == True:
                                athenew += length
                                athenewc += 1
                        elif 3174 in itemset and team1wl == False:
                                athenel += length
                                athenelc += 1                  
                                
                        if 3285 in itemset and team1wl == True:
                                ludenw += length
                                ludenwc += 1
                        elif 3285 in itemset and team1wl == False:
                                ludenl += length
                                ludenlc += 1                           
                                
                        if 3152 in itemset and team1wl == True:
                                wotaw += length
                                wotawc += 1
                        elif 3152 in itemset and team1wl == False:
                                wotal += length
                                wotalc += 1
                
                for pack in team2: #same as above for second team
                        for summoner in pack:
                                item1 = pack['stats']['item0']
                                item2 = pack['stats']['item1']
                                item3 = pack['stats']['item2']
                                item4 = pack['stats']['item3']
                                item5 = pack['stats']['item4']
                                item6 = pack['stats']['item5']
                                itemset = [item1, item2, item3, item4, item5, item6]
                                
                        if 3089 in itemset and team2wl == True:
                                rabadonw += length
                                rabadonwc += 1
                        elif 3089 in itemset and team2wl == False:
                                rabadonl += length
                                rabadonlc += 1
                                        
                        if 3003 in itemset and team2wl == True:
                                archw += length
                                archwc += 1
                        elif 3003 in itemset and team2wl == False:
                                archl += length
                                archlc += 1
                                
                        if 3040 in itemset and team2wl == True: #seraphs is arch
                                archw += length
                                archwc += 1
                        elif 3040 in itemset and team2wl == False:
                                archl += length
                                archlc += 1
                                
                        if 3027 in itemset and team2wl == True:
                                roaw += length
                                roawc += 1
                        elif 3027 in itemset and team2wl == False:
                                roal += length
                                roalc += 1         
                                                        
                        if 3115 in itemset and team2wl == True:
                                nashorw += length
                                nashorwc += 1
                        elif 3115 in itemset and team2wl == False:
                                nashorl += length
                                nashorlc += 1
                                                                
                        if 3116 in itemset and team2wl == True:
                                rylaiw += length
                                rylaiwc += 1
                        elif 3116 in itemset and team2wl == False:
                                rylail += length
                                rylailc += 1        
                                
                        if 3135 in itemset and team2wl == True:
                                voidw += length
                                voidwc += 1
                        elif 3135 in itemset and team2wl == False:
                                voidl += length
                                voidlc += 1        
                                
                        if 3151 in itemset and team2wl == True:
                                lianw += length
                                lianwc += 1
                        elif 3151 in itemset and team2wl == False:
                                lianl += length
                                lianlc += 1          
                                
                        if 3157 in itemset and team2wl == True:
                                zhonw += length
                                zhonwc += 1
                        elif 3157 in itemset and team2wl == False:
                                zhonl += length
                                zhonlc += 1    
                                
                        if 3165 in itemset and team2wl == True:
                                morelw += length
                                morelwc += 1
                        elif 3165 in itemset and team2wl == False:
                                morell += length
                                morellc += 1      
                                
                        if 3174 in itemset and team2wl == True:
                                athenew += length
                                athenewc += 1
                        elif 3174 in itemset and team2wl == False:
                                athenel += length
                                athenelc += 1                  
                                
                        if 3285 in itemset and team2wl == True:
                                ludenw += length
                                ludenwc += 1
                        elif 3285 in itemset and team2wl == False:
                                ludenl += length
                                ludenlc += 1
                                
                        if 3152 in itemset and team2wl == True:
                                wotaw += length
                                wotawc += 1
                        elif 3152 in itemset and team2wl == False:
                                wotal += length
                                wotalc += 1                        
         
        print('arch')                       
        print(archw / archwc) #prints average wintime, total win length / total wins (time per game)
        print(archl / archlc)
        print('roa')
        print(roaw / roawc)
        print(roal / roalc)
        print('rabadon')
        print(rabadonw / rabadonwc)
        print(rabadonl / rabadonlc)
        print('nashor')
        print(nashorw / nashorwc)
        print(nashorl / nashorlc)
        print('rylai')
        print(rylaiw / rylaiwc)
        print(rylail / rylailc)
        print('void')
        print(voidw / voidwc)
        print(voidl / voidlc)
        print('liandry')
        print(lianw / lianwc)
        print(lianl / lianlc)
        print('zhonya')
        print(zhonw / zhonwc)
        print(zhonl / zhonlc)
        print('morello')
        print(morelw / morelwc)
        print(morell / morellc)
        print('athene')
        print(athenew / athenewc)
        print(athenel / athenelc)
        print('luden')
        print(ludenw / ludenwc)
        print(ludenl / ludenlc)
        print('wota')
        print(wotaw / wotawc)
        print(wotal / wotalc)