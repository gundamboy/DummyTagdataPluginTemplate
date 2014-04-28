'''
Dummy Tag Plugin

Copyright: Charles Rowland

Name-US: Dummy Tag Data Plugin
 
Description-US: A dummy template for a tagdata plugin

Creation Date: 04/27/2014
'''


import os
import c4d
from c4d import bitmaps, plugins, utils

# Testing ids 1000001 - 1000010
# be sure to use a unique ID obtained from www.plugincafe.com
__plugin_id__ = 1000111
__version__ = "1.0"
__plugin_title__ = "Dummy Tag Plugin"


class DummyTagPlugin(plugins.TagData):

    def Draw(self, tag, op, bd, bh):
        '''
        Override - Called when the display is updated for you to display some visual element of your tag in the 3D view.
        '''
        pass
        return True

    
    def Init(self, node):
        tag = node
        data = tag.GetDataInstance()
        # now do stuff and blah blah blah.

        return True
    

    def Message(self, node, type, data):
        '''
        Override - Use to react to more messages. The return value depends on the message.
        '''

        if type == c4d.MSG_DESCRIPTION_COMMAND:
            if data['id'][0].id == 1000:
                print("congratulations, you have successfully pushed a button.")

                c4d.EventAdd()

        return True 


    def CoreMessage(self, id, msg):
        '''
        Override - Receives C4D core messages.
        '''
        pass
        return True


    def Free(self, node):
        ''' 
        Override - If your class has a destructor it is called as usual after this function.
        '''
        pass


    def AddToExecution(self, tag, list):
        '''
        Override - By default this function returns False. Then C4D will call Execute() at 
        the priority specified by the user in the EXPRESSION_PRIORITY parameter of the container.
        '''
        pass
        return True


    def Execute(self, tag, doc, op, bt, priority, flags):
        data = tag.GetDataInstance()
        
        return c4d.EXECUTIONRESULT_OK


if __name__ == "__main__":
    icon = bitmaps.BaseBitmap()
    dir, file = os.path.split(__file__)
    iconPath = os.path.join(dir, "res", "icon.tif")
    icon.InitWith(iconPath)

    plugins.RegisterTagPlugin(id = __plugin_id__,
                                  str = __plugin_title__,
                                  info = c4d.TAG_EXPRESSION|c4d.TAG_VISIBLE,
                                  g = DummyTagPlugin,
                                  description = "Tdummytagplugin",
                                  icon = icon)  