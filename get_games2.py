#! /usr/bin/env python3
import psycopg2, sys, pprint, time
from pyriot.wrapper import PyRiot, NORTH_AMERICA

key = ''
region = NORTH_AMERICA
riot = PyRiot(key)

def getSummonerByName(name, reg='na'):
    return riot.summoner_get_by_name(reg, name)

def getSummonerById(id, reg='na'):
    return riot.summoner_get_by_id(reg, id)

def getGames(id, reg='na'):
    return riot.recent_games(region, id)

def printWins(games):
    for game in games:
        won = getWinningTeam(game.statistics, int(game.team_id))
        
        print("Game ID %s: %d wins" % (game.game_id, won))
        print("On team %d" % game.team_id)

def getTeam(t):
    if (t == 100):
        return "Blue"
    else:
        return "Purple"

def getWinningTeam(stats, onTeam):
    won = ''
    for st in stats:
        if(st.id == "win"):
            won = st.value
            #print("\n%s:%s:%s" %(onTeam,st.id,st.value))
    
    if(str(won) == 'True'):
        #print("%d wins" % onTeam)
        return int(onTeam)
    else:
        if(onTeam == 100):
            #print("200 zwins")
            return 200
        else:
            #print("100 zwins")
            return 100
        

def insertSummoners(games, cur, i):
    for game in games:
        for player in game.fellow_players:
            if(exists("summoners","id",player.summoner_id,cur) is False):
                time.sleep(1)
                s = getSummonerById(player.summoner_id)
                print("insert into summoners values (%s,'%s',%s,%d,%s)" %
                      (s.id,s.name,s.profile_icon_id,i,s.summoner_level))

                cur.execute("insert into summoners values (%s,%s,%s,%s,%s)",
                            (s.id,s.name,s.profile_icon_id,i,s.summoner_level))

def insertSummonersLess(games, cur, i):
    for game in games:
        for player in game.fellow_players:
            if(exists("summoners","id",player.summoner_id,cur) is False):
                #print("insert into summoners values (%d,'%s',%s,%s,%s)" %
                #     (player.summoner_id,None,None,None,None))
                cur.execute("insert into summoners values (%s,%s,%s,%s,%s)",
                            (player.summoner_id,None,None,None,None))

            
def exists(a,b,c, cur):
    q = "select * from %s where %s = %s" % (a,b,c)
    cur.execute(q)
    return cur.fetchone() is not None

def insertGames(games, id, cur):
    for game in games:
        if(exists("games","gameid",game.game_id, cur) is False):
            #print("insert into games values(%s,%s,%d,%s,%s,%s)"%
            #      (game.create_date, game.game_id,
            #       getWinningTeam(game.statistics,game.team_id),
            #       game.game_mode, game.game_type, game.sub_type))
            cur.execute("insert into games values(%s,%s,%s,%s,%s,%s)",
                        (game.create_date, game.game_id,
                         getWinningTeam(game.statistics,game.team_id),
                         game.game_mode, game.game_type, game.sub_type))
            
            #print("insert into playerdto values(%d,%d,%d,%d)"%
            #      (game.champion_id, id, game.team_id, game.game_id))
            cur.execute("insert into playerdto values(%s,%s,%s,%s)",
                        (game.champion_id, id, game.team_id, game.game_id))
            
            for player in game.fellow_players:
            #    print("insert into playerdto values(%d,%d,%d,%d)"%
            #          (player.champion_id, player.summoner_id,
            #           player.team_id, game.game_id))
                cur.execute("insert into playerdto values(%s,%s,%s,%s)",
                            (player.champion_id, player.summoner_id, 
                             player.team_id, game.game_id))
                
def updateTimeSum(id, val, cur):
    cur.execute("update summoners set revisiondate = %s where id = %s", (val,id))


if __name__ == "__main__":
    conn_string = "host='localhost' dbname='league' user='jbond' password=''"
    print("Connecting to database\n->%s" % (conn_string))
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur2 = conn.cursor()

    #s = getSummonerByName('diolex')

    
    cur.execute("select count(*) from summoners where revisiondate is Null or revisiondate = -1")
    total = cur.fetchone()[0]
    print("total = %d" % total)
    count = 0
    cur.execute("select id from summoners where revisiondate is Null or revisiondate = -1")
    real_start = time.clock()
    start = time.clock()
    for row in cur:
        g = getGames(row[0])
        insertSummonersLess(g, cur2, 1)
        insertGames(g, row[0], cur2)
        updateTimeSum(row[0], 1, cur2)
        conn.commit()
        print("\nCommiting: %.2f%% done." % (100*count/total))
        end = time.clock()
        time.sleep(1 - (end - start))
        print("Elapsed time: %.2fs" % (end - real_start + count))
        start = end
        count +=1
    #printWins(g)
    

    cur.close()
    conn.close()
