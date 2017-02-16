/*-----------------------------------------------------------------------------------
/* Styles Switcher
-----------------------------------------------------------------------------------*/

window.console = window.console || (function(){
    var c = {}; c.log = c.warn = c.debug = c.info = c.error = c.time = c.dir = c.profile = c.clear = c.exception = c.trace = c.assert = function(){};
    return c;
})();


jQuery(document).ready(function($) {
        var currentcolor = $.cookie("scheme");
        
        
        var fileurl = workscoutsw.switchercss;
        if(currentcolor) {
            $("#colors" ).attr("href", fileurl+"colors/"+currentcolor+".css" );
        }
        
        // Color Changer
        $("#style-switcher .green" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/green.css" );
            $.cookie('scheme', 'green', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .blue" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/blue.css" );
            $.cookie('scheme', 'blue', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .orange" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/orange.css" );
            $.cookie('scheme', 'orange', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .navy" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/navy.css" );
            $.cookie('scheme', 'navy', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .yellow" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/yellow.css" );
            $.cookie('scheme', 'yellow', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .peach" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/peach.css" );
            $.cookie('scheme', 'peach', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .beige" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/beige.css" );
            $.cookie('scheme', 'beige', { expires: 7, path: '/' });
            return false;
        });

        $("#style-switcher .purple" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/purple.css" );
            $.cookie('scheme', 'purple', { expires: 7, path: '/' });
            return false;
        });

        $("#style-switcher .red" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/red.css" );
            $.cookie('scheme', 'red', { expires: 7, path: '/' });
            return false;
        });

        $("#style-switcher .pink" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/pink.css" );
            $.cookie('scheme', 'pink', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .celadon" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/celadon.css" );
            $.cookie('scheme', 'celadon', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .brown" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/brown.css" );
            $.cookie('scheme', 'brown', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .cherry" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/cherry.css" );
            $.cookie('scheme', 'cherry', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .gray" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/gray.css" );
            $.cookie('scheme', 'gray', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .darkcol" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/dark.css" );
            $.cookie('scheme', 'dark', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .cyan" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/cyan.css" );
            $.cookie('scheme', 'cyan', { expires: 7, path: '/' });
            return false;
        });
        
        $("#style-switcher .olive" ).click(function(){
            $("#colors" ).attr("href", fileurl+"colors/olive.css" );
            $.cookie('scheme', 'olive', { expires: 7, path: '/' });
            return false;
        });


        $("#style-switcher h2 a").click(function(e){
            e.preventDefault();
            var div = $("#style-switcher");
            console.log(div.css("left"));
            if (div.css("left") === "-205px") {
                $("#style-switcher").animate({
                    left: "0px"
                }); 
            } else {
                $("#style-switcher").animate({
                    left: "-205px"
                });
            }
        });


        //Layout Switcher
       $("#layout-style").change(function(e){
            if( $(this).val() == 1){
                $("body").addClass("boxed");
                 $.cookie('layout', 'boxed', { expires: 7, path: '/' });
                $("body").removeClass("fullwidth");
                //$(window).resize();
            } else{
                $("body").removeClass("boxed");
                $.cookie('layout', 'fullwidth', { expires: 7, path: '/' });
                $("body").addClass("fullwidth");
                //$(window).resize();
            }
        });
       

        //Layout Switcher
       $("#header-style").change(function(e){
            if( $(this).val() == 1){
                $("header").removeClass("alternative full-width");
 
            } 
            if( $(this).val() == 2){
                $("header").removeClass("alternative full-width").addClass("alternative")

            }
            if( $(this).val() == 3){
                $("header").removeClass("alternative full-width").addClass("full-width")
            }
            $(".sticky-header.cloned.alternative").removeClass('alternative');
        });


        $("#layout-switcher").on('change', function() {
            $('#layout').attr('href', $(this).val() + '.css');
        });

        $(".colors li a").click(function(e){
            e.preventDefault();
            $(this).parent().parent().find("a").removeClass("active");
            $(this).addClass("active");
        });
        
        $('.bg li a').click(function() {
            var current = $('#style-switcher select[id=layout-style]').find('option:selected').val();
            if(current == '1') {
                var bg = $(this).css("backgroundImage");
                $("body").css("backgroundImage",bg);
            } else {
                alert('Please select boxed layout');
            }
        });

        $('.bgsolid li a').click(function() {
            var current = $('#style-switcher select[id=layout-style]').find('option:selected').val();
            if(current == '1') {
            var bg = $(this).css('backgroundColor');
            $('body').css('backgroundColor',bg).css('backgroundImage','none')
            } else {
                alert('Please select boxed layout');
            }
        });


        $("#reset a").click(function(e){
            e.preventDefault();
            $.cookie('scheme', 'green', { expires: 7, path: '/' });
            $("body" ).removeClass("boxed");
            $("header" ).removeClass("alternative");
            $("header" ).removeClass("full-width");
            $(".colors li a" ).removeClass("active");
            $("#colors" ).attr("href", fileurl+"colors/green.css" );
            $(window).resize();
        });
            

    });

