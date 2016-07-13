#!/usr/bin/env python3
import os,subprocess,time

pths=['/whatever/path/','/pth2'] #Enter the paths for directories to set log management for
mx = 25 #for 25 MB i.e. Max size of the logs
nm = 7 # Number of Log archives to maintain


def fetchLogs():
    logs = []
    logsc = []
    for pth in pths:
        for root, dirs, files in os.walk(pth):
            for file in files:
                if file.endswith(".log"):
                    logs.append(os.path.join(root, file))
    for l in logs:
        if os.path.getsize(l) > (mx/(1024*1024)):
            logsc.append(l)
    return logsc

def archiveLogs():
    for l in logsc:
        ind = l[::-1].index("/")
        fPath = l[:len(l)-ind]
        fil = l[len(l)-ind:]
        cnt = 0
        filist = []
        for i in os.listdir(fPath):
            if os.path.isfile(os.path.join(fPath,i)) and fil in i and ".gz" in i:
                filist.append(os.path.join(fPath,i))
                cnt += 1
        if cnt > nm:
            os.remove(sorted(filist,key=os.path.getmtime)[0])
        os.chdir(fPath)
        subprocess.call(["gzip --suffix " + '.'.join([str(i) for i in time.localtime(time.time())[1:5]]) + ".gz --best " + fil + "; echo > " + fil],shell=True)


logsc = list(set(fetchLogs()))
archiveLogs()
