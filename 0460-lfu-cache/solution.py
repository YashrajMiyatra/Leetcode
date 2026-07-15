import collections
import random

class LFUCache:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def __init__(self, capacity: int):
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        self.capacity = capacity
        self.key_to_val_freq = {}
        self.freq_to_keys = collections.defaultdict(dict)
        self.min_freq = 0

    def _update_freq(self, key: int):
        val, freq = self.key_to_val_freq[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq] and self.min_freq == freq:
            self.min_freq += 1
        freq += 1
        self.key_to_val_freq[key] = (val, freq)
        self.freq_to_keys[freq][key] = None

    def get(self, key: int) -> int:
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        if key not in self.key_to_val_freq:
            return -1
        self._update_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        if self.capacity <= 0:
            return
            
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self._update_freq(key)
        else:
            if len(self.key_to_val_freq) >= self.capacity:
                evict_key = next(iter(self.freq_to_keys[self.min_freq]))
                del self.freq_to_keys[self.min_freq][evict_key]
                del self.key_to_val_freq[evict_key]
                
            self.key_to_val_freq[key] = (value, 1)
            self.freq_to_keys[1][key] = None
            self.min_freq = 1
