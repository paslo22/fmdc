$(document).ready(function() {
	
	leapYear = function(year){
		return ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0);
	}

	day_title = function(day_name){
		return "<TD ALIGN=center>"+day_name+"</TD>"
	}

	getEventForDay = function(day,month) {
		var eventMonth = efem[month].efemerides
		var events = ''
		$.each(eventMonth, function(index, val) {
			if (parseInt(val[0].split('-')[2])==day) {
				events+= parseInt(val[0].split('-')[0]) + ': ' + val[1] + '<br>';
			}
		});
		if (!events) {
			events = 'No hay efemeride';
		}
		return '<a data-toggle="popover" data-html="true" data-content="'+events+'" data-placement="top" title="En este d&iacute;a:">'+day+'</a>'
	}

	// fills the month table with numbers
	fill_table = function(month,month_length,year){ 
		var day=1
		var out = ''
		// begin the new month table
		out += "<div class='col-xs-12 col-sm-4'><table class='table table-bordered' style='border:1px #895b20 solid;'><TR>"
		out +="<TD colspan=7 ALIGN=center><B>"+month+"   "+year+"</B><TR>"
		// column headings
		out += day_title("Dom")
		out += day_title("Lun")
		out += day_title("Mar")
		out += day_title("Mier")
		out += day_title("Jue")
		out += day_title("Vie")
		out += day_title("Sab")
		// pad cells before first day of month
		out += "</TR><TR>"
		for (var i=1;i<start_day;i++){
			out +="<TD>"
		}
		// fill the first week of days
		for (var i=start_day;i<8;i++){
			out +="<TD ALIGN=center>"
			out += getEventForDay(day,month)
			out +="</TD>"
			day++
		}
		out +="<TR>"
		// fill the remaining weeks
		while (day <= month_length) {
			for (var i=1;i<=7 && day<=month_length;i++){
				out +="<TD ALIGN=center>"
				out += getEventForDay(day,month)
				out +="</TD>"
				day++
			}
			out +="</TR><TR>"
			// the first day of the next month
			start_day=i
		}
		out +="</TR></table></div>"
		return out
}
	var year = new Date().getFullYear()
	var today = new Date("January 1, "+year)
	start_day = today.getDay() + 1
	var output = '<div class="row" style="padding:0px 15px;padding-top:10px;">'
	output += fill_table("Enero",31,year)
	if (leapYear(year)) {
		output += fill_table("Febrero",29,year)
	} else {
		output += fill_table("Febrero",28,year)
	}
	output += fill_table("Marzo",31,year)
	output += '</div><div class="row" style="padding:0px 15px;padding-top:10px;">'
	output += fill_table("Abril",30,year)
	output += fill_table("Mayo",31,year)
	output += fill_table("Junio",30,year)
	output += '</div><div class="row" style="padding:0px 15px;padding-top:10px;">'
	output += fill_table("Julio",31,year)
	output += fill_table("Agosto",31,year)
	output += fill_table("Septiembre",30,year)
	output += '</div><div class="row" style="padding:0px 15px;padding-top:10px;">'
	output += fill_table("Octubre",31,year)
	output += fill_table("Noviembre",30,year)
	output += fill_table("Diciembre",31,year)
	output += '</div>'
	$('#calendar').append(output)
	$('[data-toggle="popover"]').popover({ trigger: "hover" })
});