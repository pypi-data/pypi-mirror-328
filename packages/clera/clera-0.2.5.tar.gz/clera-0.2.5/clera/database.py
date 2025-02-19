import os.path as path
import sqlite3


from .utils.exceptions import *


class blob: pass
class null: pass

class Database:
    def __init__(self, name: str = 'clera', PATH: str | None = path.abspath('.')):
        """
        Initializes a database connection.

        :param name: Name of the database file (without .db extension).
        :param path: Directory path for the database file.
        """
        name = name.strip()
        if not name.endswith('.db'):
            name += '.db'

        # PATH: path.dirname(__file__)

        self.name = name
        self.connection = sqlite3.connect(path.join(PATH, name))
        self.handler = self.connection.cursor()

    def create(self, name: str, data: dict, commit: bool = True):
        """
        Creates a new table in the database.

        :param name: Name of the table.
        :param schema: Dictionary where keys are column names and values are data types.
        :param commit: Whether to commit the transaction after creation.
        """
        datatype = {
            int: 'INTEGER',
            float: 'REAL',
            str: 'TEXT',
            blob: 'BLOB',
            null: 'NULL',
            None: 'NULL',
        }

        def type_check(data):
            accepted_types = [int, float, str, blob, null, None]

            for KEY in data:
                user_type = data[KEY]
                if user_type not in accepted_types:
                    raise DataTypeError(f'"{user_type}" is not a valid datatype')

        type_check(data)

        VALUE = [f"{KEY} {datatype[data[KEY]]}" for KEY in data]
        data = ', '.join(VALUE)

        is_exist = False

        try:
            self.handler.execute(f'''CREATE TABLE {name} ({data})''')
        except sqlite3.OperationalError:
            raise TableExistsError(f'Table "{name}" already exists')

        if commit == True:
            self.commit()

        return True
    
    def insert(self, table: str, value: any, commit: bool = True):
        """
        Inserts data into a table.

        :param table: Name of the table.
        :param values: Data to insert (list, tuple, or dictionary).
        :param commit: Whether to commit the transaction after insertion.
        """
        error_value = value

        self.handler.execute(f'SELECT * FROM {table}')
        headers = [header[0] for header in self.handler.description]

        table_map = {header: 'NULL' for header in headers}
        query = type(value)

        if type(value) == dict:
            try:
                value = [[KEY, value[KEY]] for KEY in value]
                for i in value:
                    header, value = i
                    table_map[header] = f"'{value}'"

            except KeyError:
                raise HeaderError(header)
            
        accepted = [list, tuple, dict]

        if query in accepted:
            if query in accepted[0:2]:
                value = [f"'{item}'" for item in value]
                
                key_map = [KEY for KEY in table_map]
                
                for i in range(len(value)):
                    table_map[key_map[i]] = value[i]

            value = [table_map[KEY] for KEY in table_map]
            value = ', '.join(value)
        else:
            # if len(table_map) != len(list(value)):
            raise InvalidValueError(f'{type(error_value)} is not a valid type. Use a Dictionary, List or Tuple')
        
        self.handler.execute(f'''INSERT INTO {table} VALUES ({value})''')
        
        if commit == True:
            self.commit()

        return True

    def select(self, table, data: str = "*", condition: str = ''):
        """
        Selects data from a table.

        :param table: Name of the table.
        :param columns: Columns to retrieve (default is all columns).
        :param condition: WHERE condition for the query.
        :return: Query result as a list of tuples.
        """
        if condition.strip() != '':
            condition = f'WHERE {condition}'

        self.handler.execute(f'SELECT {data} FROM {table} {condition}')
        # headers = [header[0] for header in self.handler.description]
        
        return self.handler.fetchall()
        # return headers, self.handler.fetchall()
    def update(self, table: str, value: dict, condition: str):
        """
        Updates data in a table.

        :param table: Name of the table.
        :param values: Dictionary of column-value pairs to update.
        :param condition: WHERE condition for the update.
        """
        VALUE = [f"{KEY}='{value[KEY]}'"for KEY in value]
        value = ', '.join(VALUE)

        self.handler.execute(f'UPDATE {table} SET {value} WHERE {condition}')
        self.commit()
        
        return True
    def delete(self, table: str, condition: str):
        """
        Deletes rows from a table based on a condition.

        :param table: Name of the table.
        :param condition: WHERE condition for the deletion.
        """
        self.handler.execute(f'DELETE FROM {table} WHERE {condition}')
        self.commit()
        
        return True

    def drop(self, table: str):
        """
        Drops a table from the database.

        :param table: Name of the table.
        """
        is_exists = True

        try:
            self.handler.execute(f'DROP TABLE {table}')
        except:
            is_exists = False
        
        if is_exists == False:
            raise TableNotFoundError(f'no such table: {table}')

        self.commit()

        return True
    
    def close(self):
        """Closes the database connection."""
        self.connection.close()

    def commit(self):
        """Commits the current transaction."""
        self.connection.commit()


class database(Database):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)