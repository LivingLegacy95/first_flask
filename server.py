from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
from user import User

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

#! CREATE
@app.route('/new')
def new():
    return render_template('new.html')


@app.route('/create', methods=['post'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/')

#! READ ALL
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    users = User.get_all()
    # print(users)
    return render_template('index.html', users = users)  # Return the string 'Hello World!' as a response

#! READ ONE
@app.route('/user/<int:id>')
def show(id):
    data = {'id': id}
    user = User.get_user(data)
    return render_template('show.html', user = user)



#! UPDATE
@app.route('/user/edit/<int:id>')
def edit_user(id):
    data = {'id': id}
    return render_template('edit.html', user = User.get_user(data))

@app.route('/update', methods=['post'])
def update_user():
    print(request.form)
    User.update_user(request.form)
    return redirect('/')


#! DELETE
@app.route('/user/delete/<int:id>')
def delete_user(id):
    data = {'id': id}
    User.delete_user(data)
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)