from numpy import load
import pandas as pd

def load_data(knob='default', replication=0, model='baseline', train_test='train'):
    """
    loading train test experiment results
    """

    file_path = '/Users/anniewang/Desktop/dragonnet/result/ihdp/{}/'.format(knob)
    data = load(file_path + '{}/{}/0_replication_{}.npz'.format(replication, model, train_test))

    # q_t0,q_t1 -> predicted outcomes under (0,1) treatment
    # g -> predicted propensity score
    # t -> treatment
    # y -> original y before transformation
    # index
    # eps -> epsilon
    # NOTE: rechape (-1,1) return a two-dimensional array with one column and as many rows as necessary to accommodate all elements.

    return data['q_t0'].reshape(-1, 1), data['q_t1'].reshape(-1, 1), data['g'].reshape(-1, 1), \
           data['t'].reshape(-1, 1), data['y'].reshape(-1, 1), data['index'].reshape(-1, 1), data['eps'].reshape(-1, 1)

q_t0, q_t1, g, t, y_dragon, index, eps =  load_data('dragonnet', 0, 'targeted_regularization', 'train')
print(eps)