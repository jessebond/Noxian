#! /usr/bin/env python3
import psycopg2, time


def writeTotalGames(cur):
    f = open("data/total_games.csv",'w')
    cur.execute("select sub_type as Game_Type, count(*) as Total from games group by sub_type")

    f.write("game_type,total\n")
    for row in cur:
        f.write(str(row[0]) + ',' + str(row[1]) + '\n')
    f.close()

def writeWins(cur):
    f = open("data/total_wins.csv",'w')
    cur.execute("select teamid, count(*) as Total from games where sub_type = 'RANKED_SOLO_5x5' group by teamid")

    f.write("teamid,total\n")
    for row in cur:
        f.write(str(row[0]) + ',' + str(row[1]) + '\n')
    f.close()

def writeChamps(cur):
    f = open("data/total_champs.csv",'w')
    cur.execute("select championid,count(*) as total from games, playerdto where games.gameid = playerdto.gameid and sub_type = 'RANKED_SOLO_5x5' group by championid order by championid")

    f.write("championid,total\n")
    for row in cur:
        f.write(str(row[0]) + ',' + str(row[1]) + '\n')
    f.close()

def writeWinrates(cur):
    f = open("data.total_champs_wins.csv",'w')

    cur.execute("select championid,count(*) as total from games natural join playerdto where sub_type = 'RANKED_SOLO_5x5' and games.teamid = playerdto.teamid group by championid order by championid")

    f.write("championid,wins\n")
    for row in cur:
        f.write(str(row[0]) + ',' + str(row[1]) + '\n')
    f.close()



if __name__ == "__main__":
    conn_string = "host='localhost' dbname='league' user='jbond' password=''"
    print("Connecting to database\n->%s" % (conn_string))
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    
    writeTotalGames(cur)
    writeWins(cur)
    writeChamps(cur)
    writeWinrates(cur)

    cur.close()
    conn.close()
            
