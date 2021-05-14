from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from .models import LogBook
from .utils import get_database_url


class LogBookManager:

    model = LogBook

    def __init__(self):
        self.engine = create_engine(get_database_url(), echo=False)
        self.session = sessionmaker(bind=self.engine)()

        if not inspect(self.engine).has_table(self.model.__tablename__):
            self.model.metadata.create_all(bind=self.engine)

    def list(self):
        return self.session.query(self.model).order_by(
            self.model.log_datetime.desc()
        ).limit(20).all()

    def find(self, description_contains):
        return self.session.query(self.model).filter(
            self.model.description.contains(description_contains)
        ).order_by(
            self.model.log_datetime.desc()
        ).all()

    def get(self, id):
        return self.session.query(self.model).get(id)

    def create(self, description, log_datetime):
        log_entry = self.model(
            description=description,
            log_datetime=log_datetime
        )

        try:
            self.session.add(log_entry)
            self.session.commit()
            return (True, 'Log Entry Created')
        except Exception as e:
            self.session.rollback()
            return (False, f'An error occured while creating Log Entry. {e}')

    def update(self, id, description=None, log_datetime=None):
        if not description and not log_datetime:
            return (False, 'You must provide "--description" and/or "--date and --time"')

        log_entry = self.session.query(self.model).get(id)

        if log_entry:
            if description:
                log_entry.description = description

            if log_datetime:
                log_entry.log_datetime = log_datetime

            try:
                self.session.commit()
                return (True, 'Log Entry Updated')
            except Exception as e:
                self.session.rollback()
                return (False, f'An error occured while updating Log Entry. {e}')
        else:
            return (False, f'No Log Entry found with id={id}')

    def delete(self, id):
        delete_count = self.session.query(self.model).filter_by(id=id).delete()

        if delete_count > 0:
            try:
                self.session.commit()
                return (True, 'Log Entry Deleted')
            except Exception as e:
                self.session.rollback()
                return (False, f'An error occured while deleting Log Entry. {e}')
        else:
            return (False, f'No Log Entry found with id={id}')
