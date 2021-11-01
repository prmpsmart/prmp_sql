"Access Control"

from keywords.non_reserved import ROLE
from keywords.reserved import GRANT as _GRANT, REVOKE as _REVOKE, CREATE, DROP
from . import STATEMENT


class Access_Control(STATEMENT):
    ...


GRANT = Access_Control([_GRANT], "Grants user access privileges")

REVOKE = Access_Control([_REVOKE], "Removes user access privileges")

CREATE_ROLE = Access_Control([CREATE, ROLE], "Adds a new role to the database")

GRANT_ROLE = Access_Control(
    [_GRANT, ROLE], "Grants role containing user access privileges"
)

DROP_ROLE = Access_Control([DROP, ROLE], "Removes a role from the database")
