function mapersonne(){
var mypersonid=$("#rumeur_personne_id").length > 0 ? $("#rumeur_personne_id").val() : $("#hack_personne_id").val();
var text=$("#rumeur_personne_id").length > 0 ? $("#rumeur_text").val() : $("#hack_text").val();
$.ajax({
url: "/personne/"+mypersonid,
success:function(data){
var personne=data.personne;
$("#blah").html("<img src=\""+personne.pic+"\" class=\"picperson\" alt=\""+personne.name+"\" /><div class=\"hackertext\">"+text+"</div>");

}
});
}
function monlieu(){
var lieuid=$("#rumeur_lieu_id").length > 0 ? $("#rumeur_lieu_id").val() : $("#hack_lieu_id").val();
var text=$("#rumeur_personne_id").length > 0 ? $("#rumeur_text").val() : $("#hack_text").val();
$.ajax({
url: "/lieu/"+lieuid,
success:function(data){
$("#blah")[0].style.backgroundImage=("url(\""+data.lieu.pic+"\")");
$("#blah")[0].style.backgroundRepeat="no-repeat";
$("#blah")[0].style.backgroundSize="100% 100%";
$("#blah")[0].style.height="200px";
}
});
}

$(function(){
$(".meschaussures").click(function(){
$.ajax({url:$(this)[0].dataset.url,success:function(data){$('#text').html(data);$('#overlay')[0].style.display='block';


	$('#text form').on('submit', function () {
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
if ($("#personne_photo").length > 0 || $("#lieu_photo").length > 0){
var fileElem=$("#personne_photo").length > 0 ? personne_photo : lieu_photo;
fileElem.addEventListener("change", handleFiles, false);

function handleFiles() {
  if (!this.files.length) {
    fileList.innerHTML = "<p>Aucun fichier sélectionné !</p>";
  } else {
    fileList.innerHTML = "";
    const list = document.createElement("ul");
    fileList.appendChild(list);
    for (let i = 0; i < this.files.length; i++) {
      const li = document.createElement("li");
      list.appendChild(li);

      const img = document.createElement("img");
      img.src = URL.createObjectURL(this.files[i]);
      img.height = 60;
      img.onload = () => {
        URL.revokeObjectURL(img.src);
      };
      li.appendChild(img);
      const info = document.createElement("span");
      info.innerHTML = `${this.files[i].name} : ${this.files[i].size} octets`;
      li.appendChild(info);
    }
  }
}
}


}});
});
});
