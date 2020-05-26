'''
Let's take a look at the BratS csv.
'''
import pandas as pd

path = "/home/diedre/Dropbox/bigdata/brats/2020/train/survival_info.csv"
path2 = "/home/diedre/Dropbox/bigdata/brats/2020/train/name_mapping.csv"

brats_survival = pd.read_csv(path)

print(brats_survival.head())

subject_names = brats_survival["Brats20ID"].to_numpy()

survival = brats_survival["Survival_days"].to_numpy()

ages = brats_survival["Age"].to_numpy()

print(subject_names, survival, ages)

grade_csv = pd.read_csv(path2)

for index, row in brats_survival.iterrows():
    print(row["Brats20ID"], row["Age"], row["Survival_days"])
    print(grade_csv.loc[grade_csv['BraTS_2020_subject_ID'] == row['Brats20ID']]['Grade'].values[0])