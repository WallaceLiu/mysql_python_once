# -*- coding: utf-8 -*-

import mysql.connector
from collections import OrderedDict

class MysqlPythonOnce(object):
    """
        Python Class for connecting  with MySQL server.
    """

    __instance = None
    __host = None
    __user = None
    __password = None
    __database = None
    __session = None
    __connection = None

    def __init__(self, host='localhost', user='root', password='', database=''):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
    ## End def __init__

    def open(self):
        try:
            cnx = mysql.connector.connect(host=self.__host,\
                user= self.__user,\
                password= self.__password,\
                database= self.__database)
            self.__connection = cnx
            self.__session = cnx.cursor()
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))
    ## End def open

    def close(self):
        self.__session.close()
        self.__connection.close()
    ## End def close

    def select(self, table, where=None, *args, **kwargs):
        result = None
        query = 'SELECT '
        keys = args
        values = tuple(kwargs.values())
        l = len(keys) - 1

        for i, key in enumerate(keys):
            query += "`" + key + "`"
            if i < l:
                query += ","
        ## End for keys

        query += 'FROM %s' % table

        if where:
            query += " WHERE %s" % where
        ## End if where

        self.__session.execute(query, values)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)
        result = self.__session.fetchall()

        return result
    ## End def select

    def update(self, table, where=None, *args, **kwargs):
        try:
            query = "UPDATE %s SET " % table
            keys = kwargs.keys()
            values = tuple(kwargs.values()) + tuple(args)
            l = len(keys) - 1
            for i, key in enumerate(keys):
                query += "`" + key + "` = %s"
                if i < l:
                    query += ","
                ## End if i less than 1
            ## End for keys
            query += " WHERE %s" % where

            self.__session.execute(query, values)
            self.__connection.commit()

            # Obtain rows affected
            update_rows = self.__session.rowcount

        except mysql.connector.Error as e:
            print(e.value)

        return update_rows
    ## End function update

    def insert(self, table, *args, **kwargs):
        values = None
        query = "INSERT INTO %s " % table
        if kwargs:
            keys = kwargs.keys()
            values = tuple(kwargs.values())
            query += "(" + ",".join(["`%s`"] * len(keys)) % tuple(keys) + ") VALUES (" + ",".join(["%s"] * len(values)) + ")"
        elif args:
            values = args
            query += " VALUES(" + ",".join(["%s"] * len(values)) + ")"

        self.__session.execute(query, values)
        self.__connection.commit()
        cnt = self.__session.rowcount
        return cnt
    ## End def insert

    def delete(self, table, where=None, *args):
        query = "DELETE FROM %s" % table
        if where:
            query += ' WHERE %s' % where

        values = tuple(args)

        self.__session.execute(query, values)
        self.__connection.commit()
        delete_rows = self.__session.rowcount
        return delete_rows
    ## End def delete

    def select_advanced(self, sql, *args):
        od = OrderedDict(args)
        query = sql
        values = tuple(od.values())
        self.__session.execute(query, values)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)
        result = self.__session.fetchall()
        return result
    ## End def select_advanced
## End class
