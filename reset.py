from splash.models import *
from computerModels import comps

db.drop_all()
db.create_all()

for c in comps:
	if Computer.query.filter(Computer.model == c[2]).first():
		continue

	# normalize drivespace
	driveSpace = c[6]
	if c[7]:
		driveSpace = c[7]
	
	if len([s for s in driveSpace.split(' ') if "GB" in s]) > 0:
		driveSpace_normalized = [s for s in driveSpace.split(' ') if "GB" in s][0][:-2]
	else:
		driveSpace_normalized = '1000'

	# normalize price
	price_normalized = c[1][1:]

	# normalize operatingSystem
	if 'Apple' in c[2]:
		os_normalized = 'mac'
	else:
		os_normalized = 'windows'

	# normalize battery
	battery_normalized = c[9].split(' ')[0]
	if battery_normalized.find('hrs') > 0:
		battery_normalized = battery_normalized[:battery_normalized.find('hrs')]

	# memory normalized
	memory_normalized = c[5][:c[5].find('GB')]

	# size normalized
	size_normalized = str(int(float(c[8].split(' ')[0][:-1])))

	newComp = Computer(budget=c[0], price=c[1], model=c[2], cpu=c[3], graphics=c[4], ram=c[5], drive=driveSpace, display=c[8], battery=c[9], quality=c[10], weight=c[11], thickness=c[12], price_normalized=price_normalized, operating_system=os_normalized, battery_normalized=battery_normalized, harddrive_normalized=driveSpace_normalized, memory_normalized=memory_normalized, size_normalized=size_normalized)
	db.session.add(newComp)
	db.session.commit()

w = Weights(operating_system = 0.3, battery = 0.1, harddrive = 0.1, budget = 0.3, memory = 0.1, size = 0.1)
db.session.add(w)
db.session.commit()
