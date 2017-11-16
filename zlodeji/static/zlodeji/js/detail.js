        $(document).ready(function() {
          $(".expandable").on("click", ".add-more", function(e) {
            e.preventDefault();
            var rmButton = '<button class="btn btn-danger remove-me" type="button">-</button>';
            var grandParent = $(this).parent().parent();
            var countVal = grandParent.data("count");
            var count = parseInt(countVal);
            if (count == 1) {
              $(this).before(rmButton);
            }
            var toBeCopied = $(this).parent().clone();
            if (count == 1) {
                var curClass = toBeCopied.find("input").attr('class');
                toBeCopied.find("input:first").attr('class', curClass + " offset-md-3");
                toBeCopied.find("label").remove();

            }
            var add_button = $(this).detach();
            grandParent.append(toBeCopied);
            count++;
            grandParent.data("count", count);
          });
          $(".expandable").on("click", ".remove-me", function(e) {
            e.preventDefault();
            var grandParent = $(this).parent().parent();
            var countVal = grandParent.data("count");
            count = parseInt(countVal);
            count--;
            grandParent.data("count", count);

            var nextButton = $(this).next("button");
            var prevButton = $(this).parent().prev().find("button");

            //When we click remove on the last entry:
            if (/add-more/.test(nextButton.attr("class")) && /remove-me/.test(prevButton.attr("class"))) {
              var add_button = nextButton.detach();
              $(this).parent().prev().find(".remove-me").after(add_button);
            }
            //When we click on the first entry:
            if ($(this).parent().children().is("label")) {
                secondEntry=$(this).parent().next().find("input");
                secondEntry.removeClass("offset-md-3");
                secondEntry.before($(this).parent().find("label"));
            }
            if (count == 1) {
              $(this).parent().prev().find(".remove-me").remove();
              $(this).parent().next().find(".remove-me").remove();
            }
            $(this).parent().remove();
          });


        });




             $(document).ready(function(){
      var i=1;
     $("#add_row").click(function(){
      $('#addr'+i).html("<td>"+ (i+1) +"</td><td><input name='name"+i+"' type='text' placeholder='Name' class='form-control input-md'  /> </td><td><input  name='mail"+i+"' type='text' placeholder='Mail'  class='form-control input-md'></td><td><input  name='mobile"+i+"' type='text' placeholder='Mobile'  class='form-control input-md'></td>");

      $('#tab_logic').append('<tr id="addr'+(i+1)+'"></tr>');
      i++;
  });
     $("#delete_row").click(function(){
    	 if(i>1){
		 $("#addr"+(i-1)).html('');
		 i--;
		 }
	 });

});
