import pandas as pd

fpath = './Hari_NH_List.xlsx'

def getdf() -> pd.DataFrame:
    df = pd.read_excel(fpath)
    return df

def removeSlash(df: pd.DataFrame) -> pd.DataFrame:
    for index, row in df.iterrows():
        print(df.at[index, 'Comments'])
        comment = str(df.at[index, 'Comments']).rstrip()
        if comment.endswith('/'):
            comment = comment[:-1]
            df.at[index, 'Comments'] = comment
    return df

if __name__ == '__main__':
    df = getdf()
    print(df.dtypes)
    df = removeSlash(df)
    group2List = ['Concord', 'Hooksett', 'Epping', 'Lee', 'DURHAM', 'MADBURY', 'Dover', 'Somersworth', 'Portsmouth']
    df1 = df.loc[df['City'].isin(group2List)]
    df2 = df.loc[~df['City'].isin(group2List)]
    df1.to_excel('./NH1.xlsx')
    df2.to_excel('./NH2.xlsx')
    print(df)