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


function highlightIds(id_list) {
  id_list.split(",").forEach(function(id) {
    $('#'+id).addClass('mark'); // add class highlight to element whose id is the word after the hash
  })
}

function dehighlightIds(id_list) {
  id_list.split(",").forEach(function(id) {
    $('#'+id).removeClass('mark'); // add class highlight to element whose id is the word after the hash
  })
}

function highlightHash() {
  var id_list_string  = location.hash.substr(1); //Get the word after the hash from the url
  highlightIds(id_list_string)
}

function highlightUse(elem) {
    console.log(elem.data)
    highlightIds(elem.data)
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

