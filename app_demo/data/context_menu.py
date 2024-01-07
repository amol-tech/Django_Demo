import yaml
from traitlets import Container


class ContextMenuProvider:
    __instance = None
    __dict_ctxt_menu = None

    def __init__(self):
        if ContextMenuProvider.__instance is None:
            print('Creating ContextMenuProvider instance')
            ContextMenuProvider.__instance = self
        else:
            raise Exception('This class is singleton')

    @staticmethod
    def get_instance():
        if ContextMenuProvider.__instance is None:
            ContextMenuProvider()
        return ContextMenuProvider.__instance

    def _get_context_menu(self,name):
        if self.__dict_ctxt_menu is None:
            with open('app_demo/data/context_menu.yaml', 'r') as file:
                self.__dict_ctxt_menu = yaml.safe_load(file)
        if name in self.__dict_ctxt_menu:
            list_dict_menu = self.__dict_ctxt_menu[name]
            list_dict_menu = [self.__update_dict_with_action_url(d) for d in list_dict_menu]
            return list_dict_menu
        return {}

    def __update_dict_with_action_url(self,dict_menu):
        #print('action_url' not in dict_menu)
        if ('action_index' not in dict_menu):
            dict_menu['action_index'] = 'NOT-DEFINE'
            dict_menu['action_title'] = 'NOT-DEFINE'
        if ('children' in dict_menu):
            list_dict_children = dict_menu['children']
            dict_menu['children'] = [self.__update_dict_with_action_url(d) for d in list_dict_children]
        return dict_menu
