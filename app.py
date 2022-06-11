class IPLDet:

    iplTeams = {}

    team_names= ("GT", "LSG", "RR", "DC", "RCB", "KKR", "PBKS", "SRH", "CSK", "MI")
    nrr = (0.391, 0.251, 0.304, 0.255, 0.323, 0.146, 0.043, 0.230,0.206,0.577)
    pts= (20, 18, 16, 14, 14, 12, 12, 12, 8, 6)
    last_5_res = ((1,1,0,0,1),(1,0,0,1,1),(1,0,1,0,0),(1,1,0,1,0),(0,1,1,0,0),(0,1,1,0,0),(0,1,0,1,1),(1,0,0,0,0),(0,0,1,0,1),(0,1,0,1,1))

    det = []
    for i in range(len(team_names)):
        det.append([team_names[i], nrr[i], pts[i], last_5_res[i]])

    iplTeams = {"Team" : team_names, "NRR": nrr, "pts": pts, "Last 5": last_5_res}

    mRes = iplTeams.get('Last 5')

    searchKey, nVals = None, None


    def findTeams(searchKey, nVals, mRes=mRes):
        fLen = len(mRes[0])
        ind = []
        searchKey = searchKey
        nVals = nVals

        for vInd in range(len(mRes)):
            ct = 0
            prevVal = mRes[vInd][0]

            for i in range(1,fLen):
                if mRes[vInd][i] == searchKey and prevVal == searchKey:
                    ct += 1
                else:
                    ct = 0

                prevVal = mRes[vInd][i]

                if ct == (nVals-1):
                    ind.append(vInd)
                    break
        return ind
    
    def findAvg(res, iplTeams= iplTeams):

        rLen = len(res)
        sum = 0
        avgPts = None

        if rLen > 0:
            for val in res:
                sum += iplTeams.get('pts')[val]
            avgPts = sum/rLen
        else:
            avgPts = 0.0

        return avgPts
    
    if __name__ == "__main__":
        key = input("Enter Loss/Win : ")
        key = key.lower()
        if key == "loss":
            searchKey = 0
        elif key == "win":
            searchKey = 1
        else:
            exit

        nVals = int(input(f'Enter no of {key} : '))

        res = findTeams(searchKey, nVals)
        avgPts = findAvg(res)

        for val in res:
            print((iplTeams.get('Team')[val]), iplTeams.get('pts')[val], sep=" --- ")
        
        print(f'Average Team points with {nVals} of {key} : {avgPts}')





    

