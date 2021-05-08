from testbin import app
import os

if __name__ == '__main__':
    os.system('sudo apt-get install unixodbc unixodbc-dev')
    app.run()
