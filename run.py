from app import create_app
from app.models import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # creat las tablas si no existen
    app.run(debug=True)  # correr el server en modo desarrollo
# Funcional