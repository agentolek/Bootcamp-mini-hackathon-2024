from read_data import create_frame
import numpy as np
from numpy.linalg import norm


class Clusterizer:

    sentences = None
    dataframe = None
    threshold_value = 0.4

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
    
    def _convert_clusters(self, cluster_set):
        new_clusters = []
        for elem in cluster_set:
            temp = [self.sentences[i] for i in elem]
            new_clusters.append(temp)
        return new_clusters

    def _create_clusters(self, sim_matrix):
        clusters = []

        # outdated selection mechanism
        # for i in range(len(sim_matrix)):
        #     curr_cluster = []
        #     row = sim_matrix[i]
        #     for v_i in range(len(row)):
        #         if row[v_i] >= self.threshold_value:
        #             curr_cluster.append(v_i)
        #     clusters.append(tuple(sorted(curr_cluster)))
        unused_rows = list(range(len(sim_matrix)))

        while len(unused_rows) != 0:
            curr_cluster = []
            row = sim_matrix[np.random.choice(unused_rows)]
            for v_i in range(len(row)):
                if row[v_i] >= self.threshold_value and v_i in unused_rows:
                    unused_rows.remove(v_i)
                    curr_cluster.append(v_i)
            clusters.append(tuple(curr_cluster))          

        clusters = self._convert_clusters(clusters)
        return clusters


    def _create_heatmap():
        pass


    def clusterize(self):
        embeddings = self.vectorize_all(self.sentences)
        sim_matrix = (self.cosine_sim_all(embeddings, self.cosine_sim))
        self.clusters = self._create_clusters(sim_matrix)
        print(f"Created {len(self.clusters)} clusters.")


    def __init__(self, sentences, frame) -> None:
        self.sentences = sentences
        self.dataframe = frame


if __name__ == "__main__":
    # create embedding
    df = create_frame()
    clus = Clusterizer(df["sequence_values"], df)
    clus.clusterize()