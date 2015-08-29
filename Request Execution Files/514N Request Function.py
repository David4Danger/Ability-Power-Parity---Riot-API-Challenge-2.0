from RiotAPI import RiotAPI
import json

#These 10 variables are for each region in 5.14 normal 5x5, holding 10,000 gameIds in a list each
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\NORMAL_5X5\BR.json') as data_file:
        BR514N = json.load(data_file) 
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\NORMAL_5X5\EUNE.json') as data_file:
        EUNE514N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\NORMAL_5X5\EUW.json') as data_file:
        EUW514N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\NORMAL_5X5\KR.json') as data_file:
        KR514N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\NORMAL_5X5\LAN.json') as data_file:
        LAN514N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\NORMAL_5X5\LAS.json') as data_file:
        LAS514N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\NORMAL_5X5\NA.json') as data_file:
        NA514N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\NORMAL_5X5\OCE.json') as data_file:
        OCE514N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\NORMAL_5X5\RU.json') as data_file:
        RU514N = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\NORMAL_5X5\TR.json') as data_file:
        TR514N = json.load(data_file)

#Ten dictionaries, each to hold 10,000 executed requests of gameIds
BRGames514N = {}
EUNEGames514N = {}
EUWGames514N = {}
KRGames514N = {}
LANGames514N = {}
LASGames514N = {}
NAGames514N = {}
OCEGames514N = {}
RUGames514N = {}
TRGames514N = {}

#Fills all 10 dictionaries with the request responses.
def main():
        api = RiotAPI('API KEY HERE')

        for match in BR514N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('br', strmatch)
                                BRGames514N[strmatch] = game          
                                print(len(BRGames514N)) #helps keep track of X/10,000 requests completed
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\NORMAL_5X5\BR.json', 'w') as fp:
                json.dump(BRGames514N, fp)                
        
        for match in EUNE514N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('eune', strmatch)
                                EUNEGames514N[strmatch] = game
                                print(len(EUNEGames514N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\NORMAL_5X5\EUNE.json', 'w') as fp:
                json.dump(EUNEGames514N, fp)                
        
        for match in EUW514N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('euw', strmatch)
                                EUWGames514N[strmatch] = game 
                                print(len(EUWGames514N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\NORMAL_5X5\EUW.json', 'w') as fp:
                json.dump(EUWGames514N, fp)                
    
        for match in KR514N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('kr', strmatch)
                                KRGames514N[strmatch] = game
                                print(len(KRGames514N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\NORMAL_5X5\KR.json', 'w') as fp:
                json.dump(KRGames514N, fp)                 
                
        for match in LAN514N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('lan', strmatch)
                                LANGames514N[strmatch] = game
                                print(len(LANGames514N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\NORMAL_5X5\LAN.json', 'w') as fp:
                json.dump(LANGames514N, fp)                 
                
        for match in LAS514N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('las', strmatch)
                                LASGames514N[strmatch] = game       
                                print(len(LASGames514N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\NORMAL_5X5\LAS.json', 'w') as fp:
                json.dump(LASGames514N, fp)                 
                
        for match in NA514N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('na', strmatch)
                                NAGames514N[strmatch] = game
                                print(len(NAGames514N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\NORMAL_5X5\NA.json', 'w') as fp:
                json.dump(NAGames514N, fp)                 
                
        for match in OCE514N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('oce', strmatch)
                                OCEGames514N[strmatch] = game   
                                print(len(OCEGames514N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\NORMAL_5X5\OCE.json', 'w') as fp:
                json.dump(OCEGames514N, fp)                 
                
        for match in RU514N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('ru', strmatch)
                                RUGames514N[strmatch] = game   
                                print(len(RUGames514N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\NORMAL_5X5\RU.json', 'w') as fp:
                json.dump(RUGames514N, fp)                 
                
        for match in TR514N:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('tr', strmatch)
                                TRGames514N[strmatch] = game         
                                print(len(TRGames514N))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\NORMAL_5X5\TR.json', 'w') as fp:
                json.dump(TRGames514N, fp)                 
    
if __name__ == "__main__":
        main()