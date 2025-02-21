from colppy.helpers.errors import ColppyError

class Response:
    def __init__(self, model, response):
        self._model = model
        self._response = response

    def get_items(self):
        if not ColppyError(self._response).is_error():
            if self._response['response']['data']:
                return [self._model(**item) for item in self._response['response']['data']]
        return []