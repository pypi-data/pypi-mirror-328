from ucamvrobillpsql.tests.utils import tables


def test_user_insertion(user_db_fixture):
    db = user_db_fixture
    result = db.insert_vrauser("im530", "Ishan", tables.get("user"))
    info = db.get_vrauser(None, None, tables.get("user"))
    assert len(info) == 1
    assert result


def test_user_update(user_db_fixture):
    db = user_db_fixture
    db.insert_vrauser("im530", "Ishan", tables.get("user"))
    result = db.update_vrauser("im530", "ll220", "Len", tables.get("user"))
    info = db.get_vrauser(None, None, tables.get("user"))
    assert len(info) == 1
    assert result
    assert info[0][1] == "ll220"


def test_user_remove(user_db_fixture):
    db = user_db_fixture
    db.insert_vrauser("im530", "Ishan", tables.get("user"))
    result = db.remove_vrauser("im530", tables.get("user"))
    info = db.get_vrauser(None, None, tables.get("user"))
    assert len(info) == 0
    assert result


def test_user_fetchall(user_db_fixture):
    db = user_db_fixture
    db.insert_vrauser("im530", "Ishan", tables.get("user"))
    db.insert_vrauser("im532", "Ishan", tables.get("user"))
    info = db.get_vrauser(None, None, tables.get("user"))
    assert len(info) == 2
    assert info[0][1] == "im530"
    assert info[1][1] == "im532"


def test_user_fetch_by_id(user_db_fixture):
    db = user_db_fixture
    db.insert_vrauser("im530", "Ishan", tables.get("user"))
    db.insert_vrauser("im532", "Ishan", tables.get("user"))
    info = db.get_vrauser_by_id(2, tables.get("user"))
    assert info[1] == "im532"


def test_user_fetch_one(user_db_fixture):
    db = user_db_fixture
    db.insert_vrauser("im530", "Ishan", tables.get("user"))
    db.insert_vrauser("im532", "Ishan", tables.get("user"))
    info = db.get_vrauser("im530", None, tables.get("user"))
    assert len(info) == 1
    assert info[0][1] == "im530"


def test_user_fetch_primary_key_crsid(user_db_fixture):
    db = user_db_fixture
    db.insert_vrauser("im530", "Ishan", tables.get("user"))
    db.insert_vrauser("im532", "Ishan", tables.get("user"))
    info = db.get_vrauser_primary_key("im532", tables.get("user"))
    assert info == 2


def test_project_insertion(project_db_fixture):
    db = project_db_fixture
    result = db.insert_project("Project01", "UIS", tables.get("project"))
    info = db.get_project(None, None, tables.get("project"))
    assert len(info) == 1
    assert result


def test_proj_update(project_db_fixture):
    db = project_db_fixture
    db.insert_project("Project01", "UIS", tables.get("project"))
    result = db.update_project(1, "Project02", "CSCS", tables.get("project"))
    info = db.get_project(None, None, tables.get("project"))
    assert len(info) == 1
    assert result
    assert info[0][1] == "Project02"
    assert info[0][2] == "CSCS"


def test_proj_remove(project_db_fixture):
    db = project_db_fixture
    db.insert_project("Project01", "UIS", tables.get("project"))
    prj = db.get_project(None, None, tables.get("project"))
    result = db.remove_project(prj[0][0], tables.get("project"))
    info = db.get_project(None, None, tables.get("project"))
    assert result
    assert len(info) == 0


def test_proj_fetchall(project_db_fixture):
    db = project_db_fixture
    db.insert_project("Project01", "UIS", tables.get("project"))
    db.insert_project("Project02", "CSCS", tables.get("project"))
    info = db.get_project(None, None, tables.get("project"))
    assert len(info) == 2
    assert info[0][2] == "UIS"
    assert info[1][2] == "CSCS"


def test_proj_fetch_one(project_db_fixture):
    db = project_db_fixture
    db.insert_project("Project01", "UIS", tables.get("project"))
    db.insert_project("Project02", "CSCS", tables.get("project"))
    info = db.get_project("Project02", None, tables.get("project"))
    assert len(info) == 1
    assert info[0][2] == "CSCS"


