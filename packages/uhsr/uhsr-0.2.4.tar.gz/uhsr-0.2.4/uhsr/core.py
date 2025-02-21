import numpy as np
from .bm25 import BM25
from .faiss_retrieval import FAISSRetrieval
from .vector_db import PineconeVectorDB
from .similarity import compute_semantic_similarity
from .utils import logistic_norm
from .reranker import Reranker

class UHSR:
    """
    Unified Hyperbolic Spectral Retrieval (UHSR) is a hybrid retrieval model that 
    integrates lexical search (BM25) and semantic search (FAISS/Pinecone) into a unified system.
    
    Attributes:
        documents (list): List of textual documents.
        embeddings (numpy.ndarray): Precomputed vector embeddings for semantic search.
        use_pinecone (bool): Whether to use Pinecone instead of FAISS.
        reranker (Reranker): Optional reranker model.
    """

    def __init__(self, documents, embeddings, use_pinecone=False, pinecone_api_key=None, 
                 reranker_type=None, model_name=None, openai_api_key=None):
        """
        Initializes the UHSR retrieval model.

        Parameters:
            documents (list of str): The textual documents.
            embeddings (numpy.ndarray): Precomputed document embeddings.
            use_pinecone (bool): Whether to use Pinecone instead of FAISS.
            pinecone_api_key (str, optional): API key for Pinecone (if using Pinecone).
            reranker_type (str, optional): Type of reranker to use ('huggingface', 'openai', or None).
            model_name (str, optional): Model name for reranking (if using Hugging Face).
            openai_api_key (str, optional): OpenAI API key (if using OpenAI reranker).
        """
        self.documents = documents
        self.embeddings = embeddings
        self.bm25 = BM25(documents)

        # Choose FAISS or Pinecone for vector search
        if use_pinecone:
            if not pinecone_api_key:
                raise ValueError("Pinecone API key is required when use_pinecone=True.")
            self.vector_db = PineconeVectorDB(api_key=pinecone_api_key)
            self.vector_db.add_embeddings(range(len(documents)), embeddings)  # Upload embeddings to Pinecone
        else:
            self.vector_db = FAISSRetrieval(embeddings)

        # Initialize reranker if specified
        self.reranker = None
        if reranker_type:
            self.reranker = Reranker(model_name=model_name, reranker_type=reranker_type, openai_api_key=openai_api_key)

    def build_similarity_graph(self, candidate_embeddings):
        """
        Constructs a similarity graph using cosine similarity.

        Parameters:
            candidate_embeddings (numpy.ndarray): Embeddings of retrieved documents.

        Returns:
            numpy.ndarray: Graph similarity matrix.
        """
        n = candidate_embeddings.shape[0]
        sim_matrix = np.zeros((n, n))

        for i in range(n):
            for j in range(n):
                sim_matrix[i, j] = compute_semantic_similarity(candidate_embeddings[i], candidate_embeddings[j], metric='cosine')

        return sim_matrix

    def spectral_rerank(self, candidate_embeddings, fusion_scores):
        """
        Applies spectral re-ranking using Graph Laplacian and Fiedler Vector.

        Parameters:
            candidate_embeddings (numpy.ndarray): Embeddings of retrieved documents.
            fusion_scores (numpy.ndarray): Fused BM25 + semantic scores.

        Returns:
            numpy.ndarray: Re-ranked scores based on spectral analysis.
        """
        sim_matrix = self.build_similarity_graph(candidate_embeddings)
        degrees = np.sum(sim_matrix, axis=1)
        D = np.diag(degrees)
        L = D - sim_matrix  # Compute Graph Laplacian

        eigvals, eigvecs = np.linalg.eigh(L)
        if len(eigvals) > 1:
            fiedler_vector = eigvecs[:, 1]  # Extract second smallest eigenvector
        else:
            fiedler_vector = np.ones(len(fusion_scores))

        centrality = np.abs(fiedler_vector)
        centrality_norm = logistic_norm(centrality, a=5)

        return centrality_norm
    
    def harmonic_fusion(self, s1, s2, eps=1e-8):
        """
        Fuse two scores using the harmonic mean.
        
        Parameters:
            s1 (np.array): First set of normalized scores.
            s2 (np.array): Second set of normalized scores.
            eps (float): Small constant to avoid division by zero.
        
        Returns:
            np.array: Fused scores, guaranteed to be in (0,1] if s1 and s2 are in (0,1].
        
        The harmonic mean ensures that neither score dominates, promoting balanced ranking.
        """
        return 2.0 / ((1.0 / (s1 + eps)) + (1.0 / (s2 + eps)))

    def retrieve(self, query, query_embedding, top_k=5, metric='cosine', gamma=0.7, rerank=False):
        """
        Retrieves the top-ranked documents for a given query using BM25 + Semantic Search (FAISS/Pinecone) + Spectral Re-Ranking.

        Parameters:
            query (str): The input query.
            query_embedding (numpy.ndarray): Embedding of the query.
            top_k (int): Number of documents to return.
            metric (str): Similarity metric for semantic search ('cosine', 'euclidean', 'mahalanobis').
            gamma (float): Weight controlling BM25 vs. semantic contribution.
            rerank (bool): Whether to apply reranking.

        Returns:
            tuple: (final_documents, final_scores)
                final_documents (list): List of retrieved documents.
                final_scores (numpy.ndarray): Normalized relevance scores.
        """
        bm25_indices, bm25_docs, bm25_scores = self.bm25.search(query, top_k)
        bm25_norm = logistic_norm(np.tanh(np.array(bm25_scores)), a=5)

        if isinstance(self.vector_db, PineconeVectorDB):
            semantic_results = self.vector_db.query(query_embedding, top_k)
            semantic_scores = np.array([score for _, score in semantic_results])
            semantic_indices = [int(doc_id) for doc_id, _ in semantic_results]
        else:
            semantic_indices, semantic_scores = self.vector_db.search(query_embedding, top_k)

        full_semantic_scores = compute_semantic_similarity(query_embedding, self.embeddings, metric=metric)

        semantic_scores_aligned = np.zeros(top_k)
        for i, bm25_idx in enumerate(bm25_indices):
            if bm25_idx in semantic_indices:
                idx = semantic_indices.index(bm25_idx)
                semantic_scores_aligned[i] = semantic_scores[idx]
            else:
                semantic_scores_aligned[i] = full_semantic_scores[bm25_idx]

        semantic_norm = logistic_norm(np.tanh(semantic_scores_aligned), a=5)

        if gamma is None:
            B_avg = np.mean(bm25_norm)
            S_avg = np.mean(semantic_norm)
            gamma = B_avg / (B_avg + S_avg + 1e-8)

        fusion_scores = self.harmonic_fusion(gamma * bm25_norm, (1 - gamma) * semantic_norm)

        # Spectral Re-Ranking
        candidate_embeddings = self.embeddings[bm25_indices]
        spectral_scores = self.spectral_rerank(candidate_embeddings, fusion_scores)

        final_scores = gamma * fusion_scores + (1 - gamma) * spectral_scores
        ranked_indices = np.argsort(final_scores)[::-1]
        final_docs = [bm25_docs[i] for i in ranked_indices]
        final_scores = final_scores[ranked_indices]

        # Apply Reranking (Optional)
        if rerank and self.reranker:
            final_docs, final_scores = self.reranker.rerank(query, final_docs)

        return final_docs, final_scores
