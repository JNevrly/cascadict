'''
.. module:: cascadict.test_cascadict
   :platform: Unix, Windows
   :synopsis:
.. moduleauthor:: JNevrly

'''
import unittest
from cascadict import CascaDict, CascaDictError
import pickle


def access_key(dict, key):
    return dict[key] == None

class TestCascaDict(unittest.TestCase):
    
    def setUp(self):
        self.cd_root = CascaDict([('name', 'Root'), ('color', 'Root color'), ('lvl', 0)]) #usuall, args based init
        self.cd_level1 = CascaDict(name='Lvl1', color='Lvl1 color', lvl= 1, ancestor=self.cd_root) #kwargs based init
        self.cd_level2 = self.cd_level1.cascade()
        self.cd_level2.update({'name': 'Lvl2', 'color': 'Lvl2 color', 'lvl': 2, 'nest': {'name': 'nested_lvl_2', 'lvl': 22, 'color': 'nested_color lvl2'}}) #cascade&update style init
        
        #Insert something with to level1
        self.cd_level1['test_insert'] = 'contents'
        
        #Insert something onlu to level1
        self.cd_level1['test_insert_level1'] = 'contents-lvl1'
        
        #Insert something to root level
        self.cd_root['test_insert_root'] = 'contents-root'
        
        #Insert something to root level which has the same name as the level1
        self.cd_root['test_insert'] = 'contents_root_only'
    
    def test_insert(self):
        self.assertTrue(self.cd_level1['test_insert'] == 'contents')
        
    def test_insert_level(self):
        self.assertRaises(KeyError, access_key, self.cd_root, 'test_insert_level1')
    
    def test_getitem(self):
        self.assertTrue(self.cd_level1['test_insert_root'] == 'contents-root')
        
    def test_getitem_level(self):
        self.assertTrue(self.cd_root['test_insert'] == 'contents_root_only')
    
    def test_get(self):
        self.assertTrue(self.cd_level1.get('test_insert_root') == 'contents-root')
        
    def test_get_default(self):
        self.assertTrue(self.cd_level1.get('test_nonexistent', 'response') == 'response')
        
    def test_has_key(self):
        self.assertTrue(self.cd_level1.has_key('test_insert_root'))
        
    def test_contains(self):
        self.assertTrue('test_insert_root' in self.cd_level1)
        
    def test_final_dict(self):
        print(self.cd_level1.final_dict)
        
    def test_flatten_dict_top(self):
        temp = self.cd_level1.__flatten__()
        print(temp)
        self.assertTrue(temp['name'] == 'Lvl1')
    
    def test_flatten_dict_bottom(self):
        temp = self.cd_level1.__flatten__(level='bottom')
        print(temp)
        self.assertTrue(temp['name'] == 'Root')
        
    def test_get_cascaded(self):
        temp = self.cd_level2.get_cascaded('lvl')
        print(temp)
        self.assertTrue(temp == [2, 1, 0])
        
    def test_get_cascaded_default(self):
        temp = self.cd_level2.get_cascaded('lvl_nonexistent', 'nic')
        self.assertTrue(temp == 'nic')
        
    def test_items(self):
        print(self.cd_level2.items())
        
    def test_inherit(self):
        temp = self.cd_level2.cascade({'name':'lvl3', 'lvl':3})
        self.assertTrue(temp['name'] == 'lvl3')
    
    def test_repr(self):
        print(self.cd_level2)
        
    def test_delete_valid(self):
        del self.cd_level2['color']
        self.assertTrue(self.cd_level2['color'] == 'Lvl1 color')
        
    def test_delete_invalid(self):
        def delsomething():
            del self.cd_level2['color']
            del self.cd_level2['color']
        self.assertRaises(CascaDictError, delsomething)
        
    def test_pickle(self):
        self.cd_level2['nest']['lvl'] = 23
        ptemp = pickle.dumps(self.cd_level2)
        temp = pickle.loads(ptemp)
        print(temp['nest'].get_cascaded('lvl'))
        self.assertTrue(temp['nest'].get_cascaded('lvl') == [23, 22])
        
        
    def test_nesting(self):
        self.cd_level2['nest']['color'] = 'nested overriden color'
        print(self.cd_level2['nest'].get_cascaded('color'))
        
#     def test_viewkeys(self):
#         print self.cd_level2.viewkeys()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
