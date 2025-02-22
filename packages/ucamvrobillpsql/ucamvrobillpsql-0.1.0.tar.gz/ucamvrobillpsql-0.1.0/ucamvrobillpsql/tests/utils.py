import psycopg2
import time

from ucamvrobillpsql import utils
from ucamvrobillpsql.DBA import DB
from ucamvrobillpsql.exceptions import DbException
from ucamvrobillpsql.tests.dbconnect import db_params

db_params = db_params

tables = {
    "user": "test_vrauser",
    "project": "test_vraproject",
    "paysources": "test_paymentsources",
    "deploymentid": "test_vradeploymentid",
    "charges": "test_charges",
}


def check_db_connection(data_params):
    retries = 3
    state = False
    while retries > 0:
        try:
            conn = psycopg2.connect(**db_params)
            state = True
            break
        except psycopg2.OperationalError:
            time.sleep(2)  # Wait for 2 seconds before retrying
            retries -= 1
    if state:
        conn.close()
    return state


def setup_user_table_func(data_params):
    utils.create_user_table(tables.get("user"), data_params)
    db = DB(db_params)
    return db


def teardown_user_table_func(data_params):
    return utils.drop_table(tables.get("user"), data_params)


def setup_project_table_func(data_params):
    db = DB(db_params)
    utils.create_project_table(tables.get("project"), data_params)
    return db


def teardown_project_table_func(data_params):
    return utils.drop_table(tables.get("project"), data_params)


def setup_paysources_table_func(data_params):
    db = DB(db_params)
    utils.create_paysource_table(tables.get("paysources"), data_params)
    return db


def teardown_paysources_table_func(data_params):
    return utils.drop_table(tables.get("paysources"), data_params)


def setup_deployment_table_func(data_params):
    if utils.create_project_table(tables.get("project"), data_params):
        utils.create_deployment_table(
            tables.get("deploymentid"), tables.get("project"), data_params
        )
        db = DB(db_params)
        return db
    raise DbException("Creation of the deployment DB failed.")


def teardown_deployment_table_func(data_params):
    result = []
    result.append(utils.drop_table(tables.get("deploymentid"), data_params))
    result.append(utils.drop_table(tables.get("project"), data_params))
    return False not in result


def setup_charges_table_func(data_params):
    db = DB(db_params)
    if utils.create_user_table(tables.get("user"), data_params):
        if utils.create_project_table(tables.get("project"), data_params):
            if utils.create_deployment_table(
                tables.get("deploymentid"), tables.get("project"), data_params
            ):
                if utils.create_paysource_table(tables.get("paysources"), data_params):
                    if utils.create_charge_table(
                        tables.get("charges"),
                        tables.get("deploymentid"),
                        tables.get("paysources"),
                        tables.get("user"),
                        data_params,
                    ):
                        return db
    raise DbException("Creation of the charges DB failed.")


def teardown_charges_table_func(data_params):
    result = []
    result.append(utils.drop_table(tables.get("charges"), data_params))
    result.append(utils.drop_table(tables.get("deploymentid"), data_params))
    result.append(utils.drop_table(tables.get("project"), data_params))
    result.append(utils.drop_table(tables.get("paysources"), data_params))
    result.append(utils.drop_table(tables.get("user"), data_params))
    return False not in result
