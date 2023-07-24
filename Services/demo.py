from numpy import insert
from sqlalchemy import create_engine
from sqlalchemy import select
#from sqlalchemy import filter, filter_by


#engine = create_engine('mssql+pyodbc://@' + DESKTOP-8FANH7R + '/' + BWorks + '?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')

#engine = create_engine('mssql+pyodbc://@' + 'DESKTOP-8FANH7R' + '/' + 'BWorks' + '?trusted_connection=yes&driver=ODBC Driver 17 for SQL Server')

engine = create_engine('mssql+pyodbc://@' + 'DESKTOP-8FANH7R' + '/' + 'BWorks' + '?trusted_connection=yes&driver=SQL Server', use_setinputsizes=False)

from datetime import datetime
from sqlalchemy import ForeignKey,DateTime,Boolean
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session

# qualify the base with __allow_unmapped__.  Can also be
# applied to classes directly if preferred
class Base:
    pass
    #__allow_unmapped__ = True


Base = declarative_base(cls=Base)

# existing mapping proceeds, Declarative will ignore any annotations
# which don't include ``Mapped[]``
class Users(Base):
    __tablename__ = "Users"

    UserId: int = Column(Integer, primary_key=True)
    Name: str = Column(String,nullable=False )
    ContactId: int = Column(Integer, nullable = False)
    Email: str = Column(String, nullable = False)
    Address: str = Column(String, nullable = False)
    UserName: str = Column(String, nullable = False)
    Password: str = Column(String, nullable = False)

class Bicycles(Base):
    __tablename__ = "Bicycles"

    BicycleId: int = Column(Integer, primary_key=True)
    CycleName: str = Column(String,nullable=False )
    CycleImage: str = Column(String, nullable = False)
    
class Transactions(Base):
    __tablename__ = "Transactions"
    
    TransactionId: int = Column(Integer,primary_key = True)
    UserId = Column(Integer, ForeignKey('Users.UserId'))
    BicycleId = Column(Integer, ForeignKey('Bicycles.BicycleId'))
    BicycleNo = Column(Integer, nullable = True)
    IsBuy: bool = Column(Boolean, nullable = False)
    IsDonate: bool = Column(Boolean, nullable = False)
    Address: str = Column(String, nullable = False)
    ContactId: int = Column(Integer, nullable = False)
    DateOfDonate = Column(DateTime, nullable = True)
    DateOfBuy = Column(DateTime, nullable = True)
    Status: bool = Column(Boolean, nullable = False)

    user = relationship("Users", backref="transactions")
    bicycle = relationship("Bicycles", backref="transactions")

class Data(Base):
    __tablename__ = "Data"

    ID:int = Column(Integer, primary_key= True)
    Name: str = Column(String,nullable=False )
    EmailId: str = Column(String,nullable=False )
    Survey: str = Column(String,nullable=False )
    DropOff_Location: str = Column(String,nullable=False )
    DateTime = Column(DateTime, nullable = True)
    BikeModel: str = Column(String,nullable=False )
    BikeColor: str = Column(String,nullable=False )
    BikeWheel = Column(Integer, nullable = True)



def register_db(req):
    with Session(engine) as session:
        user = Users(Name = req['Name'],ContactId = req['ContactId'],Email=req['Email'],Address=req['Address'],UserName = req['UserName'],Password=req['Password'])
        session.add_all([user])
        session.commit()
        return {"issuccess": True} 
    return {"issuccess": False}


def bicycle_db():
    with Session(engine) as session:
       
        result = session.query(Bicycles).all() # Assuming 'User' is a SQLAlchemy model
        bicycle_list = list()
        for row in result:
            bicycle_list.append({
                "bicycleId": row.BicycleId,
                "cycleName": row.CycleName,
                "cycleImage": row.CycleImage
            })
            
        return bicycle_list
    
def login_db(req):
    try:

        from sqlalchemy import text
        with Session(engine) as session:
            sql_statement = text("SELECT * FROM Users WHERE UserName = :userName and Password = :password" )
            query = session.query(Users).from_statement(sql_statement)
            query = query.params(userName=req['UserName'],password = req['Password'])


            result = query.first()
            response = {
                "UserId": result.UserId,
                "Name" : result.Name,
                "ContactId": result.ContactId,
                "Email": result.Email,
                "UserName": result.UserName,
                "Address": result.Address
            }

            return response
    except Exception as e:
        return e


    
