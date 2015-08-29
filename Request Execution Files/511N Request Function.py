from RiotAPI import RiotAPI
import json

#These 10 variables are for each region in 5.11 normal 5x5, holding 10,000 gameIds in a list each
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\NORMAL_5X5\BR.json') as data_file:
        BR511N = json.load(data_file) 
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\NORMAL_5X5\EUNE.json') as data_file:
        EUNE511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\NORMAL_5X5\EUW.json') as data_file:
        EUW511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\NORMAL_5X5\KR.json') as data_file:
        KR511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\NORMAL_5X5\LAN.json') as data_file:
        LAN511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\NORMAL_5X5\LAS.json') as data_file:
        LAS511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\NORMAL_5X5\NA.json') as data_file:
        NA511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\NORMAL_5X5\OCE.json') as data_file:
        OCE511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\NORMAL_5X5\RU.json') as data_file:
        RU511N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.11\NORMAL_5X5\TR.json') as data_file:
        TR511N = json.load(data_file)
        
#Ten dictionaries, each to hold 10,000 executed requests of gameIds, initialized to be empty
BRGames511N = {}
EUNEGames511N = {}
EUWGames511N = {}
KRGames511N = {}
LANGames511N = {}
LASGames511N = {}
NAGames511N = {}
OCEGames511N = {}
RUGames511N = {}
TRGames511N = {}

#Fills all 10 dictionaries with the request responses.
def main():
        api = RiotAPI('API KEY HERE')
        
        for match in BR511N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('br', strmatch)
                                BRGames511N[strmatch] = game
                                print(len(BRGames511N)) #helps keep track of X/10,000 requests completed
                        except:
                                continue
                        break
        
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\BR.json', 'w') as fp:
                json.dump(BRGames511N, fp)
        
        for match in EUNE511N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('eune', strmatch)
                                EUNEGames511N[strmatch] = game
                                print(len(EUNEGames511N))
                        except:
                                continue
                        break
        
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\EUNE.json', 'w') as fp:
                json.dump(EUNEGames511N, fp)                
        
        for match in EUW511N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('euw', strmatch)
                                EUWGames511N[strmatch] = game      
                                print(len(EUWGames511N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\EUW.json', 'w') as fp:
                json.dump(EUWGames511N, fp)        
    
        for match in KR511N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('kr', strmatch)
                                KRGames511N[strmatch] = game
                                print(len(KRGames511N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\KR.json', 'w') as fp:
                json.dump(KRGames511N, fp)        
                
        for match in LAN511N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('lan', strmatch)
                                LANGames511N[strmatch] = game
                                print(len(LANGames511N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\LAN.json', 'w') as fp:
                json.dump(LANGames511N, fp)                
                
        for match in LAS511N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('las', strmatch)
                                LASGames511N[strmatch] = game       
                                print(len(LASGames511N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\LAS.json', 'w') as fp:
                json.dump(LASGames511N, fp)                
                
        for match in NA511N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('na', strmatch)
                                NAGames511N[strmatch] = game
                                print(len(NAGames511N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\NA.json', 'w') as fp:
                json.dump(NAGames511N, fp)                
                
        for match in OCE511N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('oce', strmatch)
                                OCEGames511N[strmatch] = game        
                                print(len(OCEGames511N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\OCE.json', 'w') as fp:
                json.dump(OCEGames511N, fp)                
                
        for match in RU511N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('ru', strmatch)
                                RUGames511N[strmatch] = game   
                                print(len(RUGames511N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\RU.json', 'w') as fp:
                json.dump(RUGames511N, fp)                
                
        for match in TR511N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('tr', strmatch)
                                TRGames511N[strmatch] = game
                                print(len(TRGames511N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.11\NORMAL_5X5\TR.json', 'w') as fp:
                json.dump(TRGames511N, fp)                
    
if __name__ == "__main__":
        main()