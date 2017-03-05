import sqlite3
conn = sqlite3.connect("blog.db")
c = conn.cursor()
c.execute("""CREATE TABLE posts(title TEXT, post TEXT)""")
c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
c.execute('INSERT INTO posts VALUES("Well" , "I\'m well.")')
c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
c.execute('INSERT INTO posts VALUES ("Okay", "I\'m okay.")')
conn.commit()
