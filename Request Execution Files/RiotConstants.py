URL = {'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
       'match_by_matchid':'v{version}/match/{matchId}'}
#The first line is the 'base' part of the request url

API_VERSIONS = {'match':'2.2'}
#The latest version of the match API found at the full api reference

REGIONS = {'brazil':'br',
           'europe_nordic_and_east':'eune',
           'europe_west':'euw',
           'korea':'kr',
           'latin_america_north':'lan',
           'latin_america_south':'las',
           'north_america':'na',
           'oceania':'oce',
           'russia':'ru',
           'turkey':'tr',
           'public_beta_environment':'pbe'}
#Note that PBE is not supported by all request types.
#These are all the regions and their appropriate acronyms used for formatting.