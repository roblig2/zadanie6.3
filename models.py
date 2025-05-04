from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Station(Base):
    __tablename__ = 'stations'
    station = Column(String, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
    name = Column(String)
    country = Column(String)
    state = Column(String)

    measurements = relationship("Measurement", back_populates="station_obj")


class Measurement(Base):
    __tablename__ = 'measurements'
    station = Column(String, ForeignKey('stations.station'), primary_key=True)
    date = Column(String, primary_key=True)
    precip = Column(Float)
    tobs = Column(Float)

    station_obj = relationship("Station", back_populates="measurements")
