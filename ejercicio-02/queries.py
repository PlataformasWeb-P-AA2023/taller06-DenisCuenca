from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from gendb import Country, engine


Session = sessionmaker(bind=engine)
session = Session()



    # Presentar todos los países del continente americano

# countries = session.query(Country).filter(Country.continent=="AM" or Country.continent=="AS" or Country.continent=="NA" ).all()

# for x in countries:
#     print("%s" % (x))
#     print("------")

    # Presentar los países de Asía, ordenados por el atributo Dial.


# countries = session.query(Country).filter(Country.continent=="AS" ).order_by(Country.dial).all()



# for x in countries:
#     print("%s" % (x))
#     print("------")

#     # Presentar los lenguajes de cada país.

# countries = session.query(Country).all()
# for x in countries:

#     print(f"país: {x.name}  lenguajes: {x.languages}")

#     # Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa

# countries = session.query(Country).filter(Country.continent=="EU" ).order_by(Country.capital).all()


# for x in countries:
#     print("%s" % (x))
#     print("------")


#     # Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".


    
# countries = session.query(Country).filter(Country.continent=="EU" ).order_by(Country.capital).all()
# print(countries)

countries = session.query(Country).filter(or_(Country.name.like("%uador%"), Country.capital.like("%ito"))).all()
# print(countries)    

for x in countries:
    print("%s" % (x))
    print("------")
# docentes = session.query(Docente).all()