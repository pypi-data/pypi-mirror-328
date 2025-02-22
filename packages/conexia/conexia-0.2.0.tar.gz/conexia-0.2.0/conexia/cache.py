import os, json, sqlite3, redis, time
from cachetools import TTLCache
#from abc import ABC, abstractmethod



# Constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_FILE = os.path.join(BASE_DIR, "cache.json")
SQLITE_DB = os.path.join(BASE_DIR, "cache.sqlite")


'''
# ================================
# Base Cache Interface
# ================================
class BaseCache(ABC):
    """Abstract base class for different cache backends."""

    @abstractmethod
    def get_cached_info(self, ip):
        pass

    @abstractmethod
    def cache_stun_info(self, ip, port, nat_type, timestamp):
        pass

    @abstractmethod
    def clear_cache(self):
        pass
'''

# ================================
# 1️⃣ In-Memory Cache (TTLCache)
# ================================
class InMemoryCache:
    def __init__(self, max_size=100, ttl=300):
        """Initialize TTL cache with a max size and expiration time (TTL)."""
        self.cache = TTLCache(maxsize=max_size, ttl=ttl)

    def get_cached_info(self, user_id):
        """Retrieve STUN info if available in cache."""
        # TTLCache is used for time-based expiry of cached entries
        # Hence no need for cache expiry validation upon retrieval
        return self.cache.get(user_id)

    def cache_stun_info(self, user_id, data):
        """Store STUN info in cache."""
        self.cache[user_id] = data

    def clear_cache(self, user_id=None):
        """Clear cache for a specific user_id or all if None."""
        if user_id:
            self.cache.pop(user_id, None)  # Remove specific user_id if it exists
        else:
            self.cache.clear()  # Clear entire cache if no user_id is specified


