from models import db, Puppy, Owner, Toy

# Creating 2 puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add puppies to DB
db.session.add_all([rufus, fido])
db.session.commit()

# Check
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').all()[0]
print(rufus)

# Create onwer object
jose = Owner('Jose', rufus.id)

# Give Rufus some report_toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

# Grab Rufus after those additions
rufus = Puppy.query.filter_by(name='Rufus').all()[0]
print(rufus)
print(rufus.report_toys())
