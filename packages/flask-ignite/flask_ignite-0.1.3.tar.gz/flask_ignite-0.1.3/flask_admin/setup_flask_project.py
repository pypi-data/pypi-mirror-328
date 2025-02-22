import os
import argparse

# Define project structure
project_structure_template = {
    "flask_app": {
        "app": {
            "models": {
                "__init__.py": "",
                "user.py": """from ..extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
""",
                "post.py": """from ..extensions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<Post {self.title}>"
""",
            },
            "routes": {
                "__init__.py": "",
                "user_routes.py": """from flask import Blueprint, jsonify

bp = Blueprint("user", __name__)

@bp.route("/users")
def get_users():
    return jsonify({"message": "List of users"})
""",
                "post_routes.py": """from flask import Blueprint, jsonify

bp = Blueprint("post", __name__)

@bp.route("/posts")
def get_posts():
    return jsonify({"message": "List of posts"})
""",
            },
            "services": {
                "__init__.py": "",
                "user_service.py": """def get_all_users():
    return ["User1", "User2"]
""",
            },
            "config": {
                "__init__.py": "",
                "settings.py": """import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
""",
            },
            "extensions.py": """from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
""",
            "__init__.py": """from flask import Flask
from .config.settings import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import user_routes, post_routes
    app.register_blueprint(user_routes.bp, url_prefix="/api")
    app.register_blueprint(post_routes.bp, url_prefix="/api")

    return app
""",
        },
        "migrations": {},
        ".env": "DATABASE_URL=sqlite:///app.db",
        "config.py": """import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
""",
        "requirements.txt": """flask
flask-sqlalchemy
flask-migrate
python-dotenv
""",
        "wsgi.py": """from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
""",
        "run.py": """from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
""",
    }
}


# Function to create directories and files
def create_structure(base_path: str, structure: dict):
    """Create directories and files

    Args:
        base_path (str): Base path to create the structure
        structure (dict): Structure of the project
    """
    for name, content in structure.items():
        path = os.path.join(base_path, name)

        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)


def main():
    """Create the project structure"""
    parser = argparse.ArgumentParser(description="Generate a Flask project structure.")
    parser.add_argument(
        "--project",
        type=str,
        default="flask_app",
        help="Name of the project directory (default: flask_app)",
    )
    args = parser.parse_args()

    # Use the provided project name or default to 'flask_app'
    project_name = args.project

    # Build a new project structure with the given project name as the top-level folder
    project_structure = {project_name: project_structure_template["flask_app"]}

    base_dir = os.getcwd()
    create_structure(base_dir, project_structure)

    print("\n✅ Flask project structure created successfully!")
    print("\n👉 Next Steps:")
    print(f"1. Navigate into the project: `cd {project_name}`")
    print("2. Create a virtual environment: `python -m venv venv`")
    print("3. Activate the virtual environment:")
    print("   - Windows: `venv\\Scripts\\activate`")
    print("   - Mac/Linux: `source venv/bin/activate`")
    print("4. Install dependencies: `pip install -r requirements.txt`")
    print(
        "5. Initialize database: `flask db init && flask db migrate -m 'Initial' && flask db upgrade`"
    )
    print("6. Run the app: `python run.py`")


if __name__ == "__main__":
    main()
