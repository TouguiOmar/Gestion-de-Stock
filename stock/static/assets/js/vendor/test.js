$('.aaa select').on('change', function(event){
	
	event.preventDefault();

	$.ajax({
		url : '/quantite/',
		type : 'GET',
		data : { ID_Article : this.value },
		success : function(response){
			if (response.quantite==0) {
				$(".aaa #test").html('Il reste encore : ' + response.quantite);
				$(".aaa #id_Quantite").attr({
					"max" : response.quantite,
					"min" : 1
				});
				$(".aaa #id_Quantite").prop('disabled', true);
				$(".aaa button").prop('disabled', true);
				$(".aaa #id_Quantite").css("border-color", "red");
				$(".aaa #test").css("color", "red");
			}
			else{
				$(".aaa #test").html('Il reste encore : ' + response.quantite);
				$(".aaa #id_Quantite").attr({
					"max" : response.quantite,
					"min" : 1
				});
				$(".aaa #id_Quantite").prop('disabled', false);
				$(".aaa button").prop('disabled', false);
				$(".aaa #id_Quantite").css("border-color", "green");
				$(".aaa #test").css("color", "green");
			}
			$("#id_Prix").val(response.prix);
		}
	});
});

$('.bbb select').on('change', function(event){
	
	event.preventDefault();

	$.ajax({
		url : '/retproduit/',
		type : 'GET',
		data : { ID_Article : this.value },
		success : function(response){
			$("#retproduit").html(response);
		}
	});
});