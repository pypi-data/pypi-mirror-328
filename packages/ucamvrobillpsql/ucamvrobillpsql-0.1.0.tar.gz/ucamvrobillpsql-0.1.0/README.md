# Script for VRA database for Costing

# Developing
1. [Install docker-compose](https://docs.docker.com/compose/install/).
2. Docker will run the postgres on port 5455 so, ensure the system has the port available

```
# run pytest testing 
./developer.sh pytest start

# run flake8 testing 
./developer.sh flake8 start 

# delete the testing environment
./developer.sh pytest stop

# delete the flake8 environment
./developer.sh flake8 stop
```


## Package usage

- To setup database 
```
from ucamvrobillpsql.utils import pre_setupconfig
from ucamvrobillpsql.DBA import DB
db_params = {
    "dbname": "vrapricing",
    "user": "postgres",
    "password": <1Password: vrapricingpostgres>,
    "host": "infra-db.srv.uis.cam.ac.uk", 
    "port": "5432",
    "sslmode": "require",
    "sslrootcert": "./ca.crt",  # path to your client certificate
}
db = DB(db_params)
pre_setupconfig(db_params)
```
- To perform CRUD operation 
```
from ucamvrobillpsql.DBA import DB
from datetime import datetime

db_params = {
    "dbname": "vrapricing",
    "user": "postgres",
    "password": <1Password: vrapricingpostgres>,
    "host": "infra-db.srv.uis.cam.ac.uk", 
    "port": "5432",
    "sslmode": "require",
    "sslrootcert": "./ca.crt",  # path to your client certificate
}
db = DB(db_params)

# CRUD on user DB./

# create user
db.insert_vrauser("ll220", "Ling-Yan Lau")

# read user
print(db.get_vrauser())

# read user specific user by crsid
print(db.get_vrauser("ll220"))

# read user specific user by user id
print(db.get_vrauser_by_id(1))

# get the primary key of user using crsid
print(db.get_vrauser_primary_key("ll220"))

# update user
db.update_vrauser("ll220", "bda20", 'Ben Argyle')

# delete user
db.remove_vrauser('bda20')

# create project 
db.insert_project("Project01","UIS Group")

# read all the projects 
print(db.get_project())

# read specific project
print(db.get_project("Project01"))

# read project from the ID
print(db.get_project_by_id(1))

# get the primary key of the project
print(db.get_project_primary_key("Project01"))

# update project with new information 1 is the primary key
db.update_project(1, "Project03", "VET Group")

# delete project using primary key of project
# db.remove_project(1)

# create project source 
db.insert_paymentsource("grant",21001)
print(db.insert_paymentsource("project"))

# read all the project source
print(db.get_paymentsource())

# read specific project source
print(db.get_paymentsource("grant","21001"))

# read project source from the ID
print(db.get_paymentsource_by_id(1))

# get the primary key of the project source
print(db.get_paymentsource_primary_key("grant",21001))

# update project source with new information 1 is the primary key of project source
db.update_paymentsource(1, "grant","21001")

# delete project source  1 is the primary key of the project source.
db.remove_paymentsource(1)

# create vra deploymentid 
db.insert_deployment_id("1231ee112ad11212", 2)

# read all the vra deployment ids
print(db.get_deployment_id())

# read specific specific deploymentid by deploymentid
print(db.get_deployment_id("1231ee112ad11212"))

# read specific deploymentid by primary key
print(db.get_deployment_id_by_id(1))

# update vra deployment id
db.update_deployment_id(1, "1231ee112ad11212", "1231a")

# read primary key of specific deploymentid
print(db.get_deployment_id_primary_key("1231a"))

# delete vra deployment id
db.remove_deployment_id(1)

# create charges 
db.insert_charge(2, "Initial Resource",paymentsrc=2, paidby=1, cpucost=2.0, ramcost=1.0, storagecost=0.3, totalcost=3.3)

# read all the charges 
print(db.get_costing())

# read specific charges using primary key of the charge
print(db.get_costing_by_id(1))

# update charges where 1 is the primary key of the charges.
print(db.update_charge(1, 2, "Duration Expansion", new_paymentsrc=2, 
                  new_paidby=1, new_cpucost=2.3, new_ramcost=4.0, 
                  new_storagecost=3.0, new_totalcost=9.3))

# read specific charges for the type "Initial Resource" and deployment_id 2
print(db.get_charge(deployment_id=2, typee="Initial Resource")) 

# read specific charges for the type "Initial Resource" 
print(db.get_charge(typee="Initial Resource")) 

# fetch the charge of specific primary key.
print(db.get_charge_by_id(1))

# get primary key for the specific charge.
print(db.get_charge_primary_key(2, "Duration Expansion",paysource_id=2, paidby_id=1))

# get primary key for the specific charges created on specific date
print(db.get_charge_primary_key(2, "Duration Expansion",paysource_id=2, paidby_id=1, datestmp=datetime(2025, 2, 19, 15, 0, 8, 693705)))

# delete charges where 1 is the primary key
db.remove_charge(3)

# to close db connection
db.closedb()
```

---
### Design

![DB Design](./db.jpg "DB design")

## - VRAUSER table 
```
vrobilling=# \d vrauser
                                    Table "public.vrauser"
 Column |          Type          | Collation | Nullable |               Default
--------+------------------------+-----------+----------+-------------------------------------
 id     | integer                |           | not null | nextval('vrauser_id_seq'::regclass)
 crsid  | character varying(255) |           |          |
 name   | character varying(255) |           |          |
Indexes:
    "vrauser_pkey" PRIMARY KEY, btree (id)
    "vrauser_crsid_key" UNIQUE CONSTRAINT, btree (crsid)
Referenced by:
    TABLE "charges" CONSTRAINT "charges_paidby_fkey" FOREIGN KEY (paidby) REFERENCES vrauser(id)
```

## - VRA Deployment ID tabel 
```
vrobilling=# \d vradeploymentid
                                      Table "public.vradeploymentid"
    Column    |         Type          | Collation | Nullable |                   Default
--------------+-----------------------+-----------+----------+---------------------------------------------
 id           | integer               |           | not null | nextval('vradeploymentid_id_seq'::regclass)
 deploymentid | character varying(50) |           |          |
 projectid    | integer               |           |          |
Indexes:
    "vradeploymentid_pkey" PRIMARY KEY, btree (id)
    "vradeploymentid_deploymentid_key" UNIQUE CONSTRAINT, btree (deploymentid)
Foreign-key constraints:
    "vradeploymentid_projectid_fkey" FOREIGN KEY (projectid) REFERENCES vraproject(id)
Referenced by:
    TABLE "charges" CONSTRAINT "charges_deploymentid_fkey" FOREIGN KEY (deploymentid) REFERENCES vradeploymentid(id)
```

## - project table 
```
vrobilling=# \d vraproject
                                         Table "public.vraproject"
      Column       |          Type          | Collation | Nullable |                Default
-------------------+------------------------+-----------+----------+----------------------------------------
 id                | integer                |           | not null | nextval('vraproject_id_seq'::regclass)
 projectname       | character varying(255) |           |          |
 projectadmingroup | character varying(255) |           |          |
Indexes:
    "vraproject_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "vradeploymentid" CONSTRAINT "vradeploymentid_projectid_fkey" FOREIGN KEY (projectid) REFERENCES vraproject(id)
```

## - payment source table 
```
vrobilling=# \dt
              List of relations
 Schema |      Name       | Type  |  Owner
--------+-----------------+-------+----------
 public | charges         | table | postgres
 public | paymentsources  | table | postgres
 public | vradeploymentid | table | postgres
 public | vraproject      | table | postgres
 public | vrauser         | table | postgres
(5 rows)

vrobilling=# \d paymentsources
                                    Table "public.paymentsources"
 Column |          Type          | Collation | Nullable |                  Default
--------+------------------------+-----------+----------+--------------------------------------------
 id     | integer                |           | not null | nextval('paymentsources_id_seq'::regclass)
 type   | character varying(255) |           |          |
 code   | character varying(255) |           |          |
Indexes:
    "paymentsources_pkey" PRIMARY KEY, btree (id)
    "paymentsources_type_code_key" UNIQUE CONSTRAINT, btree (type, code)
    "unique_project_grant_code_null" UNIQUE, btree (type) WHERE type::text = 'project'::text OR type::text = 'grant'::text AND code IS NULL
Check constraints:
    "paymentsources_type_check" CHECK (type::text = ANY (ARRAY['project'::character varying, 'grant'::character varying]::text[]))
Referenced by:
    TABLE "charges" CONSTRAINT "charges_paysource_fkey" FOREIGN KEY (paysource) REFERENCES paymentsources(id)

```

## - Charge table 
```
vrobilling=# \d charges;
                                          Table "public.charges"
    Column     |            Type             | Collation | Nullable |               Default
---------------+-----------------------------+-----------+----------+-------------------------------------
 id            | integer                     |           | not null | nextval('charges_id_seq'::regclass)
 date          | timestamp without time zone |           |          | CURRENT_TIMESTAMP
 type          | character varying(100)      |           |          |
 deployment_id | integer                     |           |          |
 paysource     | integer                     |           |          |
 cpucost       | double precision            |           |          | 0.0
 ramcost       | double precision            |           |          | 0.0
 storagecost   | double precision            |           |          | 0.0
 totalcost     | double precision            |           | not null |
 paidby        | integer                     |           |          |
Indexes:
    "charges_pkey" PRIMARY KEY, btree (id)
Check constraints:
    "charges_type_check" CHECK (type::text = ANY (ARRAY['Resource Expansion'::character varying, 'Duration Expansion'::character varying, 'Initial Resource'::character varying]::text[]))
Foreign-key constraints:
    "charges_deployment_id_fkey" FOREIGN KEY (deployment_id) REFERENCES vradeploymentid(id)
    "charges_paidby_fkey" FOREIGN KEY (paidby) REFERENCES vrauser(id)
    "charges_paysource_fkey" FOREIGN KEY (paysource) REFERENCES paymentsources(id)
```
