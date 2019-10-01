from app_db1.apps import AppDb1Config

class Router_C(object):
    """
    A router to control all database operations on models in the
    app_db1 application.
    """
    
    db = 'db1'

    def db_for_read(self, model, ** hints):
        """
        Attempts to read app_db1 models go to db1.
        """

        return self.db

    def db_for_write(self, model, ** hints):
        """
        Attempts to write app_db1 models go to db1.
        """

        return self.db

    def allow_relation(self, obj1,obj2, ** hints):
        """
        Allow relations if a model in the app_db1 app is involved.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, ** hints):
        """
        Make sure the auth app only appears in the 'db1'
        database.
        """
        return True
