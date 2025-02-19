from .exceptions import SierraResponseConverterException


class SierraResponseConverter:
    """  Takes a JSON response from the Sierra API (https://tester.ester.ee/iii/sierra-api/swagger/index.html)
    and converts it to MARC-in-JSON format.
    
    """
    
    def __init__(self, response: dict):
        if not isinstance(response, dict):
            raise SierraResponseConverterException("Please provide a valid JSON response.")
        self.response = response
        
    def _map_field_data(self, field):
        tag = field.get("tag")
        if not tag:
            raise SierraResponseConverterException("Field is missing a valid 'tag'.")
        data = field.get("data", {})
        return {tag: data}
        
    def _convert_response(self):
        response = self.response
        
        entries = response.get("entries")
        if not entries:
            raise SierraResponseConverterException("No entries found in the response.")
        
        try:
            fields = [self._map_field_data(f) for e in entries for f in e["marc"]["fields"]]
        except KeyError as e:
            raise SierraResponseConverterException(f"Missing expected MARC fields in the response: {e}")
        
        return {"fields": fields}
            
    def convert(self):
        """Runner method, converts the response to MARC-in-JSON format with error handling."""
        try:
            return self._convert_response()
        except Exception as e:
            raise SierraResponseConverterException(f"An unexpected error occurred during conversion: {e}")