def test_proj_fetch_by_id(project_db_fixture):
    db = project_db_fixture
    db.insert_project("Project01", "UIS", tables.get("project"))
    db.insert_project("Project02", "CSCS", tables.get("project"))
    info = db.get_project_by_id(2, tables.get("project"))
    assert info[2] == "CSCS"


def test_proj_fetch_primary_key(project_db_fixture):
    db = project_db_fixture
    db.insert_project("Project01", "UIS", tables.get("project"))
    db.insert_project("Project02", "CSCS", tables.get("project"))
    info = db.get_project_primary_key("Project02", None, tables.get("project"))
    assert info == 2


def test_paysrc_insertion(paysources_db_fixture):
    db = paysources_db_fixture
    result = db.insert_paymentsource("grant", "grant01", tables.get("paysources"))
    info = db.get_paymentsource(None, None, tables.get("paysources"))
    assert len(info) == 1
    assert result


def test_paysrc_update(paysources_db_fixture):
    db = paysources_db_fixture
    db.insert_paymentsource("grant", "grant01", tables.get("paysources"))
    result = db.update_paymentsource(1, "grant", "grant11", tables.get("paysources"))
    info = db.get_project(None, None, tables.get("paysources"))
    assert len(info) == 1
    assert result
    assert info[0][1] == "grant"
    assert info[0][2] == "grant11"


def test_paysrc_remove(paysources_db_fixture):
    db = paysources_db_fixture
    db.insert_paymentsource("grant", "grant01", tables.get("paysources"))
    prjsrc = db.get_paymentsource(None, None, tables.get("paysources"))
    result = db.remove_paymentsource(prjsrc[0][0], tables.get("paysources"))
    info = db.get_paymentsource(None, None,tables.get("paysources"))
    assert result
    assert len(info) == 0


def test_paysrc_fetchall(paysources_db_fixture):
    db = paysources_db_fixture
    db.insert_paymentsource("grant", "grant01", tables.get("paysources"))
    db.insert_paymentsource("grant", "grant11", tables.get("paysources"))
    info = db.get_project(None, None, tables.get("paysources"))
    assert len(info) == 2
    assert info[0][2] == "grant01"
    assert info[1][2] == "grant11"


def test_paysrc_fetch_one(paysources_db_fixture):
    db = paysources_db_fixture
    db.insert_paymentsource("grant", "grant01", tables.get("paysources"))
    db.insert_paymentsource("grant", "grant11", tables.get("paysources"))
    info = db.get_paymentsource("grant", "grant11", tables.get("paysources"))
    assert len(info) == 1
    assert info[0][2] == "grant11"


def test_paysrc_fetch_by_id(paysources_db_fixture):
    db = paysources_db_fixture
    db.insert_paymentsource("grant", "grant01", tables.get("paysources"))
    db.insert_paymentsource("grant", "grant11", tables.get("paysources"))
    info = db.get_paymentsource_by_id(2, tables.get("paysources"))
    assert info[2] == "grant11"


def test_paysrc_fetch_primary_key(paysources_db_fixture):
    db = paysources_db_fixture
    db.insert_paymentsource("grant", "grant01", tables.get("paysources"))
    db.insert_paymentsource("grant", "grant11", tables.get("paysources"))
    info = db.get_paymentsource_primary_key("grant", "grant11", tables.get("paysources"))
    assert info == 2


def test_deployment_insertion(deploymentid_db_fixture):
    db = deploymentid_db_fixture
    prj = db.insert_project("Project01", "UIS", tables.get("project"))
    result = db.insert_deployment_id("121212", prj, tables.get("deploymentid"))
    info = db.get_deployment_id(None, None, tables.get("deploymentid"))
    assert len(info) == 1
    assert result


def test_deployment_update(deploymentid_db_fixture):
    db = deploymentid_db_fixture
    prj = db.insert_project("Project01", "UIS", tables.get("project"))    
    dply_id = db.insert_deployment_id("12345", prj, tables.get("deploymentid"))
    result = db.update_deployment_id(dply_id, "9567", prj, tables.get("deploymentid"))
    info = db.get_deployment_id(None, None, tables.get("deploymentid"))
    assert len(info) == 1
    assert result
    assert info[0][1] == "9567"


