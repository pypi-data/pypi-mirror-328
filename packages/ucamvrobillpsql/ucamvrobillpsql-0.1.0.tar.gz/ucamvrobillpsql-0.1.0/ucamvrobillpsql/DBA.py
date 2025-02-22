import logging
from datetime import datetime
from typing import Optional

import psycopg2

from ucamvrobillpsql.exceptions import DbException
from ucamvrobillpsql.tools import DEFAULT_TABLES

LOG = logging.getLogger(__name__)


class DB:
    def __init__(self, config: dict[str:str]) -> None:
        db_params = config
        self.connection = psycopg2.connect(**db_params)
        self.cursor = self.connection.cursor()

    def db_connection(self):
        """Provied the connection details of DB

        Returns:
            object: connection informtion of the DB
        """
        return self.connection

    def db_cursor(self):
        """Provied the cursor details of DB

        Returns:
            object: cursor informtion of the DB
        """
        return self.cursor

    def insert_vrauser(
        self, crsid: str, name: str, table_name: str = DEFAULT_TABLES.get("user")
    ) -> int:
        """Insertion of the vrauser detail.

        Args:
            crsid (str): crsid of the user.
            name (str): name of the user.
            table_name (str): table name of the user.

        Raises:
            DbException: Exception for the provided inputs.

        Returns:
            int: Primary key of the user.
        """
        with self.connection:
            if crsid and name:
                try:
                    self.cursor.execute(
                        f"INSERT INTO {table_name} (crsid, name) VALUES ('{crsid}', '{name}') RETURNING id;"
                    )
                    LOG.info(
                        f"INFO: {table_name} insersion successful: CRSID {crsid} and Name {name}"
                    )
                    return self.cursor.fetchone()[0]
                except Exception as e:
                    LOG.error(f"Error: {table_name} insertion : {e}")
                    raise DbException(f"Error: {table_name} insertion fail")
            else:
                LOG.error(
                    f"Error: Please provide both crid and name for {table_name} insertion"
                )
                raise DbException(f"Error: {table_name} insertion fail")

    def update_vrauser(
        self,
        old_crsid: str,
        new_crsid: str,
        name: str,
        table_name: str = DEFAULT_TABLES.get("user"),
    ) -> int:
        """Updation of the vrauser.

        Args:
            old_crsid (str): CRSID which need to be updated.
            new_crsid (str): New CRSID which replaces the old CRSID.
            name (str): Name of the user
            table_name (str): table name of the user.

        Returns:
            int: primary key of the user which is updated.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"UPDATE {table_name} SET crsid ='{new_crsid}' ,\
                    name='{name}' WHERE crsid='{old_crsid}' RETURNING id;"
                )
                LOG.info(f"INFO: {table_name} update successful for CRSID {old_crsid}")
                return self.cursor.fetchone()[0]
            except Exception as e:
                LOG.error(f"Error: {table_name} Updating : {e}")
                raise DbException(f"Error: {table_name} Updating : {e}")

    def remove_vrauser(
        self, crsid: str, table_name: str = DEFAULT_TABLES.get("user")
    ) -> bool:
        """Removal of the vrauser.

        Args:
            crsid (str): CRSID need to be removed of the vrauser.
            table_name (str): table name of the user.

        Returns:
            bool: True for the success and False for the failure.
        """
        with self.connection:
            try:
                self.cursor.execute(f"DELETE from {table_name} WHERE crsid='{crsid}';")
                LOG.info(f"INFO: {table_name} removed CRSID {crsid} successfully.")
                return True
            except Exception as e:
                LOG.error(f"Error: {table_name} removing : {e}")
                return False

    def get_vrauser(
        self,
        crsid: Optional[str] = None,
        name: Optional[str] = None,
        table_name: str = DEFAULT_TABLES.get("user"),
    ) -> any:
        """Retreive the information from the vrauser table.

        Args:
            crsid (Optional[str], optional): CRSID need to be fetched. Defaults to None.
            name (Optional[str], optional): Name of the user to fetcb. Defaults to None.
            table_name (str): table name of the user.

        Returns:
            any: retreive the data from the vrauser database.
        """
        with self.connection:
            if crsid:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where crsid = '{crsid}';"
                )
            elif name:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where name = '{name}';"
                )
            elif crsid and name:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where crsid = '{crsid}' and name = '{name}';"
                )
            else:
                self.cursor.execute(f"SELECT * FROM {table_name};")
            LOG.info(f"INFO: {table_name} information is fetched successfully")
            return self.cursor.fetchall()

    def get_vrauser_by_id(
        self,
        user_id: int,
        table_name: str = DEFAULT_TABLES.get("user"),
    ) -> any:
        """Retreive the information from the vrauser table.

        Args:
            user_id (int): primary key of user to fetch information.
            table_name (str): table name of the user.

        Raises:
            DbException: Raise exception in case of retrieving information

        Returns:
            any: retreive the data from the vrauser database.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where id = '{user_id}';"
                )
                LOG.info(f"INFO: {table_name} information is fetched successfully")
                return self.cursor.fetchone()
            except Exception as e:
                LOG.error(
                    f"Error: Unable to fetch user id from table '{table_name}': {e}"
                )
                raise DbException(
                    f"Error: Unable to fetch user id from table '{table_name}': {e}"
                )

    def get_vrauser_primary_key(
        self,
        crsid: Optional[str] = None,
        table_name: str = DEFAULT_TABLES.get("user"),
    ) -> any:
        """Retreive the information from the vrauser table.

        Args:
            crsid (Optional[str], optional): CRSID need to be fetched. Defaults to None.
            table_name (str): table name of the user.

        Returns:
            any: retreive the data from the vrauser database.
        """
        with self.connection:
            self.cursor.execute(f"SELECT * FROM {table_name} where crsid = '{crsid}';")
            LOG.info(f"INFO: {table_name} information is fetched successfully")
            return self.cursor.fetchone()[0]

    def insert_project(
        self,
        projectname: str,
        projectadmingroup: str,
        table_name: str = DEFAULT_TABLES.get("project"),
    ) -> int:
        """Insertion of the project table.

        Args:
            projectname (str): name of the project information.
            projectadmingroup (str): detail of projectadmin group.
            table_name (str): table name of the project.

        Raises:
            DbException: Exception for the provided inputs.

        Returns:
            int: primary key of the project.
        """
        with self.connection:
            if projectname:
                try:
                    self.cursor.execute(
                        f"INSERT INTO {table_name} (projectname, projectadmingroup) VALUES \
                            ('{projectname}', '{projectadmingroup}') RETURNING id;"
                    )
                    LOG.info(
                        f"INFO: Insertion of {projectname} is performed successfully"
                    )
                    return self.cursor.fetchone()[0]
                except Exception as e:
                    LOG.error(
                        f"Error: project insertion in a table '{table_name}':\n {e}"
                    )
                    raise DbException(
                        f"Error: project insertion in a table '{table_name}':\n {e}"
                    )
            else:
                LOG.error(
                    "Error: Please provide projectname, & projectadmingroup for Project"
                )
                raise DbException(
                    f"Error: project insertion fail in table {table_name}"
                )

    def update_project(
        self,
        project_id: int,
        new_projectname: str,
        new_projectadmingroup: str,
        table_name: str = DEFAULT_TABLES.get("project"),
    ) -> int:
        """Updation of the the project detail in project table

        Args:
            project_id (int): primary key of project to be updated.
            new_projectname (str): new project name to replace old project name.
            new_projectadmingroup (int): new projectadmingroup of the project.
            table_name (str): table name of the project.

        Returns:
            int: Primary key of the project.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"UPDATE {table_name} SET \
                    projectname ='{new_projectname}', projectadmingroup='{new_projectadmingroup}'\
                    WHERE id='{project_id}' RETURNING id;"
                )
                LOG.info(
                    f"INFO: Updation of the project {project_id} has been peformed successfully"
                )
                return self.cursor.fetchone()[0]
            except Exception as e:
                LOG.error(f"Error: Project Updating in table {table_name} : {e}")
                raise DbException(
                    f"Error: Project Updating in table {table_name} : {e}"
                )

    def remove_project(
        self, project_id: int, table_name: str = DEFAULT_TABLES.get("project")
    ) -> bool:
        """Removal of the project.

        Args:
            project_id (int): project id which need to be removed.
            table_name (str): table name of the project.

        Returns:
            bool: True for the success and False for the failure.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"DELETE from {table_name} WHERE id='{project_id}';"
                )
                LOG.info(
                    f"INFO: Removing of the project '{project_id}' has been performed successfully."
                )
                return True
            except Exception as e:
                LOG.error(f"Error: project removing from table '{table_name}': {e}")
                raise DbException(
                    f"Error: project removing from table '{table_name}': {e}"
                )

    def get_project(
        self,
        project: Optional[str] = None,
        projectadmingroup: Optional[str] = None,
        table_name: str = DEFAULT_TABLES.get("project"),
    ) -> any:
        """Retreive the information from the project table.

        Args:
            project (Optional[str], optional): Name of the project which need to be fetched. Defaults to None.
            projectadmingroup (Optional[str], optional): Name of the projectadmingroup which need to be fetched.
                                                        Defaults to None.
            table_name (str): table name of the project.

        Returns:
            any: Retreive the data from the project database.
        """
        with self.connection:
            if project and projectadmingroup:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where projectname = '{project}'\
                        and projectadmingroup = '{projectadmingroup}';"
                )
            elif project and not projectadmingroup:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where projectname = '{project}';"
                )
            elif not project and projectadmingroup:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where projectadmingroup = '{projectadmingroup}';"
                )
            else:
                self.cursor.execute(f"SELECT * FROM {table_name};")
            LOG.info("INFO: project information has been fetched successfully.")
            return self.cursor.fetchall()

    def get_project_by_id(
        self,
        project_id: int,
        table_name: str = DEFAULT_TABLES.get("project"),
    ) -> any:
        """Retreive the information from the project table.

        Args:
            project_id (Optional[int], optional): project which need to be fetched. Defaults to None.
            table_name (str): table name of the project.

        Returns:
            any: Retreive the data from the project database.
        """
        with self.connection:
            self.cursor.execute(
                f"SELECT * FROM {table_name} where id = '{project_id}';"
            )
            LOG.info("INFO: project information has been fetched successfully.")
            return self.cursor.fetchone()

    def get_project_primary_key(
        self,
        project: str,
        projectadmingroup: str = None,
        table_name: str = DEFAULT_TABLES.get("project"),
    ) -> any:
        """Retreive the primary key of the project from the project table.

        Args:
            project (str): project which need to be fetched.
            projectadmingroup (str): projectadmingroup to be retrieved. Defaults to None.
            table_name (str, optional): table name of the project. Defaults to DEFAULT_TABLES.get("project").

        Returns:
            any: Retreive the data from the project database.
        """
        with self.connection:
            if projectadmingroup:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} \
                    where projectname = '{project}' and projectadmingroup = '{projectadmingroup}';"
                )
            else:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where projectname = '{project}';"
                )
            LOG.info("INFO: project information has been fetched successfully.")
            return self.cursor.fetchone()[0]

    def insert_paymentsource(
        self,
        typee: str,
        code: str = None,
        table_name: str = DEFAULT_TABLES.get("paysources"),
    ) -> int:
        """Insertion of the paymentsource detail.

        Args:
            type (str): type of the payment ['project'/'grant'].
            code (str): code for grant. Default is None.
            table_name (str): table name of the payment source.

        Raises:
            DbException: Exception for the provided inputs.

        Returns:
            int: Primary key of the payment source.
        """
        with self.connection:
            if code:
                try:
                    self.cursor.execute(
                        f"INSERT INTO {table_name} (type, code) VALUES ('{typee}', '{code}') RETURNING id;"
                    )
                    LOG.info(
                        f"INFO: {table_name} insersion successful: type {typee} and code {code}"
                    )
                    return self.cursor.fetchone()[0]
                except Exception as e:
                    LOG.error(f"Error: {table_name} insertion : {e}")
                    raise DbException(f"Error: {table_name} insertion fail")
            else:
                try:
                    self.cursor.execute(
                        f"INSERT INTO {table_name} (type) VALUES ('{typee}') RETURNING id;"
                    )
                    LOG.info(f"INFO: {table_name} insersion successful: type {typee}")
                    return self.cursor.fetchone()[0]
                except Exception as e:
                    LOG.error(f"Error: {table_name} insertion : {e}")
                    raise DbException(f"Error: {table_name} insertion fail")

    def update_paymentsource(
        self,
        paymentsource_id: int,
        new_type: str,
        new_code: str,
        table_name: str = DEFAULT_TABLES.get("paysources"),
    ) -> int:
        """Updation of the paymentsource.

        Args:
            paymentsource_id (int): primary key of the pauyment source.
            new_type (str): Type of the payment source.
            new_code (str): Code of the grant.
            table_name (str): table name of the paymentsources.

        Returns:
            int: primary key of the paymentsources which is updated.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"UPDATE {table_name} SET type ='{new_type}' , code='{new_code}'\
                    WHERE id='{paymentsource_id}' RETURNING id;"
                )
                LOG.info(
                    f"INFO: {table_name} update successful for payment source {paymentsource_id}"
                )
                return self.cursor.fetchone()[0]
            except Exception as e:
                LOG.error(f"Error: {table_name} Updating : {e}")
                raise DbException(f"Error: {table_name} Updating : {e}")

    def remove_paymentsource(
        self, paymentsource_id: str, table_name: str = DEFAULT_TABLES.get("paysources")
    ) -> bool:
        """Removal of the vrauser.

        Args:
            paymentsource_id (int): primary key of the payment source which need to be removed of the paymentsources.
            table_name (str): table name of the paymentsources.

        Returns:
            bool: True for the success and False for the failure.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"DELETE from {table_name} WHERE id='{paymentsource_id}';"
                )
                LOG.info(
                    f"INFO: {table_name} removed paymentsource_id {paymentsource_id} successfully."
                )
                return True
            except Exception as e:
                LOG.error(f"Error: {table_name} removing : {e}")
                return False

    def get_paymentsource(
        self,
        typee: Optional[str] = None,
        code: Optional[str] = None,
        table_name: str = DEFAULT_TABLES.get("paysources"),
    ) -> any:
        """Retreive the information from the paymentsources table.

        Args:
            typee (Optional[str], optional): type of payment which need to be fetched. Defaults to None.
            code (Optional[str], optional): code of the grant to be fetch. Defaults to None.
            table_name (str): table name of the payment source.

        Returns:
            any: retreive the data from the paymentsources database.
        """
        with self.connection:
            if typee and code:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where type = '{typee}' and code = '{code}';"
                )
            elif code:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where code = '{code}';"
                )
            elif typee:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where type = '{typee}';"
                )
            else:
                self.cursor.execute(f"SELECT * FROM {table_name};")
            LOG.info(f"INFO: {table_name} information is fetched successfully")
            return self.cursor.fetchall()

    def get_paymentsource_by_id(
        self,
        paymentsource_id: int,
        table_name: str = DEFAULT_TABLES.get("paysources"),
    ) -> any:
        """Retreive the information from the vrauser table.

        Args:
            paymentsource_id (int): primary key of payment source to fetch information.
            table_name (str): table name of the payment sources.

        Raises:
            DbException: Raise exception in case of retrieving information

        Returns:
            any: retreive the data from the paymentsources database.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where id='{paymentsource_id}';"
                )
                LOG.info(f"INFO: {table_name} information is fetched successfully")
                return self.cursor.fetchone()
            except Exception as e:
                LOG.error(
                    f"Error: Unable to fetch paymentsource id from table '{table_name}': {e}"
                )
                raise DbException(
                    f"Error: Unable to fetch paymentsource id from table '{table_name}': {e}"
                )

    def get_paymentsource_primary_key(
        self,
        typee: str,
        code: Optional[str] = None,
        table_name: str = DEFAULT_TABLES.get("paysources"),
    ) -> any:
        """Retreive the information from the paymentsource table.

        Args:
            typee (str): Type of the payment souce to be fetched.
            code (Optional[str], optional): grant code need to be fetched. Defaults to None.
            table_name (str): table name of the paymentsource.

        Returns:
            any: retreive the data from the paymentsource database.
        """
        with self.connection:
            if code:
                try:
                    self.cursor.execute(
                        f"SELECT * FROM {table_name} where type = '{typee}' and code = '{code}';"
                    )
                    LOG.info(f"INFO: {table_name} information is fetched successfully")
                    return self.cursor.fetchone()[0]
                except Exception as e:
                    LOG.error(
                        f"Error: Unable to fetch paymentsource id from table '{table_name}': {e}"
                    )
                    raise DbException(
                        f"Error: Unable to fetch paymentsource id from table '{table_name}': {e}"
                    )
            try:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where type = '{typee}';"
                )
                LOG.info(f"INFO: {table_name} information is fetched successfully")
                return self.cursor.fetchone()[0]
            except Exception as e:
                LOG.error(
                    f"Error: Unable to fetch paymentsource id from table '{table_name}': {e}"
                )
                raise DbException(
                    f"Error: Unable to fetch paymentsource id from table '{table_name}': {e}"
                )

    def insert_deployment_id(
        self,
        deployment_id: str,
        project_id: int,
        table_name: str = DEFAULT_TABLES.get("deploymentid"),
    ) -> int:
        """Insertion of the deployment detail.

        Args:
            deployment_id (str): deployment ID information.
            project_id (int): primary key to the project.
            table_name (str): table name of the deploymentid.

        Raises:
            DbException: Exception for the provided inputs.

        Returns:
            int: primary key of the deployment.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"INSERT INTO {table_name} (deploymentID, projectid) \
                    VALUES ('{deployment_id}', '{project_id}') RETURNING id;"
                )
                LOG.info(f"INFO: deployment ID {deployment_id} inserted successfully")
                return self.cursor.fetchone()[0]
            except Exception as e:
                LOG.error(f"Error: deployment ID insertion in {table_name}: {e}")
                raise DbException(
                    f"Error: deployment ID insertion in {table_name}: {e}"
                )

    def update_deployment_id(
        self,
        deployment_pk: int,
        new_deployment_id: str,
        project_id: int,
        table_name: str = DEFAULT_TABLES.get("deploymentid"),
    ) -> int:
        """Updation of the the deployment ID in deployment table.

        Args:
            deployment_pk (int): primary key which need to be updated.
            new_deployment_id (str): New Deployment ID which replaces the old Deployment ID.
            project_id (int): primary key of the  project which need to be updated.
            table_name (str): table name of the deploymentid.

        Returns:
            int: primary key of the deployment.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"UPDATE {table_name} SET deploymentID='{new_deployment_id}', projectid='{project_id}' \
                    WHERE id='{deployment_pk}' RETURNING id;"
                )
                LOG.info(
                    f"INFO: deployment ID of id {deployment_pk} updated successfully with \
                    {new_deployment_id} in table {table_name} ."
                )
                return self.cursor.fetchone()[0]
            except Exception as e:
                LOG.error(f"Error: deployment ID update for table {table_name}: {e}")
                raise DbException(
                    f"Error: deployment ID update for table {table_name}: {e}"
                )

    def remove_deployment_id(
        self, deployment_pk: int, table_name: str = DEFAULT_TABLES.get("deploymentid")
    ) -> bool:
        """Removal of the deployment ID.

        Args:
            deployment_pk (int): Primary key of the deployment ID need to be removed from the Deployment table.
            table_name (str): table name of the deploymentid.

        Returns:
            bool: True for the success and False for the failure.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"DELETE from {table_name} WHERE id='{deployment_pk}';"
                )
                LOG.info(
                    f"INFO: Removal of the deployment ID whose pk' {deployment_pk} ' has been performed successfully"
                )
                return True
            except Exception as e:
                LOG.error(
                    f"Error: deployment ID removing from table '{table_name}': {e}"
                )
                return False

    def get_deployment_id(
        self,
        deployment_id: Optional[str] = None,
        project_id: Optional[int] = None,
        table_name: str = DEFAULT_TABLES.get("deploymentid"),
    ) -> any:
        """Retreive the information from the deployment table.

        Args:
            deployment_id (Optional[str], optional): Deployment ID need to be fetched. Defaults to None.
            project_id (Optional[str], optional): Deployment ID need to be fetched. Defaults to None.
            table_name (str): table name of the deploymentid.

        Returns:
            any: Retreive the data from the Deployment ID database.
        """
        with self.connection:
            if deployment_id and project_id:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where deploymentID = '{deployment_id}' and projectid = '{project_id}';"
                )
            elif deployment_id:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where deploymentID = '{deployment_id}';"
                )
            elif project_id:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where projectid = '{project_id}';"
                )
            else:
                self.cursor.execute(f"SELECT * FROM {table_name};")
            LOG.info("INFO: deployment ID information is fetched successfully")
            return self.cursor.fetchall()

    def get_deployment_id_by_id(
        self,
        deployment_id: int,
        table_name: str = DEFAULT_TABLES.get("deploymentid"),
    ) -> any:
        """Retreive the information from the deployment table.

        Args:
            deployment_id (int): primary key of the Deployment ID need to be fetched.
            table_name (str, optional): table name of the deploymentid. Defaults to DEFAULT_TABLES.get("deploymentid").

        Raises:
            DbException: Raise exception in case of retrieving information

        Returns:
            any: Retreive the data from the Deployment ID database.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where id = '{deployment_id}';"
                )
                LOG.info("INFO: deployment ID information is fetched successfully")
                return self.cursor.fetchone()
            except Exception as e:
                LOG.error(
                    f"Error: Unable to fetch deployment id from table '{table_name}': {e}"
                )
                raise DbException(
                    f"Error: Unable to fetch deployment id from table '{table_name}': {e}"
                )

    def get_deployment_id_primary_key(
        self,
        deployment_id: str,
        table_name: str = DEFAULT_TABLES.get("deploymentid"),
    ) -> any:
        """Retreive the primary key from the deployment table.

        Args:
            deployment_id (str): Deployment ID need to be fetched.
            table_name (str): table name of the deploymentid.

        Returns:
            any: Retreive the data from the Deployment ID database.
        """
        with self.connection:
            if deployment_id:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where deploymentID = '{deployment_id}';"
                )
            LOG.info("INFO: deployment ID information is fetched successfully")
            return self.cursor.fetchone()[0]

    def insert_charge(
        self,
        deployment_id: int,
        typee: str,
        paymentsrc: int,
        paidby: int,
        cpucost: float = 0,
        ramcost: float = 0,
        storagecost: float = 0,
        totalcost: float = 0,
        table_name: str = DEFAULT_TABLES.get("charges"),
    ) -> int:
        """Insertion of charge in a database

        Args:
            deployment_id (int): primary key of the deployment in deploymentID table.
            typee (str): type of charges ['Resource Expansion', 'Duration Expansion', 'Initial Resource']
            paymentsrc (int): primary key of the payment source.
            paidby (int): primary key of the user in vrauser.
            cpucost (float, optional): CPU cost . Defaults to 0.
            ramcost (float, optional): RAM cost. Defaults to 0.
            storagecost (float, optional): Storage cost. Defaults to 0.
            totalcost (float, optional): Total cost. Defaults to 0.
            table_name (str, optional): table name of the charge. Defaults to DEFAULT_TABLES.get("charges").

        Raises:
            DbException: Exception for the provided inputs.

        Returns:
            int: Primary key of the charge.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"INSERT INTO {table_name} (deployment_id, type, paysource, \
                    cpucost, ramcost, storagecost, totalcost, paidby) VALUES \
                    ('{deployment_id}', '{typee}', '{paymentsrc}','{cpucost}',\
                    '{ramcost}', '{storagecost}', '{totalcost}', '{paidby}') RETURNING id;"
                )
                LOG.info("INFO: Charge insertion has been performed successfully")
                return self.cursor.fetchone()[0]
            except Exception as e:
                LOG.error(
                    f"Error: charge insertion failed in table '{table_name}': {e}"
                )
                raise DbException(
                    f"Error: charge insertion failed in table '{table_name}': {e}"
                )

    def update_charge(
        self,
        charge_id: int,
        new_deployment_id: int,
        new_typee: str,
        new_paymentsrc: int,
        new_paidby: int,
        new_cpucost: float,
        new_ramcost: float,
        new_storagecost: float,
        new_totalcost: float,
        table_name: str = DEFAULT_TABLES.get("charges"),
    ) -> int:
        """Updation of the charges database entry.

        Args:
            charge_id (int): primary key of the charge id.
            new_deployment_id (int): primary key of the deployment id.
            new_typee (str): type of the license.
            new_paymentsrc (int): primary key of the payment source.
            new_paidby (int): primary key of the user in vrauser.
            new_cpucost (float): CPU cost . Defaults to 0.
            new_ramcost (float): RAM cost. Defaults to 0.
            new_storagecost (float): Storage cost. Defaults to 0.
            new_totalcost (float): Total cost. Defaults to 0.
            table_name (str): table name of the charge.

        Raises:
            DbException: Exception for the provided inputs.

        Returns:
            int: Primary key of the charge.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"UPDATE {table_name} SET \
                    deployment_id ='{new_deployment_id}', type='{new_typee}', paysource='{new_paymentsrc}', \
                    cpucost='{new_cpucost}', ramcost='{new_ramcost}', storagecost='{new_storagecost}', \
                    totalcost='{new_totalcost}', paidby='{new_paidby}' WHERE id='{charge_id}' RETURNING id;"
                )
                LOG.info(
                    f"INFO: updation of the charge id '{charge_id}' has been performed successfully."
                )
                return self.cursor.fetchone()[0]
            except Exception as e:
                LOG.error(
                    f"Error: Updation of charge has failed in table '{table_name}': \n {e}"
                )
                raise DbException(
                    f"Error: Updation of charge has failed in table '{table_name}'"
                )

    def remove_charge(
        self,
        charge_id: int,
        table_name: str = DEFAULT_TABLES.get("charges"),
    ) -> bool:
        """Removal of the charge detail from charges database.

        Args:
            charge_id (int): primary key of the charge id.
            table_name (str): table name of the charges.

        Raises:
            DbException: Exception for the provided inputs.

        Returns:
            bool: True for the success and False for the failure.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"DELETE from {table_name} WHERE id = '{charge_id}';"
                )
                LOG.info(
                    "INFO: Removing of the charge has been performed successfully."
                )
                return True
            except Exception as e:
                LOG.error(
                    f"Error: Removing of costing has failed in table {table_name}: \n {e}"
                )
                raise DbException(
                    f"Error: Removing of costing has failed in table {table_name}: \n {e}"
                )

    def get_charge(
        self,
        deployment_id: Optional[int] = None,
        typee: Optional[str] = None,
        paysource_id: Optional[int] = None,
        paidby_id: Optional[int] = None,
        table_name: str = DEFAULT_TABLES.get("charges"),
    ) -> any:
        """Retreive the information from the charges table.

        Args:
            deployment_id (Optional[int], optional): primary key of the deployment id.. Defaults to None.
            typee (Optional[str], optional): type of the license.. Defaults to None.
            paysource_id (Optional[int], optional): primary key of the paysource. Defaults to None.
            paidby_id (Optional[int], optional): primary key of the user in vrauser table. Defaults to None.
            table_name (str): table name of the charge.

        Returns:
            any: Retreive the data from the charge database.
        """
        with self.connection:
            arguments = [deployment_id, typee, paysource_id, paidby_id]
            parameters = ["deployment_id", "type", "paysource", "paidby"]

            def _form_query(parameters, arguments):
                query_parts = [
                    f"{param}='{arg}'"
                    for param, arg in zip(parameters, arguments)
                    if arg is not None
                ]
                query = " and ".join(query_parts)
                return query

            query = _form_query(parameters, arguments)
            final_query = ""
            if query:
                final_query = " where " + query
            self.cursor.execute(f"SELECT * FROM {table_name} {final_query};")
            LOG.info("INFO: charge information has been performed successfully")
            return self.cursor.fetchall()

    def get_charge_by_id(
        self,
        charge_id: int,
        table_name: str = DEFAULT_TABLES.get("charges"),
    ) -> any:
        """Retreive the information from the charges table.

        Args:
            charge_id (int): primary key of the charge id.
            table_name (str): table name of the charge.

        Returns:
            any: Retreive the data from the charge database.
        """
        with self.connection:
            try:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} where id = '{charge_id}';"
                )
                LOG.info("INFO: charge information has been performed successfully")
                return self.cursor.fetchone()
            except Exception as e:
                LOG.error(
                    f"Error: Unable to fetch charge id from table '{table_name}': {e}"
                )
                raise DbException(
                    f"Error: Unable to fetch charge id from table '{table_name}': {e}"
                )

    def get_charge_primary_key(
        self,
        deployment_id: int,
        typee: str,
        paysource_id: int,
        paidby_id: int,
        datestmp: datetime = None,
        table_name: str = DEFAULT_TABLES.get("charges"),
    ) -> any:
        """Retreive the primary key from the charges table.

        Args:
            deployment_id (int): primary key of the deployment id.
            typee (str): type of the license.
            project_id (Optional[int], optional): primary key of the payment order. Defaults to None.
            grant_id (Optional[int], optional): primary key of the grant id. Defaults to None.
            table_name (str): table name of the costing.

        Returns:
            any: Retreive the data from the costing database.
        """
        with self.connection:
            if datestmp:
                try:
                    self.cursor.execute(
                        f"SELECT * FROM {table_name} where deployment_id = '{deployment_id}' and type = '{typee}' \
                        and date = '{datestmp}' and paysource = '{paysource_id}' and paidby = '{paidby_id}';"
                    )
                except Exception as e:
                    LOG.error(
                        f"Error: Unable to fetch information from table '{table_name}': {e}"
                    )
                    raise DbException(
                        f"Error: Unable to fetch information from table '{table_name}': {e}"
                    )
            else:
                try:
                    self.cursor.execute(
                        f"SELECT * FROM {table_name} where deployment_id='{deployment_id}' and type='{typee}'\
                        and paysource = '{paysource_id}' and paidby = '{paidby_id}';"
                    )
                except Exception as e:
                    LOG.error(
                        f"Error: Unable to fetch information from table '{table_name}': {e}"
                    )
                    raise DbException(
                        f"Error: Unable to fetch information from table '{table_name}': {e}"
                    )
            LOG.info("INFO: Charge information has been fetched successfully")
            return self.cursor.fetchone()[0]

    def closedb(self) -> None:
        """
        To close the databse connection.
        """
        self.connection.close()
