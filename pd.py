import sqlite3 as lite
import sys

##PD = (
##	(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16),
##        (14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29)
##)

con = lite.connect('pd.db')

with con:

        cur = con.cursor()
	
        cur.execute("DROP TABLE IF EXISTS PD")
        cur.execute("CREATE TABLE PD(Order_id INTEGER PRIMARY KEY AUTOINCREMENT, User_id TEXT, Total_price INT, A4_lecture_pad TEXT, Seven_colour_sticky_note_with_pen TEXT, A5_ring_book TEXT, A5_note_book_with_zip_bag TEXT, Pencil TEXT, Stainless_steel_tumbler TEXT, A4_clear_holder TEXT, A4_vanguard_file TEXT, Name_card_holder TEXT, Umbrella TEXT, School_badge_Junior_High TEXT, School_badge_Senior_High TEXT, Dunman_dolls_pair TEXT)")
##        cur.executemany("INSERT INTO PD VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", PD)

con.close()
