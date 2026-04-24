from app import app  # Import your Flask app
from io import BytesIO
from base64 import b64encode

def handler(request):
    # Handle Vercel serverless environment
    if request.method == 'GET':
        # Handle GET requests
        with app.test_client() as client:
            response = client.get(request.path, query_string=request.args)
    else:
        # Handle POST requests
        with app.test_client() as client:
            response = client.post(
                request.path, 
                data=request.get_data(),
                query_string=request.args,
                content_type=request.headers.get('Content-Type', 'application/json')
            )
    
    # Convert response to Vercel format
    headers = dict(response.headers)
    body = response.get_data()
    
    # Handle binary data (like images)
    if 'image' in headers.get('Content-Type', ''):
        body = b64encode(body).decode('utf-8')
        is_base64 = True
    else:
        is_base64 = False
    
    return {
        'statusCode': response.status_code,
        'headers': headers,
        'body': body,
        'isBase64Encoded': is_base64
    }
