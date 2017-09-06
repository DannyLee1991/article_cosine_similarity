import os

def _remove_duplicate(dict_list):
    seen = set()
    new_dict_list = []
    for dict in dict_list:
        # t_dict = {'res_model': dict['res_model'], 'res_id': dict['res_id']}
        t_dict = dict
        t_tup = tuple(t_dict.items())
        if t_tup not in seen:
            seen.add(t_tup)
            new_dict_list.append(dict)
    return new_dict_list
