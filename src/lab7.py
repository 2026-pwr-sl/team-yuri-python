class HTTPRequest:
    def __init__(self, request_type, resource_path, http_protocol):
        self.request_type = request_type
        self.resource_path = resource_path
        self.http_protocol = http_protocol


def reqstr2obj(request_string):
    """Function gets text HTTP request and returns HTTP request object"""
    if not isinstance(request_string, str):
        raise TypeError("request_string must be a string")

    if not len(request_string.strip(' ').split(' '))==3:
        return None

    request_splitted = request_string.split(" ")

    possible_request_types = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]
    possible_http_protocols = ["HTTP0.9", "HTTP1.0", "HTTP1.1", "HTTP2", "HTTP3"]

    if not request_splitted[0] in possible_request_types:
        raise TypeError("request_type is nonexistent")
    if not request_splitted[1].startswith('/'):
     raise TypeError("resource_path should start with /")

    if not request_splitted[2] in possible_http_protocols:
        raise TypeError("http_protocol is nonexistent")

    return HTTPRequest(*request_splitted) # sorry for this gross line



