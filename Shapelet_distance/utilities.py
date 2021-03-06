import numpy as np
import os
from os.path import basename, join
def strip_suffix(s, suffix):
    '''
    Removes a suffix from a string if the string contains it. Else, the
    string will not be modified and no error will be raised.
    '''

    if not s.endswith(suffix):
        return s
    return s[:len(s)-len(suffix)]

def get_ucr_dataset(data_dir: str, dataset_name: str):
    '''
    Loads train and test data from a folder in which
    the UCR data sets are stored.
    '''
    X_train, y_train, _ = read_ucr_data(data_dir+dataset_name+'/'+dataset_name+'_TRAIN.tsv')
    X_test, y_test, _ = read_ucr_data(data_dir+dataset_name+'/'+dataset_name+'_TEST.tsv')
    #X_train, y_train, _ = read_ucr_data(os.path.join(data_dir, dataset_name, f'{dataset_name}_TRAIN'))
    #X_test, y_test, _ = read_ucr_data(os.path.join(data_dir, dataset_name, f'{dataset_name}_TEST'))

    return X_train, y_train, X_test, y_test

def read_ucr_data(filename):
    '''
    Loads an UCR data set from a file, returning the samples and the
    respective labels. Also extracts the data set name such that one
    may easily display results.
    '''

    data = np.loadtxt(filename, delimiter='\t')
    
    Y = data[:, 0]
    X = data[:, 1:]

    # Remove all potential suffixes to obtain the data set name. This is
    # somewhat inefficient, but we only have to do it once.
    name = os.path.basename(filename)
    name = strip_suffix(name, '_TRAIN')
    name = strip_suffix(name, '_TEST')
    #remove Nan values
    X=np.nan_to_num(X)
    Y=np.nan_to_num(Y)
    return X, Y, name