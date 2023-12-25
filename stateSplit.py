import pandas as pd
from datetime import datetime


fs = './mainSheet.xlsx'
outfs = "./out.xlsx"
startTime = datetime.now()
def getData() -> pd.DataFrame:
    df = pd.read_excel(fs)
    df.sort_values(by=["State"], inplace=True)
    df["State"].apply(str)
    df.dropna(subset=["State"], inplace=True)
    df.dropna(subset=["Verified Whatsapp Number"], inplace=True)
    df["State"].apply(lambda x: str(x).upper())
    df["Verified Whatsapp Number"].apply(str)
    return df

def getStates(df) -> set:
    df = getData()
    stateList =  df["State"].unique().tolist()
    stateSet = set()
    for state in stateList:
        # print("state is ", state, " and type is ", type(state))
        if len(state) == 2:
            stateSet.add(state.upper())
    return stateSet

def writeStateData(df, state):
    dfr = df[df["State"] == state]
    print("Number of Rows in the state : ", state, " is : ", dfr.shape[0])
    if dfr.shape[0] > 0:
        outfile = "./out/" + state + ".xlsx"
        dfr.to_excel(outfile, index=False)
    return

if __name__ == '__main__':
    df = getData()
    stateSet = getStates(df)
    print(stateSet)
    with pd.ExcelWriter("path to file\filename.xlsx") as writer:
        df.to_excel(writer, index=False)
    for state in stateSet:
        writeStateData(df, state)
    endTime = datetime.now()
    totalTime = endTime - startTime
    print("Start Time is : ", startTime)
    print("End Time is : ", endTime)
    print("Total Time taken is : ", totalTime)