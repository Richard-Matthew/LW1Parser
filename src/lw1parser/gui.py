import tkinter as tk
from tkinter import filedialog
from pathlib import Path

from lw1parser.config import Config
from lw1parser.update import Update
from lw1parser.export import Export
from lw1parser.savegame import Save
from lw1parser.database import Engine
from lw1parser.utils import path_to_csv, resource_path


class GUI:
	def __init__(self):
		# Load Config
		Config.load_config()

		self.root = tk.Tk()
		self.root.iconbitmap(resource_path("icon.ico"))
		self.root.title("LW1 Parser")
		self.root.geometry("250x300")

		# Core Buttons
		self.btn_update = tk.Button(self.root, text="Update", width=20, command=self.do_update)
		self.btn_convert = tk.Button(self.root, text="Convert", width=20, command=self.do_convert)

		# Database Buttons
		self.btn_export = tk.Button(self.root, text="Export", width=20, command=self.do_export)
		self.btn_analyze = tk.Button(self.root, text="Analyze", width=20, command=self.do_analyze)

		self.btn_update.pack(pady=10)
		self.btn_convert.pack(pady=10)

		self.btn_export.pack(pady=10)
		self.btn_analyze.pack(pady=10)

		# Status label
		self.status = tk.Label(self.root, text="", fg="blue")
		self.status.pack(pady=10)

		# Modify buttons based on Config settings
		self.config_buttons()

	# BUTTON ACTIONS #
	def do_update(self):
		"""
		Updates database or exports to csv based on Config settings.
		"""
		try:
			self.set_status("...", "Black")
			save = Save()
			update = Update(save)
			was_inserted = update.do_update()

			if was_inserted:
				self.set_status("Update completed.", "Green")
			elif Config.use_database:
				self.set_status("Save already exists in database.", "Blue")
			else:
				self.set_status(f"{Config.spreadsheet_format} export completed.", "Green")
				
		except Exception as e:
			self.set_status(f"Error: {e}", "Red")

	def do_export(self):
		if not Config.use_database:
			self.set_status("Database currently disabled by config.", "Blue")
			return
		try:
			self.set_status("...", "Black")
			database = Engine()

			units = database.get_units()

			if not units:
				self.set_status("No data found.", "Blue")
				return

			Export.export_csv(units)

			self.set_status(f"{Config.spreadsheet_format} export completed.", "Green")
		except Exception as e:
			self.set_status(f"Error: {e}", "Red")

	def do_analyze(self):
		self.set_status("...", "Black")
		self.set_status("Analyze feature not yet implemented.", "Blue")

	def do_convert(self):
		try:
			self.set_status("...", "Black")

			save_path = filedialog.askopenfilename(
				title = "Select XCOM Save File",
				initialdir= (
					str(Config.save_path) if Config.convert_opens_save_folder else None
				),
				filetypes = [
					("XCOM Save Files", "save*"),
					("All Files", "*.*")
					]
			)
			if not save_path:
				self.set_status("No file selected.", "Blue")
				return
			
			export_path = filedialog.asksaveasfilename(
				title = f"Save {Config.spreadsheet_format} As",
				defaultextension = ".csv",
				filetypes=  self._get_export_file_extension()
			)
			if not export_path:
				self.set_status("No export location selected.", "Blue")
				return

			path_to_csv(Config.spreadsheet_format, Path(save_path), Path(export_path))
			
			self.set_status(f"Converted to {Config.spreadsheet_format}: \n{save_path}", "Green")

		except Exception as e:
			import traceback
			traceback.print_exc()
			self.set_status(f"Error: {e}", "Red")
		
	
	# Status
	def set_status(self, msg, color="Pink"):
		self.status.config(text=msg, fg=color)

	def run(self):
		self.root.mainloop()

	def config_buttons(self):
		# Disable database buttons if database is not enabled
		self.btn_export.config(state="normal" if Config.use_database else "disabled")
		self.btn_analyze.config(state="normal" if Config.use_database else "disabled")

		self.btn_analyze.pack_forget()

	# Helpers
	def _get_export_file_extension(self):
		match Config.spreadsheet_format:
			case "CSV":
				return [("CSV Files", "*.csv")]
			case "EXCEL":
				return [("Excel Workbook", "*.xlsx")]

def run_gui():
	gui = GUI()
	gui.run()
