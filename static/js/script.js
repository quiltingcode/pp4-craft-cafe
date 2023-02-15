
$(document).ready(function() {

    /* Time delay for auto-dismissal script on alert messages */ 


    setTimeout(function() {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);


    /* Booking Form Validation - check which workshop option has been selected */


    $('#id_workshop').change(function(){ 
        if ($(this).val() == 'All things Wool'){
            console.log(this.value)
            enableMondays()
            removeMorning()
        } else if ($(this).val() == 'Quilting'){
            console.log(this.value)
            enableTuesdays()
        } else if ($(this).val() == 'Clothing'){
            console.log(this.value)
            enableWednesdays()
        } else if ($(this).val() == 'Home Crafts'){
            console.log(this.value)
            enableThursdays()
        } else if ($(this).val() == 'Needlepoint'){
            console.log(this.value)
            enableFridays()
        } else if ($(this).val() == 'Kids Crafts'){
            console.log(this.value)
            enableSaturdays()
        } else {
            disableAllDays()
        }

    })

    /* Validation to show available days of the week based on the workshop selected */

   function enableMondays() {
        $("#id_day").datepicker({
            dateFormat: 'dd-mm-yy',
            minDate: +0,
            maxDate: '+5M',
            beforeShowDay: mondays
        });
    };

    function mondays(in_date) {
        if (in_date.getDay() != 1) {
            return [false, "notav", 'Not Available'];
        } else {
            return [true, "av", "available"];
        }
    }

    function enableTuesdays() {
        $("#id_day").datepicker({
            dateFormat: 'dd-mm-yy',
            minDate: +0,
            maxDate: '+5M',
            beforeShowDay: tuesdays
        });
    };

    function tuesdays(in_date) {
        if (in_date.getDay() != 2) {
            return [false, "notav", 'Not Available'];
        } else {
            return [true, "av", "available"];
        }
    }

    function enableWednesdays() {
        $("#id_day").datepicker({
            dateFormat: 'dd-mm-yy',
            minDate: +0,
            maxDate: '+5M',
            beforeShowDay: wednesdays
        });
    };

    function wednesdays(in_date) {
        if (in_date.getDay() != 3) {
            return [false, "notav", 'Not Available'];
        } else {
            return [true, "av", "available"];
        }
    }

    function enableThursdays() {
        $("#id_day").datepicker({
            dateFormat: 'dd-mm-yy',
            minDate: +0,
            maxDate: '+5M',
            beforeShowDay: thursdays
        });
    };

    function thursdays(in_date) {
        if (in_date.getDay() != 4) {
            return [false, "notav", 'Not Available'];
        } else {
            return [true, "av", "available"];
        }
    }

    function enableFridays() {
        $("#id_day").datepicker({
            dateFormat: 'dd-mm-yy',
            minDate: +0,
            maxDate: '+5M',
            beforeShowDay: fridays
        });
    };

    function fridays(in_date) {
        if (in_date.getDay() != 5) {
            return [false, "notav", 'Not Available'];
        } else {
            return [true, "av", "available"];
        }
    }

    function enableSaturdays() {
        $("#id_day").datepicker({
            dateFormat: 'dd-mm-yy',
            minDate: +0,
            maxDate: '+5M',
            beforeShowDay: saturdays
        });
    };

    function saturdays(in_date) {
        if (in_date.getDay() != 6) {
            return [false, "notav", 'Not Available'];
        } else {
            return [true, "av", "available"];
        }
    }

    /* If Monday - Friday workshop selected, only show afternoon time slots */

    function removeMorning() {
        $("#id_time option[value='10 - 11:30am']").remove();
        $("#id_time option[value='11:30am - 1pm']").remove();
    }

    function removeAfternoon() {
        $("#id_time option[value='4 - 6pm']").remove();
        $("#id_time option[value='6 - 8 pm']").remove();
    }

  




})