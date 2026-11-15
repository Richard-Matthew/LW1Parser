import tkinter as tk
from functools import wraps
from pathlib import Path
from tkinter import filedialog

from lw1parser.config import Config
from lw1parser.database import Database
from lw1parser.export import export_spreadsheet
from lw1parser.savegame import Savegame
from lw1parser.update import Update
from lw1parser.utils import path_to_csv, resource_path


def gui_buttons(func):
	@wraps(func)
	def wrapper(self, *args, **kwargs):
		try:
			return func(self, *args, **kwargs)
		except (ValueError, NameError, KeyError) as e:
			self._set_status(f"Error: {e}", "Red")
		except PermissionError as e:
			self._set_status(f"File Access Error: {e}\n", "Red")
		except FileNotFoundError as e:
			self._set_status(f"Missing File Error: {e}\n", "Red")
		except Exception as e:  # noqa: BLE001
			# Tkinter likes to silently hide error messages
			self._set_status(f"Unknown Error: {e}\n", "Red")
	return wrapper
		
class GUI:
	def __init__(self):
		# Load Config
		Config.load_config()

		self.root = tk.Tk()
		self.root.iconbitmap(resource_path("icon.ico"))
		self.root.title("LW1 Parser")
		self.root.geometry("250x300")

		# Event binding
		self.root.bind("<Configure>", self._on_resize)

		# BUTTON FRAME
		self.button_frame = tk.Frame(self.root)
		self.button_frame.pack(fill="x", pady=10)

		# Core Buttons
		self.btn_update = tk.Button(self.button_frame, text="Update", width=20, command=self._do_update)
		self.btn_convert = tk.Button(self.button_frame, text="Convert", width=20, command=self._do_convert)
		# Database Buttons
		self.btn_export = tk.Button(self.button_frame, text="Export", width=20, command=self._do_export)
		self.btn_analyze = tk.Button(self.button_frame, text="Analyze", width=20, command=self._do_analyze)

		self.btn_update.pack(pady=5)
		self.btn_convert.pack(pady=5)

		self.btn_export.pack(pady=5)
		self.btn_analyze.pack(pady=5)

		# STATUS FRAME
		self.status_frame = tk.Frame(self.root)
		self.status_frame.pack(fill="x", pady=0)

		# Status label
		self.status = tk.Label(
			self.status_frame,
			text="",
			fg="blue",
			justify="center",
			anchor="center",
		)
		self.status.pack(fill="both", expand=True, padx=10, pady=5)

		# Modify buttons based on Config settings
		self._config_buttons()

	def run(self):
		self.root.mainloop()

	# EVENT HANDLERS #
	def _on_resize(self, event):
		new_width = self.status_frame.winfo_width() - 10
		min_text_width = 50

		if new_width > min_text_width:
			self.status.config(wraplength=new_width)

	# BUTTON ACTIONS #
	@gui_buttons
	def _do_update(self):
		"""
		Updates database or exports to csv based on Config settings.
		"""
		self._set_status("...", "Black")
		save = Savegame.load()
		update = Update(save)
		was_inserted = update.do_update()

		if was_inserted:
			self._set_status("Update completed.", "Green")
		elif Config.use_database:
			self._set_status("Save already exists in database.", "Blue")
		else:
			self._set_status(f"{Config.spreadsheet_format} export completed.", "Green")

	@gui_buttons
	def _do_export(self):
		if not Config.use_database:
			self._set_status("Database currently disabled by config.", "Blue")
			return

		self._set_status("...", "Black")
		database = Database()

		save = database.get_save()

		if not save:
			self._set_status("No data found.", "Blue")
			return

		export_spreadsheet(Config.spreadsheet_format, save)

		self._set_status(f"{Config.spreadsheet_format} export completed.", "Green")

	@gui_buttons
	def _do_analyze(self):
		self._set_status("...", "Black")
		self._set_status("Analyze feature not yet implemented.", "Blue")

	@gui_buttons
	def _do_convert(self):
		self._set_status("...", "Black")

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
			self._set_status("No file selected.", "Blue")
			return
		
		export_path = filedialog.asksaveasfilename(
			title = f"Save {Config.spreadsheet_format} As",
			defaultextension = ".csv",
			filetypes=  self._get_export_file_extension()
		)
		if not export_path:
			self._set_status("No export location selected.", "Blue")
			return

		path_to_csv(Config.spreadsheet_format, Path(save_path), Path(export_path))
		
		self._set_status(f"Converted to {Config.spreadsheet_format}: \n{save_path}", "Green")
	
	# Status
	def _set_status(self, msg, color="Pink"):
		self.status.config(text=msg, fg=color)

	def _config_buttons(self):
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
