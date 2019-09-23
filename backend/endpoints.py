from nba_api.stats.endpoints import commonallplayers

def allplayers():
    players = commonallplayers.CommonAllPlayers(0, "00", "2018-19")
    resp = []
    
    data = players.data_sets[0].get_dict()["data"]
    for entry in data:
        resp.append([entry[0], entry[2]])
    print(resp)
    return resp, 200