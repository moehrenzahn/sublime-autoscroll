# import time
import sublime
import sublime_plugin

centered = 1

class AutoScroll(sublime_plugin.EventListener):
    def on_modified_async(self, view):
        if (view.settings().get('auto_scroll') == 1):
            for region in view.sel():
                view.show_at_center(region)

def experimental():
    # On centering the view, on_selection_modified gets called again. The varible centered serves to check that we don't get into a loop.
    if (view.settings().get('auto_scroll') == 1):
        # Get selected text
        global centered
        global region1
        global region2
        
        if centered == 1:
            print ('Loop 1')
            centered = 2
            for region in view.sel():
                region1 = region
                #print (region1) # DEBUG
                s = view.substr(region)
                length1 = (len(s))
            # Wait a moment
            time.sleep(.2)
            # Get the now selected text 
            for region in view.sel():  
                region2 = region
                #print (region2) # DEBUG
                s = view.substr(region)
                length2 = (len(s))
            # See if selection changed
            if (length1 == 0 and length2 == 0 and region1 == region2):
                view.show_at_center(region)
        if centered == 2:
            centered = 1
            print ('Loop 2')
        print('done')