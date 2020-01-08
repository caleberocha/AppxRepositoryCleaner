from utils import convert_to_binsid
from dbo import execute_query, execute_remove

def get_user(usersid):
    return execute_query(f"""
        SELECT
            _UserID,
            hex(UserSid) as UserSid
        FROM User
        WHERE u.UserSid = {convert_to_binsid(usersid)}
    """)

def remove_user(usersid):
    return execute_remove(
        f"""
            DELETE
            FROM User
            WHERE UserSid = X'{convert_to_binsid(usersid)}'
        """,
        None,
        "User"
    )

# def get_user_id(usersid):
#     rs = execute_query(f"""
#         SELECT _UserID
#         FROM User
#         WHERE UserSid = X'{convert_to_binsid(usersid)}'
#     """)
    
#     try:
#         user_id = rs[0][0]
#     except IndexError:
#         user_id = None
#     return user_id