"""
Creating a simple class with Python
"""

class LogTomcat:

	def __init__(self,addressLog,dateLog,contextLog):
		self.addressLog = addressLog
		self.dateLog = dateLog
		self.contextLog = contextLog

	def affichageLogs(self):
		return '{} {} {} '.format(self.addressLog, self.dateLog, self.contextLog)

logOne = LogTomcat('10.10.10.1','2017','wwww.python.com')
logTwo = LogTomcat('10.10.10.100','2015','wwww.abidjan.net')

#print(logOne.addressLog, logOne.dateLog, logOne.contextLog)
#print(logTwo.addressLog, logTwo.dateLog, logTwo.contextLog)

#Utilisation de la function affichageLogs pour l'affichage des instances de Logs
print(logOne.affichageLogs())
print(logTwo.affichageLogs())
