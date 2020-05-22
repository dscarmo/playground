'''
Let's take a look at the BratS csv.
'''
import pandas as pd

path = "/home/diedre/Dropbox/bigdata/brats/2020/train/survival_info.csv"

brats_survival = pd.read_csv(path)

print(brats_survival.head())

subject_names = brats_survival["Brats20ID"].to_numpy()

survival = brats_survival["Survival_days"].to_numpy()

ages = brats_survival["Age"].to_numpy()

print(subject_names, survival, ages)
