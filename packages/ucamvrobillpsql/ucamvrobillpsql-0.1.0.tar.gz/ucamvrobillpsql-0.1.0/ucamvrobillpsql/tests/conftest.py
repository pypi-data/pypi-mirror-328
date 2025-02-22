import pytest

from ucamvrobillpsql.tests import utils as tools
from ucamvrobillpsql.exceptions import DbException


data_params = tools.db_params


@pytest.fixture
def user_db_fixture():
    # Setup
    if tools.check_db_connection(data_params):
        db = tools.setup_user_table_func(data_params)
        yield db
        # tear_down
        tools.teardown_user_table_func(data_params)
    else:
        raise DbException("Could not connect to the database after several retries.")


@pytest.fixture
def deploymentid_db_fixture():
    # Setup
    if tools.check_db_connection(data_params):
        db = tools.setup_deployment_table_func(data_params)
        yield db
        tools.teardown_deployment_table_func(data_params)
    else:
        raise DbException("Could not connect to the database after several retries.")


@pytest.fixture
def project_db_fixture():
    # Setup
    if tools.check_db_connection(data_params):
        db = tools.setup_project_table_func(data_params)
        yield db
        tools.teardown_project_table_func(data_params)
    else:
        raise DbException("Could not connect to the database after several retries.")


@pytest.fixture
def paysources_db_fixture():
    # Setup
    if tools.check_db_connection(data_params):
        db = tools.setup_paysources_table_func(data_params)
        yield db
        tools.teardown_paysources_table_func(data_params)
    else:
        raise DbException("Could not connect to the database after several retries.")


@pytest.fixture
def charges_db_fixture():
    # Setup
    if tools.check_db_connection(data_params):
        db = tools.setup_charges_table_func(data_params)
        yield db
        tools.teardown_charges_table_func(data_params)
    else:
        raise DbException("Could not connect to the database after several retries.")
