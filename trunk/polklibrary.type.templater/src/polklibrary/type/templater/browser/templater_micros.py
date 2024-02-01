from chameleon import PageTemplate
from plone import api
from Products.CMFPlone.utils import safe_unicode
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from AccessControl import getSecurityManager
from Products.CMFCore.permissions import AddPortalContent, ModifyPortalContent, ReviewPortalContent , ManagePortal



class BaseTemplaterView(BrowserView):

    def check_permission(self, check):
        sm = getSecurityManager()
        
        if check == "Anonymous":
            if api.user.is_anonymous():
                return True
        elif check == "Authenticated":
            if not api.user.is_anonymous():
                return True
        elif check == "Contributor":
            if sm.checkPermission(AddPortalContent , self.context):
                return True
        elif check == "Editor":
            if sm.checkPermission(ModifyPortalContent, self.context):
                return True
        elif check == "Reviewer":
            if sm.checkPermission(ReviewPortalContent , self.context):
                return True
        elif check in ["Manager", "Site Manager", "Administrator", "Site Administrator"]:
            if sm.checkPermission(ManagePortal, self.context):
                return True
        return False



class ImageTemplater(BaseTemplaterView):

    template = ViewPageTemplateFile("image_micro.pt")
    
    def __call__(self, show_description):
        self.show_description = show_description
        return self.template()

    @property
    def portal(self):
        return api.portal.get()
        
class FileTemplater(BaseTemplaterView):

    template = ViewPageTemplateFile("file_micro.pt")
    
    def __call__(self, show_description):
        self.show_description = show_description
        return self.template()

    @property
    def portal(self):
        return api.portal.get()
        

class DocumentTemplater(BaseTemplaterView):

    template = ViewPageTemplateFile("document_micro.pt")
    
    def __call__(self, show_description):
        self.show_description = show_description
        return self.template()

    @property
    def portal(self):
        return api.portal.get()
        
        
class FolderTemplater(BaseTemplaterView):

    template = ViewPageTemplateFile("folder_micro.pt")
    
    def __call__(self, show_description):
        self.show_description = show_description
        return self.template()

    @property
    def get_contents(self):
        folder_path = '/'.join(self.context.getPhysicalPath())
        return api.content.find(context=self.context, sort_on='getObjPositionInParent')

    @property
    def portal(self):
        return api.portal.get()
        