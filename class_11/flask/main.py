from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Get the value of the 'filter' query parameter from the URL
    filter_value = request.args.get('filter')
    
    # Use the filter value to filter data from a hypothetical database
    data = []
    if filter_value == 'foo':
        data = [{'id': 1, 'name': 'foo'}, {'id': 2, 'name': 'foo'}]
    elif filter_value == 'bar':
        data = [{'id': 3, 'name': 'bar'}, {'id': 4, 'name': 'bar'}]
    else:
        return 'Invalid filter value', 400
    
    # Return the filtered data as a JSON response
    return {'data': data}

if __name__ == '__main__':
    app.run(debug=True)