def transaction_db(req):
    with Session(engine) as session:
        transaction = Transactions(UserId = req['UserId'],BicycleId = req['BicycleId'],BicycleNo=req['BicycleNo'],IsBuy=req['IsBuy'],IsDonate = req['IsDonate'],Address=req['Address'],ContactId=req['ContactId'],DateOfDonate=datetime.utcnow(), DateOfBuy=datetime.utcnow(),Status=True)
        session.add_all([transaction])
        session.commit()
        return {"issuccess": True}
    return {"issuccess": False}

def gettransaction_db():
    try:

        from sqlalchemy import text
        with Session(engine) as session:
            #sql_statement = text("SELECT * FROM Transactions" )
            #query = session.query(Transactions).from_statement(sql_statement)
            result = session.query(Transactions).all()
            transaction_list = list()
            for row in result:
                transaction_list.append({
                    "TransactionId": row.UserId,
                    "UserId": row.ContactId,
                    "BicycleId" : row.BicycleId,
                })
            return transaction_list;

    except Exception as e:
        return e



import pandas as pd


def etlbicycles_db():
    try:
        result = 0
        print("reading csv data")
        df = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\Open_Source\Services\Bicycles.csv')
        print("length of df", len(df) )
        with Session(engine) as session:
            count1 = session.query(Bicycles).count()
            df.to_sql('Bicycles',engine,if_exists= 'append',index= False)
            count2 = session.query(Bicycles).count()
            result = count2-count1
        return {
            "status":True,
            "records_inserted":result 
        }

    except Exception as e:
        print(e)

    
# def data_db():
#     try:
#         from sqlalchemy import text
#         with Session(engine) as session:
#             #sql_statement = text("SELECT * FROM Transactions" )
#             #query = session.query(Transactions).from_statement(sql_statement)
#             result = session.query(Data).all()
#             data_list = list()
#             for row in result:
#                 data_list.append({
#                     "ID" :row.ID,
#                     "Name":row.Name,
#                     "EmailId":row.EmailId,
#                     "Survey":row.Survey,
#                     "DropOff_Location":row.DropOff_Location,
#                     "DateTime":row.DateTime,
#                     "BikeModel":row.BikeModel,
#                     "BikeColor":row.BikeColor,
#                     "BikeWheel ":row.BikeWheel
#                 })
#             print(data_list)
#             return data_list
            

#     except Exception as e:
#         print(e)
#         return e
    

def data_db(data):
    try:
        lst = []
        for req in data:

            
           
            data_insert = Data(Name = req['Name'],EmailId = req['EmailId'],Survey=req['Survey'],DropOff_Location=req['DropOff_Location'],BikeModel = req['BikeModel'],BikeColor=req['BikeColor'],BikeWheel=req['BikeWheel'],DateTime=datetime.utcnow())
            lst.append(data_insert)
        result = []
        with Session(engine) as session:
            session.add_all(lst)
            session.commit()
            result = session.query(Data).all()

            
            # Create a list of dictionaries representing the data
            data_list = []
            for row in result:
                data_list.append({
                    "ID": row.ID,
                    "Name": row.Name,
                    "EmailId": row.EmailId,
                    "Survey": row.Survey,
                    "DropOff_Location": row.DropOff_Location,
                    "DateTime": row.DateTime,
                    "BikeModel": row.BikeModel,
                    "BikeColor": row.BikeColor,
                    "BikeWheel": row.BikeWheel
                })
            return data_list
            
    except Exception as e:
        print(e)
        return e
    



# from sqlalchemy import select, bindparam
# scalar_subq = (
#     select(data_db.c.id)
#     .where(data_db.c.name == bindparam("username"))
#     .scalar_subquery()
# )

# with engine.connect() as conn:
#     result = conn.execute(
#         insert(data_db).values(user_id=scalar_subq),
#         [
#             {
#                 "username": "spongebob",
#                 "email_address": "spongebob@sqlalchemy.org",
#             },
#             {"username": "sandy", "email_address": "sandy@sqlalchemy.org"},
#             {"username": "sandy", "email_address": "sandy@squirrelpower.org"},
#         ],
#     )
#     conn.commit()