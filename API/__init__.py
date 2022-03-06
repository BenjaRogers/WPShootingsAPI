from app import app
from models import Person, User
from views import *

if __name__ == '__main__':
    app.run(debug=True)