# sendApi
SendIT is a courier service that helps users deliver parcels to different destinations.

[![Build Status](https://travis-ci.org/neelxie/sendApi.svg?branch=develop)](https://travis-ci.org/neelxie/sendApi)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a439c5890cce4f94b3b50e53036c014e)](https://www.codacy.com/app/neelxie/sendApi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=neelxie/sendApi&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/neelxie/sendApi/badge.svg?branch=develop)](https://coveralls.io/github/neelxie/sendApi?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/ec4df4bc881ee34bf6a2/maintainability)](https://codeclimate.com/github/neelxie/sendApi/maintainability)


<b> Site has been built with.</b>
*   Language - Python
*   Serverside Framework - Flask 
*   Testing Framework - Pytest
*   Linting Framework - Pylint
*   Style GuideLine - Autopep8

# Application Demo 

*   UserInterface ``` https://neelxie.github.io/SendIT/UI/ ```

# Features

  | REQUESTS     | APP ROUTES                           | FUNCTION                                             |
  |--------------|---------------------------------------------------------------------------------------------|
  |  GET         |  /api/v1/parcels                     | Fetch all parcel delivery orders.                    |
  |  GET         |  /api/v1/parcels/[parcel_id]         | Fetch parcel delivery order by id.                   |
  |  GET         |  /api/v1/users/[user_id]/parcels     | Fetch all parcel delivery orders by a specific user. |
  |  PUT         |  /api/v1/parcels/[parce_id]/cancel   | Cancel a specific parcel delivery order.             |
  |  POST        |  /api/v1/parcels                     | Create a parcel delivery order.                      |
  |  POST        |  /api/v1/users                       | Create a SendIT App user.                            |  

# Installation:

*  Clone git repo to local directory ``` https://github.com/neelxie/SendApi.git ```
``` cd SendApi ```

*  Create a virtual environment
``` virtualenv env ```

*  Activate virtual environment
``` env\Scripts\activate ```

*  Install dependencies
``` pip install -r requirements.txt ```

*  Do not forget to run this in the develop branch
``` git checkout develop ```

# Running the application:

*   Inside the SendApi folder run this command.
``` python run.py ```

# Running the tests:

*   Run this command in the project directory.
``` pytest ```

# Deployment

*  This app has been deployed on Heroku at the url below
``` https://mysenditapp.herokuapp.com/api/v1/ ```

# Contribute

*  Join me and let us create super amazing stuff together.
``` https://github.com/neelxie/SendApi ```

# Credits

*   I thank GOD, to whom everything plays out.
*   I thank all fellow bootcampers for the help offered to better me.
*   I would like to thank Andela for the opportunity to change the world.

# Author

*   Sekidde Derrick