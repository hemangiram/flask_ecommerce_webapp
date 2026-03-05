from unwrap import app, db

with app.app_context():
    db.create_all()
    print("Tables Created Successfully!")

if __name__ == '__main__':
    app.run(debug=True)