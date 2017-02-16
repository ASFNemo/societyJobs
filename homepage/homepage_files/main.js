function htmlentities(value)
{
	if (value) {
		return jQuery('<span />').text(value).html();
	}
	
	return '';
}

function is_array(variable)
{
	return (variable instanceof Array);
}

function empty(variable)
{
	return (variable === "" || variable === 0 || variable === "0" || variable === null || variable === false || (is_array(variable) && variable.length === 0));
}

function in_array(value, array)
{
	for (var i = 0; i < array.length; i++ ) {
		if (value == array[i]) {
			return true;
		}
	}
	
	return false;
}

function array_key_exists(key, array)
{
	if (!array || (array.constructor !== Array && array.constructor !== Object)) {
		return false;
	}
	
	return array[key] !== undefined;
}

$(document).on('change', '#all_checkboxes_control', function() {
	var checked = $(this).is(':checked');
	$(this).closest('form').find(':checkbox')
		.prop('checked', checked);
	$('.bulk').toggleClass('inline-block', checked);
});

$(document).on('click', '.with-bulk tbody .cr-styled', function() {
	var checkboxes = $(this).closest('form').find('tbody :checkbox:checked');
	$('.bulk').toggleClass('inline-block', checkboxes.length > 0);
});
