import json
import sqlite3
from keys_config import db_keys
from datetime import datetime

table_name = 'planning'


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as ex:
        print(ex)

    return conn


def get_ordered_pair_from_dict(dict_obj):
    key_val_split_dict = {"key_list": [], "val_list": []}
    for key, val in dict_obj.items():
        key_val_split_dict["key_list"].append(key)
        key_val_split_dict["val_list"].append(val)

    key_list = key_val_split_dict["key_list"]
    val_list = key_val_split_dict["val_list"]

    return key_list, val_list


def transform_data(task):
    task['requiredSkills'] = json.dumps(task['requiredSkills'])
    task['optionalSkills'] = json.dumps(task['optionalSkills'])

    format = '%m/%d/%Y %I:%M %p'
    task['startDate'] = datetime.strptime(task['startDate'], format).strftime("%m/%d/%Y %H:%M")
    task['endDate'] = datetime.strptime(task['endDate'], format).strftime("%m/%d/%Y %H:%M")
    return task


def rename_keys(task):
    task = transform_data(task)
    new_dict = dict(zip(list(task.keys()), db_keys))
    return {new_dict[oldKey]: value for oldKey, value in task.items()}


def create_task(conn, task):
    renamed_task = rename_keys(task)
    col_list, val_list = get_ordered_pair_from_dict(renamed_task)

    column_list_new = list(map(lambda key: "`{}`".format(key), col_list))
    column_list_new = ",".join(column_list_new)

    value_list_new = str(val_list).replace('nan', 'null').replace('[', '').replace(']', '')
    value_list_new = value_list_new.replace('None', 'null')

    sql = """ INSERT INTO {table_name} ({column_names})
              VALUES ({list_of_values})
          """.format(table_name=table_name,
                    column_names=column_list_new,
                    list_of_values=value_list_new)
    try:
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise Exception(e)


if __name__ == "__main__":
    try:
        db_file = '../planning.db'
        conn = create_connection(db_file)
        with conn:
            file_data = open("../planning.json")
            data_objects = json.load(file_data)
            for object in data_objects:
                create_task(conn, object)
                print(object)

    except Exception as ex:
        print("Error in the script: {}".format(ex))
