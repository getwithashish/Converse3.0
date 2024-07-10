from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def bulk_save_objects(objects):
    db.session.bulk_save_objects(objects)
    db.session.commit()


def delete_objects(objects):
    for obj in objects:
        db.session.delete(obj)

    db.session.commit()
