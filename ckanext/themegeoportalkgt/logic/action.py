import ckan.plugins.toolkit as tk
import ckanext.themegeoportalkgt.logic.schema as schema


@tk.side_effect_free
def themegeoportalkgt_get_sum(context, data_dict):
    tk.check_access(
        "themegeoportalkgt_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.themegeoportalkgt_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'themegeoportalkgt_get_sum': themegeoportalkgt_get_sum,
    }
