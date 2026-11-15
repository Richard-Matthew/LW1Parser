import json
import subprocess
import sys
from pathlib import Path

from lw1parser.exceptions import (
	TacticalSaveError,
	Xcom2jsonMissingError,
	Xcom2jsonUnknownError,
)


class _Converter:
	def __init__(self):
		self.last_json_path: Path | None = None

	def convert(self, save_path: Path) -> dict:
		"""
		Returns the json output of xcom2json from the xcomsave project.
		"""
		if not save_path.exists():
			raise FileNotFoundError(f"Save file not found: {save_path}")


		# Check for xcom2json.exe
		exe_path = Path("xcom2json.exe")
		if not exe_path.exists():
			raise FileNotFoundError("Could not locate xcom2json.exe")

		output_path = Path("export.json")
		self.last_json_path = output_path

		# Suppress console popup
		try:
			subprocess.run(
				["xcom2json.exe", "-o", str(output_path), str(save_path)],
				check=True,
				capture_output=True,
				text=True,
				creationflags=(
					subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
				)
			)
		except FileNotFoundError as e:
			raise Xcom2jsonMissingError("xcom2json.exe failed or missing") from e
			
		except subprocess.CalledProcessError as e:
			stderr = e.stderr or ""

			if "Saved games in tactical missions are not supported" in stderr:
				raise TacticalSaveError from e

			raise Xcom2jsonUnknownError(stderr) from e
			
		with open(output_path, "r", encoding="utf-8") as f:
			return json.load(f)

	def cleanup(self):
		if self.last_json_path and self.last_json_path.exists():
			self.last_json_path.unlink()