def CEP(amb, start_response):
    arch = open(f"CEP.html", "rb")
    body = arch.read()
    status = "200 OK"
    response_headers = [("Content-type", "text/html")]
    start_response(status, response_headers)
    return [body]

def Address(amb, start_response):
    arch = open(f"Address.html", "rb")
    body = arch.read()
    status = "200 OK"
    response_headers = [("Content-type", "text/html")]
    start_response(status, response_headers)
    return [body]