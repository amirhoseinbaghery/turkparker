
(() => {
    "use strict";
    const e = bootstrap;
    function t(e, t) {
        for (var n = 0; n < t.length; n++) {
            var a = t[n];
            a.enumerable = a.enumerable || !1, a.configurable = !0, "value" in a && (a.writable = !0), Object.defineProperty(e, a.key, a)
        }
    }
    var n = function() {
        function n() {
            ! function(e, t) {
                if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function")
            }(this, n)
        }
        var a, r, o;
        return a = n, o = [{
            key: "init",
            value: function() {
                document.querySelectorAll(".ce_tabcontrol").forEach((function(t, n, a) {
                    if ("true" === t.dataset.rememberLastTab) {
                        var r = sessionStorage.getItem(t.id);
                        if (null !== r) {
                            var o = t.querySelector("#" + r);
                            null !== o && new e.Tab(o).show()
                        } else new e.Tab(t.querySelector("a.nav-link")).show()
                    }
                    t.querySelectorAll("a.tab-link").forEach((function(n, a, r) {
                        n.addEventListener("click", (function(a) {
                            a.preventDefault(), n.addEventListener("shown.bs.tab", (function(e) {
                                sessionStorage.setItem(t.id, a.target.id)
                            })), new e.Tab(n).show()
                        }))
                    }))
                }))
            }
        }], (r = null) && t(a.prototype, r), o && t(a, o), n
    }();
    document.addEventListener("DOMContentLoaded", n.init)
})();