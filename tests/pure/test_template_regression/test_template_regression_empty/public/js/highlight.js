$(document).ready ( function () { //Work as soon as the DOM is ready for parsing
    highlightHash();
    // Set the offset when entering page with hash present in the url
    window.setTimeout(offsetAnchor, 400);
});
// The function actually applying the offset
function offsetAnchor() {
  if (location.hash.length !== 0) {
    window.scrollTo(window.scrollX, window.scrollY - $("#menubar").height());
  }
}

function highlightHash() {
  var id_list  = location.hash.substr(1); //Get the word after the hash from the url
  id_list.split(",").forEach(function(id) {
    $('#'+id).addClass('mark'); // add class highlight to element whose id is the word after the hash
  })

}
// Captures click events of all <a> elements with href containing #
$(document).on('click', 'a[href*="#"]', function(event) {
// Click events are captured before hashchanges. Timeout
// causes offsetAnchor to be called after the page jump.
  window.setTimeout(function() {
    highlightHash();
    offsetAnchor();
  }, 0);
});

