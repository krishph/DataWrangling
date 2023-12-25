import pandas as pd
import os
import glob
cwd = os.getcwd()

mySys = "Mac"
if mySys == "Mac":
    xlsPath = cwd + '/*.xlsx'
    dirSep = '/'
else:
    xlsPath = cwd + '\\*.xlsx'
    dirSep = '\\'

def getFileNames():
    xlsPath = cwd + dirSep + '*.xlsx'
    print(xlsPath)
    xlsPath = glob.glob(xlsPath)
    rcwd = cwd + dirSep
    flist = []
    for xl in xlsPath:
        fname = ((xl.replace(rcwd, '')).replace('Plan','')).replace('.xlsx', '')
        if fname not in flist:
            flist.append(fname)
    print(flist)
    return flist

def mergeRoutes(route):
    
    try:
        fname = cwd + dirSep + route + 'Plan.xlsx'
        df_plan = pd.read_excel(fname)
    except:
        print('Route Plan file Not Found : ', route)
        return

    try:
        fname = cwd + dirSep + route + '.xlsx'
        df_data = pd.read_excel(fname)
    except:
        print('Route file Not Found : ', route)
        return
    
    rdf = df_data.merge(df_plan, how='inner', on='Name')
    srdf = rdf.sort_values(by=['Stop'])
    print(srdf)
    final = cwd + dirSep + "out" + dirSep + route + 'Final.xlsx'
    srdf.to_excel(final, index=False)
        


if __name__ == '__main__':
    routes = getFileNames()
    for route in routes:
        mergeRoutes(route)