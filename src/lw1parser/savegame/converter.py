import json
import subprocess
import sys
from pathlib import Path


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
		result = subprocess.run(
			["xcom2json.exe", "-o", str(output_path), str(save_path)],
			check=True,
			capture_output=True,
			text=True,
			creationflags=(
				subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
			)
		)

		if result.returncode != 0:
			raise RuntimeError(f"xcom2json failed or missing: {result.stderr}")

		with open(output_path, "r", encoding="utf-8") as f:
			return json.load(f)

	def cleanup(self):
		if self.last_json_path and self.last_json_path.exists():
			self.last_json_path.unlink()