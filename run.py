from flask import Flask, jsonify, abort, make_response, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

# APP Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models DB
class Dealership(db.Model):
    id = Column(Integer, primary_key=True)
    brand = Column(String(250), nullable=False)
    price = Column(Float, nullable=False)
    color = Column(String(250), nullable=False)
    matriculation = Column(String(250), nullable=False)

    def __repr__(self):
        return "ID: {}, brand: {}, price: {}, color: {}, matriculation: {}".format(self.id, self.brand, self.price, self.color, self.matriculation)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'price': self.price,
            'color': self.color,
            'matriculation': self.matriculation
        }

# Functions
def get_cars():
    cars = Dealership.query.all()
    return jsonify(cars=[car.serialize for car in cars])

def post_car(brand, price, color, matriculation):
    car = Dealership(brand=brand, price=price, color=color, matriculation=matriculation)
    db.session.add(car)
    db.session.commit()
    return jsonify(car=car.serialize)

def get_car(id):
    car = Dealership.query.get_or_404(id)
    return jsonify(car=car.serialize)

def update_car(id, brand, price, color, matriculation):
    car = Dealership.query.get_or_404(id)
    if brand:
        car.brand = brand
    if price:
        car.price = price
    if color:
        car.color = color
    if matriculation:
        car.matriculation = matriculation
    db.session.add(car)
    db.session.commit()
    return make_response(jsonify({'Updated': 'Updated car with ID: {}'.format(id)}), 200)

def delete_car(id):
    car = Dealership.query.get_or_404(id)
    db.session.delete(car)
    db.session.commit()
    return make_response(jsonify({'Deleted': 'Removed Car with ID {}'.format(id)}), 200)

# Routes
@app.route('/')
def home():
    return render_template('documentation.html', title='Documentation')

@app.route('/api/cars', methods=['GET', 'POST'])
def carsFunction():
    if request.method == 'GET':
        return get_cars()

    elif request.method == 'POST':
        brand = request.json['brand']
        price = request.json['price']
        color = request.json['color']
        matriculation = request.json['matriculation']
        return post_car(brand, price, color, matriculation)

@app.route('/api/car/<id>', methods=['GET', 'PUT', 'DELETE'])
def carFunction(id):
    if not id:
        abort(404)

    if request.method == 'GET':
        return get_car(id)

    elif request.method == 'PUT':
        brand = request.json.get('brand', '')
        price = request.json.get('price', '')
        color = request.json.get('color', '')
        matriculation = request.json.get('matriculation', '')
        return update_car(id, brand, price, color, matriculation)

    elif request.method == 'DELETE':
        return delete_car(id)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
