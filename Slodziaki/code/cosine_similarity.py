from read_data import create_frame
import numpy as np

dataframe = create_frame()


def create_seq_set(frame) -> set:
    seqs = set()
    for seq in frame["sequence_values"]:
        seqs.update(seq)
    return seqs

def vectorize_sequence(seq, embed_list):
    pass


def cosine_sim(seq1, seq2):
    pass