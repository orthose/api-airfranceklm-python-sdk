class FlatteningException(Exception):
    def __init__(self):
        Exception.__init__(self, f'Exception when converting JSON to Pandas DataFrame')