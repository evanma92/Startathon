(function ($) {

  var elem = $( '#test1' )[0];
  var elem2 = $( '#test2' )[0];
  var elem3 = $( '#test3' )[0];
  var elem4 = $( '#test4' )[0];
  var elem5 = $( '#test5' )[0];
  var elem6 = $( '#test6' )[0];

  $( document ).on( 'click', function toggleText() 
  {
      elem = $( '#test1' )[0];
     if ( elem.style.visibility == "visible")     
     { 
         elem.style.visibility = "hidden";
          elem2.style.visibility = "visible";
     }
     else if ( elem2.style.visibility == "visible") 
     { 
       elem2.style.visibility = "hidden";
       elem3.style.visibility = "visible";
     }
      else if ( elem3.style.visibility == "visible")
      {
       elem3.style.visibility = "hidden";
       elem4.style.visibility = "visible";
      }
      else if ( elem4.style.visibility == "visible")
      {
       elem4.style.visibility = "hidden";
       elem5.style.visibility = "visible";
      }
      else if ( elem5.style.visibility == "visible")
      {
       elem5.style.visibility = "hidden";
       elem6.style.visibility = "visible";
      }
  });
}(jQuery));
          
