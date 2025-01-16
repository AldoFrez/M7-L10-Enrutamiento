class MultiDBRouter:
    """
    Rutas para manejar las bases de datos 'default' y 'secondary'.
    """

    def db_for_read(self, model, **hints):
        """
        Asigna la base de datos para operaciones de lectura. # se debe identificar la relacion y el modelo
        """
        if model._meta.app_label == 'multi_app': # toma el modelo, la clase meta y app_label, y el modelo de la clase meta buscamos db_table y deberia estar en la BBD por default que es posgrest, reconoce a app_label
            if model._meta.db_table == 'modelo_primario': # modelo primario es tabla de models
                return 'default'  # la retorna a  PostgreSQL
            elif model._meta.db_table == 'secondary':
                return 'secondary'  # MySQL
        return None

    def db_for_write(self, model, **hints):
        """
        Asigna la base de datos para operaciones de escritura.
        """
        if model._meta.app_label == 'multi_app':
            if model._meta.db_table == 'modelo_primario':
                return 'default'  # PostgreSQL
            elif model._meta.db_table == 'secondary':
                return 'secondary'  # MySQL
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permite relaciones entre objetos en bases de datos diferentes.
        """
        db_list = ('default', 'secondary') 
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Controla qué migraciones se aplican a cada base de datos.
        """
        if app_label == 'multi_app':
            if model_name == 'modeloprimario':
                return db == 'default'  # PostgreSQL
            elif model_name == 'modelosecundario':
                return db == 'secondary'  # MySQL
        return None