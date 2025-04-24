import sqlite3

def create_table(db_conn):
  sql = "create table coffee (coffee_id integer, name text, origin text, roast_level text, price_per_pound text)"
  db_conn.execute(sql)
  print('\nTable created successfully.')


def drop_table(db_conn):
  sql = "drop table if exists coffee"
  db_conn.execute(sql)
  print('\nTable dropped successfully.')

def insert_row(db_conn):
  sql = "insert into coffee values (?, ?, ?, ?, ?)"

  coffee_id = input('Enter the coffee id: ')
  name = input('Enter the name of the coffee: ')
  origin = input('Enter the origin of the coffee: ')
  roast_level = input('Enter the roast level of the coffee: ')
  price_per_pound = float(input('Enter the price per pound of the coffee (float): '))

  db_conn.execute(sql, (coffee_id, name, origin, roast_level, price_per_pound))
  db_conn.commit()
  print('\nRow inserted successfully.')

def select_all(db_conn):
  sql = "select * from coffee"

  cursor = db_conn.execute(sql)
  for row in cursor:
    print(row)

  print('\nAll rows selected successfully.')


def select_row(db_conn):
  sql = "select * from coffee where coffee_id = ?"

  coffee_id = input('Enter the coffee id: ')
  cursor = db_conn.execute(sql, (coffee_id,))

  for row in cursor:
    print(row)

  print('\nRow selected successfully.')


def update_row(db_conn):
  sql = "update coffee set price_per_pound = ? where coffee_id = ?"

  price_per_pound = input('Enter the new price per pound: ')
  coffee_id = input('Enter the coffee id: ')

  db_conn.execute(sql, (price_per_pound, coffee_id))
  db_conn.commit()


def display_menu(db_conn):
  while True:
    # if statements
    if user_choice == 'S':
      drop_table(db_conn)
      create_table(db_conn)
    elif user_choice == 'I':
      insert_row(db_conn)
    elif user_choice == 'R':
      select_row(db_conn)
    elif user_choice == 'U':
      update_row(db_conn)
    elif user_choice == 'D':
      delete_row(db_conn)
    elif user_choice == 'Q':
      break

    print('Menu Options:')
    print('Enter S to start a new database')
    print('Enter I to insert a new row')
    print('Enter R to read a single row')
    print('Enter U to update a single row')
    print('Enter D to delete a single row')
    print('Enter Q to quit the program')
    user_choice = input('Enter your choice: ').upper()

  select_all(db_conn)


def main():
  # get connection to the db
  sqlite3.connect('coffee_inventory.db')

  # call the display_menu function - heart
  display_menu(db_conn)

  # takedown - close the db conn
  db_conn.close(db_conn)
