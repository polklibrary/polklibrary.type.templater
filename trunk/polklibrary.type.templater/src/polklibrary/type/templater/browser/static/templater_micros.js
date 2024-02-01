$(document).ready(function(){
    
    $('.templater-option').on('mouseenter', 
        function(){
            $(this).parents('.templater-section').addClass('templater-active');
        }
    );
    $('.templater-option').on('mouseleave', 
        function(){
            $(this).parents('.templater-section').removeClass('templater-active');
        }
    );
});
