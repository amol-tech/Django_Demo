import yaml

def next_line(ctr=0):
    return '\n' + '   ' * ctr

def get_model_metadata(model_class):
    list_out = []
    attributes = ['name','max_length','null','primary_key','max_digits']
    fields = model_class._meta.fields
    for f in fields:
        dict_field_attr = {}
        field_meta = f.__dict__
        for attr in attributes:
            dict_field_attr[attr] = field_meta[attr] if attr in field_meta else None
        list_out.append(dict_field_attr)
    return list_out

def generate_model_html(model_class,dir_app,model_name):
    # Html Tags and Meta Data
    with open('html_tags.yaml', 'r') as file:
        html_tags = yaml.safe_load(file)
    list_field_meta = get_model_metadata(model_class)
    
    # Start creating html text
    str_out = '{% load static %}'
    str_out = str_out + next_line() +  html_tags['table'].replace('%table_id%','tb_'+model_name)
    
    # Table Header
    str_out = str_out + next_line(1) + html_tags['thead']
    str_out = str_out + next_line(2) + '<tr>'
    for f_meta in list_field_meta:
        str_out =  str_out + next_line(3) + html_tags['th'] + f_meta['name'].title() + '</th>'
    str_out =  str_out + next_line(2) + '</tr>'
    str_out =  str_out + next_line(1) + '</thead>'
    
    # Table Body
    
    str_out = str_out + next_line(1) + html_tags['tbody']
    str_out = str_out + next_line(2) + '{% for ' + model_name + ' in ' + model_name + '_list %}'
    str_out = str_out + next_line(3) + html_tags['tr']
    for f_meta in list_field_meta:
        str_out =  str_out + next_line(4) + html_tags['td'] + '{{' + model_name + '.' +f_meta['name'] + '}}'  + '</td>'
    str_out = str_out + next_line(3) + '</tr>'
    str_out = str_out + next_line(2) + '{% endfor %}'
    str_out = str_out + next_line(1) + '</tbody>'
    
    str_out =  str_out + next_line() + '</table>'
    
    html_table = 'templates/'+dir_app+'/tables/table_'+model_name+'.html'
    with open(html_table, 'w') as f:
        f.write(str_out)
    print('Generated successfully ...' + html_table)
    
    html_list_tmpl = 'bootstrap_src/list.template'
    html_list = 'templates/'+dir_app+'/list_'+model_name+'.html'
    replace_app_model(html_list_tmpl,html_list,dir_app,model_name)
    print('Generated successfully ...' + html_list)
    
def generate_model_code(app_name,model_name):
    fin_name = 'bootstrap_src/code.template'
    fout_name = app_name + '/' + model_name +'.code'
    fout = open(fout_name, "w")
    replace_app_model(fin_name,fout_name,app_name,model_name)
    print('Code generated successfully ...' + fout_name)
    
def replace_app_model(fin_name,fout_name,app_name,model_name):
    #input file
    fin = open(fin_name, "rt")
    #output file to write the result to
    fout = open(fout_name, "w")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        ln = line.replace('#application#', app_name)
        ln = ln.replace('#model#', model_name)
        ln = ln.replace('#Model#', model_name.title())
        fout.write(ln)
    #close input and output files
    fin.close()
    fout.close()
    