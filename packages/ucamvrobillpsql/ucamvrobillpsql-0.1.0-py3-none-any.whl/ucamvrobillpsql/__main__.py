import logging
import sys

# from datetime import datetime
from ucamvrobillpsql import VERSION, utils
from ucamvrobillpsql.DBA import DB
from ucamvrobillpsql.exceptions import DbException
from ucamvrobillpsql.secrets import password


def setloggerdetail():
    LOG = logging.getLogger(__name__)
    stdout_handler = logging.StreamHandler(sys.stdout)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        handlers=[stdout_handler],
    )
    return LOG


def main():
    LOG = setloggerdetail()
    LOG.info(f"VERSION : {VERSION}")
    db_params = {
        "dbname": "vrobilling",
        "user": "postgres",
        "password": password,
        "host": "infra-db.srv.uis.cam.ac.uk",  # or your database host
        "port": "5432",  # default PostgreSQL port
        "sslmode": "require",  # or 'verify-ca' or 'verify-full' based on your needs
        "sslrootcert": "./ca.crt",  # path to your client certificate
    }
    db = DB(db_params)

    if not utils.pre_setupconfig(db_params):
        raise DbException("ERROR: Tables are not created successfully")

    # print(db.insert_vrauser("ll221", "leny"))
    # print(db.get_vrauser("ll221"))
    # print(db.get_vrauser_primary_key("ll221"))
    # db.update_vrauser("ll221", "bda20", 'Ben Argyle')
    # print(db.get_vrauser())
    # db.remove_vrauser('bda20')
    # print(db.insert_vrauser("ll220", "len"))
    # print(db.get_vrauser_by_id(2))
    # print(db.insert_vrauser("ll220", "len"))
    # print(db.get_vrauser())

    # print(db.insert_project("Project01","UIS Group"))
    # print(db.insert_project("Project02","CSC Group"))
    # print(db.get_project())
    # db.update_project(2, "Project03", "VET Group")
    # print(db.get_project())
    # db.remove_project(1)
    # print(db.get_project())
    # print(db.get_project_primary_key("Project03"))
    # print(db.get_project(2))
    # print(db.get_project("Project03"))
    # print(db.get_project())

    # print(db.insert_paymentsource("grant",21001))
    # print(db.get_paymentsource())
    # print(db.insert_paymentsource("project"))
    # print(db.get_paymentsource())
    # print(db.insert_paymentsource("grant",21002))
    # print(db.get_paymentsource('grant'))
    # print(db.get_paymentsource("grant","21001"))
    # print(db.get_paymentsource_primary_key("grant",21002))
    # print(db.get_paymentsource_primary_key("project"))
    # print(db.get_paymentsource_by_id(5))
    # print(db.get_paymentsource())
    # db.remove_paymentsource(1)

    # db.insert_deployment_id("1231ee112ad11212", 2)
    # print(db.get_deployment_id("1231ee112ad11212"))
    # print(db.get_deployment_id_primary_key("1231ee112ad11212"))
    # db.update_deployment_id(1, "1231a", 2)
    # print(db.get_deployment_id("1231a"))
    # print(db.get_deployment_id_primary_key("1231a"))
    # print(db.get_deployment_id_by_id(1))
    # db.remove_deployment_id(1)
    # print(db.get_deployment_id())
    # db.insert_charge(2, "Initial Resource",paymentsrc=2, paidby=1, cpucost=2.0,
    #                  ramcost=1.0, storagecost=0.3, totalcost=3.3)
    # db.insert_charge(2, "Initial Resource",paymentsrc=5, paidby=1,
    #                  cpucost=2.0, ramcost=1.0, storagecost=0.3, totalcost=3.3)
    # print(db.get_charge())
    # print(db.update_charge(2, 2, "Duration Expansion", new_paymentsrc=2,
    #                   new_paidby=1, new_cpucost=2.3, new_ramcost=4.0,
    #                   new_storagecost=3.0, new_totalcost=9.3))
    # print(db.get_charge())
    # print(db.get_charge(deployment_id=2, typee="Initial Resource"))
    # print(db.get_charge(typee="Initial Resource"))
    # print(db.get_charge())
    # print(db.get_charge_by_id(1))
    # db.remove_charge(1)
    # print(db.get_charge_primary_key(2, "Duration Expansion",paysource_id=2, paidby_id=1))
    # print(db.get_charge_primary_key(2, "Duration Expansion",paysource_id=2,
    #                                 paidby_id=1, datestmp=datetime(2025, 2, 19, 15, 0, 8, 693705)))
    # print(db.get_costing())

    db.closedb()


if __name__ == "__main__":
    main()
