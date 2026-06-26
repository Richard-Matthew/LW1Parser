from pathlib import Path
import re

class _Locator:
	def find_latest(self, save_dir: Path) -> Path:
		if not save_dir.exists():
			raise FileNotFoundError(f"Save directory not found: {save_dir}")

		save_files = [
			f for f in save_dir.iterdir()
			if f.is_file() and re.fullmatch(r"save(\d+)", f.name)
		]

		if not save_files:
			raise FileNotFoundError(f"No XCOM save files found in {save_dir}")

		save_files.sort(key=lambda f: f.stat().st_mtime)
		return save_files[-1]