from .router1 import Router_A

class Router_B(object):
    """
    A router to control all database operations on models in the
    app_db2 application.
    """

    app_db = ['db2',]

    def db_for_read(self, model, ** hints):#model._state.db
        print("db2 ... read request ...")
        return self.app_db[0]

    def db_for_write(self, model, ** hints):
        print("db2 ... write request ...")
        return self.app_db[0]

    def allow_relation(self, obj1,obj2, ** hints):
        """
        Allow relations if a model in has same database.
        """
        print("db2 ... relation request ...")
        #db is same and obj1._state.db in self.app_db
        return obj1._state.db == obj2._state.db and \
            obj1._state.db in self.app_db

    def allow_migrate(self, db, app_label, model_name=None, ** hints):
        """
        Make sure the auth app only appears in the 'db2'
        database.
        """
        print("db2 ... %s ... migrate request ..." % (model_name,))
        #print(db)
        #print(app_label)
        #print(model_name)
        #print(hints)

        if db == self.app_db[0]:
            if app_label in Router_A.apps:
                return False

            return True

        #if app_label in apps_a:
        #    return True
        #
        #return None

        print("db2 ... fail ...")
        return False
