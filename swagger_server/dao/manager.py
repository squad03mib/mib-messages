from swagger_server import db


class Manager(object):

    @staticmethod
    def check_none(**kwargs):
        for name, arg in zip(kwargs.keys(), kwargs.values()):
            if arg is None:
                raise ValueError('You can\'t set %s argument to none' % name)

    @staticmethod
    def create(**kwargs):
        Manager.check_none(**kwargs)

        for bean in kwargs.values():
            db.add(bean)

        db.commit()

    @staticmethod
    def retrieve():
        ''' 
        It should be implemented by child
        :return:
        '''
        pass

    @staticmethod
    def update(**kwargs):
        Manager.check_none(**kwargs)
        db.commit()

    @staticmethod
    def delete(**kwargs):
        Manager.check_none(**kwargs)

        for bean in kwargs.values():
            db.delete(bean)

        db.commit()
