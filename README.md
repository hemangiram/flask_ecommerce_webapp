# E-Commerce Web App Using Python Flask and SQLAlchemy.

After completing my first computer science class through CS50 (EDX), I decided to build an e-commerce website
using Python, Flask, SQLalchemy (and also HTML, CSS, Jinja).

The original website is hosted [here](https://unwrapla.com/) and was built on Shopify. This is a zero waste business offering
refilling services for cleaning and beauty products.

I reproduced this web app and tried to imitate their design and main features. 

On this project I focused on implementing a shopping cart.

Once logged in, users can:
- Add products to their shopping cart
- Update the quantity, or Remove items
- See the total cost

The database includes 3 models: User, Products and Cart. When a user add a product to his cart, a new "cart item" will be added
to the Cart model with the user id and product id.


## How to run this application locally

To install all the packages, run:

```
pip3 install -r requirements.txt
```

Then run:

```
cd unwrap
python run.py
```


## Resources

- Bootstrap
https://getbootstrap.com/
