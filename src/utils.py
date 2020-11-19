import pandas as pd

def explore_data(fname, show_df=False):
    ftype = fname.split('.')[-1]
    
    if ftype == "csv" or ftype == "tsv":
        sample_df = pd.read_csv(fname, nrows=10)
    elif ftype == "json":
        sample_df = pd.read_json(fname, nrows=10, lines=True)
    else:
        raise Exception()
        
    print("{: <35}{: <15}{}".format("Column name", "Type", "Sample"))
    print("{:-<35}{:-<15}{:-<10}".format("", "", ""))
    for i, j, k in zip(sample_df.keys(), sample_df.dtypes, sample_df.iloc[9].values):
        if isinstance(k, str):
            print("{:-<35}{:-<15}{:.48}".format(i, str(j), k))
        else:
            print("{:-<35}{:-<15}{:}".format(i, str(j), k))
    if show_df:
        display(sample_df)