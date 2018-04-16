# -*- coding: utf-8 -*-
import dataset
import keys
import numpy as np
import torch

characters = keys.alphabet[:]
from model import get_model

nclass = len(characters) + 1

trainroot = '../data/lmdb/train'
valroot = '../data/lmdb/val'
# workers = 4  #FIXME tmp commented
workers = 32
imgH = 32
imgW = 256
keep_ratio = False
random_sample = False
batchSize = 32
n_len = 10

model, basemodel = get_model(height=imgH, nclass=nclass)


def one_hot(text, length=10, characters=characters):
    label = np.zeros(length)
    for i, char in enumerate(text):
        index = characters.find(char)
        if index == -1:
            index = characters.find(u' ')
        if i < length:
            label[i] = index
    return label


if random_sample:
    sampler = dataset.randomSequentialSampler(train_dataset, batchSize)
else:
    sampler = None
train_dataset = dataset.lmdbDataset(root=trainroot, target_transform=one_hot)

test_dataset = dataset.lmdbDataset(
    root=valroot, transform=dataset.resizeNormalize((imgW, imgH)), target_transform=one_hot)

import os

modelPath = '../pretrain-models/keras.hdf5'
if os.path.exists(modelPath):
    basemodel.load_weights(modelPath)

train_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size=batchSize,
    shuffle=True, sampler=sampler,
    num_workers=int(workers),
    collate_fn=dataset.alignCollate(imgH=imgH, imgW=imgW, keep_ratio=keep_ratio))

testSize = 16
# print test_dataset[0]
test_loader = torch.utils.data.DataLoader(
    test_dataset, batch_size=testSize,
    shuffle=True, num_workers=int(workers))

j = 0
crrentLoss = 1000
loss = 1000
interval = 50
for i in range(3):
    for X, Y in train_loader:
        X = X.numpy()
        X = X.reshape((-1, imgH, imgW, 1))
        Y = np.array(Y)

        Length = int(imgW / 4) - 2
        batch = X.shape[0]
        X, Y = [X, Y, np.ones(batch) * Length, np.ones(batch) * n_len], np.ones(batch)
        model.train_on_batch(X, Y)
        if j % interval == 0:
            X, Y = next(iter(test_loader))
            X = X.numpy()
            X = X.reshape((-1, imgH, imgW, 1))
            Y = Y.numpy()
            Y = np.array(Y)
            batch = X.shape[0]
            X, Y = [X, Y, np.ones(batch) * Length, np.ones(batch) * n_len], np.ones(batch)

            crrentLoss = model.evaluate(X, Y)
            print("step:{},loss:{},crrentLoss:{}".format(j, loss, crrentLoss))
            if crrentLoss < loss:
                loss = crrentLoss
                path = 'save_model/model{}.h5'.format(loss)
                print("save model:{}".format(path))
                # same as pretrain
                basemodel.save('save_model/ocr0.2.h5')
                # basemodel.save(path)

        j += 1
