import csv

class Export():
	def export_csv(units, filename = "unit_export.csv"):
		"""
		Writes unit stats to a .csv file.
		"""
		with open(filename, "w", newline="") as f:
			writer = csv.DictWriter(f, fieldnames=units[0].to_dict().keys())
			writer.writeheader()

			for unit in units:
				writer.writerow(unit.to_dict())