$(function(){

$('form').on('submit', function () {
  if (window.filesize > 1024*5) {
    alert('max upload size is 5k');
return false;
  }
  $.ajax({
    // Your server script to process the upload
    url: $(this).attr("action"),
    type: $(this).attr("method"),

    // Form data
    data: new FormData($(this)[0]),

    // Tell jQuery not to process data or worry about content-type
    // You *must* include these options!
    cache: false,
    contentType: false,
    processData: false,

    // Custom XMLHttpRequest
    success: function (data) {
	    console.log("HEY")
	    console.log(JSON.stringify(data))
	    console.log(JSON.stringify(data.redirect))
	    if (data.redirect){
	    window.location=data.redirect;
	    }else{
	    window.location="/";
	    }
},
    xhr: function () {
      var myXhr = $.ajaxSettings.xhr();
      if (myXhr.upload) {
        // For handling the progress of the upload
        myXhr.upload.addEventListener('progress', function (e) {
          if (e.lengthComputable) {
            $('progress').attr({
              value: e.loaded,
              max: e.total,
            });
          }
        }, false);
      }
      return myXhr;
    }
  });
	return false;
  });
			const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
			const charactersLength = characters.length;
	if($(".ajouter").length > 0){
		$(".ajouter").click(function(){
			document.getElementById("overlay").style.display = "block";
			$(".heynom").html($($(this)[0].parentElement).children("h5").html());
		});
		$(".close").click(function(){
			  document.getElementById("overlay").style.display = "none";
			var str1=$(".heynom").html();
			var str=$(".heynom").html().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
                        var length=$(".meschamp")[0].children.length;
			var name=$("[name='myname']");
			//random string
			let result = '';

			let counter = 0;
			var mylength=10;
			while (counter < mylength) {
				result += characters.charAt(Math.floor(Math.random() * charactersLength));
				counter += 1;
			if (counter === mylength){
				console.log(result,"hey");
                        $(".meschamp").append(`
			<div>
			<div class="champ">
			ajout #${length}
                                     nom de la ou du ${str1}
				     <input name="${str}[]name" value="${name.val()}" />
				</div>
			<div class="champ">
                                     image
				     <input class="${result}" type="file" name="${str}[]image" />
				</div>
				</div>
				`);

			name.val("");
			}
			}



		});
	}

  
});
