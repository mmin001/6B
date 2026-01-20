<<<<<<< HEAD
import sqlite3
DB_FILE = "cafeteria.db"
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS menus(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     store_name TEXT,
                     date TEXT,
                     meal_type TEXT,
                     menu_name TEXT,
                     price INTEGER,
                     has_pork BOOLEAN
                   )
                   ''')
    conn.commit()
    print("테이블 생성 완료")
    conn.close()
def save_to_db(data_list):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM menus")
    
    for item in data_list:
        cursor.execute('''
                       INSERT INTO menus (store_name, date, meal_type, menu_name, price, has_pork)
                       VALUES (?, ?, ?, ?, ?, ?)
                    ''', 
                    (
                     item['식당명'],
                     item['날짜'],
                     item['구분'],
                     item['메뉴명'],
                     item['가격'],
                     item['돼지고기포함']
                    ))
    conn.commit()
    print("db저장 완료")
    conn.close()
def get_all_menus():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM menus")
    rows = cursor.fetchall()
    
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()

    test_data = [
        {
            "식당명": "공식당",
            "날짜": "12/15(월)",
            "구분": "중식",
            "메뉴명": "쟁반수육",
            "가격": 5500,
            "돼지고기포함": True
        },
        {
            "식당명": "공식당",
            "날짜": "12/16(화)",
            "구분": "중식",
            "메뉴명": "육회비빔밥",
            "가격": 7000,
            "돼지고기포함": False
        }
    ]

    save_to_db(test_data)

    print("\n--- DB 저장 결과 확인 ---")
    rows = get_all_menus()
    for row in rows:
        print(row)


        
=======
import sqlite3
DB_FILE = "cafeteria.db"
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS menus(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     store_name TEXT,
                     date TEXT,
                     meal_type TEXT,
                     menu_name TEXT,
                     price INTEGER,
                     has_pork BOOLEAN
                   )
                   ''')
    conn.commit()
    print("테이블 생성 완료")
    conn.close()
def save_to_db(data_list):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM menus")
    
    for item in data_list:
        cursor.execute('''
                       INSERT INTO menus (store_name, date, meal_type, menu_name, price, has_pork)
                       VALUES (?, ?, ?, ?, ?, ?)
                    ''', 
                    (
                     item['식당명'],
                     item['날짜'],
                     item['구분'],
                     item['메뉴명'],
                     item['가격'],
                     item['돼지고기포함']
                    ))
    conn.commit()
    print("db저장 완료")
    conn.close()
def get_all_menus():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM menus")
    rows = cursor.fetchall()
    
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()

    test_data = [
        {
            "식당명": "공식당",
            "날짜": "12/15(월)",
            "구분": "중식",
            "메뉴명": "쟁반수육",
            "가격": 5500,
            "돼지고기포함": True
        },
        {
            "식당명": "공식당",
            "날짜": "12/16(화)",
            "구분": "중식",
            "메뉴명": "육회비빔밥",
            "가격": 7000,
            "돼지고기포함": False
        }
    ]

    save_to_db(test_data)

    print("\n--- DB 저장 결과 확인 ---")
    rows = get_all_menus()
    for row in rows:
        print(row)


        
>>>>>>> 7369ecf21210002c344af5406dcbdbd7e29480f9
