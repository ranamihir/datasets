import h5py
import pickle
import gzip
import os


def get_store(fname='data'):
    print('Loading from data_dir {}'.format(fname))
    return h5py.File(fname, 'r')


def build_store(data_dir='data', filename='mnist.pkl.gz'):
    '''Build a hdf5 data store for MNIST.
    '''
    file_path = os.path.join(data_dir, filename)
    print('Reading {}'.format(file_path))
    f = gzip.open(file_path,'rb')
    train_set, val_set, test_set = pickle.load(f, encoding='latin1')
    datasets_dict = {
        'train': train_set,
        'val': val_set,
        'test': test_set,
    }
    f.close()

    for dataset_type in ['train', 'val', 'test']:
        file_path = os.path.join(data_dir, '{}_{}.h5'.format(filename.split('.')[0], dataset_type))
        print('Writing to {}'.format(file_path))
        h5file = h5py.File(file_path, 'w')

        print('Creating {} set.'.format(dataset_type))
        h5file.create_dataset('inputs', data=datasets_dict[dataset_type][0].reshape(-1, 28, 28))
        h5file.create_dataset('targets', data=datasets_dict[dataset_type][1])

        print('Closing {}'.format(file_path))
        h5file.close()


if __name__=='__main__':
    build_store()
