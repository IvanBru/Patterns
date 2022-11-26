
class Connect:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connect, cls).__new__(cls)
        return cls.instance

    def get_coonection(self):
        print(self.connection)


class ConnectionS3(Connect):
    connect = "S3"
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connect, cls).__new__(cls)
        return cls.instance

    def get_connection(self):
        print("Connect to S3")

class ConnectionFileSystem(Connect):
    connect = "File System"
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connect, cls).__new__(cls)
        return cls.instance

    def get_connection(self):
        print("Connect to File System")
