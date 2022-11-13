from flask.cli import FlaskGroup
import unittest
import coverage

from project import create_app, db
from project.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)
COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py'
    ]
)
COV.start()

@cli.command(name="recreate_db", help="Recreate db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command(name="cov", help="Run Coverage")
def cov():
    ''' 
    Runs the unit tests with coverage
    to see which parts of the code are, and are not,
    coverted by a test
    '''
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print("Coverage Summary:")
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1

@cli.command(name='test')
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command(name='seed_db')
def seed_db():
    """ Seeds the database """
    db.session.add(User(username='anya', email='anya@spyx.com'))
    db.session.add(User(username='loid', email='loid@spyx.com'))
    db.session.commit()

if __name__ == "__main__":
    cli()