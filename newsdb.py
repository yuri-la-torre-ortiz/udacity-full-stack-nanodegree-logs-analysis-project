#! /usr/bin/python2.7

import psycopg2

# Run 3 queries to find most popular authors, the most popular articles,
# and days with error rates over 1% of all requests.
db = psycopg2.connect("dbname=news")
# Find the three most popular articles of all time.
a = db.cursor()
a.execute(
    "select articles.title, count(*) as num from articles, log "
    "where articles.slug = substring(log.path, 10) "
    "group by articles.title "
    "order by num desc limit 3;"
)
articles = a.fetchall()
print("1.  The top three articles of all time are:\n")
for article in articles:
    print('"' + article[0] + '"' + " -- " + str(article[1]) + " views")

# Find the three most popular authors of all time.
b = db.cursor()
b.execute(
    "select authors.name, count(*) as num from authors, articles, log "
    "where articles.slug = substring(log.path, 10) "
    "AND authors.id = articles.author "
    "group by authors.name order by num desc;"
)
authors = b.fetchall()
print("2. The most popular authors of all time are:\n")
for author in authors:
    print(author[0] + " -- " + str(author[1]) + " views")

# Find the days on which more than 1% of requests lead to errors.
c = db.cursor()
c.execute(
    "select to_char(time,'dd fmMonth fmyyyy') as yearmonthday,"
    "round(count(*) filter (where "
    "cast(substring(status, 1, 3) as int) >= 400) * 100.0 / count(*), 2) "
    "as errorrate from log "
    "group by yearmonthday "
    "having round(count(*) filter (where "
    "cast(substring(status, 1, 3) as int) >= 400) * 100.0 / count(*), 2) > 1;"
)
errordays = c.fetchall()
print("3.  The day(s) on which more than 1% of requests lead to errors:\n")
for errorday in errordays:
    print(errorday[0] + " -- " + str(errorday[1]) + "% errors")
db.close()
