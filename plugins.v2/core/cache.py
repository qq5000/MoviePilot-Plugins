from cachetools import LRUCache


class IdPathCache:
    """
    文件路径ID缓存
    """

    def __init__(self, maxsize=128):
        self.id_to_dir = LRUCache(maxsize=maxsize)
        self.dir_to_id = LRUCache(maxsize=maxsize)

    def add_cache(self, id: int, directory: str):
        """
        添加缓存
        """
        self.id_to_dir[id] = directory
        self.dir_to_id[directory] = id

    def get_dir_by_id(self, id: int):
        """
        通过 ID 获取路径
        """
        return self.id_to_dir.get(id)

    def get_id_by_dir(self, directory: str):
        """
        通过路径获取 ID
        """
        return self.dir_to_id.get(directory)

    def clear(self):
        """
        清空所有缓存
        """
        self.id_to_dir.clear()
        self.dir_to_id.clear()
