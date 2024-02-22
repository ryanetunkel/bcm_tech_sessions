import warnings

def api_v1_check_if_john_in_names(names: list[str]) -> bool:
    """Check if the name `John` is in the list of names"""
    warnings.warn('use v2 `api_v2_check_if_given_name_in_names` of this api', DeprecationWarning)
    if "john" in names:
        return True
    return False

def api_v2_check_if_given_name_in_names(name: str, names: list[str]) -> bool:
    """Checks that a given name exist in a list of names"""
    if name in names:
        return True
    return False
