import main

if __name__ == '__main__':
    db.create_all()
    add_test_data()
    app.run(debug=True)