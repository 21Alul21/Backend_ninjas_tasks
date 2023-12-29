from flask import Flask, jsonify, request
  
app = Flask(__name__) # intance of the app

data = {
'name': 'Austin',
'github': 'https://github.com/21Alul21',
'sex': 'male'
}

@app.route('/api/about', methods=['GET']) # using the .route decocator to create route
def about_route():
    if request.method == 'GET':
        return jsonify(data)
   


@app.route('/api/update', methods=['GET', 'POST'])
def update_data():
    if request.method == 'POST':
        new_data = request.get_json()
        return jsonify(new_data)

if __name__ == '__main__':
    app.run()
