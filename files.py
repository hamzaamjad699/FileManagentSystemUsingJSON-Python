class File:
    def __init__(self, id, name, size, chunks):
        self.id = id
        self.name = name
        self.size = size
        self.chunks = chunks

    def file_structure(self):
        return {
            self.id: {
                "name": self.name,
                "size": self.size,
                "chunks": self.chunks
            }
        }

    def create_f(self):
        new_file = self.file_structure()
        return new_file
