from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_data = {
            'code': getattr(exc, 'default_code', 'error').upper(),
            'message': response.data.get('detail', str(exc))
        }
        
        # If it's a validation error, include field details
        if response.status_code == 400 and isinstance(response.data, dict):
            custom_data['fields'] = response.data

        response.data = custom_data

    return response
