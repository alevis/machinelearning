#!../kenv/bin/python
from app import app
if __name__=="__main__":
    app.run('localhost', port=8000, debug=True)
