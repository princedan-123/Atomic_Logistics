from app import initialize_app

app = initialize_app()
app.run(host='localhost', port=5000, debug=True)