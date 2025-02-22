import datetime as dt
import enum
import random
import string
from abc import abstractmethod

from sqlalchemy import MetaData, Column, text
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.dialects.postgresql import TIMESTAMP, TEXT

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "%(table_name)s_%(column_0_name)s_unique",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}

metadata = MetaData(naming_convention=convention)


class Base(DeclarativeBase):
    metadata = metadata

    def __repr__(self):
        """
        This method is used to represent the model instance in a more
        readable format.
        """
        try:
            identity = inspect(self).identity
        except:
            identity = self.__dict__
        return f'<{self.__class__.__name__} {identity}>'



class HumanIDMixin:
    __prefix__: str
    __id_length__: int = 16

    @declared_attr
    def id(cls):
        return Column(TEXT, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False, 
                        server_default=text('now()'))
    
    def __init__(self, *args, **kwargs):
        if not self.__prefix__:
            raise ValueError('No prefix defined')

        if len(self.__prefix__) > 4:
            raise ValueError("object prefix is too long")

        if 'id' not in kwargs or kwargs['id'] is None:
            kwargs['id'] = self.gen_obj_id(prefix=self.__prefix__,
                                           length=self.__id_length__)
        super().__init__(*args, **kwargs)

    @staticmethod
    def gen_obj_id(prefix: str, length: int):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choices(characters, k=length))
        return f'{prefix}_{random_string}'
