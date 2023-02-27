from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)

# Crear modelo de base de datos 
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(11), nullable=False)


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }

    # def __init__(self, name, email, phone) -> None:
    #     self.name = name
    #     self.email = email
    #     self.phone = phone

    # def as_dict(self):
    #     return {'id': self.id, 'name': self.name, 'email': self.email, 'phone': self.phone}

# Crea las trablas en la base de datos
with app.app_context():
    db.create_all()


# Obtener todos los contactos
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify({'contacts': [contact.serialize() for contact in contacts]})

# Obtener un contacto por su id
@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({'message': 'Contacto no encontrado'}), 404
    return jsonify(contact.serialize())

# Crear un nuevo contacto
@app.route('/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    contact = Contact(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(contact)
    db.session.commit()
    return jsonify({'message': 'Contacto creado con éxito', 'contact': contact.serialize()})

# Editar un contacto existente
@app.route('/contacts/<int:contact_id>', methods=['PUT', 'PATCH'])
def edit_contact(contact_id):
    # Buscar el contacto por su ID
    contact = Contact.query.get_or_404(contact_id)

    # Obtener los datos enviados por el usuario
    data = request.get_json()

    # Actualizar los campos del contacto con los nuevos datos
    if 'name' in data:
        contact.name = data['name']
    if 'email' in data:
        contact.email = data['email']
    if 'phone' in data:
        contact.phone = data['phone']

    # Guardar los cambios en la base de datos
    db.session.commit()

    # Devolver los datos actualizados del contacto
    #return jsonify(contact.as_dict())
    return jsonify({'message': 'Contacto actualizado con éxito', 'contact': contact.serialize()})

# Eliminar un contacto existente
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({'message': 'Contacto no encontrado'}), 404
    db.session.delete(contact)
    db.session.commit()
    return

# # Crear todas las rutas 
# @app.route('/contacts', methods=['POST'])
# def add_contact():
#     data = request.get_json()
#     contact = Contact(data['name'], data['email'], data['phone'])
#     db.session.add(contact)
#     db.session.commit()
#     return jsonify(contact.as_dict()), 201


# @app.route('/contacts', methods=['GET'])
# def get_contacts():
#     contacts = Contact.query.all()
#     # list_contact = []
#     # for contact in contacts:
#     #     list_contact.append(contact.as_dict())
#     # return jsonify(list_contact)
#     return jsonify([contact.as_dict() for contact in contacts])

# @app.route('/contacts/<int:id>', methods=['GET'])
# def get_contact(id):
#     contact = Contact.query.get_or_404(id)
#     return jsonify(contact.as_dict())

# @app.route('/contacts/<int:id>', methods=['PUT'])
# def update_contact(id):
#     contact = Contact.query.get_or_404(id)
#     data = request.get_json()
#     contact.name = data.get('name', contact.name)
#     contact.email = data.get('email', contact.email)
#     contact.phone = data.get('phone', contact.phone)
#     db.session.commit()
#     return jsonify(contact.as_dict())

# @app.route('/contacts/<int:id>', methods=['DELETE'])
# def delete_contact(id):
#     contact = Contact.query.get_or_404(id)
#     db.session.delete(contact)
#     db.session.commit()
#     return '', 204