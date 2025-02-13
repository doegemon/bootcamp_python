from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()


class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(20))
    email = Column(String(50))
    address = Column(String(100))


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    price = Column(Integer)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))

    vendor = relationship("Vendor")


engine = create_engine("sqlite:///adv_database.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

try:
    with Session() as session:
        vendors_list = [
            Vendor(
                name="Vendor A",
                phone="12345678",
                email="contact@a.com",
                address="Address A",
            ),
            Vendor(
                name="Vendor B",
                phone="87654321",
                email="contact@b.com",
                address="Address B",
            ),
            Vendor(
                name="Vendor C",
                phone="12348765",
                email="contact@c.com",
                address="Address C",
            ),
            Vendor(
                name="Vendor D",
                phone="56781234",
                email="contact@d.com",
                address="Address D",
            ),
            Vendor(
                name="Vendor E",
                phone="43217865",
                email="contact@e.com",
                address="Address E",
            ),
        ]
        session.add_all(vendors_list)
        session.commit()
except SQLAlchemyError as e:
    print(f"There was an error while adding the vendors: {e}")

try:
    with Session() as session:
        products_list = [
            Product(
                name="Product 1",
                description="Product Description 1",
                price=100,
                vendor_id=1,
            ),
            Product(
                name="Product 2",
                description="Product Description 2",
                price=200,
                vendor_id=2,
            ),
            Product(
                name="Product 3",
                description="Product Description 3",
                price=300,
                vendor_id=3,
            ),
            Product(
                name="Product 4",
                description="Product Description 4",
                price=400,
                vendor_id=4,
            ),
            Product(
                name="Product 5",
                description="Product Description 5",
                price=500,
                vendor_id=5,
            ),
        ]
        session.add_all(products_list)
        session.commit()
except SQLAlchemyError as e:
    print(f"There was an error while adding the products: {e}")


result = (
    session.query(Vendor.name, func.sum(Product.price).label("total_price"))
    .join(Product, Vendor.id == Product.vendor_id)
    .group_by(Vendor.name)
    .all()
)

for name, total_price in result:
    print(f"Vendor: {name} | Total Product Price: {total_price}.")
