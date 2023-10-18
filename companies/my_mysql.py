import MySQLdb
import base64


password = ""

class use_of_proceed:
    def __init__(self):
        self.conn = MySQLdb.Connection(host="localhost", user="root", password=password, database="citi")


    def select_by_code(self, code: str):
        sql = f"select * from use_of_proceed where code = '{code}'"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        res = []
        for r in result:
            res.append({"id": r[0], "code": r[1], "category": r[2], "eligibility": r[3], "objective": r[4]})

        return res


    def insert(self, code: str, use: dict):
        category = use["category"]
        eligibility = use["eligibility"]
        objective = use["objective"]

        sql = "insert into use_of_proceed (code, category, eligibility, objective) " \
              f"values ('{code}', '{category}', '{eligibility}', '{objective}')"

        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()


    def delete_by_id(self, id):
        sql = f"delete from use_of_proceed where id = '{id}'"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()


    def update_by_id(self, id, use):
        category = use["category"]
        eligibility = use["eligibility"]
        objective = use["objective"]
        sql = f"update use_of_proceed set category = '{category}', eligibility = '{eligibility}', " \
              f"objective = '{objective}' where id = '{id}'"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()


    def close_db(self):
        self.conn.close()


if __name__ == '__main__':
    proceed = use_of_proceed()
    proceed.delete_by_id(4)
    print(proceed.select_by_code("09988HKSE"))
    proceed.close_db()
