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

def champitemcount(regiontry): #set argument as the region you're processing
        kayle_nashor = 0 #if you import more than one json at a time, put them in a list and set the argument as said list
        kayle_count = 0 #then add an additional for loop to process said list.
        ryze_arch = 0
        ryze_count = 0
        azir_nashor = 0
        azir_rylai = 0
        azir_count = 0
        lulu_luden = 0
        lulu_morello = 0
        lulu_count = 0
        viktor_raba = 0
        viktor_count = 0
        rumble_lian = 0
        rumble_zhon = 0
        rumble_rylai = 0
        rumble_count = 0
        kog_luden = 0
        kog_count = 0
        vlad_wota = 0
        vlad_count = 0
        kennen_zhon = 0
        kennen_wota = 0
        kennen_count = 0
        orianna_athene = 0
        orianna_count = 0
        ahri_luden = 0
        ahri_morel = 0
        ahri_raba = 0
        ahri_count = 0
        morg_zhon = 0
        morg_count = 0
        cho_roa = 0
        cho_count = 0
        lux_luden = 0
        lux_count = 0
        aniv_roa = 0
        aniv_arch = 0
        aniv_count = 0
        karth_roa = 0
        karth_raba = 0
        karth_count = 0
        vei_raba = 0
        vei_count = 0
        syndra_luden = 0
        syndra_raba = 0
        syndra_count = 0
        leb_morel = 0
        leb_luden = 0
        leb_count = 0
        kat_luden = 0
        kat_zhon = 0
        kat_count = 0
        kass_roa = 0
        kass_count = 0
        heim_zhon = 0
        heim_raba = 0
        heim_count = 0
        xer_luden = 0
        xer_count = 0
        soraka_zhonya = 0
        soraka_count = 0        
        
        for key, value in regiontry.items(): #for loop to process dictionaries in json
                players = regiontry[key]['participants']
                for pack in players:
                        for summoner in pack: #each summoner (1-10) in the game
                                champion = pack['championId']
                                item1 = pack['stats']['item0']
                                item2 = pack['stats']['item1']
                                item3 = pack['stats']['item2']
                                item4 = pack['stats']['item3']
                                item5 = pack['stats']['item4']
                                item6 = pack['stats']['item5']
                                itemset = [item1, item2, item3, item4, item5, item6] #set of items unique to each summoner 
                          
                        if champion == 10: #all champ ids are found in champion.json
                                kayle_count += 1
                                if 3115 in itemset: #all item ids are found in item.json
                                        kayle_nashor += 1
                                
                        if champion == 13:
                                ryze_count += 1
                                if 3003 in itemset:
                                        ryze_arch += 1
                                elif 3040 in itemset:
                                        ryze_arch += 1
                 
                        if champion == 268:
                                azir_count += 1
                                if 3116 in itemset:
                                        azir_rylai += 1
                                elif 3115 in itemset:
                                        azir_nashor +=1
                        
                        if champion == 117:
                                lulu_count += 1
                                if 3285 in itemset:
                                        lulu_luden += 1
                                elif 3165 in itemset:
                                        lulu_morello += 1
                                
                        if champion == 112:
                                viktor_count += 1
                                if 3089 in itemset:
                                        viktor_raba += 1
                        
                        if champion == 68:
                                rumble_count += 1
                                if 3151 in itemset:
                                        rumble_lian += 1
                                if 3157 in itemset:
                                        rumble_zhon += 1
                                if 3116 in itemset:
                                        rumble_rylai += 1
                                
                        if champion == 96:
                                kog_count += 1
                                if 3285 in itemset:
                                        kog_luden += 1
                                
                        if champion == 8:
                                vlad_count += 1
                                if 3152 in itemset:
                                        vlad_wota += 1
                                
                        if champion == 85:
                                kennen_count += 1
                                if 3157 in itemset: 
                                        kennen_zhon +=1
                                if 3152 in itemset:
                                        kennen_wota +=1
                                
                        if champion == 61:
                                orianna_count += 1
                                if 3174 in itemset:
                                        orianna_athene += 1
                                
                        if champion == 103:
                                ahri_count += 1
                                if 3285 in itemset:
                                        ahri_luden += 1
                                if 3165 in itemset:
                                        ahri_morel += 1
                                if 3089 in itemset:
                                        ahri_raba += 1
                                
                        if champion == 25:
                                morg_count += 1
                                if 3157 in itemset:
                                        morg_zhon += 1
                                
                        if champion == 31:
                                cho_count += 1
                                if 3027 in itemset:
                                        cho_roa += 1
                                
                        if champion == 99:
                                lux_count += 1
                                if 3285 in itemset:
                                        lux_luden += 1
                                
                        if champion == 34:
                                aniv_count += 1
                                if 3027 in itemset:
                                        aniv_roa += 1
                                if 3003 in itemset or 3040 in itemset: #archangels or seraphs
                                        aniv_arch += 1
                                
                        if champion == 30:
                                karth_count += 1
                                if 3027 in itemset:
                                        karth_roa += 1
                                if 3089 in itemset:
                                        karth_raba += 1
                                        
                        if champion == 45:
                                vei_count += 1
                                if 3089 in itemset:
                                        vei_raba += 1
                                
                        if champion == 134:
                                syndra_count += 1
                                if 3285 in itemset:
                                        syndra_luden += 1
                                if 3089 in itemset:
                                        syndra_raba += 1
                                
                        if champion == 7:
                                leb_count += 1
                                if 3165 in itemset:
                                        leb_morel += 1
                                if 3285 in itemset:
                                        leb_luden += 1
                                
                        if champion == 55:
                                kat_count += 1
                                if 3157 in itemset:
                                        kat_zhon += 1
                                if 3285 in itemset:
                                        kat_luden += 1
                                
                        if champion == 38:
                                kass_count += 1
                                if 3027 in itemset:
                                        kass_roa += 1
                                
                        if champion == 74:
                                heim_count += 1
                                if 3157 in itemset:
                                        heim_zhon += 1
                                if 3089 in itemset:
                                        heim_raba += 1
                                
                        if champion == 101:
                                xer_count += 1
                                if 3285 in itemset:
                                        xer_luden += 1
                                
        print((kayle_nashor / kayle_count)*100) #makes it into a percentile
        print((ryze_arch / ryze_count)*100)
        print((azir_nashor / azir_count)*100)
        print((lulu_morello / lulu_count)*100)
        print((viktor_raba / viktor_count)*100)
        print((rumble_lian / rumble_count)*100)
        print((rumble_zhon / rumble_count)*100)
        print((rumble_rylai / rumble_count)*100)
        print((kog_luden / kog_count)*100)
        print((vlad_wota / vlad_count)*100)
        print((kennen_zhon / kennen_count)*100)
        print((orianna_athene / orianna_count)*100)
        print((ahri_luden / ahri_count)*100)
        print((ahri_morel / ahri_count)*100)
        print((ahri_raba / ahri_count)*100)
        print((morg_zhon / morg_count)*100)
        print((cho_roa / cho_count)*100)
        print((lux_luden / lux_count)*100)
        print((aniv_roa / aniv_count)*100)
        print((aniv_arch / aniv_count)*100)
        print((karth_roa / karth_count)*100)
        print((karth_raba / karth_count)*100)
        print((vei_raba / vei_count)*100)
        print((syndra_luden / syndra_count)*100)
        print((syndra_raba / syndra_count)*100)
        print((leb_morel / leb_count)*100)
        print((leb_luden / leb_count)*100)
        print((kat_luden / kat_count)*100)
        print((kat_zhon / kat_count)*100)
        print((kass_roa / kass_count)*100)
        print((heim_zhon / heim_count)*100)
        print((heim_raba / heim_count)*100)
        print((xer_luden / xer_count)*100)