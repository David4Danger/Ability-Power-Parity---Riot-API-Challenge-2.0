from RiotAPI import RiotAPI
import json

#These 10 variables are for each region in 5.14 ranked solo, holding 10,000 gameIds in a list each     
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\RANKED_SOLO\BR.json') as data_file:
        BR514R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\RANKED_SOLO\EUNE.json') as data_file:
        EUNE514R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\RANKED_SOLO\EUW.json') as data_file:
        EUW514R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\RANKED_SOLO\KR.json') as data_file:
        KR514R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\RANKED_SOLO\LAN.json') as data_file:
        LAN514R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\RANKED_SOLO\LAS.json') as data_file:
        LAS514R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\RANKED_SOLO\NA.json') as data_file:
        NA514R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\RANKED_SOLO\OCE.json') as data_file:
        OCE514R = json.load(data_file)
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\RANKED_SOLO\RU.json') as data_file:
        RU514R = json.load(data_file)   
with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Dataset\5.14\RANKED_SOLO\TR.json') as data_file:
        TR514R = json.load(data_file)

#Ten dictionaries, each to hold 10,000 executed requests of gameIds
BRGames514R = {}
EUNEGames514R = {}
EUWGames514R = {}
KRGames514R = {}
LANGames514R = {}
LASGames514R = {}
NAGames514R = {}
OCEGames514R = {}
RUGames514R = {}
TRGames514R = {}

#Fills all 10 dictionaries with the request responses.
def main():
        api = RiotAPI('API KEY HERE')
        
        for match in BR514R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('br', strmatch)
                                BRGames514R[strmatch] = game         
                                print(len(BRGames514R)) #helps keep track of X/10,000 requests completed
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\RANKED_SOLO\BR.json', 'w') as fp:
                json.dump(BRGames514R, fp)                
        
        for match in EUNE514R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('eune', strmatch)
                                EUNEGames514R[strmatch] = game
                                print(len(EUNEGames514R))
                        except:
                                continue
                        break
        
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\RANKED_SOLO\EUNE.json', 'w') as fp:
                json.dump(EUNEGames514R, fp)                
        
        for match in EUW514R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('euw', strmatch)
                                EUWGames514R[strmatch] = game        
                                print(len(EUWGames514R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\RANKED_SOLO\EUW.json', 'w') as fp:
                json.dump(EUWGames514R, fp)                
    
        for match in KR514R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('kr', strmatch)
                                KRGames514R[strmatch] = game
                                print(len(KRGames514R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\RANKED_SOLO\KR.json', 'w') as fp:
                json.dump(KRGames514R, fp)                
                
        for match in LAN514R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('lan', strmatch)
                                LANGames514R[strmatch] = game
                                print(len(LANGames514R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\RANKED_SOLO\LAN.json', 'w') as fp:
                json.dump(LANGames514R, fp)                
                
        for match in LAS514R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('las', strmatch)
                                LASGames514R[strmatch] = game       
                                print(len(LASGames514R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\RANKED_SOLO\LAS.json', 'w') as fp:
                json.dump(LASGames514R, fp)                
                                
        for match in NA514R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('na', strmatch)
                                NAGames514R[strmatch] = game
                                print(len(NAGames514R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\RANKED_SOLO\NA.json', 'w') as fp:
                json.dump(NAGames514R, fp)                
                
        for match in OCE514R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('oce', strmatch)
                                OCEGames514R[strmatch] = game       
                                print(len(OCEGames514R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\RANKED_SOLO\OCE.json', 'w') as fp:
                json.dump(OCEGames514R, fp)                
                
        for match in RU514R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('ru', strmatch)
                                RUGames514R[strmatch] = game   
                                print(len(RUGames514R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\RANKED_SOLO\RU.json', 'w') as fp:
                json.dump(RUGames514R, fp)                
                
        for match in TR514R:
                while True:
                        try:
                                strmatch = str(match)
                                game = api.get_match_by_matchid('tr', strmatch)
                                TRGames514R[strmatch] = game        
                                print(len(TRGames514R))
                        except:
                                continue
                        break
                
        with open(r'E:\Python Programs\API Challenge Aug 2015\API Challenge Executed Requests\5.14\RANKED_SOLO\TR.json', 'w') as fp:
                json.dump(TRGames514R, fp)                
                           
if __name__ == "__main__":
        main()