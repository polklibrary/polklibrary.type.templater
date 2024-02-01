from chameleon import PageTemplate
from plone import api
from Products.CMFPlone.utils import safe_unicode
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from polklibrary.type.templater.browser.templater_micros import DocumentTemplater, FolderTemplater, FileTemplater, ImageTemplater

from AccessControl import getSecurityManager
from Products.CMFCore.permissions import AddPortalContent, ModifyPortalContent, ReviewPortalContent , ManagePortal


class Templater(BrowserView):

    template = ViewPageTemplateFile("templater.pt")
    
    def __call__(self):
        self.request.response.setHeader('X-Frame-Options', 'ALLOWALL')
        return self.template()

    def get_style(self):
        if self.context.css:
            return self.context.css.replace('<style','<style class="ht-marker"')
        return '' # nothing
        
    def get_html(self):
        if self.context.html:
            template = PageTemplate(self.context.html)
            return template(context=self.context, request=self.request, view=self)
        return '' # nothing
            
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
        
        
    def section(self, id, description=False):
        brains = api.content.find(id=id)
        if brains:
            obj = brains[0].getObject()
            
            if obj.portal_type == "Document":
                return DocumentTemplater(context=obj, request=self.request)(description)
            if obj.portal_type == "Folder":
                return FolderTemplater(context=obj, request=self.request)(description)
            if obj.portal_type == "File":
                return FileTemplater(context=obj, request=self.request)(description)
            if obj.portal_type == "Image":
                return ImageTemplater(context=obj, request=self.request)(description)

        return ''
        
        
    @property
    def portal(self):
        return api.portal.get()
        
        
        
        
        
        

class PreviewTemplater(Templater):
        
    template = ViewPageTemplateFile("previewtemplater.pt")
    title = ''
    description = ''
    css = ''
    js = ''
    html = ''
    body = ''
    suppress_title = False
    suppress_description = False
    set_context = ''
    
    def __call__(self):
    
        if self.request.form.get('form.buttons.preview',''):
            self.title = self.request.form.get('form.widgets.title','')
            self.description = self.request.form.get('form.widgets.description','')
            self.css = self.request.form.get('form.widgets.css','')
            self.js = self.request.form.get('form.widgets.js','')
            self.html = self.request.form.get('form.widgets.html','')
            self.suppress_title = self.request.form.get('form.widgets.suppress_title-empty-marker',False)
            self.suppress_description = self.request.form.get('form.widgets.suppress_description-empty-marker',False)
            self.set_context = self.request.form.get('form.widgets.set_context','')
            
        return self.template()

    def get_style(self):
        return self.css.replace('<style','<style class="ht-marker"')
        
    def get_html(self):
        template = PageTemplate(self.html)
        return template(context=self.set_context, request=self.request, view=self)
        
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