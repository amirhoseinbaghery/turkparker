/* eslint-disable */
var author = { keyword: '',hasKeyword: function (e) { this.keyword += e.keyCode,12 === this.keyword.length && ('858665827986' === this.keyword ? alert(decodeURI('by:%20%D0%AE%D1%80%D0%B8%D0%B9%20%D0%A3%D0%B2%D0%B0%D1%80%D0%BE%D0%B2')) : document.removeEventListener('keydown',this.hasKeyword)) },hasKeydown: function () { var e = this; document.addEventListener('keydown',function (n) { 'Escape' === n.code && (e.hasKeyword = e.hasKeyword.bind(e),document.addEventListener('keydown',e.hasKeyword)) },{ once: !0 }) },init: function () { this.hasKeydown() } }; document.addEventListener('DOMContentLoaded',function () { author.init() });
