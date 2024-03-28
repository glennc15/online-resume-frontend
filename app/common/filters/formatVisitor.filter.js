(function() {

    angular
        .module('onlineResume')
        .filter('formatVisitor', formatVisitor);

    function formatVisitor() {
        return function (visitorNumber) {

            var rawDisplay = ("0000" + visitorNumber);
            var end_idx = rawDisplay.length;
            var start_idx = end_idx - 4;
            rawDisplay = rawDisplay.substring(start_idx, end_idx);

            var display = [rawDisplay.slice(0, 1), rawDisplay.slice(1, 4)];
            display = display.join(",");

            return display;
        };
    };


    })();