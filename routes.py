from flask import *
from functools import wraps
import sqlite3
	
TD = 'td.db'
PD = 'pd.db'
# AD = 'ad.db'

# PD = '/home/polaricicle/mysite/pd.db'
# TD = '/home/polaricicle/mysite/td.db'
# AD = '/home/polaricicle/mysite/ad.db'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_pd():
    return sqlite3.connect(app.config['PD'])
	
def connect_td():
    return sqlite3.connect(app.config['TD'])
	
# def connect_ad():
    # return sqlite3.connect(app.config['ad'])

app.secret_key = 'S9621257G'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/store')
def store():
	# atd = connect_td()
	# cur = atd.execute('SELECT Order_id, User_id, Total_price, A4_lecture_pad, Seven_colour_sticky_note_with_pen, A5_ring_book, A5_note_book_with_zip_bag, Pencil, Stainless_steel_tumbler, A4_clear_holder, A4_vanguard_file, Name_card_holder, Umbrella, School_badge_Junior_High, School_badge_Senior_High, Dunman_dolls_pair from td')
	# orders = [dict(Order_id=row[0], User_id=row[1], Total_price=row[2], A4_lecture_pad=row[3], Seven_colour_sticky_note_with_pen=row[4], A5_ring_book=row[5], A5_note_book_with_zip_bag=row[6], Pencil=row[7], Stainless_steel_tumbler=row[8], A4_clear_holder=row[9], A4_vanguard_file=row[10], Name_card_holder=row[11], Umbrella=row[12], School_badge_Junior_High=row[13], School_badge_Senior_High=row[14], Dunman_dolls_pair=row[15]) for row in cur.fetchall()]
	return render_template('store.html')

@app.route('/add_td', methods = ['POST'])	
def add_td():
	atd = connect_td()
	# cur = atd.execute('SELECT Order_id, User_id, Total_price, A4_lecture_pad, Seven_colour_sticky_note_with_pen, A5_ring_book, A5_note_book_with_zip_bag, Pencil, Stainless_steel_tumbler, A4_clear_holder, A4_vanguard_file, Name_card_holder, Umbrella, School_badge_Junior_High, School_badge_Senior_High, Dunman_dolls_pair from td')
	# orders = [dict(Order_id=row[0], User_id=row[1], Total_price=row[2], A4_lecture_pad=row[3], Seven_colour_sticky_note_with_pen=row[4], A5_ring_book=row[5], A5_note_book_with_zip_bag=row[6], Pencil=row[7], Stainless_steel_tumbler=row[8], A4_clear_holder=row[9], A4_vanguard_file=row[10], Name_card_holder=row[11], Umbrella=row[12], School_badge_Junior_High=row[13], School_badge_Senior_High=row[14], Dunman_dolls_pair=row[15]) for row in cur.fetchall()]
	atd.execute('INSERT INTO TD (User_id, Total_price, A4_lecture_pad, Seven_colour_sticky_note_with_pen, A5_ring_book, A5_note_book_with_zip_bag, Pencil, Stainless_steel_tumbler, A4_clear_holder, A4_vanguard_file, Name_card_holder, Umbrella, School_badge_Junior_High, School_badge_Senior_High, Dunman_dolls_pair) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',["Guest", request.form['total'], request.form['list1'], request.form['list2'], request.form['list3'], request.form['list4'], request.form['list5'], request.form['list6'], request.form['list7'], request.form['list8'], request.form['list9'], request.form['list10'], request.form['list11'], request.form['list12'], request.form['list13']])
	atd.commit()
	atd.close()
	return redirect(url_for('confirm'))

@app.route('/delete/<int:Order_id>',)
def delete(Order_id):
	atd = connect_td()
	cur = atd.execute('delete from TD where Order_id='+str(Order_id))
	atd.commit()
	atd.close()
	flash('Your order was deleted')
	return redirect(url_for('confirm'))
	
@app.route('/confirm')
def confirm():
	atd = connect_td()
	cur = atd.execute('SELECT Order_id, User_id, Total_price, A4_lecture_pad, Seven_colour_sticky_note_with_pen, A5_ring_book, A5_note_book_with_zip_bag, Pencil, Stainless_steel_tumbler, A4_clear_holder, A4_vanguard_file, Name_card_holder, Umbrella, School_badge_Junior_High, School_badge_Senior_High, Dunman_dolls_pair from TD')
	orders = [dict(Order_id=row[0], User_id=row[1], Total_price=row[2], A4_lecture_pad=row[3], Seven_colour_sticky_note_with_pen=row[4], A5_ring_book=row[5], A5_note_book_with_zip_bag=row[6], Pencil=row[7], Stainless_steel_tumbler=row[8], A4_clear_holder=row[9], A4_vanguard_file=row[10], Name_card_holder=row[11], Umbrella=row[12], School_badge_Junior_High=row[13], School_badge_Senior_High=row[14], Dunman_dolls_pair=row[15]) for row in cur.fetchall()]
	atd.close()
	return render_template('confirm.html', orders = orders)
	
@app.route('/add_pd', methods = ['POST'])
def add_pd():
	apd = connect_pd()
	apd.execute('INSERT INTO PD(Order_id, User_id, Total_price, A4_lecture_pad, Seven_colour_sticky_note_with_pen, A5_ring_book, A5_note_book_with_zip_bag, Pencil, Stainless_steel_tumbler, A4_clear_holder, A4_vanguard_file, Name_card_holder, Umbrella, School_badge_Junior_High, School_badge_Senior_High, Dunman_dolls_pair) SELECT * FROM TD')
	apd.commit()
	apd.close()
	atd = connect_td()
	atd.execute('DROP TABLE')
	atd.close()
	flash('Your order has been confirmed')
	return redirect(url_for('store'))
	
# def login_required(test):
	# @wraps(test)
	# def wrap(*args, **kwargs):
		# if 'logged_in' in session:
			# return test(*args, **kwargs)
		# else:
			# flash('You need to login first.')
			# return redirect(url_for('log'))
	# return wrap

# @app.route('/logout')
# def logout():
	# session.pop('logged_in', None)
	# flash('You were logged out')
	# return redirect(url_for('log'))
	
# @app.route('/register', methods=['GET', 'POST'])
# def register():
	# form = RegistrationForm(request.form)
	# if request.method == 'POST' and form.validate():
		# user = User(form.username.data, form.email.data,
                    # form.password.data)
		# db_session.add(user)
		# flash('Thanks for registering')
		# return redirect(url_for('login'))
	# return render_template('register.html', form=form)

# @app.route('/myAccount')
# @login_required
# def myAccount():
	# aad  = connect_ad()
	# cur = aad.execute('select rep_name, amount from reps')
	# sales = [dict(rep_name=row[0], amount=row[1]) for row in cur.fetchall()]
	# g.db.close()
	# return render_template('myAccount.html', sales=sales)

# @app.route('/log', methods=['GET', 'POST'])
# def log():
	# error = None
	# if request.method == 'POST':
		# if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			# error = 'Invalid Credentials. Please try again.'
		# else:
			# session['logged_in'] = True
			# return redirect(url_for('store'))
	# return render_template('log.html', error = error)

if __name__ == '__main__':
    app.run(debug=True)