
var Templater = {



    init : function(){
        this._construct();
    },

    _clean_text : function(text) {
        text = text.replace(' ','');
        text = text.replace('\n','');
        return text;
    },
    
    _construct : function() {
        var self = this;
        
        $('#content-core *').contents().each(function(){
        
            if (this.nodeType == 3)
                console.log($(this));
        
        });
        
        
        
        // $('#content-core *').contents().filter(function() {
            // return this.nodeType == 3;
        // }).parent().addClass('text-edit-on');
        
    
    }
    

}






$(document).ready(function(){
    Templater.init();
});