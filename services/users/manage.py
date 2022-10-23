from unicodedata import name
from flask.cli import FlaskGroup

from project import app, db

cli = FlaskGroup(app)

@cli.command(name="recreate_db", help="Recreate db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    cli()