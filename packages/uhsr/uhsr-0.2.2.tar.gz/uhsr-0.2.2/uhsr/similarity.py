import numpy as np

def compute_cosine_similarity(query_embedding, embeddings):
    """Compute cosine similarity between query and document embeddings."""
    if np.ndim(embeddings) == 1:
        dot_product = np.dot(embeddings, query_embedding)
        norm_embeddings = np.linalg.norm(embeddings)
        norm_query = np.linalg.norm(query_embedding)
        return dot_product / (norm_embeddings * norm_query + 1e-8)
    else:
        dot_product = np.dot(embeddings, query_embedding)
        norm_embeddings = np.linalg.norm(embeddings, axis=1)
        norm_query = np.linalg.norm(query_embedding)
        return dot_product / (norm_embeddings * norm_query + 1e-8)

def compute_euclidean_similarity(query_embedding, embeddings):
    """Compute Euclidean similarity (1 / (1 + distance))."""
    if np.ndim(embeddings) == 1:
        distance = np.linalg.norm(embeddings - query_embedding)
        return 1 / (1 + distance)
    else:
        distances = np.linalg.norm(embeddings - query_embedding, axis=1)
        return 1 / (1 + distances)

def compute_mahalanobis_similarity(query_embedding, embeddings):
    """Compute Mahalanobis similarity (normalized)."""
    cov = np.cov(embeddings.T)
    try:
        inv_cov = np.linalg.inv(cov)
    except np.linalg.LinAlgError:
        inv_cov = np.linalg.pinv(cov)  # Use pseudo-inverse if singular

    if np.ndim(embeddings) == 1:
        diff = embeddings - query_embedding
        distance = np.sqrt(np.dot(np.dot(diff, inv_cov), diff.T))
        return 1 / (1 + distance)
    else:
        diff = embeddings - query_embedding
        distances = np.array([np.sqrt(np.dot(np.dot(d, inv_cov), d.T)) for d in diff])
        return 1 / (1 + distances)

def compute_semantic_similarity(query_embedding, embeddings, metric='cosine'):
    """Wrapper function to compute similarity based on the chosen metric."""
    if metric == 'cosine':
        return compute_cosine_similarity(query_embedding, embeddings)
    elif metric == 'euclidean':
        return compute_euclidean_similarity(query_embedding, embeddings)
    elif metric == 'mahalanobis':
        return compute_mahalanobis_similarity(query_embedding, embeddings)
    else:
        raise ValueError("Unsupported metric. Choose from 'cosine', 'euclidean', or 'mahalanobis'.")
