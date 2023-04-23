`# checklist

- [x] create a new directory
- [x] inside the directory run:

```bash
pipenv install flask
```

- [ ] activate the virtual environment

```bash
pipenv shell
```

- [ ] create [server.py](server.py)

```bash
from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

## MORE ROUTES HERE 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
``` 

- [ ] go to [localhost:5000](http://localhost:5000/)
- [ ] create a [templates](templates/index.html)

## Connect to a database

- [ ] create ERD: ![](comics_ERD.png)
- [ ] install the module to connect flask to mysql:

```bash
pipenv install pymysql
```

- [ ] create [mysqlconnection.py](mysqlconnection.py)
- [ ] create [comics.py](comics.py)