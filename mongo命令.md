# 显示所有数据库
show dbs
# 切换数据库
use db_name
# 显示所有集合
show collections
# 查询指定集合
db['user-timeline'].find().pretty()
db.post.find().pretty()

# 条件查询
db.post.find({"creator.username": "username_666"}).pretty()
db['user-timeline'].find({"user_id" : NumberLong(666)}).pretty()