/*!
 * jQuery Cookie Plugin v1.4.1
 * https://github.com/carhartl/jquery-cookie
 *
 * Copyright 2006, 2014 Klaus Hartl
 * Released under the MIT license
 */
(function (factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD (Register as an anonymous module)
        define(['jquery'], factory);
    } else if (typeof exports === 'object') {
        // Node/CommonJS
        module.exports = factory(require('jquery'));
    } else {
        // Browser globals
        factory(jQuery);
    }
}(function ($) {

    var pluses = /\+/g;

    function encode(s) {
        return config.raw ? s : encodeURIComponent(s);
    }

    function decode(s) {
        return config.raw ? s : decodeURIComponent(s);
    }

    function stringifyCookieValue(value) {
        return encode(config.json ? JSON.stringify(value) : String(value));
    }

    function parseCookieValue(s) {
        if (s.indexOf('"') === 0) {
            // This is a quoted cookie as according to RFC2068, unescape...
            s = s.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, '\\');
        }

        try {
            // Replace server-side written pluses with spaces.
            // If we can't decode the cookie, ignore it, it's unusable.
            // If we can't parse the cookie, ignore it, it's unusable.
            s = decodeURIComponent(s.replace(pluses, ' '));
            return config.json ? JSON.parse(s) : s;
        } catch(e) {}
    }

    function read(s, converter) {
        var value = config.raw ? s : parseCookieValue(s);
        return $.isFunction(converter) ? converter(value) : value;
    }

    var config = $.cookie = function (key, value, options) {

        // Write

        if (arguments.length > 1 && !$.isFunction(value)) {
            options = $.extend({}, config.defaults, options);

            if (typeof options.expires === 'number') {
                var days = options.expires, t = options.expires = new Date();
                t.setMilliseconds(t.getMilliseconds() + days * 864e+5);
            }

            return (document.cookie = [
                encode(key), '=', stringifyCookieValue(value),
                options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
                options.path    ? '; path=' + options.path : '',
                options.domain  ? '; domain=' + options.domain : '',
                options.secure  ? '; secure' : ''
            ].join(''));
        }

        // Read

        var result = key ? undefined : {},
            // To prevent the for loop in the first place assign an empty array
            // in case there are no cookies at all. Also prevents odd result when
            // calling $.cookie().
            cookies = document.cookie ? document.cookie.split('; ') : [],
            i = 0,
            l = cookies.length;

        for (; i < l; i++) {
            var parts = cookies[i].split('='),
                name = decode(parts.shift()),
                cookie = parts.join('=');

            if (key === name) {
                // If second argument (value) is a function it's a converter...
                result = read(cookie, value);
                break;
            }

            // Prevent storing a cookie that we couldn't decode.
            if (!key && (cookie = read(cookie)) !== undefined) {
                result[name] = cookie;
            }
        }

        return result;
    };

    config.defaults = {};

    $.removeCookie = function (key, options) {
        // Must not alter options, thus extending a fresh object...
        $.cookie(key, '', $.extend({}, options, { expires: -1 }));
        return !$.cookie(key);
    };

}));