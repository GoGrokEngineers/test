import threading
import time

class Cache:
    def __init__(self, expiration_time=300):
        self.cache = {}
        self.expiration_time = expiration_time
        # Cleaner
        self.cleaner_thread = threading.Thread(target=self.cleaner)
        self.cleaner_thread.daemon = True
        self.cleaner_thread.start()

    def set(self, key, value):
        expire_at = time.time() + self.expiration_time
        self.cache[key] = (value, expire_at)

    def get(self, key):
        if key in self.cache:
            value, expire_at = self.cache[key]
            if time.time() < expire_at:
                return value
            else:
                del self.cache[key]
        return None

    def contains(self, key):
        return self.get(key) is not None

    def cleaner(self):
        while True:
            time.sleep(1800)# 30mins 
            for key in list(self.cache.keys()):
                _, expire_at = self.cache[key]
                if time.time() >= expire_at:
                    del self.cache[key]

    def clear(self):
        self.cache.clear()


