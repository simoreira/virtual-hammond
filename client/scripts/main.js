$(document).ready(function() {
	var effects = ['echo', 'tremolo', 'distortion', 'percussion', 'chorus', 'envelop'];

	effects.forEach(function(effect) {
		var element = $('#effect-' + effect);
		element.hide();
		var slider = $('#slider-' + effect).slider();

		$('#btn-'+effect).change(function() {
			if(this.checked)
			{
				element.show();
			}
			else
			{
				element.hide();
				slider.slider('setValue', 0)
			}
		});
	});
});