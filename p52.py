"""
You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

    bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
    int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
"""
class FileSystem(object):
    def __init__(self):
        # Store path-value mapping
        self.paths = {'': -1}  # Including root (empty string) for parent lookup convenience

    def createPath(self, path, value):
        # Path must not exist, parent must exist, path format is '/a/b'
        if path in self.paths or not path or path == '/':
            return False
        parent = path[:path.rfind('/')]
        if parent not in self.paths:
            return False
        self.paths[path] = value
        return True

    def get(self, path):
        return self.paths.get(path, -1)
