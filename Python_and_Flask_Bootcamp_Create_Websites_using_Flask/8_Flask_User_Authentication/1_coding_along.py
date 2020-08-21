from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed_password = bcrypt.generate_password_hash(password=password)
#print(hashed_password)

check = bcrypt.check_password_hash(hashed_password, 'wrongpassword')
#print(check)

check = bcrypt.check_password_hash(hashed_password, 'supersecretpassword')
#print(check)

from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass = generate_password_hash(password)
print(hashed_pass)

check = check_password_hash(hashed_pass, 'wrong')
print(check)

check = check_password_hash(hashed_pass, 'supersecretpassword')
print(check)
