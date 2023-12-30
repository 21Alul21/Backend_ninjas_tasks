from flask import Flask, jsonify, request
  
app = Flask(__name__) # intance of the app

data = {
'name': 'Austin',
'github': 'https://github.com/21Alul21',
'sex': 'male'
}

@app.route('/api', methods=['GET', 'POST']) # using the .route decocator to create route
def about_route():
    """ view function that handles both GET
    and POST requests
    """
    if request.method == 'GET':
        return jsonify(data), 200
    if request.method == 'POST':
       new_data = request.get_json()
       return jsonify(new_data), 201
   

if __name__ == '__main__':
    app.run()
