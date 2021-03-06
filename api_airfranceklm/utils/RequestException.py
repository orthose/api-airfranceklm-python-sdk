class RequestException(Exception):
    """
    Erreur lors de la requête à l'API
    https://docs.airfranceklm.com/docs/read/opendata/offers/Errors_Code
    """
    def __init__(self, json_error):
        # On choisit uniquement la première erreur
        error = json_error['errors'][0]
        self.code = error.get('code')
        self.name = error.get('name')
        self.description = error.get('description')
        self.error_in_input_path = error.get('errorInInputPath')
        Exception.__init__(self, f'[{self.code} {self.name}] {self.description} in {self.error_in_input_path}')

    @staticmethod
    def check(json_response):
        if json_response.__contains__('errors'):
            raise RequestException(json_response)
