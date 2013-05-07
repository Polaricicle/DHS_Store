from flask import *
from functools import wraps
import sqlite3

DB = 'DATABASE.db'

# db = '/home/polaricicle/mysite/DATABASE.db'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DB'])

app.secret_key = 'S9621257G'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/store')
def store():
	return render_template('store.html')

@app.route('/add_td', methods = ['POST'])	
def add_td():
	atd = connect_db()
	atd.execute('DROP TABLE IF EXISTS TD')
	atd.execute('CREATE TABLE TD(User_id TEXT, Total_price MONEY, A4_lecture_pad TEXT, Seven_colour_sticky_note_with_pen TEXT, A5_note_book_with_zip_bag TEXT, Pencil TEXT, Stainless_steel_tumbler TEXT, A4_clear_holder TEXT, A4_vanguard_file TEXT, Name_card_holder TEXT, Umbrella TEXT, School_badge_Junior_High TEXT, School_badge_Senior_High TEXT, Dunman_dolls_pair TEXT)')
	atd.execute('INSERT INTO TD (User_id, Total_price, A4_lecture_pad, Seven_colour_sticky_note_with_pen, A5_note_book_with_zip_bag, Pencil, Stainless_steel_tumbler, A4_clear_holder, A4_vanguard_file, Name_card_holder, Umbrella, School_badge_Junior_High, School_badge_Senior_High, Dunman_dolls_pair) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',["Guest", request.form['total'], request.form['list1'], request.form['list2'], request.form['list4'], request.form['list5'], request.form['list6'], request.form['list7'], request.form['list8'], request.form['list9'], request.form['list10'], request.form['list11'], request.form['list12'], request.form['list13']])
	atd.commit()
	atd.close()
	return redirect(url_for('confirm'))

@app.route('/confirm')
def confirm():
	atd = connect_db()
	cur = atd.execute('SELECT User_id, Total_price, A4_lecture_pad, Seven_colour_sticky_note_with_pen, A5_note_book_with_zip_bag, Pencil, Stainless_steel_tumbler, A4_clear_holder, A4_vanguard_file, Name_card_holder, Umbrella, School_badge_Junior_High, School_badge_Senior_High, Dunman_dolls_pair from TD')
	orders = [dict(User_id=row[0], Total_price=row[1], A4_lecture_pad=row[2], Seven_colour_sticky_note_with_pen=row[3], A5_note_book_with_zip_bag=row[4], Pencil=row[5], Stainless_steel_tumbler=row[6], A4_clear_holder=row[7], A4_vanguard_file=row[8], Name_card_holder=row[9], Umbrella=row[10], School_badge_Junior_High=row[11], School_badge_Senior_High=row[12], Dunman_dolls_pair=row[13]) for row in cur.fetchall()]
	atd.close()
	return render_template('confirm.html', orders = orders)

@app.route('/add_pd', methods = ['GET', 'POST'])
def add_pd():
	atd = connect_db()
	atd.execute('INSERT INTO PD(User_id, Total_price, A4_lecture_pad, Seven_colour_sticky_note_with_pen, A5_note_book_with_zip_bag, Pencil, Stainless_steel_tumbler, A4_clear_holder, A4_vanguard_file, Name_card_holder, Umbrella, School_badge_Junior_High, School_badge_Senior_High, Dunman_dolls_pair) SELECT * FROM TD')
	atd.commit()
	atd.close()
	flash('Your order has been confirmed')
	return redirect(url_for('store'))

def login_required(test):
  @wraps(test)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return test(*args, **kwargs)
    else:
      flash('You need to login first.')
      return redirect(url_for('log'))
  return wrap

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('log'))

@app.route('/myAccount')
@login_required
def myAccount():
  return render_template('myAccount.html')

@app.route('/log', methods=['GET', 'POST'])
def log():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			session['logged_in'] = True
			return redirect(url_for('myAccount'))
	return render_template('log.html', error = error)

if __name__ == '__main__':
  app.run(debug=True)