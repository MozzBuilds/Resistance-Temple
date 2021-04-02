from db.run_sql import run_sql

from models.session import Session

def select_all():
    sessions = []
    sql = 'SELECT * FROM sessions'
    results = run_sql(sql)
    for row in results:
        session = Session(row['name'], row['id'])
        sessions.append(session)
    return sessions