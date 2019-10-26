#! /home/steve/anaconda3/bin/python3.7

import numpy as np
train_images = np.load("train_images.npy")

padded_train_images = []
print("padding train images")

for i in train_images:
    entry=[]
    entry.append(np.zeros(32))
    entry.append(np.zeros(32))
    for j in i:
        entry.append([0,0]+list(j)+[0,0])
    entry.append(np.zeros(32))
    entry.append(np.zeros(32))
    padded_train_images.append(entry)
print("saving padded train images")
np.save("padded_train_images.npy", np.array(padded_train_images))




test_images = np.load("test_images.npy")

padded_test_images = []
print("padding test images")

for i in test_images:
    entry=[]
    entry.append(np.zeros(32))
    entry.append(np.zeros(32))
    for j in i:
        entry.append([0,0]+list(j)+[0,0])
    entry.append(np.zeros(32))
    entry.append(np.zeros(32))
    padded_test_images.append(entry)

print("saving padded test images")
np.save("padded_test_images.npy", np.array(padded_test_images))

