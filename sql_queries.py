import sqlite3


class BlogDB:
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = None
        self.cursor = None

    def open(self):
        self.conn = sqlite3.connect(self.dbname) #підключаємо до БД
        self.cursor = self.conn.cursor() #створюємо курсор

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_all_posts(self):
        self.open()
        self.cursor.execute("SELECT * FROM posts")
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_posts_by_category(self, category_id):
        self.open()
        self.cursor.execute("SELECT * FROM posts WHERE category_id=?", [category_id])
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_all_categories(self):
        self.open()
        self.cursor.execute("SELECT * FROM categories")
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_post(self, post_id):
        self.open()
        self.cursor.execute("SELECT * FROM posts WHERE id=?", [post_id])
        data = self.cursor.fetchone()
        self.close()
        return data
    
    def create_post(self, title, text, category, image_name):
        self.open()
        self.cursor.execute("SELECT * FROM categories WHERE title=?", [category])
        category_db = self.cursor.fetchone()
        if not category_db:
            self.cursor.execute('''INSERT INTO categories(title) VALUES(?)''', [category])
            self.conn.commit()
            self.cursor.execute("SELECT * FROM categories WHERE title=?", [category])
            category_db = self.cursor.fetchone()
        
        self.cursor.execute('''INSERT INTO posts(title, text, category_id, image) 
                            VALUES(?, ?, ?, ?)''', [title, text, category_db[0], image_name])
        self.conn.commit()
        self.close()




