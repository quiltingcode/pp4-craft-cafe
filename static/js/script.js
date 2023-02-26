/* global $ */

$(document).ready(function() {


    /* Initial reset state of all fields before selection */
    var workshopDropDownValues = $("#id_workshop").val();
    var dayDropDownValues = $("#id_day").attr( 'readOnly' , 'true' );
    var timeDropdownValues = $('#id_time').html();
    var placesDropdownValues = $('#id_places').html();

    /* Check pre-populated field data in the edit booking page */
    checkWorkshopField();
    setPlaceholders();

    /* Set placeholder text over the booking form date field, the Comments comment field */
    function setPlaceholders() {
        $("#id_day").attr('placeholder', 'Select a Date' );
        $("#id_comment_content").attr('placeholder', 'Write your comments here');
        $("#id_content").attr('placeholder', 'Describe your craft creation here');
        $("#id_title").attr('placeholder', 'Give your post a title');
    }

    /* Booking Form Validation - check which workshop option has been selected */

    $('#id_workshop').change(function(){ 
        /* Reset fieds each time workshop field is changed */
        $("#id_day").attr( 'readOnly', 'true' ).addClass('required');
        $('#id_time').html(timeDropdownValues);
        $('#id_places').html(placesDropdownValues);
        /* Subsequent dropdown changes based on workshop dropdown selection */
        if ($(this).val() == 'All things Wool'){
            console.log(this.value);
            resetAllDays();
            enableMondays();
            removeMorning();
        } else if ($(this).val() == 'Clothing'){
            console.log(this.value);
            resetAllDays();
            enableTuesdays();
            removeMorning();
        } else if ($(this).val() == 'Quilting'){
            console.log(this.value);
            resetAllDays();
            enableWednesdays();
            removeMorning();
        } else if ($(this).val() == 'Home Crafts'){
            console.log(this.value);
            resetAllDays();
            enableThursdays();
            removeMorning();
            $("#datepicker").datepicker("destroy");
        } else if ($(this).val() == 'Needlepoint'){
            console.log(this.value);
            resetAllDays();
            enableFridays();
            removeMorning();
        } else if ($(this).val() == 'Kids Crafts'){
            console.log(this.value);
            resetAllDays();
            enableSaturdays();
            removeAfternoon();
        } else {
            disableAllDays();
        }

    });

    /* Validation to show available days of the week based on the workshop selected */

   function enableMondays() {
        $("#id_day").datepicker({
            dateFormat: 'dd-mm-yy',
            minDate: +0,
            maxDate: '+5M',
            beforeShowDay: mondays
        });
        console.log($("#id_day"));
    }

    function mondays(in_date) {
        if (in_date.getDay() != 1) {
            return [false, "notav", 'Not Available'];
        } else {
            return [true, "av", "available"];
        }
    }

    function enableTuesdays() {
        console.log("enableTuesday");
        $("#id_day").datepicker({
            dateFormat: 'dd-mm-yy',
            minDate: +0,
            maxDate: '+5M',
            beforeShowDay: tuesdays
        });
    }

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
    }

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
    }

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
    }

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
    }

    function saturdays(in_date) {
        if (in_date.getDay() != 6) {
            return [false, "notav", 'Not Available'];
        } else {
            return [true, "av", "available"];
        }
    }

    function disableAllDays() {
        $("#id_day").datepicker({
            dateFormat: 'dd-mm-yy',
            minDate: null,
            maxDate: '+5M',
            beforeShowDay: disableall
        });
        $("#id_day").attr( 'readOnly' , 'true' );
    }

    function disableall(in_date) {
        if (in_date.getDay() == 1) {
            return [false, "notav", 'Not Available'];
        } else if (in_date.getDay() == 2) {
            return [false, "notav", 'Not Available'];
        } else if (in_date.getDay() == 3) {
            return [false, "notav", 'Not Available'];
        } else if (in_date.getDay() == 4) {
            return [false, "notav", 'Not Available'];
        } else if (in_date.getDay() == 5) {
            return [false, "notav", 'Not Available'];
        } else if (in_date.getDay() == 6) {
            return [false, "notav", 'Not Available'];
        } else if (in_date.getDay() == 0) {
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

    /* If Saturday workshop selected, only show morning time slots */

    function removeAfternoon() {
        $("#id_time option[value='4 - 6pm']").remove();
        $("#id_time option[value='6 - 8pm']").remove();
    }

     /* Reset the calendar datepicker completely each time a new workshop is selected */
    function resetAllDays() {
        $('#id_day').datepicker('destroy');
    }

     /* Set the correct filters based on the pre-populated workshop category selected */
    function checkWorkshopField() {
        if (workshopDropDownValues == 'Kids Crafts'){
            removeAfternoon();
            enableSaturdays();
        } else if (workshopDropDownValues == 'Clothing'){
            removeMorning();
            enableTuesdays();
        } else if (workshopDropDownValues == 'All things Wool'){
            removeMorning();
            enableMondays();
        } else if (workshopDropDownValues == 'Quilting'){
                removeMorning();
                enableWednesdays();
        } else if (workshopDropDownValues == 'Home Crafts'){
                removeMorning();
                enableThursdays();
        } else if (workshopDropDownValues == 'Needlepoint'){
                removeMorning();
                enableFridays();
        }
    }


});

