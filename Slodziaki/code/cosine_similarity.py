from read_data import create_frame
import numpy as np
from numpy.linalg import norm
from gensim.models import Word2Vec


class Clusterizer:

    sentences = None
    dataframe = None
    threshold_value = 0.4
    sim_func = None
    model = None

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
        # temp = list(zip(seq1, seq2))
        # return sum([min(x) for x in temp])

        # does the same thing as the above lines
        return np.dot(seq1, seq2)


    def vectorize_all(self, sequences) -> np.array:
        embed = self._create_seq_list()
        vecs = []
        for seq in sequences:
            # vecs.append(self._vectorize_sequence(seq, embed))
            vecs.append(self.word_2_vec(seq))
        return np.array(vecs)


    def word_2_vec(self, sequence):
        embedded = [self.model.wv[char] for char in sequence if char in self.model.wv]
        return sum(embedded) / len(embedded)

    def create_sim_matrix(self, embeds):
        # the matrix returned shows, in each row, the similarity of a single sequence to each other sequence
        my_matrix = np.zeros(shape=(len(embeds), len(embeds)))
        for i in range(len(embeds)):
            for c in range(i, len(embeds)):
                temp = self.sim_func(embeds[i], embeds[c])
                my_matrix[i][c] = temp
                my_matrix[c][i] = temp

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

        # selects random sequence as being descriptive, creates cluster around it based on threshold value
        while len(unused_rows) != 0:
            curr_cluster = []
            index = np.random.choice(unused_rows)
            row = sim_matrix[index]
            for v_i in range(len(row)):
                if row[v_i] >= self.threshold_value and v_i in unused_rows:
                    unused_rows.remove(v_i)
                    curr_cluster.append(v_i)

            # if current element deosn't create cluster, make it a one-element cluster
            if len(curr_cluster) == 0:
                unused_rows.remove(index)
                curr_cluster.append(index)

            clusters.append(tuple(curr_cluster))

        clusters = self._convert_clusters(clusters)
        return clusters


    def _create_heatmap():
        pass


    def clusterize(self):
        embeddings = self.vectorize_all(self.sentences)
        sim_matrix = self.create_sim_matrix(embeddings)
        self.clusters = self._create_clusters(sim_matrix)
        print(f"Created {len(self.clusters)} clusters.")
        return self.clusters


    def __init__(self, sentences, frame, func=cosine_sim) -> None:
        self.sentences = sentences
        self.dataframe = frame
        self.sim_func = func

        self.model = Word2Vec(sentences=sentences, min_count=1, window=2, vector_size=128)


if __name__ == "__main__":
    # create embedding
    df = create_frame()
    clus = Clusterizer(df["sequence_values"][:7], df[:7])
    print(clus.same_symbols_sum([1, 2, 3], [1, 2, 3]))
    clus.threshold_value = 2
    clus.sim_func = clus.same_symbols_sum
    print(clus.clusterize())