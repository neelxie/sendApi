# sendApi
[![Build Status](https://travis-ci.org/neelxie/sendApi.svg?branch=develop)](https://travis-ci.org/neelxie/sendApi)
[![Coverage Status](https://coveralls.io/repos/github/neelxie/sendApi/badge.svg?branch=develop)](https://coveralls.io/github/neelxie/sendApi?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/ec4df4bc881ee34bf6a2/maintainability)](https://codeclimate.com/github/neelxie/sendApi/maintainability)

SendIT is a courier service that helps users deliver parcels to different destinations.

<b> Site has been built with.</b>
 * Language - Python
 * Serverside Framework - Flask /Flask Restful
 * Testing Framework - Pytest
 * Linting Framework - Pylint
 * Style GuideLine - Autopep8

# Application Demo 
 * UserInterface - https://neelxie.github.io/SendIT/UI/
 * Heroku - https://mysenditapp.herokuapp.com/api/v1/

# Features

  * Fetch all parcel delivery orders - https://mysenditapp.herokuapp.com/api/v1/parcels
  * Fetch a specific parcel delivery order - https://mysenditapp.herokuapp.com/api/v1/parcels/<parcel_id>
  * Get all parcel delivery orders by a specific user - https://mysenditapp.herokuapp.com/api/v1/users/<user_id>/parcels
  * Cancel the specific parcel delivery order - https://mysenditapp.herokuapp.com/api/v1/parcels/<parcel_id>/cancel
  * Create a parcel delivery order. https://mysenditapp.herokuapp.com/api/v1/parcels

# Installation:
 * Clone git repo to local directory -- https://github.com/neelxie/SendApi.git
 * cd SendApi
 * Create a virtual environment:
  - virtualenv env
 * Activate virtual environment:
  - env\Scripts\activate
 * Install dependencies:
  - pip install -r requirements.txt
 * Do not forget to run this in the develop branch:
  - Git checkout develop

# Running the application:
 * 'Python run.py'

# Running the tests:
 * Pytest --cov=.

# Contribute
 * Join me and let us create super amazing stuff together.
 * https://github.com/neelxie/SendApi

# Credits
 * I thank GOD, to whom everything plays out.
 * I thank all fellow bootcampers for the help offered to better me.
 * I would like to thank Andela for the opportunity to change the world.

# Author
 * Sekidde Derrick