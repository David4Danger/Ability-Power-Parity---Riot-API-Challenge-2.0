import requests
import RiotConstants as RC
        
class RiotAPI(object):
    def __init__(self, api_key, defaultregion=RC.REGIONS['north_america']): #if no region provided, NA is default
        self.api_key = api_key
        self.defaultregion = defaultregion
        
    def _request(self, api_url, region, params={}):
        if region is None:
            region = self.defaultregion
        
        entries = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in entries:
                entries[key] = value
        
        response = requests.get(
            RC.URL['base'].format(
                proxy = region,
                region = region,
                url = api_url),
            params = entries)
        
        return response.json()

    def get_match_by_matchid(self, region, matchid): #our request wrapper function for match by matchID (matchIDs provided)
        api_url = RC.URL['match_by_matchid'].format(
            version = RC.API_VERSIONS['match'],
            matchId = matchid)
        return self._request(api_url, region)