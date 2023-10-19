def app(environ, start_response):
        query = environ["QUERY_STRING"].split("&")
        bytes_query = [bytes(item+'\n', encoding='utf-8') for item in query]
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(environ["QUERY_STRING"])))
        ])
        return bytes_query
