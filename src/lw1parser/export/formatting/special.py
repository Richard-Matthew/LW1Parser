from openpyxl.styles import PatternFill

from lw1parser import Config
from lw1parser.maps import MEDAL_MAP, PSI_RANK_MAP

from .rules import add_text_fill_rule


def apply_special_formatting(sheet, headers) -> None:
	if not Config.do_special_formatting:
		return
	
	# Find the column index
	try:
		special_idx = headers.index("Special")
	except ValueError:
		return
	
	column_special = chr(ord("A") + special_idx)

	# Officer formatting
	officer_fill = PatternFill(start_color=Config.officer_fill, end_color=Config.officer_fill, fill_type="solid")
	add_text_fill_rule(sheet, column_special, MEDAL_MAP.values(), officer_fill, Config.officer_text)

	# Psi formatting
	psi_fill = PatternFill(start_color=Config.psi_fill, end_color=Config.psi_fill, fill_type="solid")
	add_text_fill_rule(sheet, column_special, PSI_RANK_MAP.values(), psi_fill, Config.psi_text)

	# MEC formatting
	mec_fill = PatternFill(start_color=Config.mec_fill, end_color=Config.mec_fill, fill_type="solid")
	add_text_fill_rule(sheet, column_special, "MEC", mec_fill, Config.mec_text)