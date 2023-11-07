from flask import Flask, jsonify, request, g,send_file
import sqlite3
import io

app = Flask(__name__)

#Sqlite database config

DATABASE = '/app/d.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/query', methods=['GET'])
def query_database() :
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT id, name, associated_file_name, version FROM data')
        results = cursor.fetchall()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_file/<int:id>', methods=['GET'])
def get_file(id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT associated_file_data, associated_file_name FROM data WHERE id = ?', (id,))
        file_data, file_name = cursor.fetchone()

        #serve the file via Flask's send_file
        response = send_file(io.BytesIO(file_data), mimetype='application/tar-x')

        #Set content-disposition header to specify the file_name
        response.headers['Content-Disposition'] = f'attachment; filename="{file_name}"'
        
        return response
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5000)