def test_deployment_remove(deploymentid_db_fixture):
    db = deploymentid_db_fixture
    prj = db.insert_project("Project01", "UIS", tables.get("project"))    
    dply_id = db.insert_deployment_id("12345", prj, tables.get("deploymentid"))
    result = db.remove_deployment_id(1, tables.get("deploymentid"))
    info = db.get_deployment_id(None, None, tables.get("deploymentid"))
    assert len(info) == 0
    assert result


def test_deployment_fetchall(deploymentid_db_fixture):
    db = deploymentid_db_fixture
    prj = db.insert_project("Project01", "UIS", tables.get("project"))    
    db.insert_deployment_id("12345", prj, tables.get("deploymentid"))
    db.insert_deployment_id("9567", prj, tables.get("deploymentid"))
    info = db.get_deployment_id(None, None, tables.get("deploymentid"))
    assert len(info) == 2
    assert info[0][1] == "12345"
    assert info[1][1] == "9567"


def test_deployment_fetch_by_id(deploymentid_db_fixture):
    db = deploymentid_db_fixture
    prj = db.insert_project("Project01", "UIS", tables.get("project"))    
    db.insert_deployment_id("12345", prj, tables.get("deploymentid"))
    db.insert_deployment_id("9567", prj, tables.get("deploymentid"))
    info = db.get_deployment_id_by_id(2, tables.get("deploymentid"))
    assert info[1] == "9567"


def test_deployment_fetch_one(deploymentid_db_fixture):
    db = deploymentid_db_fixture
    prj = db.insert_project("Project01", "UIS", tables.get("project"))    
    db.insert_deployment_id("12345", prj, tables.get("deploymentid"))
    db.insert_deployment_id("9567", prj, tables.get("deploymentid"))
    info = db.get_deployment_id("9567", None, tables.get("deploymentid"))
    assert len(info) == 1
    assert info[0][1] == "9567"


def test_deployment_fetch_primary_key_deployment(deploymentid_db_fixture):
    db = deploymentid_db_fixture
    prj = db.insert_project("Project01", "UIS", tables.get("project"))    
    db.insert_deployment_id("12345", prj, tables.get("deploymentid"))
    db.insert_deployment_id("9567", prj, tables.get("deploymentid"))
    info = db.get_deployment_id_primary_key("9567", tables.get("deploymentid"))
    assert info == 2


def test_charge_insertion(charges_db_fixture):
    db = charges_db_fixture
    user_id = db.insert_vrauser("im530", "Ishan", tables.get("user"))
    prj_id = db.insert_project("Project01", "UIS", tables.get("project"))    
    dpy_id = db.insert_deployment_id("12345", prj_id, tables.get("deploymentid"))
    paysrc_id = db.insert_paymentsource("grant", "grant01", tables.get("paysources"))

    result = db.insert_charge(
        dpy_id, "Resource Expansion", paysrc_id, user_id, 
        3.0, 3.0, 3.0, 9.0, tables.get("charges")
    )
    info = db.get_charge(None, None, None, None, tables.get("charges"))
    assert len(info) == 1
    assert result


def test_charge_update(charges_db_fixture):
    db = charges_db_fixture
    user_id = db.insert_vrauser("im530", "Ishan", tables.get("user"))
    prj_id = db.insert_project("Project01", "UIS", tables.get("project"))    
    dpy_id = db.insert_deployment_id("12345", prj_id, tables.get("deploymentid"))
    paysrc_id = db.insert_paymentsource("grant", "grant01", tables.get("paysources"))

    db.insert_charge(
        dpy_id, "Resource Expansion", paysrc_id, user_id, 
        3.0, 3.0, 3.0, 9.0, tables.get("charges")
    )

    result = db.update_charge(
        1,
        dpy_id,
        "Resource Expansion",
        paysrc_id,
        user_id,
        4.0, 
        4.0, 
        4.0, 
        12.0,
        tables.get("charges"),
    )

    info = db.get_charge(None, None, None, None, tables.get("charges"))
    assert len(info) == 1
    assert result
    assert info[0][6] == 4.0


def test_charge_remove(charges_db_fixture):
    db = charges_db_fixture
    user_id = db.insert_vrauser("im530", "Ishan", tables.get("user"))
    prj_id = db.insert_project("Project01", "UIS", tables.get("project"))    
    dpy_id = db.insert_deployment_id("12345", prj_id, tables.get("deploymentid"))
    paysrc_id = db.insert_paymentsource("grant", "grant01", tables.get("paysources"))

    db.insert_charge(
        dpy_id, "Resource Expansion", paysrc_id, user_id, 
        3.0, 3.0, 3.0, 9.0, tables.get("charges")
    )

    result = db.remove_charge(1, tables.get("charges"))

    info = db.get_charge(None, None, None, None, tables.get("charges"))
    assert len(info) == 0
    assert result


