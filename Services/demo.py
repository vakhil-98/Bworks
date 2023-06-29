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

# Base.metadata.create_all(engine)



# with Session(engine) as session:
#     user = Users(Name = "Naga",ContactId = 123,Email="naga",Address="hno",UserName = "naga",Password="naga")
#     session.add_all([user])
#     session.commit()

#     Bicycle = Bicycles(CycleName = "Naga",CycleImage = 'img.jpg')
#     session.add_all([Bicycle])
#     session.commit()

#     transaction = Transactions(UserId = 1,BicycleId = 1,BicycleNo = 123, IsBuy = False,IsDonate = True, Address = "abc", ContactId = 1234, DateOfDonate = datetime.utcnow(), DateOfBuy = None, Status = True)
#     session.add_all([transaction])
#     session.commit()

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
        # with Session(engine) as session:
            
        #     result = session.query(Users).filter(Users.UserName == req['UserName']).filter(Users.Password == req['Password']).first()
        #     print(result)
        #     print(result.UserId)
        #     response = {
        #         "UserId": result.UserId,
        #         "Name" : result.Name,
        #         "ContactId": result.ContactId,
        #         "Email": result.Email,
        #         "UserName": result.UserName,
        #         "Address": result.Address
        #     }

        # from sqlalchemy.orm import sessionmaker
        # Session = sessionmaker(bind=engine)
        # session = Session()
        # result = session.query(Users).fy(UserName=req['UserName'], Password=req['Password']).first()
        # #result = session.query(Users)
        # print(result)

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




