from splash.models import *
from computerModels import comps

db.drop_all()
db.create_all()

for c in comps:
	driveSpace = c[6]
	if c[7]:
		driveSpace = c[7]

	newComp = Computer(budget=c[0], price=c[1], model=c[2], cpu=c[3], graphics=c[4], ram=c[5], drive=driveSpace, display=c[8], battery=c[9], quality=c[10], weight=c[11], thickness=c[12])
	db.session.add(newComp)

db.session.commit()