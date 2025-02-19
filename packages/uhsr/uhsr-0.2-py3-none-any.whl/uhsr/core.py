import numpy as np
from bm25 import BM25
from faiss_retrieval import FAISSRetrieval
from similarity import compute_semantic_similarity
from utils import logistic_norm

class UHSR:
    """
    Unified Hyperbolic Spectral Retrieval (UHSR) is a hybrid retrieval model that 
    integrates lexical search (BM25) and semantic search (FAISS) into a unified system.
    
    Attributes:
        documents (list): List of textual documents.
        embeddings (numpy.ndarray): Precomputed vector embeddings for semantic search.
        bm25 (BM25): BM25 instance for lexical retrieval.
    """

    def __init__(self, documents, embeddings):
        """
        Initializes the UHSR retrieval model.

        Parameters:
            documents (list of str): The textual documents.
            embeddings (numpy.ndarray): Precomputed document embeddings.
        """
        self.documents = documents
        self.embeddings = embeddings
        self.bm25 = BM25(documents)
        self.faiss = FAISSRetrieval(embeddings)

    def retrieve(self, query, query_embedding, top_k=5, metric='cosine', gamma=0.7):
        """
        Retrieves the top-ranked documents for a given query.

        The retrieval process follows these steps:
        1. Perform BM25 lexical filtering to retrieve candidate documents.
        2. Compute semantic similarity scores between query and candidate embeddings.
        3. Fuse BM25 and semantic scores using logistic normalization.
        4. Return ranked results.

        Parameters:
            query (str): The input query.
            query_embedding (numpy.ndarray): Embedding of the query.
            top_k (int): Number of documents to return.
            metric (str): Similarity metric for semantic search (cosine, euclidean, or mahalanobis).
            gamma (float): Weight controlling BM25 vs. semantic contribution.

        Returns:
            tuple: (final_documents, final_scores)
                final_documents (list): List of retrieved documents.
                final_scores (numpy.ndarray): Normalized relevance scores.
        """
        # Step 1: BM25 lexical filtering
        bm25_indices, bm25_docs, bm25_scores = self.bm25.search(query, top_k)
        bm25_norm = logistic_norm(np.tanh(np.array(bm25_scores)), a=5)

        # Step 2: Semantic similarity computation
        semantic_scores = compute_semantic_similarity(query_embedding, self.embeddings, metric=metric)
        semantic_norm = logistic_norm(np.tanh(semantic_scores[bm25_indices]), a=5)

        # Step 3: Weighted fusion of scores
        fusion_scores = gamma * bm25_norm + (1 - gamma) * semantic_norm

        # Step 4: Sort and return results
        ranked_indices = np.argsort(fusion_scores)[::-1]
        return [bm25_docs[i] for i in ranked_indices], fusion_scores[ranked_indices]
