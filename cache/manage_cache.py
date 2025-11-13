"""
Utility script to manage the response cache.
Provides functions to view, clear, and analyze cache.
"""

import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime
from collections import defaultdict


class CacheManager:
    """Manager for cache operations."""
    
    def __init__(self, cache_dir: str = "cache/responses"):
        """
        Initialize cache manager.
        
        Args:
            cache_dir: Directory containing cache files
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
    
    def get_cache_files(self) -> List[Path]:
        """Get all cache files."""
        return list(self.cache_dir.glob("*.json"))
    
    def get_cache_stats(self) -> Dict:
        """
        Get statistics about the cache.
        
        Returns:
            Dictionary with cache statistics
        """
        cache_files = self.get_cache_files()
        total_size = sum(f.stat().st_size for f in cache_files)
        
        # Analyze cache entries
        entries = []
        for cache_file in cache_files:
            try:
                with open(cache_file, 'r') as f:
                    data = json.load(f)
                    entries.append({
                        'file': cache_file.name,
                        'timestamp': data.get('timestamp', 0),
                        'size': cache_file.stat().st_size
                    })
            except Exception:
                pass
        
        return {
            'total_files': len(cache_files),
            'total_size_mb': total_size / 1024 / 1024,
            'entries': entries
        }
    
    def clear_cache(self, older_than_days: int = None):
        """
        Clear cache files.
        
        Args:
            older_than_days: If specified, only clear files older than N days
        """
        cache_files = self.get_cache_files()
        cleared = 0
        
        if older_than_days:
            from datetime import timedelta
            cutoff_time = datetime.now().timestamp() - (older_than_days * 24 * 60 * 60)
        
        for cache_file in cache_files:
            should_delete = True
            
            if older_than_days:
                try:
                    with open(cache_file, 'r') as f:
                        data = json.load(f)
                        timestamp = data.get('timestamp', 0)
                        if timestamp > cutoff_time:
                            should_delete = False
                except Exception:
                    pass
            
            if should_delete:
                try:
                    cache_file.unlink()
                    cleared += 1
                except Exception as e:
                    print(f"Error deleting {cache_file}: {e}")
        
        print(f"✓ Cleared {cleared} cache file(s)")
        return cleared
    
    def show_cache_info(self):
        """Display cache information."""
        stats = self.get_cache_stats()
        
        print("=" * 60)
        print("Cache Statistics")
        print("=" * 60)
        print(f"Total cache files: {stats['total_files']}")
        print(f"Total cache size: {stats['total_size_mb']:.2f} MB")
        
        if stats['entries']:
            # Show oldest and newest entries
            sorted_entries = sorted(stats['entries'], key=lambda x: x['timestamp'])
            if sorted_entries:
                oldest = datetime.fromtimestamp(sorted_entries[0]['timestamp'])
                newest = datetime.fromtimestamp(sorted_entries[-1]['timestamp'])
                print(f"Oldest entry: {oldest.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Newest entry: {newest.strftime('%Y-%m-%d %H:%M:%S')}")
        
        print("=" * 60)
    
    def list_cache_entries(self, limit: int = 10):
        """
        List cache entries.
        
        Args:
            limit: Maximum number of entries to display
        """
        cache_files = self.get_cache_files()
        
        print("=" * 60)
        print(f"Cache Entries (showing up to {limit})")
        print("=" * 60)
        
        entries = []
        for cache_file in cache_files[:limit]:
            try:
                with open(cache_file, 'r') as f:
                    data = json.load(f)
                    timestamp = datetime.fromtimestamp(data.get('timestamp', 0))
                    query = data.get('query', 'N/A')[:50]
                    entries.append({
                        'file': cache_file.name,
                        'query': query,
                        'timestamp': timestamp,
                        'size': cache_file.stat().st_size
                    })
            except Exception as e:
                entries.append({
                    'file': cache_file.name,
                    'query': f'Error: {str(e)[:30]}',
                    'timestamp': None,
                    'size': cache_file.stat().st_size
                })
        
        for entry in entries:
            timestamp_str = entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S') if entry['timestamp'] else 'N/A'
            print(f"{entry['file']:20s} | {timestamp_str:19s} | {entry['query']}")
        
        if len(cache_files) > limit:
            print(f"\n... and {len(cache_files) - limit} more entries")
        
        print("=" * 60)


if __name__ == "__main__":
    import sys
    
    manager = CacheManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "stats":
            manager.show_cache_info()
        elif command == "list":
            limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
            manager.list_cache_entries(limit)
        elif command == "clear":
            older_than = int(sys.argv[2]) if len(sys.argv) > 2 else None
            manager.clear_cache(older_than_days=older_than)
        else:
            print(f"Unknown command: {command}")
            print("Usage: python manage_cache.py [stats|list|clear] [args]")
    else:
        # Default: show stats
        manager.show_cache_info()
        print("\nUsage:")
        print("  python manage_cache.py stats     - Show cache statistics")
        print("  python manage_cache.py list [N]  - List cache entries (default: 10)")
        print("  python manage_cache.py clear [N] - Clear cache (or files older than N days)")

