"""
LLM Response Caching System
Optimizes performance by caching frequently requested responses.
"""

from typing import Optional, Dict
import hashlib
import json
from pathlib import Path


class ResponseCache:
    """
    Cache for LLM responses to improve performance.
    """
    
    def __init__(self, cache_dir: str = "cache/responses", ttl: int = 3600):
        """
        Initialize response cache.
        
        Args:
            cache_dir: Directory for cache files
            ttl: Time to live in seconds
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.ttl = ttl
        self.memory_cache: Dict[str, str] = {}
    
    def _generate_key(self, query: str, context: str) -> str:
        """
        Generate cache key from query and context.
        
        Args:
            query: User query
            context: Context string
            
        Returns:
            Cache key (hash)
        """
        combined = f"{query}|||{context}"
        return hashlib.md5(combined.encode()).hexdigest()
    
    def get(self, query: str, context: str) -> Optional[str]:
        """
        Get cached response if available.
        
        Args:
            query: User query
            context: Context string
            
        Returns:
            Cached response or None
        """
        key = self._generate_key(query, context)
        
        # Check memory cache first
        if key in self.memory_cache:
            return self.memory_cache[key]
        
        # Check disk cache
        cache_file = self.cache_dir / f"{key}.json"
        if cache_file.exists():
            with open(cache_file, 'r') as f:
                data = json.load(f)
                return data.get('response')
        
        return None
    
    def set(self, query: str, context: str, response: str):
        """
        Cache a response.
        
        Args:
            query: User query
            context: Context string
            response: LLM response to cache
        """
        key = self._generate_key(query, context)
        
        # Store in memory cache
        self.memory_cache[key] = response
        
        # Store in disk cache
        cache_file = self.cache_dir / f"{key}.json"
        with open(cache_file, 'w') as f:
            json.dump({
                'query': query,
                'response': response,
                'timestamp': Path(cache_file).stat().st_mtime
            }, f)

