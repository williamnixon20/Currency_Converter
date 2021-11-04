from app import app
from views import *

# Jika main.py dijalankan, aplikasi flask akan dijalankan.
# Fungsi update juga akan dipanggil agar memastikan data selalu up-to-date.
if __name__ == '__main__':
    update()
    app.run()
