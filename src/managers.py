from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from models import LogBook


class LogBookManager:

    model = LogBook

    def __init__(self):
        self.engine = create_engine('sqlite:///logbook.sqlite3', echo=True)
        self.session = sessionmaker()

        if not inspect(self.engine).has_table(self.model.__tablename__):
            self.model.metadata.create_all(bind=self.engine)
