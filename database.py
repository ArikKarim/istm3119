import sqlite3

def create_table(db_conn):
    sql = "create table coffee (coffee_id integer, name text, origin text, roast_level text, price_per_pound real)"
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
    print('\nRow inserted successfully.')

def select_all(db_conn):
    print("\nAll coffee records:")
    sql = "select * from coffee"
    cursor = db_conn.execute(sql)
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No records found.")

def select_row(db_conn):
    sql = "select * from coffee where coffee_id = ?"
    coffee_id = input('Enter the coffee id: ')
    cursor = db_conn.execute(sql, (coffee_id,))
    row = cursor.fetchone()
    if row:
        print("\nFound coffee record:")
        print(row)
    else:
        print(f"\nNo coffee with ID {coffee_id} found.")

def update_row(db_conn):
    coffee_id = input('Enter the coffee id to update: ')
    # Check if the record exists
    check_sql = "select * from coffee where coffee_id = ?"
    cursor = db_conn.execute(check_sql, (coffee_id,))
    if not cursor.fetchone():
        print(f"\nNo coffee with ID {coffee_id} found.")
        return
        
    price_per_pound = input('Enter the new price per pound: ')
    sql = "update coffee set price_per_pound = ? where coffee_id = ?"
    db_conn.execute(sql, (price_per_pound, coffee_id))
    print(f"\nPrice updated successfully for coffee ID {coffee_id}.")

def delete_row(db_conn):
    coffee_id = input('Enter the coffee id to delete: ')
    # Check if the record exists
    check_sql = "select * from coffee where coffee_id = ?"
    cursor = db_conn.execute(check_sql, (coffee_id,))
    if not cursor.fetchone():
        print(f"\nNo coffee with ID {coffee_id} found.")
        return
        
    sql = "delete from coffee where coffee_id = ?"
    db_conn.execute(sql, (coffee_id,))
    print(f"\nCoffee with ID {coffee_id} deleted successfully.")

def display_menu(db_conn):
    while True:
        print('\nMenu Options:')
        print('Enter S to start a new database')
        print('Enter C to insert a new row')
        print('Enter R to retrieve data')
        print('Enter U to update a row')
        print('Enter D to delete a row')
        print('Enter Q to quit the program')
        user_choice = input('Enter your choice: ').upper()
        
        if user_choice == 'S':
            drop_table(db_conn)
            create_table(db_conn)
        elif user_choice == 'C':  
            insert_row(db_conn)
            db_conn.commit()
        elif user_choice == 'R':
            select_row(db_conn)
        elif user_choice == 'U':
            update_row(db_conn)
            db_conn.commit()
        elif user_choice == 'D':
            delete_row(db_conn)
            db_conn.commit()
        elif user_choice == 'Q':
            print("\nQuit program.")
            break
        else:
            print("\nInvalid choice, please try again.")
            
        # Display all records after each operation
        select_all(db_conn)

def main():
    # Connect to the database
    db_conn = sqlite3.connect('coffee_inventory.db')
    print("Connected to the database successfully.")
    
    # Call the display_menu function
    display_menu(db_conn)
    
    # Close the database connection
    db_conn.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()
