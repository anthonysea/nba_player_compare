from nba_api.stats.endpoints import commonallplayers
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats

def allplayers():
    players = commonallplayers.CommonAllPlayers(0, "00", "2018-19")
    resp = []

    data = players.data_sets[0].get_dict()["data"]
    for entry in data:
        resp.append({
            "name": entry[2],
            "id": entry[0]
        })
    return resp, 200

def playerinfo(playerid):
    player = commonplayerinfo.CommonPlayerInfo(playerid, "00")
    data = player.get_dict()
    resp = data['resultSets'][0]
    return resp, 200

def careerstats(playerid, per_mode="PerGame"):
    resp = playercareerstats.PlayerCareerStats(per_mode36=per_mode, player_id=playerid, league_id_nullable="00").get_dict()["resultSets"]
    return resp, 200

