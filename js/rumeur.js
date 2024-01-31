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
$("#blah")[0].style.backgroundImage=(data.lieu.pic);
$("#blah")[0].style.backgroundRepeat="no-repeat";
$("#blah")[0].style.backgroundSize="100% 100%";
}
});
}

$(function(){
});
