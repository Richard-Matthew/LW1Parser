from openpyxl.styles import PatternFill

from lw1parser import Config
from lw1parser.maps import CLASS_TYPES

from .rules import add_text_fill_rule


def apply_class_formatting(sheet, headers) -> None:
	if not Config.do_class_formatting:
		return
	
	# Find the column index
	try:
		special_idx = headers.index("Class")
	except ValueError:
		return

	column_class = chr(ord("A") + special_idx)

	for class_type, class_list in CLASS_TYPES.items():
		bold = Config.bold_mec_classes and class_type == "MEC"

		for cls in class_list:
			cls_norm = cls.lower().replace("-", "_")

			add_text_fill_rule(
				sheet, column_class,
				cls,
				PatternFill(start_color=getattr(Config, f"{cls_norm}_fill"), end_color=getattr(Config, f"{cls_norm}_fill"), fill_type="solid"),
				getattr(Config, f"{cls_norm}_text", None),
				bold
			)