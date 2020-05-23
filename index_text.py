'''
How to index a text, fast?
'''
import h5py
import os

input_size = 0
with open("data/text.txt", 'r') as txt:
    for line in txt:
        input_size += 1

with open("data/text.txt", 'r') as txt:
    with h5py.File("data/h5text.hdf5", 'w') as h5txt:
        grp = h5txt.create_group('text')
        dataset = grp.create_dataset("lines", (input_size,), dtype=h5py.string_dtype())
        for i, line in enumerate(txt):
            dataset[i] = line.strip()

with h5py.File("data/h5text.hdf5", 'r') as h5txt:
    for k, v in h5txt["text"].items():
        print(k, v)
        print(v[:])

