from com.utils.DBConnectionManager import DBConnectionManager
def create_team(data):
    conn = DBConnectionManager.getConnection()
    DBConnectionManager.add_row(conn.cursor(), 'ten_team', data)
def get_teams():
    conn = DBConnectionManager.getConnection()
    cursor = DBConnectionManager.getDicCursor(conn)
    sql = "select * from ten_team"
    cursor.execute(sql)
    return cursor.fetchall()