import pip     ## only needed on first run
pip.main(['install','pandas'])    ## only needed on first run
import sys
import pandas as ps

def read_dataframe(file_path):
    print("\nReading file: %s" %file_path)
    df = ps.read_csv(file_path, sep=" ", names=["rcvd","0","1","timestamp","val","4","5"])
    df.drop(df.columns[[0,1,2,5,6]], axis=1,inplace=True)
    df["val"] = ps.to_numeric(df["val"], errors='coerce')
    df.timestamp = ps.to_numeric(df.timestamp, errors='coerce').round(1)
    print("total size: ", df.size)
    df = df[ps.notnull(df['timestamp'])]
    print("size after drop extra lines: ", df.size)
    df.drop_duplicates(subset=['timestamp'], keep=False)
    print("size after drop duplicates: ", df.size)
    return df


def merge_dataframe(df_min, df_max):
    print("\nProcessing dataframes ...")
    df_merge = ps.merge(df_min, df_max, on='timestamp', how='outer', suffixes=('_min', '_max'))
    df_merge = df_merge[ps.notnull(df_merge['val_min'])]
    df_merge = df_merge[ps.notnull(df_merge['val_max'])]
    df_merge['diff'] = (df_merge['val_max'] - df_merge['val_min']).round(3)
    df_merge['abs'] = abs(df_merge['diff'])
    return df_merge


def save_dataframe(df, file_path):
    print("\nSaving results to file: ", file_path)
    df.to_csv(file_path, sep='\t')
    print("File saved ..")
    return


if __name__ == "__main__":

    print("\nRunning script: ", sys.argv[0])
    if len(sys.argv) != 3:
        print("Please pass 2 arguments only")
        exit(100)

    df_min = read_dataframe(sys.argv[1])
    df_max = read_dataframe(sys.argv[2])
    df_final = merge_dataframe(df_min, df_max)

    output_file = sys.argv[1] + "_output"
    save_dataframe(df_final, output_file)
