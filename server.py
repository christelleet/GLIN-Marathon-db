from flask import Flask, request, render_template
import psycopg2
import psycopg2.extras

app = Flask("Meine App")

conn = psycopg2.connect(
    host="localhost",
    database="marathondb",
    user="postgres",
    password = "sommer22"
    port = 5432
)

@app.route('/')
def startseite():
    search = request.args.get('search', '')
    order = request.args.get('order', 'Name')
    page = request. args.get('page', '0')

    page = int(page)

    search_sql = '%' + search + '%'

    if order not in ['Rank', 'AgeGroup']:
        order = 'Name'

    rows_per_page = 30
    page = 0
    limit = rows_per_page
    offset = page * rows_per_page

    cur = conn.cursor()
    cur.execute("SELECT * FROM public.marathon ORDER BY " + order + " LIMIT %s OFFSET %s", (limit, offset))
    data = cur.fetchall()

    return render_template("index.html", marathon=data, search=search, page=page, order=order)


app.run(debug=True, port=5000)

