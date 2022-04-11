
from app import app, db


@app.route('/')
def index():
    return 'Vinyls'


# def login():
#     pass


# def register():
#     pass


# def logout():
#     pass


# def vinyl():
#     pass