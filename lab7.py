class HTTPRequest:
    def __init__(self, request_type, resource_path, http_protocol):
        self.request_type = request_type
        self.resource_path = resource_path
        self.http_protocol = http_protocol


def reqstr2obj(request_string):
    """Function gets text HTTP request and returns HTTP request object"""
    if not isinstance(request_string, str):
        raise TypeError("request_string must be a string")

    return HTTPRequest("GET", "/", "HTTP1.1")