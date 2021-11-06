from app import app
from views import *

# Jika main.py dijalankan, aplikasi flask akan dijalankan.
# Fungsi update juga akan dipanggil agar memastikan data selalu up-to-date.
if __name__ == '__main__':
    # Update mungkin memakan waktu yang cukup lama, terlebih jika waktu update terakhir sudah jauh dari hari ini.
    # Uncomment update untuk mengaktifkan fitur update database.
    # update()
    app.run()
