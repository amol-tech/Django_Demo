import datetime
import calendar

def get_period_tree(dt_min,dt_max):
    dict_period = {}
    list_dict_tree = []
    for y in range(dt_max.year,dt_min.year-1,-1):
        dict_node = {}
        di_detail = {}
        di_detail['from_date'] = datetime.date(y,1,1)
        di_detail['to_date'] = datetime.date(y,12,31)
        dict_period[str(y)] = di_detail
        list_dict_nodes = []
        
        for m in range(di_detail['to_date'].month,di_detail['from_date'].month-1,-1):
            dict_child_node = {}
            res = calendar.monthrange(y,m)
            di_detail = {}
            dt_start = datetime.date(y,m,1)
            name = dt_start.strftime('%b-%Y')
            di_detail['from_date'] = dt_start
            di_detail['to_date'] =  datetime.date(y,m,res[1])
            dict_period[name] = di_detail
            
            dict_child_node['name'] = name
            dict_child_node['icon'] = 'fa fa-bars'
            dict_child_node['children'] = []
            list_dict_nodes.append(dict_child_node)
            
        dict_node['name'] = str(y)
        dict_node['icon'] = 'far fa-calendar'
        dict_node['children'] = list_dict_nodes
        list_dict_tree.append(dict_node)
        
    return dict_period,list_dict_tree