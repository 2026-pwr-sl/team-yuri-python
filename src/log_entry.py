class LogEntry:
    def __init__(self, ip_address, timestamp, method, path, protocol, status_code, bytes_sent):
        self.ip_address = ip_address
        self.timestamp = timestamp
        self.method = method
        self.path = path
        self.protocol = protocol
        self.status_code = status_code
        self.bytes_sent = bytes_sent

    def __str__(self):
        return f"{self.ip_address} {self.timestamp} {self.method} {self.path} {self.protocol} {self.status_code} {self.bytes_sent}"

    def __repr__(self):
        return (
            f"LogEntry(ip_address='{self.ip_address}', "
            f"timestamp={repr(self.timestamp)}, "
            f"method='{self.method}', "
            f"path='{self.path}', "
            f"protocol='{self.protocol}', "
            f"status_code={self.status_code}, "
            f"bytes_sent={self.bytes_sent})"
        )

    def is_error(self):
        return self.status_code >= 400
