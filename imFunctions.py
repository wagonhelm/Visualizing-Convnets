import os
import math
import tarfile
from six.moves.urllib.request import urlretrieve
import numpy as np
import scipy.ndimage
from scipy.misc import imread


def downloadImages(filename, expectedSize, force=False):
    url = 'http://www.robots.ox.ac.uk/~vgg/data/pets/data/'
    path = os.getcwd()
    dest_filename = os.path.join(path, filename)
    
    if os.path.exists(dest_filename):
        statinfo = os.stat(dest_filename)
        if statinfo.st_size != expectedSize:
            force=True
            print("File {} not expected size, forcing download".format(filename))
        else:
            print("File '{}' allready downloaded :)".format(filename))
    
    if force or not os.path.exists(dest_filename):
        print('Attempting to download: {}'.format(filename)) 
        filename, _ = urlretrieve(url + filename, dest_filename)
        print("Downloaded '{}' successfully".format(filename))
        
def maybeExtract(filename, force=False):
    root = os.path.splitext(os.path.splitext(filename)[0])[0]  
    if os.path.isdir(root) and not force:
        print("{} already present - Skipping extraction of {}".format(root, filename))
    
    else:
        print("Extracting data for {}:".format(root))
        tar = tarfile.open(filename)
        tar.extractall(os.getcwd())
        tar.close()
        
def sortImages(testPer):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    path1 = os.getcwd()+'/images/'
    listing = os.listdir(path1)  
    if len(listing) == 37:
        print("Images allready sorted")
        return 

    for i in listing:
        folder = ''
        for ii in i:
            if ii in numbers:
                break
            else:
                folder += ii
    
        folder = folder.replace("_","")
        if not os.path.exists(path1+folder):
            os.makedirs(path1+folder)
        os.rename(path1+i, path1+folder+'/'+i)
        
    listing = os.listdir(path1)  

    for i in listing:
        path2 = path1+i+'/'
        listing2 = os.listdir(path2)
    
        if not os.path.exists(path2+'train'):
            os.makedirs(path2+'train')
        if not os.path.exists(path2+'test'):
            os.makedirs(path2+'test')
    
        for ii in listing2[0:int(float(math.floor(len(listing2)*testPer)))]:
            os.rename(path2+ii, path2+'test'+'/'+ii)
        for ii in listing2[int(math.floor(len(listing2)*testPer)):]:
            os.rename(path2+ii, path2+'train'+'/'+ii)    
    print("Images sorted")
            
def buildDataset():

    dataset = []
    path1 = os.getcwd()+'/images/'
    listing = os.listdir(path1)
    
    for i in listing:
        choice = input("Do you want to use {} in your dataset?  [y/n/break]".format(i))
        if choice.lower() == 'y':
            dataset.append(i)
        if choice.lower() == 'break':
            break
            
    train_x = np.zeros([1, 224, 224, 3])
    train_y = np.zeros([1,len(dataset)])
    classes = len(dataset)
    classLabels = []

    oneHotCounter = 0

    for i in dataset:
        impath = os.getcwd()+'/images/'+i+'/train/'
        listing2 = os.listdir(impath)
        classLabels.append(i)
        for i in listing2:
            img = scipy.misc.imresize(imread(impath+i).astype(np.float32), [224,224])
            img = img.reshape([1,224,224,3])
            train_x = np.vstack((train_x,img))
            onehot = np.zeros([1,len(dataset)])
            onehot[0,oneHotCounter] = 1
            train_y = np.vstack((train_y, onehot))
    
        oneHotCounter += 1
    
    mean = np.mean([train_x], axis=1)
    train_x -= mean
    
    test_x = np.zeros(shape=[1, 224, 224, 3])
    test_y = np.zeros([1,len(dataset)])

    oneHotCounter = 0

    for i in dataset:
        impath = os.getcwd()+'/images/'+i+'/test/'
        listing2 = os.listdir(impath)
   
        for ii in listing2:
            img = scipy.misc.imresize(imread(impath+ii).astype(np.float32), [224,224])
            img = img.reshape([1,224,224,3])
            test_x = np.vstack((test_x,img))
            onehot = np.zeros([1,len(dataset)])
            onehot[0,oneHotCounter] = 1
            test_y = np.vstack((test_y, onehot))
        
        print("{} = {}".format(i,onehot))
        oneHotCounter += 1
    print('Total Train Size: {}  Total Test Size: {}  Total # Classes {}'.format(train_x[1:].shape[0], test_x[1:].shape[0], classes))
    test_x -= mean
    return train_x[1:], train_y[1:], test_x[1:], test_y[1:], classes, classLabels

def shuffle(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

