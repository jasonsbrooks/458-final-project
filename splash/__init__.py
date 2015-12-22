from splash.models import *
import operator

def score(personData, adjusted_weights):
	finalScoresDict = {}
	for c in Computer.query.all():
		finalScoresDict[c.model] = 0.0

	if personData['os'] == 'dm':
		adjusted_weights[0] = 0.0
		totalWeights = sum(adjusted_weights)
		for i in range(len(adjusted_weights)):
			adjusted_weights[i] = adjusted_weights[i] / totalWeights

	if personData['battery'] == 'dm':
		adjusted_weights[1] = 0.0
		totalWeights = sum(adjusted_weights)
		for i in range(len(adjusted_weights)):
			adjusted_weights[i] = adjusted_weights[i] / totalWeights

	if personData['harddrive'] == 'dm':
		adjusted_weights[2] = 0.0
		totalWeights = sum(adjusted_weights)
		for i in range(len(adjusted_weights)):
			adjusted_weights[i] = adjusted_weights[i] / totalWeights

	if personData['memory'] == 'dm':
		adjusted_weights[4] = 0.0
		totalWeights = sum(adjusted_weights)
		for i in range(len(adjusted_weights)):
			adjusted_weights[i] = adjusted_weights[i] / totalWeights

	if personData['size'] == 'dm':
		adjusted_weights[5] = 0.0
		totalWeights = sum(adjusted_weights)
		for i in range(len(adjusted_weights)):
			adjusted_weights[i] = adjusted_weights[i] / totalWeights

	for key, value in finalScoresDict.iteritems():
		comp_data = Computer.query.filter(Computer.model == key).first()
		osscore_run = os_score(comp_data.operating_system, personData['os']) * adjusted_weights[0]
		battery_run = battery_score(comp_data.battery_normalized, personData['battery']) * adjusted_weights[1]
		hddscore_run = harddrive_score(comp_data.harddrive_normalized, personData['harddrive']) * adjusted_weights[2]
		pricescore_run = price_score(comp_data.price_normalized, personData['budget']) * adjusted_weights[3]
		memscore_run = memory_score(comp_data.memory_normalized, personData['memory']) * adjusted_weights[4]
		sizescore_run = size_score(comp_data.size_normalized, personData['size']) * adjusted_weights[5]

		totalScore = osscore_run + battery_run + hddscore_run + pricescore_run + memscore_run + sizescore_run
		finalScoresDict[key] = totalScore

	return finalScoresDict

def price_score(computer_price, target_price):
	return(max(0, float(computer_price) - float(target_price))/1500.0)

def os_score(computer_os, target_os):
	if target_os == 'dm':
		return 0.0
	if computer_os == target_os:
		return 0.0
	return 1.0

def size_score(computer_size, target_size):
	if target_size == 'dm':
		return 0.0
	return(abs(float(computer_size)-float(target_size))/10.0)

def memory_score(computer_memory, target_memory):
	if target_memory == 'dm':
		return 0.0
	return(max(0,float(target_memory) - float(computer_memory))/8.0)

def harddrive_score(computer_drive, target_drive):
	if target_drive == 'dm':
		return 0.0
	return(max(0,float(target_drive) - float(computer_drive))/3.0)

def battery_score(computer_battery, target_battery):
	if target_battery == 'dm':
		return 0.0
	return(max(0,float(target_battery) - float(computer_battery))/3.0)


def update_weights(personData, weights, history):
	for comp in history:
		comp_data = Computer.query.filter(Computer.model == comp[0]).first()
		osscore_run = os_score(comp_data.operating_system, personData['os'])
		battery_run = battery_score(comp_data.battery_normalized, personData['battery'])
		hddscore_run = harddrive_score(comp_data.harddrive_normalized, personData['harddrive'])
		pricescore_run = price_score(comp_data.price_normalized, personData['budget'])
		memscore_run = memory_score(comp_data.memory_normalized, personData['memory'])
		sizescore_run = size_score(comp_data.size_normalized, personData['size'])
		
		weights[0] = max(0,weights[0] + -(osscore_run-.2)/10.0 * comp[1])
		weights[1] = max(0,weights[1] + -(battery_run-.2)/10.0 * comp[1])
		weights[2] = max(0,weights[2] + -(hddscore_run-.2)/10.0 * comp[1])
		weights[3] = max(0,weights[3] + -(pricescore_run-.2)/10.0 * comp[1])
		weights[4] = max(0,weights[5] + -(memscore_run-.2)/10.0 * comp[1])
		weights[5] = max(0,weights[4] + -(sizescore_run-.2)/10.0 * comp[1])

	totalWeights = sum(weights)
	for i in range(len(weights)):
		weights[i] = weights[i] / totalWeights

	return weights

def whichpc(personData):
	print personData
	weights = Weights.query.first()
	initial_weights = [weights.operating_system, weights.battery, weights.harddrive, weights.budget, weights.memory, weights.size]
	history = []
	for i in personData['prior_disliked']:
		history.append([i, -1])
	for i in personData['prior_liked']:
		history.append([i, 1])
	adjusted_weights = update_weights(personData, initial_weights, history)
	print adjusted_weights

	allScores = score(personData, adjusted_weights)
	sorted_scores = sorted(allScores.items(), key=operator.itemgetter(1))
	print sorted_scores
	return sorted_scores[-3:]