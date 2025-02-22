import logging
from typing import Callable, Dict

from ucamvrobillpsql.DBA import DB
from ucamvrobillpsql.exceptions import DbException
from ucamvrobillpsql.tools import DEFAULT_TABLES

LOG = logging.getLogger(__name__)


def pre_setupconfig(db_params: Dict[str, str]) -> bool:
    """Create the Database

    Args:
        db_params (Dict[str, str]): provide parameters for DB connection.

    Returns:
        bool: True if creation of database is suceess else False
    """
    result = []
    if not check_table_exists(DEFAULT_TABLES.get("user"), db_params):
        result.append(create_user_table(DEFAULT_TABLES.get("user"), db_params))
    if not check_table_exists(DEFAULT_TABLES.get("project"), db_params):
        result.append(create_project_table(DEFAULT_TABLES.get("project"), db_params))
    if not check_table_exists(DEFAULT_TABLES.get("paysources"), db_params):
        result.append(
            create_paysource_table(DEFAULT_TABLES.get("paysources"), db_params)
        )
    if not check_table_exists(DEFAULT_TABLES.get("deploymentid"), db_params):
        result.append(
            create_deployment_table(
                DEFAULT_TABLES.get("deploymentid"),
                DEFAULT_TABLES.get("project"),
                db_params,
            )
        )
    if not check_table_exists(DEFAULT_TABLES.get("charges"), db_params):
        result.append(
            create_charge_table(
                DEFAULT_TABLES.get("charges"),
                DEFAULT_TABLES.get("deploymentid"),
                DEFAULT_TABLES.get("paysources"),
                DEFAULT_TABLES.get("user"),
                db_params,
            )
        )
    return False not in result


def create_table(tablename: str, db_params: Dict[str, str], design: str) -> bool:
    """Creation of table with provided design

    Args:
        tablename (str): Name of the table to be created.
        db_params (Dict[str, str]): provide parameters for DB connection
        design (str): design to be created.

    Raises:
        DbException: Exception for the provided inputs.

    Returns:
        bool: True for the success and False for the failure.
    """
    db = DB(db_params)
    conn = db.db_connection()
    cursor = db.db_cursor()
    with conn:
        try:
            cursor.execute(design)
            LOG.info(f"Creation of the table '{tablename}' has been successful.")
            return True
        except Exception as e:
            LOG.error(f"Error: Creation of table '{tablename}' failed: \n {e}")
            raise DbException(f"Error: Creation of table '{tablename}' failed: \n {e}")


def drop_table(tablename: str, db_params: Dict[str, str]) -> bool:
    """Drop the table.

    Args:
        tablename (str): Name of the table to be created.
        db_params (Dict[str, str]): provide parameters for DB connection.

    Raises:
        DbException: Exception for the provided inputs.

    Returns:
        bool: True for the success and False for the failure.
    """
    db = DB(db_params)
    conn = db.db_connection()
    cursor = db.db_cursor()
    with conn:
        try:
            cursor.execute(f'DROP TABLE "{tablename}";')
            LOG.info(f"Drop of the table '{tablename}' has been successful.")
            return True
        except Exception as e:
            LOG.error(f"Error: Drop of table {tablename} failed: \n {e}")
            raise DbException(f"Error: Drop of table {tablename} failed: \n {e}")


def create_user_table(
    tablename: str, db_params: Dict[str, str]
) -> Callable[[str, Dict[str, str], str], bool]:
    """create the user table.

    Args:
        tablename (str): Name of the table to be created.
        db_params (Dict[str, str]): provide parameters for DB connection.

    Returns:
        Callable[[str, Dict[str, str], str], bool]: Invoke the create table function.
    """
    design = f"CREATE TABLE {tablename} (\
        id SERIAL PRIMARY KEY, \
        crsid VARCHAR(255) UNIQUE, \
        name VARCHAR(255)\
        );"
    return create_table(tablename, db_params, design)


def create_project_table(
    proj_tablename: str, db_params: Dict[str, str]
) -> Callable[[str, Dict[str, str], str], bool]:
    """create the project table.

    Args:
        proj_tablename (str): Name of the project table to be created.
        db_params (Dict[str, str]): provide parameters for DB connection.

    Returns:
        Callable[[str, Dict[str, str], str], bool]: Invoke the create table function.
    """
    design = f"CREATE TABLE {proj_tablename} (\
        id SERIAL PRIMARY KEY, \
        projectname VARCHAR(255), \
        projectadmingroup VARCHAR(255) \
        );"
    return create_table(proj_tablename, db_params, design)


