from lw1parser import maps


class _PropertyUtils:
    @staticmethod
    def get_property(props, name, default_return=None):
        """
        Like json.get() except it looks through a list of dictionaries.
        """
        for prop in props:
            if prop.get("name") == name:
                return prop
        return default_return

    @staticmethod
    def properties_array_to_dict(props):
        """
        Converts nested array-of-dict into nested dicts.
        """
        out = {}

        for prop in props:
            name = prop.get("name")
            if not name:
                continue

			# If this property contains its own nested properties array do a recusion
            if "properties" in prop and isinstance(prop["properties"], list):
                out[name] = _PropertyUtils.properties_array_to_dict(prop["properties"])
                continue

            kind = prop.get("kind")

            # Simple types
            if kind == "StrProperty":
                out[name] = prop["value"]["str"]

            elif kind in ("IntProperty", "FloatProperty", "BoolProperty", "ByteProperty"):
                out[name] = prop["value"]

            # Arrays
            elif kind in ("StaticArrayProperty", "ArrayProperty"):
                out[name] = prop.get("int_values", prop.get("data"))

            # Otherwise store raw dict
            else:
                out[name] = prop

        return out

    @staticmethod
    def _parse_mapped_array(flags, mapping, skip_first: bool):
        """
        Takes an array of dicts then returns a dict with id:name keys based on positional mapping.
        """
        if not flags:
            return {}

        output = {}

        # Technically an integer array, and some values can be non-binary
		# Unpack index and value (usually a binary flag) just in case
        for index, flag in enumerate(flags):
            if index == 0 and skip_first:
                continue  # First value is a placeholder "None" string
            if not flag:  
                continue  # Binary-ish array, 0 means abilities is not active

            output[index] = mapping.get(index, f"Unknown({index})")

        return output

    @staticmethod
    def _parse_class(unit_dict):
        """
        Takes a normalized nested unit dict and returns a class string.
        """
        kClass = unit_dict.get("m_kSoldier", {}).get("kClass", {})

        supra_class = kClass.get("eType", "")
        infra_class = kClass.get("strName", "")

        if infra_class == "":
            return maps.SUPRA_CLASSES.get(supra_class, supra_class)
        else:
            return infra_class