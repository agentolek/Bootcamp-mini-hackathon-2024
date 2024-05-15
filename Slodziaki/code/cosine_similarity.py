from read_data import create_frame
import numpy as np
from numpy.linalg import norm


class Clusterizer:

    sentences = None
    dataframe = None
    threshold_value = 1.5

    clusters = []

    def _create_seq_list(self) -> list:
        seqs = set()
        for seq in self.sentences:
            seqs.update(seq)
        return list(seqs)

    @staticmethod
    def _vectorize_sequence(seq, embed : list):
        ret_vec = np.zeros(shape=len(embed))
        for symbol in seq:
            i = embed.index(symbol)
            ret_vec[i] += 1
        return ret_vec
    

    @staticmethod
    def cosine_sim(seq1, seq2):
        # returns values from the <-1, 1> range
        return np.dot(seq1, seq2) / (norm(seq1) * norm(seq2))
    
    
    @staticmethod
    def same_symbols_sum(seq1, seq2):
        return np.dot(seq1, seq2)


    def vectorize_all(self, sequences) -> np.array:
        embed = self._create_seq_list()
        vecs = []
        for seq in sequences:
            vecs.append(self._vectorize_sequence(seq, embed))
        return np.array(vecs)


    def cosine_sim_all(self, embeds, sim_func=cosine_sim):
        # the matrix returned shows, in each row, the similarity of a single sequence to each other sequence
        my_matrix = np.zeros(shape=(len(embeds), len(embeds)))
        for i in range(len(embeds)):
            for c in range(i + 1, len(embeds)):
                temp = sim_func(embeds[i], embeds[c])
                my_matrix[i][c] = temp
                my_matrix[c][i] = temp
            my_matrix[i][i] = 1

        return my_matrix
    

    def _create_heatmap():
        pass


    def clusterize(self):
        embeddings = self.vectorize_all(self.sentences)
        print(self.sentences)
        sim_matrix = (self.cosine_sim_all(embeddings, self.same_symbols_sum))


    def __init__(self, sentences, frame) -> None:
        self.sentences = sentences
        self.dataframe = frame


if __name__ == "__main__":
    # create embedding
    df = create_frame()
    clus = Clusterizer(df["sequence_values"][:5], df[:5])
    clus.clusterize()