from flask import Flask, request
import pymysql

app = Flask(__name__)

# === Database connection setup ===
db = pymysql.connect(
    host="localhost",
    user="chess_user",
    password="StrongPassword123!",
    database="chess_academy"
)

@app.route('/enroll', methods=['POST'])
def enroll():
    data = request.form

    try:
        with db.cursor() as cursor:
            sql = """
                INSERT INTO enrollments 
                (parent_name, email, phone, child_name, age, school, program, location, notes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                data.get('parent_name'),
                data.get('email'),
                data.get('phone'),
                data.get('child_name'),
                int(data.get('age')),
                data.get('school'),
                data.get('program'),
                data.get('location'),
                data.get('notes')
            )
            cursor.execute(sql, values)
            db.commit()

        return "Enrollment submitted successfully!", 200

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# === Run server ===
if __name__ == '__main__':
    app.run(debug=True)

