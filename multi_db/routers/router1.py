from app_db1.apps import AppDb1Config

class Router_A(object):
    """
    A router to control all database operations on models in the
    app_db1 application.
    """

    apps = [AppDb1Config.name,]
    db = 'db1'

    def db_for_read(self, model, ** hints):
        """
        Attempts to read app_db1 models go to db1.
        """

        print("read request")

        #model._meta.app_label
        #model._meta.model
        #model._meta.model_name
        #model._meta.object_name
        #model._state.db

        if model._meta.app_label in self.apps:
            return self.db

        return None

    def db_for_write(self, model, ** hints):
        """
        Attempts to write app_db1 models go to db1.
        """

        print("write request")

        if model._meta.app_label in self.apps:
            return self.db

        return None

    def allow_relation(self, obj1,obj2, ** hints):
        """
        Allow relations if a model in the app_db1 app is involved.
        """

        print("relation request")

        if obj1._meta.app_label in self.apps and \
           obj2._meta.app_label in self.apps:
            return True

        return None
        #return False

    def allow_migrate(self, db, app_label, model_name=None, ** hints):
        """
        Make sure the auth app only appears in the 'db1'
        database.
        """

        #print(db)
        #print(app_label)
        #print(model_name)
        #print(hints)

        if db == self.db:
            if app_label in self.apps:
                #print("ok ...")
                return True

        #print("fail ....")
        return None
        #return False