# ================================
# 2️⃣ File-Based Cache (Persistent)
# ================================
class FileCache:
    def __init__(self, file_path=CACHE_FILE, ttl=300):
        self.file_path = file_path  # Store the file path
        self.ttl = ttl
        self.cache = self._load_cache()  # ✅ Load cache properly

    def cache_stun_info(self, user_id, data):
        """Store STUN info in a file with timestamps."""
        self.cache[user_id] = data
        self._save_cache()

    def get_cached_info(self, user_id):
        """Retrieve cached STUN info if valid."""
        entry = self.cache.get(user_id, None)  # ✅ Now `self.cache` is a dictionary
        if not entry or "timestamp" not in entry:
            return None
        if time.time() - entry["timestamp"] < self.ttl:
            return entry
        return None

    def _load_cache(self):
        """Load cache from file, return empty dict if file does not exist."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}  # Return empty cache if JSON is corrupted
        return {}

    def _save_cache(self):
        """Save updated cache data to file."""
        with open(self.file_path, "w") as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=4)

    def clear_cache(self, user_id=None):
        """Clear cache for a specific user_id or all if None."""
        if user_id:
            self.cache.pop(user_id, None)  # Remove specific entry
        else:
            self.cache.clear()  # Clear entire cache
        self._save_cache()  # Save updated cache to file


# ================================
# 3️⃣ DB Cache (SQLite3)
# ================================
class SQLiteCache:
    def __init__(self, db_path=SQLITE_DB, ttl=300):
        self.db_path = db_path
        self.ttl = ttl
        self._initialize_db()

    def _initialize_db(self):
        """Ensure table exists with a timestamp column."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                    CREATE TABLE IF NOT EXISTS stun_cache (
                        user_id VARCHAR(255) PRIMARY KEY,
                        ip TEXT,
                        port INTEGER,
                        city VARCHAR(255),
                        region VARCHAR(255),
                        country VARCHAR(255),
                        continent VARCHAR(255),
                        timezone VARCHAR(255),
                        cord VARCHAR(255),
                        isp_info VARCHAR(255),
                        nat_type VARCHAR(255),
                        timestamp REAL
                    )
                """
            )

    def cache_stun_info(self, user_id, data):
        """Insert STUN info with timestamp."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "REPLACE INTO stun_cache (user_id, ip, port, city, region, country, continent, timezone, cord, isp_info, nat_type, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (user_id, data["data"]["ip"], data["data"]["port"], data["data"]["city"], data["data"]["region"], data["data"]["country"], data["data"]["continent"], data["data"]["timezone"], data["data"]["cord"], data["data"]["isp_info"], data["data"]["nat_type"], data["timestamp"]),
            )

    def get_cached_info(self, user_id):
        """Retrieve STUN info if not expired, otherwise delete it."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT * FROM stun_cache WHERE user_id=?", (user_id,))
            row = cursor.fetchone()
            if row:
                current_time = time.time()
                if current_time - row[11] < self.ttl:
                    return {
                        "user_id": row[0],
                        "data": {
                            "ip": row[1], 
                            "port": row[2],
                            "city": row[3],
                            "region": row[4],
                            "country": row[5],
                            "continent": row[6],
                            "timezone": row[7],
                            "cord": row[8],
                            "isp_info": row[9],
                            "nat_type": row[10]
                            },
                        "timestamp": row[11],
                    }
                conn.execute("DELETE FROM stun_cache WHERE user_id=?", (user_id,))   # Cleanup expired entry
        return None

    def clear_cache(self, user_id=None):
        """Clear cache for a specific user_id or all if None."""
        with sqlite3.connect(self.db_path) as conn:
            if user_id:
                conn.execute("DELETE FROM stun_cache WHERE user_id=?", (user_id,))
            else:
                conn.execute("DELETE FROM stun_cache")  # Clear all cache entries
            conn.commit()


# ================================
# 4️⃣ Redis Cache (Distributed + TTL)
# ================================
class RedisCache:
    def __init__(self, redis_url="redis://localhost:6379", ttl=300):
        self.redis = redis.from_url(redis_url)
        self.ttl = ttl

    def cache_stun_info(self, user_id, data):
        """Cache STUN info with automatic expiry."""
        data = json.dumps(data)
        self.redis.setex(user_id, self.ttl, data)  # Automatically expires after `ttl` seconds

    def get_cached_info(self, user_id):
        """Retrieve STUN info if available (Redis auto-deletes expired keys)."""
        data = self.redis.get(user_id)
        try:
            return json.loads(data) if data else None
        except json.JSONDecodeError:
            return None

    def clear_cache(self, user_id=None):
        """Clear cache for a specific user_id or all if None."""
        if user_id:
            self.redis.delete(user_id)  # Remove specific key
        else:
            self.redis.flushdb()  # Clear entire Redis cache (dangerous in production)


# ================================
# Cache Manager (Chooses Backend)
# ================================
class IPResolverCache:
    def __init__(self, backend:str="file", ttl:int=900, **kwargs):  
        """Initialize the appropriate cache backend with TTL support."""
        if backend == "memory":
            self.cache = InMemoryCache(ttl=ttl, **kwargs)  # Pass TTL
        elif backend == "file":
            self.cache = FileCache(ttl=ttl, **kwargs)  # Pass TTL
        elif backend == "sqlite":
            self.cache = SQLiteCache(ttl=ttl, **kwargs)  # Pass TTL
        elif backend == "redis":
            self.cache = RedisCache(ttl=ttl, **kwargs)  # Pass TTL
        else:
            raise ValueError("Invalid cache backend. Use 'memory', 'file', 'sqlite', or 'redis'.")

    def get_cached_info(self, user_id):
        """Retrieve cached STUN info if available."""
        return self.cache.get_cached_info(user_id)

    def cache_stun_info(self, user_id, data):
        """Store STUN info in cache."""
        self.cache.cache_stun_info(user_id, data)

    def clear_cache(self, user_id=None):
        """Clear cache for a specific user_id or all if None."""
        self.cache.clear_cache(user_id)