def create_paysource_table(
    paysrc_tablename: str, db_params: Dict[str, str]
) -> Callable[[str, Dict[str, str], str], bool]:
    """create the pay source table.

    Args:
        paysrc_tablename (str): Name of the paymentsource table to be created.
        db_params (Dict[str, str]): provide parameters for DB connection.

    Returns:
        Callable[[str, Dict[str, str], str], bool]: Invoke the create table function.
    """
    design = f"BEGIN;\
            CREATE TABLE {paysrc_tablename} (\
            id SERIAL PRIMARY KEY,\
            type VARCHAR(255) CHECK (type IN ('project', 'grant')),\
            code VARCHAR(255),\
            UNIQUE (type, code)\
            );\
            CREATE UNIQUE INDEX unique_project_grant_code_null ON {paysrc_tablename} (type)\
            WHERE type = 'project' OR type = 'grant' AND code IS NULL;\
            COMMIT;"
    return create_table(paysrc_tablename, db_params, design)


def create_deployment_table(
    tablename: str, project_tablename: str, db_params: Dict[str, str]
) -> Callable:
    """create the deployment table.

    Args:
        tablename (str): Name of the table to be created.
        project_tablename (str): Name of the project table to be referred.
        db_params (Dict[str, str]): provide parameters for DB connection.

    Returns:
        Callable[[str, Dict[str, str], str], bool]: Invoke the create table function.
    """
    design = f"CREATE TABLE {tablename} (\
            id SERIAL PRIMARY KEY,\
            deploymentid VARCHAR(50) UNIQUE, \
            projectid INTEGER REFERENCES {project_tablename}(id) \
     );"
    return create_table(tablename, db_params, design)


def create_charge_table(
    charge_tablename: str,
    deploy_tablename: str,
    paysrc_tablename: str,
    user_tablename: str,
    db_params: Dict[str, str],
) -> Callable[[str, Dict[str, str], str], bool]:
    """create the charge table.

    Args:
        charge_tablename (str): Name of the charge table to be created.
        deploy_tablename (str): Name of the deploy table to be referred.
        paysrc_tablename (str): Name of the payment source table to be referred.
        user_tablename (str): Name of the user table to be referred.
        db_params (Dict[str, str]): provide parameters for DB connection.

    Returns:
        Callable[[str, Dict[str, str], str], bool]: Invoke the create table function.
    """
    design = f"CREATE TABLE {charge_tablename} (\
            id SERIAL PRIMARY KEY,\
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\
            type VARCHAR(100) CHECK (type IN ('Resource Expansion', 'Duration Expansion', 'Initial Resource')),\
            deployment_id INTEGER REFERENCES {deploy_tablename}(id),\
            paysource INTEGER REFERENCES {paysrc_tablename}(id),\
            cpucost FLOAT DEFAULT 0.0, \
            ramcost FLOAT DEFAULT 0.0, \
            storagecost FLOAT DEFAULT 0.0, \
            totalcost FLOAT NOT NULL,\
            paidby INTEGER REFERENCES {user_tablename}(id) \
        );"
    return create_table(charge_tablename, db_params, design)


def check_table_exists(table_name: str, db_params: Dict[str, str]) -> bool:
    """Check the status of the table.

    Args:
        table_name (str): Name of the table to be checked.
        db_params (Dict[str, str]): provide parameters for DB connection.

    Raises:
        DbException: Exception for the provided inputs.

    Returns:
        bool: True for the success of table search and False for the failing in table search.
    """
    db = DB(db_params)
    conn = db.db_connection()
    cursor = db.db_cursor()
    with conn:
        try:
            cursor.execute(
                f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}' \
                AND table_schema = 'public')"
            )
            exists = cursor.fetchone()[0]
            LOG.info(f"'{table_name}' status : {exists}")
            return exists
        except Exception as e:
            LOG.error(f"Error: checking of table {table_name} failed: \n {e}")
            raise DbException(f"Error: checking of table '{table_name}' failed: \n {e}")
