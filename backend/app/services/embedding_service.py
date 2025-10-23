"""
Embedding service for generating vector embeddings
"""

from sentence_transformers import SentenceTransformer
from app.core.config import settings
from typing import List


class EmbeddingService:
    """Service for generating embeddings using Sentence Transformers"""

    def __init__(self):
        """Initialize the embedding model"""
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)

    async def get_embedding(self, text: str) -> List[float]:
        """
        Generate embedding for text
        
        Args:
            text: Text to embed
            
        Returns:
            List of floats representing the embedding vector
        """
        if not text or not text.strip():
            return []

        embedding = self.model.encode(text, convert_to_tensor=False)
        return embedding.tolist()

    async def get_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple texts
        
        Args:
            texts: List of texts to embed
            
        Returns:
            List of embedding vectors
        """
        if not texts:
            return []

        embeddings = self.model.encode(texts, convert_to_tensor=False)
        return [emb.tolist() for emb in embeddings]

    async def similarity(self, embedding1: List[float], embedding2: List[float]) -> float:
        """
        Calculate cosine similarity between two embeddings
        
        Args:
            embedding1: First embedding vector
            embedding2: Second embedding vector
            
        Returns:
            Similarity score between 0 and 1
        """
        import numpy as np
        from scipy.spatial.distance import cosine

        if not embedding1 or not embedding2:
            return 0.0

        # Convert to numpy arrays
        emb1 = np.array(embedding1)
        emb2 = np.array(embedding2)

        # Calculate cosine similarity
        similarity = 1 - cosine(emb1, emb2)
        return float(similarity)

