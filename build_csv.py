#! /usr/bin/env python3
import psycopg2, time


def exists(a,b,c, cur):
    q = "select * from %s where %s = %s" % (a,b,c)
    cur.execute(q)
    return cur.fetchone() is not None

def writeLine(g,w, cur, f):
    dict = {}
    cur.execute("select championid, teamid from playerdto where gameid = %s order by championid", (g,))

    count = 0
    ln = str(g)+':'

    for row in cur:
        #print("row: %d=%d:%d" % (len(row),row[0],row[1]))
        dict[getChampId(int(row[0]))] = int(row[1])
        count += 1
    #print("count : " + str(count))
    for key in sorted(dict.keys()):
        ln += str(key) + ':'
    #print(ln)
    count = 0
    line = str(w) + ","
    for i in range(1,119):
        if i in dict.keys():
            count += 1
            line += str(int((dict[i]/100)*2-3)) + ","
        else:
            line += "0,"
    line = line[:-1] + "\n"
    f.write(line)
    if(count != len(dict.keys())):
        print("gid %d :count %d:%d " % (g,count,len(dict.keys())))

def getChampId(id):
    count = 0
    if(id <= 45):
        return id
    count += 1
    if(id ==  48 ):
        return 45 + count
    count += 1
    if(id ==  50 ):
        return 45 + count
    count += 1
    if(id ==  51 ):
        return 45 + count
    count += 1
    if(id ==  53 ):
        return 45 + count
    count += 1
    if(id ==  54 ):
        return 45 + count
    count += 1
    if(id ==  55 ):
        return 45 + count
    count += 1
    if(id ==  56 ):
        return 45 + count
    count += 1
    if(id ==  57 ):
        return 45 + count
    count += 1
    if(id ==  58 ):
        return 45 + count
    count += 1
    if(id ==  59 ):
        return 45 + count
    count += 1
    if(id ==  60 ):
        return 45 + count
    count += 1
    if(id ==  61 ):
        return 45 + count
    count += 1
    if(id ==  62 ):
        return 45 + count
    count += 1
    if(id ==  63 ):
        return 45 + count
    count += 1
    if(id ==  64 ):
        return 45 + count
    count += 1
    if(id ==  67 ):
        return 45 + count
    count += 1
    if(id ==  68 ):
        return 45 + count
    count += 1
    if(id ==  69 ):
        return 45 + count
    count += 1
    if(id ==  72 ):
        return 45 + count
    count += 1
    if(id ==  74 ):
        return 45 + count
    count += 1
    if(id ==  75 ):
        return 45 + count
    count += 1
    if(id ==  76 ):
        return 45 + count
    count += 1
    if(id ==  77 ):
        return 45 + count
    count += 1
    if(id ==  78 ):
        return 45 + count
    count += 1
    if(id ==  79 ):
        return 45 + count
    count += 1
    if(id ==  80 ):
        return 45 + count
    count += 1
    if(id ==  81 ):
        return 45 + count
    count += 1
    if(id ==  82 ):
        return 45 + count
    count += 1
    if(id ==  83 ):
        return 45 + count
    count += 1
    if(id ==  84 ):
        return 45 + count
    count += 1
    if(id ==  85 ):
        return 45 + count
    count += 1
    if(id ==  86 ):
        return 45 + count
    count += 1
    if(id ==  89 ):
        return 45 + count
    count += 1
    if(id ==  90 ):
        return 45 + count
    count += 1
    if(id ==  91 ):
        return 45 + count
    count += 1
    if(id ==  92 ):
        return 45 + count
    count += 1
    if(id ==  96 ):
        return 45 + count
    count += 1
    if(id ==  98 ):
        return 45 + count
    count += 1
    if(id ==  99 ):
        return 45 + count
    count += 1
    if(id == 101 ):
        return 45 + count
    count += 1
    if(id == 102 ):
        return 45 + count
    count += 1
    if(id == 103 ):
        return 45 + count
    count += 1
    if(id == 104 ):
        return 45 + count
    count += 1
    if(id == 105 ):
        return 45 + count
    count += 1
    if(id == 106 ):
        return 45 + count
    count += 1
    if(id == 107 ):
        return 45 + count
    count += 1
    if(id == 110 ):
        return 45 + count
    count += 1
    if(id == 111 ):
        return 45 + count
    count += 1
    if(id == 112 ):
        return 45 + count
    count += 1
    if(id == 113 ):
        return 45 + count
    count += 1
    if(id == 114 ):
        return 45 + count
    count += 1
    if(id == 115 ):
        return 45 + count
    count += 1
    if(id == 117 ):
        return 45 + count
    count += 1
    if(id == 119 ):
        return 45 + count
    count += 1
    if(id == 120 ):
        return 45 + count
    count += 1
    if(id == 121 ):
        return 45 + count
    count += 1
    if(id == 122 ):
        return 45 + count
    count += 1
    if(id == 126 ):
        return 45 + count
    count += 1
    if(id == 127 ):
        return 45 + count
    count += 1
    if(id == 131 ):
        return 45 + count
    count += 1
    if(id == 133 ):
        return 45 + count
    count += 1
    if(id == 134 ):
        return 45 + count
    count += 1
    if(id == 143 ):
        return 45 + count
    count += 1
    if(id == 154 ):
        return 45 + count
    count += 1
    if(id == 157 ):
        return 45 + count
    count += 1
    if(id == 161 ):
        return 45 + count
    count += 1
    if(id == 222 ):
        return 45 + count
    count += 1
    if(id == 236 ):
        return 45 + count
    count += 1
    if(id == 238 ):
        return 45 + count
    count += 1
    if(id == 254 ):
        return 45 + count
    count += 1
    if(id == 266 ):
        return 45 + count
    count += 1
    if(id == 267 ):
        return 45 + count
    count += 1
    if(id == 412 ):
        return 45 + count
    count += 1
    
if __name__ == "__main__":
    conn_string = "host='localhost' dbname='league' user='jbond' password=''"
    print("Connecting to database\n->%s" % (conn_string))
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur2 = conn.cursor()
    
    
    cur.execute("select count(*) from games where sub_type = 'RANKED_SOLO_5x5'")
    total = cur.fetchone()[0]
    cur.execute("select gameid,teamid from games where sub_type = 'RANKED_SOLO_5x5' order by gameid")
    print("total = %d" % total)
    count = 0
    fcount = 1
    f = open("data/data" + str(fcount) + ".csv", "wt")
    for row in cur:
        writeLine(row[0],row[1], cur2, f)
        if(count % 100 == 0):
            print("%.2f%% done. %d/%d" % (100*count/total, count, total))
        if(count > 0 and count % 5000 == 0):
            print("Saving file data%d.csv" % fcount)
            f.close()
            fcount += 1
            f = open("data/data" + str(fcount) + ".csv", "wt")
        count += 1
        #if(count > 20):
        #    break;
        
            
    f.close()
    cur.close()
    cur2.close()
    conn.close()
            
