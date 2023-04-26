var form_fields = document.getElementsByTagName('input')
		form_fields[1].placeholder='Usuario';
		form_fields[2].placeholder='Correo Electronico';
		form_fields[3].placeholder='Contraseña';
		form_fields[4].placeholder='Confirmar Contraseña';


		for (var field in form_fields){	
			form_fields[field].className += ' form-control'
		}