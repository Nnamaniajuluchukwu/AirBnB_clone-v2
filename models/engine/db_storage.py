#!/usr/bin/python3
""" File Storage for AirBnB Clone Project """
""" Import necessary modules/ packages """
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base


class DBStorage:
    """
        This is the DataBase Storage class, that stores data in
        MySQL.
    """
    # Private class attributes
    __engine = None
    __session = None

    def __init__(self):
        """ Creating the engine by fetching environmental variables. """
        
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Return all the object data specified or all the data
            in the database.
        """
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review


        # Create an empty list row to store all the row data
        # gotten from the databse.
        rows = []
        if cls:
            rows = self.__session.query(cls) # Loaded as list of objects.
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for class_ in classes:
                # add each row of object in lsist to the list.
                rows += self.__session.query(class_)
        return {f'{row_obj.__class__.__name__}.{row_obj.id}': row_obj
                 for row_obj in rows}

    def new(self, obj):
        """ add the created object to session,
            but check if the obj is present. """
        if not obj:
            return        
        self.__session.add(obj)

    def save(self):
        """ commit changes to db """
        self.__session.commit()

    def delete(self, obj):
        """ delete object from db"""
        if not obj:
            return
        self.__session.delete(obj)
        self.save()

    def reload(self):
        """ reload the objects form the db"""
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        from sqlalchemy.orm import sessionmaker, scoped_session

        # create the object.
        Base.metadata.create_all(self.__engine)

        # Generate session that links to the current database.
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """ Close the session """
        self.__session.close()
