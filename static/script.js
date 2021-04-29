jQuery( document ).ready(function( $ ) {
   $(window).on('popstate', function() {
      location.reload(true);
   });
});
#window.addEventListener( "pageshow", function ( event ) {
#  var historyTraversal = event.persisted || 
#                         ( typeof window.performance != "undefined" && 
#                              window.performance.navigation.type === 2 );
#  if ( historyTraversal ) {
#    window.location.reload( true )
#  }
#});
