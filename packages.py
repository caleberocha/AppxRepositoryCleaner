from utils import convert_to_binsid
from dbo import execute_query, execute_remove

def get_packages(usersid = None):
    flt = "" if usersid is None else f"WHERE u.UserSid = X'{convert_to_binsid(usersid)}'"

    return execute_query(f"""
        SELECT
            pu._PackageUserID,
            p.PackageFullName,
            pu.User,
            hex(u.UserSid) as sid,
            CASE
                WHEN pu.DeploymentState = 2 THEN 'Installed'
                WHEN pu.DeploymentState = 1 THEN 'Staged'
                ELSE pu.DeploymentState
            END AS State
        FROM Package p
        JOIN PackageUser pu ON pu.Package = p._PackageID
        JOIN User u ON u._UserID = pu.User
        {flt}
    """)

def remove_package(packagefullname):
    return execute_remove(
        """
            DELETE
            FROM PackageUser pu
            JOIN Package p ON p._PackageID = pu.Package
            WHERE p.PackageFullName = ?
        """,
        (packagefullname,),
        'PackageUser',
        'Package'
    )

# def remove_user_packages(usersid):
#     return execute_remove(
#         f"""
#             DELETE
#             FROM PackageUser pu
#             JOIN User u ON u._UserID = pu.User
#             WHERE u.UserSid = {convert_to_binsid(usersid)}
#         """,
#         None,
#         'PackageUser'
#     )