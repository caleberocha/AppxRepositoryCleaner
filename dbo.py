import sqlite3

#APPX_REPOSITORY = "C:\\ProgramData\\Microsoft\\Windows\\AppRepository\\StateRepository-Machine.srd"
APPX_REPOSITORY = "StateRepository-Machine.srd"

def execute_query(query, params=None):
    conn = sqlite3.connect(APPX_REPOSITORY)
    cursor = conn.cursor()
    cursor.execute(query) if params is None else cursor.execute(query, params)
    rs = cursor.fetchall()
    conn.close()
    return rs

def execute_nonquery(query, params=None):
    conn = sqlite3.connect(APPX_REPOSITORY)
    cursor = conn.cursor()
    cursor.execute(query) if params is None else cursor.execute(query, params)
    rs = cursor.rowcount
    conn.commit()
    conn.close()
    return rs

def execute_remove(query, params, *tables):
    triggers = remove_deltriggers(tables)
    deleted = execute_nonquery(query, params)
    restore_deltriggers(triggers)
    return deleted

def get_deltriggers(tables):
    flt = "" if len(tables) == 0 else " AND ({})".format(" OR ".join([f"sql like '%DELETE ON {t} FOR%'" for t in tables]))
    
    return execute_query(f"""
        SELECT name, sql
        FROM sqlite_master
        WHERE type = 'trigger'{flt};
    """)

def remove_deltriggers(tables):
    triggers = get_deltriggers(tables)
    for t in triggers:
        execute_nonquery(f"DROP TRIGGER {t[0]}")
    return [t[1] for t in triggers]

def restore_deltriggers(triggers):
    for t in triggers:
        execute_query(t)