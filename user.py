from db import get_db

class User():

    def __init__(self, user_id):
        self.user_id = user_id

    def get(user_id):
        # get the user from the database

        user = db.execute(
                'SELECT * '
                'FROM user '
                ' WHERE id = ?',
                (user_id,)
                ).fetchone()

    def is_authenticated:
        pass

    def is_active:
        pass

    def is_anonymous:
        pass

    def get_id:
        pass


