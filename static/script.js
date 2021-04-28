jQuery(document).ready(function()
        {
                var d = new Date();
                d = d.getTime();
                if (jQuery('#reloadValue').val().length == 0)
                {
                        jQuery('#reloadValue').val(d);
                        jQuery('body').show();
                }
                else
                {
                        jQuery('#reloadValue').val('');
                        location.reload();
                }
        });

#window.addEventListener( "pageshow", function ( event ) {
#  var historyTraversal = event.persisted || 
#                         ( typeof window.performance != "undefined" && 
#                              window.performance.navigation.type === 2 );
#  if ( historyTraversal ) {
#    window.location.reload();
#  }
#  });
