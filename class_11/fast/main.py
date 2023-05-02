from fastapi import FastAPI

app = FastAPI()

@app.get('/data')
def get_data(filter: str):
    # Use the filter value to filter data from a hypothetical database
    data = []
    if filter == 'foo':
        data = [{'id': 1, 'name': 'foo'}, {'id': 2, 'name': 'foo'}]
    elif filter == 'bar':
        data = [{'id': 3, 'name': 'bar'}, {'id': 4, 'name': 'bar'}]
    else:
        return {'detail': 'Invalid filter value'}, 400
    
    # Return the filtered data as a JSON response
    return {'data': data}
