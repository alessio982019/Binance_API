import pandas as pd



df = pd.read_csv("data.csv")

for i in (5,20,50,100):
    df['MA' + str(i)] = df.rolling(window=i)['Close'].mean()

for i, rows in df.iterrows():
    # Check MA average increasing
    try:
        if df['MA5'] > df['MA20'] and df['MA20'] > df['MA50']  and df['MA50'] > df['MA100']:
            df['Up'] = 1
        else:
            df['Up'] = 0
    except:
        df['Up'] = 0
        
    # Check MA intersection between MA5 and MA20
    try:
        if df['MA5'] - df['MA20'] < 0.001 and df['MA5'] - df['MA20'] > 0:
            df['Close_to_zero'] = 1
        else:
            df['Close_to_zero'] = 0
    except:
        df['Close_to_zero'] = 0
        
            
        
        

# print(df)
df.to_csv("MA5.csv")