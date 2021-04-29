window.addEventListener( "pageshow", function ( event ) {
   if(performance.navigation.type == 2){
   location.reload(true);
}
});
