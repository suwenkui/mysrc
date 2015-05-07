import sys
import os
from ua_parser import user_agent_parser as uap

def sortbyvalue(d):
    items = d.items()
    #print items
    backitems = [[v[1],v[0]] for v in items]
    backitems.sort()
    return [backitems[i][1] for i in range(0,len(backitems))]

def readfiletomap(path):
    trace = []
    uas = {}
    browsers = {}
    with open(path) as lines:
        for line in lines:
            lineData = line.split('\t')
            ip = lineData[0]
            ad = lineData[1]
            url = lineData[2]
            ref = lineData[3]
            ua = lineData[4]
            ts = lineData[5]

            trace.append(lineData)
            parsrua = uap.Parse(ua)
            browser = parsrua['user_agent']['family']
            print parsrua['user_agent']['family'],parsrua['os']['family'],parsrua['device']['family'],parsrua['string']
            if browsers.has_key(browser):
                browsers[browser] += 1
            else:
                browsers[browser] = 1

            if uas.has_key(ua):
                uas[ua] += 1
            else:
                uas[ua] = 1


    for (k,v) in browsers.items():
        print k,v

    sorteduas = sortbyvalue(uas)
    #print len(uas)
    for tua in sorteduas:
        for i in range(len(trace)):
            if tua == trace[i][4]:
                #print trace[i][1]
                pass

if __name__ == '__main__':
    filePath = 'data/car.log'
    readfiletomap(filePath)