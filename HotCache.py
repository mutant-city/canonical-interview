class HotCache:
    """
        A hot cache that keeps the top X strings.
        Has O(n) for insertion if accepted into cache, takes linear time to recalculate the minimum,
        and only a O(1) if rejected from the cache.
        No cache expiration, so as it graduates to the top of the number space over time, it will approach O(1) insertion.
    """

    def __init__(self, size):
        self.min = 0
        self.min_item = None
        self.size = size
        self.hot_cache = {}

    def add(self, item, quantity):
        """
        Add item to the hot_cache if it is greater than the minimum item in the hot cache, and boot the old minimum.
        """
        # if the hot cache isn't full add item and return
        if len(self.hot_cache) < self.size:
            self.hot_cache[item] = quantity
            self.set_minimum()
            return

        # if hot cache is full, check if below minimum, if so it doesn't belong, so return
        if quantity < self.min:
            return

        # if it belongs, kick out lowest element, and add, and recalculate the minimum
        self.hot_cache.pop(self.min_item)
        self.hot_cache[item] = quantity
        self.set_minimum()

    def set_minimum(self):
        """
        Sets the variables for easy identification of lowest items in the hot cache.
        """
        low_quantity = None
        low_item = None
        for item, quantity in self.hot_cache.items():
            if low_quantity is None:
                low_quantity = quantity
                low_item = item
                continue
            if quantity < low_quantity:
                low_quantity = quantity
                low_item = item
        self.min = low_quantity
        self.min_item = low_item

    def to_ordered_list(self):
        """
        Returns an ordered list from maximum quantity to minimum.
        """
        out = [(item, quantity) for item, quantity in self.hot_cache.items()]
        return sorted(out, key=lambda tup: tup[1], reverse=True)
