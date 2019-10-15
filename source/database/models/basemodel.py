from peewee import Proxy

class BaseModel(Model):
    """
    Base Model. Import this to all Peewee models for inheritance.
    """

    class Meta:
        database = Proxy()
