from app import create_app

# This creates the actual Flask instance
app = create_app()

if __name__ == "__main__":
    # The port 5001 is common for Flask to avoid conflict with macOS AirPlay (port 5000)
    app.run(debug=True, port=5001)