def test_charge_fetchall(charges_db_fixture):
    db = charges_db_fixture
    user_id = db.insert_vrauser("im530", "Ishan", tables.get("user"))
    prj_id = db.insert_project("Project01", "UIS", tables.get("project"))    
    dpy_id = db.insert_deployment_id("12345", prj_id, tables.get("deploymentid"))
    paysrc_id = db.insert_paymentsource("grant", "grant01", tables.get("paysources"))

    db.insert_charge(
        dpy_id, "Resource Expansion", paysrc_id, user_id, 
        3.0, 3.0, 3.0, 9.0, tables.get("charges")
    )
    db.insert_charge(
        dpy_id, "Duration Expansion", paysrc_id, user_id, 
        3.0, 3.0, 3.0, 9.0, tables.get("charges")
    )

    info = db.get_charge(None, None, None, None, tables.get("charges"))
    assert len(info) == 2
    assert info[0][2] == "Resource Expansion"
    assert info[1][2] == "Duration Expansion"


def test_charge_fetch_one(charges_db_fixture):
    db = charges_db_fixture
    user_id = db.insert_vrauser("im530", "Ishan", tables.get("user"))
    prj_id = db.insert_project("Project01", "UIS", tables.get("project"))    
    dpy_id = db.insert_deployment_id("12345", prj_id, tables.get("deploymentid"))
    paysrc_id = db.insert_paymentsource("grant", "grant01", tables.get("paysources"))

    db.insert_charge(
        dpy_id, "Resource Expansion", paysrc_id, user_id, 
        3.0, 3.0, 3.0, 9.0, tables.get("charges")
    )
    db.insert_charge(
        dpy_id, "Duration Expansion", paysrc_id, user_id, 
        3.0, 3.0, 3.0, 9.0, tables.get("charges")
    )

    info = db.get_charge(
        dpy_id,
        "Duration Expansion", 
        paysrc_id,
        user_id,
        tables.get("charges")
    )
    assert len(info) == 1
    assert info[0][2] == "Duration Expansion"


def test_charge_fetch_by_id(charges_db_fixture):
    db = charges_db_fixture
    user_id = db.insert_vrauser("im530", "Ishan", tables.get("user"))
    prj_id = db.insert_project("Project01", "UIS", tables.get("project"))    
    dpy_id = db.insert_deployment_id("12345", prj_id, tables.get("deploymentid"))
    paysrc_id = db.insert_paymentsource("grant", "grant01", tables.get("paysources"))

    db.insert_charge(
        dpy_id, "Resource Expansion", paysrc_id, user_id, 
        3.0, 3.0, 3.0, 9.0, tables.get("charges")
    )
    db.insert_charge(
        dpy_id, "Duration Expansion", paysrc_id, user_id, 
        3.0, 3.0, 3.0, 9.0, tables.get("charges")
    )

    info = db.get_charge_by_id(2, tables.get("charges"))
    assert info[3] == dpy_id
    assert info[2] == "Duration Expansion"


def test_charge_fetch_primary_key(charges_db_fixture):
    db = charges_db_fixture
    user_id = db.insert_vrauser("im530", "Ishan", tables.get("user"))
    prj_id = db.insert_project("Project01", "UIS", tables.get("project"))    
    dpy_id = db.insert_deployment_id("12345", prj_id, tables.get("deploymentid"))
    paysrc_id = db.insert_paymentsource("grant", "grant01", tables.get("paysources"))

    db.insert_charge(
        dpy_id, "Resource Expansion", paysrc_id, user_id, 
        3.0, 3.0, 3.0, 9.0, tables.get("charges")
    )
    db.insert_charge(
        dpy_id, "Duration Expansion", paysrc_id, user_id, 
        3.0, 3.0, 3.0, 9.0, tables.get("charges")
    )

    info = db.get_charge_primary_key(
        dpy_id, "Duration Expansion", paysrc_id, user_id, None, tables.get("charges")
    )
    assert info == 2
