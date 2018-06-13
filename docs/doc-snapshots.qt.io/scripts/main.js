"use strict";
var $sidebar;
var sticky = false;

function createCookie(name, value, days) {
    var expires;
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    } else {
        expires = "";
    }
    document.cookie = escape(name) + "=" + escape(value) + expires + "; path=/";
    $('.cookies_yum').click(function() {
        $(this).fadeOut()
    });
}
function readCookie(name) {
    var nameEQ = escape(name) + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return unescape(c.substring(nameEQ.length, c.length));
    }
    return null;
}
function eraseCookie(name) {
    createCookie(name, "", -1);
}
$(document).ready(function($) {

    $('.cookies_yum').click(function() {
        $('.cookies_yum').fadeOut();
        createCookie("cookies_nom", "yum", 180);
        var cookie_added = 1;
    });
    if (!(readCookie('cookies_nom') == 'yum')) {
        $('.cookies_yum').fadeIn();
    } else {
        var cookie_added = 1;
    }

    $(window).resize(function() {
        setTimeout(function(){oneQt.stickySidebar();}, 80);
    });

    $sidebar = $('div.sidebar:first');
    sticky = $sidebar.css('position') == 'sticky';
    if (sticky)
        $sidebar.css({transition: '0.2s ease-out'});
    $(window).scroll(function() {
        oneQt.stickySidebar();
        oneQt.stickyHeader();
    });

    oneQt.stickySidebar();

    $("#navbar").load("/style/qt-header.html");
    $("#footer").load("/style/qt-footer.html");
    $("#sidebar-content").load("style/qt5-sidebar.html");
    $.get("/style/qt-sidebar.html", function(d) { var content = $(d).filter('div'); $("#sidebar-content").before(content); });
});

var oneQt = {
    stickySidebar: function() {
        if ($sidebar.length && $sidebar.outerHeight() > 20) {
            var $win = $(window);
            var $sidebarContainer = $sidebar.parent();
            var headerHeight = 0;
            if ($('#navbar').css('position') == 'fixed')
                headerHeight = $('#navbar').outerHeight();
            if ($win.outerWidth() > 980
                && $win.scrollTop() + headerHeight > $sidebarContainer.offset().top) {
                var newTop = 16 + headerHeight + $win.scrollTop() - $sidebarContainer.offset().top;
                var overflow = $sidebar.innerHeight() - $win.outerHeight() + headerHeight;
                if (overflow > 0) {
                    newTop -= overflow;
                    if (sticky) {
                        $sidebar.css('top', headerHeight - overflow + 'px');
                        return;
                    }
                }
                if (newTop + $sidebar.innerHeight() > $sidebarContainer.innerHeight()) {
                    newTop = $sidebarContainer.innerHeight() - $sidebar.innerHeight();
                }
                if (newTop < 0)
                    newTop = 0;
                if (sticky)
                    $sidebar.css({top: '66px'});
                else
                    $sidebar.css({top: newTop + 'px'});
            } else {
                $sidebar.css({top: '0'})
            }
        }
    },
    stickyHeader: function () {
        var originalHeaderHeight = 79;
        if ($(window).scrollTop() > originalHeaderHeight) {
            $('#navbar').addClass('fixed');

            if (!(cookie_added == 1)) {
                $('.cookies_yum').fadeOut();
                createCookie("cookies_nom", "yum", 180);
                var cookie_added = 1;
            }
        }
        else {
            $('#navbar').removeClass('fixed');
        }
    }
}
