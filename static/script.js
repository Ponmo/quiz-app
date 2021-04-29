jQuery( document ).ready(function( $ ) {
   var perfEntries = performance.getEntriesByType("navigation");

if (perfEntries[0].type === "back_forward") {
    location.reload(true);
}
});
