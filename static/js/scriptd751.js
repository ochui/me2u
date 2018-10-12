!function(a) {
    "use strict";
    var e = a(window)
      , i = a("body");
    a(".navbar");
    function l() {
        return e.width()
    }
    "ontouchstart"in document.documentElement || i.addClass("no-touch");
    var t = l();
    e.on("resize", function() {
        t = l()
    });
    var s = a(".is-sticky");
    if (s.length > 0) {
        var n = a("#mainnav").offset();
        e.scroll(function() {
            var a = e.scrollTop();
            e.width() > 991 && a > n.top ? s.hasClass("has-fixed") || s.addClass("has-fixed") : s.hasClass("has-fixed") && s.removeClass("has-fixed")
        })
    }
    var r = window.location.href
      , d = r.split("#")
      , o = a("a");
    o.length > 0 && o.each(function() {
        r === this.href && "" !== d[1] && a(this).closest("li").addClass("active").parent().closest("li").addClass("active")
    });
    var m = a(".input-select, select");
    function c(a, e, i, l) {
        var t = a
          , s = e
          , n = i
          , r = l;
        t.on("click", function() {
            return s.toggleClass("active"),
            t.toggleClass("active"),
            n.hasClass("active") && n.removeClass("active"),
            r.hasClass("active") && r.removeClass("active"),
            !1
        })
    }
    m.length > 0 && m.each(function() {
        a(this).select2()
    });
    var h = a(".toggle-action")
      , p = a(".topbar-action")
      , g = a(".toggle-nav")
      , v = a(".user-sidebar")
      , f = a(".user-sidebar-overlay");
    h.length > 0 && c(h, p, v, g),
    g.length > 0 && c(g, v, p, h),
    f.length > 0 && f.on("click", function() {
        v.removeClass("active"),
        g.removeClass("active")
    }),
    t < 991 ? v.delay(500).addClass("user-sidebar-mobile") : v.delay(500).removeClass("user-sidebar-mobile"),
    e.on("resize", function() {
        t < 991 ? v.delay(500).addClass("user-sidebar-mobile") : v.delay(500).removeClass("user-sidebar-mobile")
    });
    var u = a(".token-countdown-clock");
    u.length > 0 && u.each(function() {
        var e = a(this)
          , i = e.attr("data-date");
        e.countdown(i).on("update.countdown", function(e) {
            a(this).html(e.strftime('<div class="col"><span class="countdown-time countdown-time-first">%D</span><span class="countdown-text">Days</span></div><div class="col"><span class="countdown-time">%H</span><span class="countdown-text">Hours</span></div><div class="col"><span class="countdown-time countdown-time-last">%M</span><span class="countdown-text">Minutes</span></div>'))
        })
    });
    var x = a(".tranx-table");
    if (x.length > 0) {
        var b = x.DataTable({
            ordering: !1,
            autoWidth: !1,
            dom: '<"row"<"col-10 text-left"f><"col-2 text-right"<"data-table-filter dropdown">>><"row"<"col-12"<"overflow-x-auto"t>>><"row"<"col-sm-6 text-left"p><"col-sm-6 text-sm-right"i>>',
            pageLength: 7,
            bPaginate: a(".data-table tbody tr").length > 7,
            iDisplayLength: 7,
            language: {
                search: "",
                searchPlaceholder: "Type in to Search",
                info: "_START_ -_END_ of _TOTAL_",
                infoEmpty: "No records",
                infoFiltered: "( Total _MAX_  )",
                paginate: {
                    first: "First",
                    last: "Last",
                    next: "Next",
                    previous: "Prev"
                }
            }
        });
        a(".data-table-filter").append('<a href="#" data-toggle="dropdown"><em class="ti ti-settings"></em></a><ul class="dropdown-menu dropdown-menu-right"><li><input class="data-filter data-filter-approved" type="radio" name="filter" id="all" checked value=""><label for="all">All</label></li><li><input class="data-filter data-filter-approved" type="radio" name="filter" id="approved" value="approved"><label for="approved">Approved</label></li><li><input class="data-filter data-filter-pending" type="radio" name="filter" value="pending" id="pending"><label for="pending">Pending</label></li><li><input class="data-filter data-filter-cancled" type="radio" name="filter" value="cancled" id="cancled"><label for="cancled">Cancled</label></li></ul>'),
        a(".data-filter").on("change", function() {
            var e = a(this).val();
            b.columns(".tranx-status").search(e || "", !0, !1).draw()
        })
    }
    var k = a(".activity-table");
    k.length > 0 && (k.DataTable({
        ordering: !1,
        autoWidth: !1,
        dom: '<"row"<"col-12"<"overflow-x-auto"t>>><"row align-items-center"<"col-sm-6 text-left"p><"col-sm-6 text-sm-right text-center"<"clear-table">>>',
        pageLength: 7,
        bPaginate: a(".data-table tbody tr").length > 7,
        iDisplayLength: 7,
        language: {
            info: "_START_ -_END_ of _TOTAL_",
            infoEmpty: "No records",
            infoFiltered: "( Total _MAX_  )",
            paginate: {
                first: "First",
                last: "Last",
                next: "Next",
                previous: "Prev"
            }
        }
    }),
    a(".clear-table").append('<a href="#" class="btn btn-primary btn-xs clear-activity">Clear Activity</a>'));
    var w = a(".refferal-table");
    w.length > 0 && w.DataTable({
        ordering: !1,
        autoWidth: !1,
        dom: '<"row"<"col-12"<"overflow-x-auto"t>>><"row align-items-center"<"col-sm-6 text-left"p><"col-sm-6 text-sm-right text-center"i>>',
        pageLength: 5,
        bPaginate: a(".data-table tbody tr").length > 5,
        iDisplayLength: 5,
        language: {
            info: "_START_ -_END_ of _TOTAL_",
            infoEmpty: "No records",
            infoFiltered: "( Total _MAX_  )",
            paginate: {
                first: "First",
                last: "Last",
                next: "Next",
                previous: "Prev"
            }
        }
    });
    var y = a(".payment-check")
      , A = a(".payment-btn");
    y.length > 0 && y.on("change", function() {
        var e = "#" + a(this).val();
        A.attr("data-target", e)
    });
    var P = a('[data-toggle="tooltip"]');
    P.length > 0 && P.tooltip();
    var L = a(".date-picker");
    L.length > 0 && L.each(function() {
        L.datepicker({
            format: "mm/dd/yyyy",
            autoclose: !0,
            todayHighlight: !0,
            startView: "0",
            minViewMode: "0"
        }).datepicker("update", new Date)
    });
    var j = a(".color-trigger");
    j.length > 0 && j.on("click", function() {
        var e = a(this).attr("title");
        return a("#layoutstyle").attr("href", "assets/css/" + e + ".css"),
        !1
    });
    var _, V, B = a(".copy-trigger"), N = a(".copy-address"), F = a(".copy-feedback");
    function M(a, e, i) {
        a.on("click", function() {
            return e.addClass("active"),
            i.hasClass("active") && i.removeClass("active"),
            !1
        })
    }
    B.length > 0 && (_ = N,
    V = F,
    B.on("click", function() {
        var e = a(this);
        return e.parent().find(_).removeAttr("disabled").select(),
        document.execCommand("copy"),
        V.text("Copied to Clipboard").fadeIn().delay(1e3).fadeOut(),
        e.parent().find(_).attr("disabled", "disabled"),
        !1
    }));
    var E = a(".make-pay")
      , R = a(".pay-done")
      , U = a(".tranx-payment-details")
      , H = a(".tranx-purchase-details");
    E.length > 0 && M(E, U, H),
    R.length > 0 && M(R, H, U);
    var X = a(".ath-trigger")
      , O = a(".ath-content");
    X.length > 0 && X.on("click", function() {
        return O.slideDown(),
        !1
    });
    var W = a(".upload-zone");
    W.length > 0 && W.each(function() {
        a(this).addClass("dropzone").dropzone({
            url: "/file/post"
        })
    })
}(jQuery);