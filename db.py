import sqlite3


class DBInterface():

    def get_connection(self):
        return sqlite3.connect('db/main.db')

    def execute_fetchone_close(self,query):
        conn = self.get_connection()
        res = conn.execute(query).fetchone()
        conn.commit()
        conn.close()
        return res

    def execute_fetchall_close(self,query):
        conn = self.get_connection()
        res = conn.execute(query).fetchall()
        conn.commit()
        conn.close()
        return res

    def get_status(self, tg_id):
        query = """
            select *
            from statuses
            where tg_id = {}
        """.format(tg_id)
        status = self.execute_fetchone_close(query)
        return status if status is None else status[2]

    def set_status(self, tg_id, status):
        query_delete = """
            delete from statuses
            where tg_id = {}
        """.format(str(tg_id))
        query_create = """
            insert into statuses (tg_id, status)
            values ({}, '{}')
        """.format(str(tg_id), str(status))
        self.execute_fetchone_close(query_delete)
        self.execute_fetchone_close(query_create)

    def log_message(self, tg_id, message, time, fname, lname, uname):
        query = """
            insert into raw_messages (user, message, time,
            first_name, last_name, username)
            values ({}, '{}', {}, '{}', '{}', '{}');
        """.format(str(tg_id), str(message), str(time), fname, lname, uname)
        self.execute_fetchone_close(query)

    def get_place_by_id(self, place_id):
        query = """
            select * from places
            where id='{}'
        """.format(str(place_id))
        res = self.execute_fetchone_close(query)
        return res
