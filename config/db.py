from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:cabber123@localhost:3306/bds_python?charset=utf8mb4")

meta = MetaData()

conn = engine.connect()