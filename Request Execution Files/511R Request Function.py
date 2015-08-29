from RiotAPI import RiotAPI
import json

#These 10 variables are for each region in 5.11 ranked solo, holding 10,000 gameIds in a list each       
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\RANKED_SOLO\BR.json') as data_file:
        BR511R = json.load(data_file) 
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\RANKED_SOLO\EUNE.json') as data_file:
        EUNE511R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\RANKED_SOLO\EUW.json') as data_file:
        EUW511R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\RANKED_SOLO\KR.json') as data_file:
        KR511R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\RANKED_SOLO\LAN.json') as data_file:
        LAN511R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\RANKED_SOLO\LAS.json') as data_file:
        LAS511R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\RANKED_SOLO\NA.json') as data_file:
        NA511R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\RANKED_SOLO\OCE.json') as data_file:
        OCE511R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\RANKED_SOLO\RU.json') as data_file:
        RU511R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\RANKED_SOLO\TR.json') as data_file:
        TR511R = json.load(data_file)

#Ten dictionaries, each to hold 10,000 executed requests of gameIds
BRGames511R = {}
EUNEGames511R = {}
EUWGames511R = {}
KRGames511R = {}
LANGames511R = {}
LASGames511R = {}
NAGames511R = {}
OCEGames511R = {}
RUGames511R = {}
TRGames511R = {}

#Fills all 10 dictionaries with the request responses.
def main():
        api = RiotAPI('API KEY HERE')
        
        for match in BR511R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('br', strmatch)
                                BRGames511R[strmatch] = game
                                print(len(BRGames511R)) #helps keep track of X/10,000 requests completed
                        except: 
                                continue
                        break
                        
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\RANKED_SOLO\BR.json', 'w') as fp:
                json.dump(BRGames511R, fp)
                        
        for match in EUNE511R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('eune', strmatch)
                                EUNEGames511R[strmatch] = game
                                print(len(EUNEGames511R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\RANKED_SOLO\EUNE.json', 'w') as fp:
                json.dump(EUNEGames511R, fp)                
        
        for match in EUW511R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('euw', strmatch)
                                EUWGames511R[strmatch] = game  
                                print(len(EUWGames511R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\RANKED_SOLO\EUW.json', 'w') as fp:
                json.dump(EUWGames511R, fp)                
    
        for match in KR511R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('kr', strmatch)
                                KRGames511R[strmatch] = game
                                print(len(KRGames511R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\RANKED_SOLO\KR.json', 'w') as fp:
                json.dump(KRGames511R, fp)                
                
        for match in LAN511R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('lan', strmatch)
                                LANGames511R[strmatch] = game
                                print(len(LANGames511R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\RANKED_SOLO\LAN.json', 'w') as fp:
                json.dump(LANGames511R, fp)                
                
        for match in LAS511R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('las', strmatch)
                                LASGames511R[strmatch] = game
                                print(len(LASGames511R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\RANKED_SOLO\LAS.json', 'w') as fp:
                json.dump(LASGames511R, fp)                
                
        for match in NA511R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('na', strmatch)
                                NAGames511R[strmatch] = game
                                print(len(NAGames511R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\RANKED_SOLO\NA.json', 'w') as fp:
                json.dump(NAGames511R, fp)                
                
        for match in OCE511R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('oce', strmatch)
                                OCEGames511R[strmatch] = game
                                print(len(OCEGames511R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\RANKED_SOLO\OCE.json', 'w') as fp:
                json.dump(OCEGames511R, fp)                
                
        for match in RU511R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('ru', strmatch)
                                RUGames511R[strmatch] = game
                                print(len(RUGames511R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\RANKED_SOLO\RU.json', 'w') as fp:
                json.dump(RUGames511R, fp)                
                
        for match in TR511R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('tr', strmatch)
                                TRGames511R[strmatch] = game          
                                print(len(TRGames511R))
                        except: 
                                continue
                        break      
        
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\RANKED_SOLO\TR.json', 'w') as fp:
                json.dump(TRGames511R, fp)                
    
if __name__ == "__main__":
        main()