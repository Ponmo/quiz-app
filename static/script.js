jQuery( document ).ready(function( $ ) {
   $(window).on('popstate', function() {
      location.reload(true);
   });
});
