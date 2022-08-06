document.addEventListener("DOMContentLoaded", () => {

    // Search
    var searchIcon = document.getElementById('search_icon');
    var searchField = document.querySelectorAll('#header #search input.text')[0];
    var closeIcon = document.getElementById('close_icon');

    searchIcon.addEventListener('click', function () {
        searchField.classList.toggle('search_field_active');
        searchIcon.classList.toggle('search_icon-none');
        closeIcon.classList.toggle('close_icon-show');
    })

    // Menu Toggle & Scroll
    var hamburger = document.getElementById('nav-icon');
    var menu = document.getElementsByClassName('mod_navigation')[0];
    var mainHeader = document.getElementById("header");

    window.onscroll = function() {
        "use strict";
        if (document.body.scrollTop >= 30 || document.documentElement.scrollTop >= 30) {
            mainHeader.classList.add('header-fixed');
        } else {
            mainHeader.classList.remove('header-fixed');
        }
    }

    /*menu.onscroll = function() {
        if (menu.scrollTop >= 50) {
            mainHeader.classList.add('menu-scrolled');
        } else {
            mainHeader.classList.remove('menu-scrolled');
        }
    }*/

    var navMenu = false;

    function openNav() {
        menu.classList.add('menu-open');
        hamburger.classList.add('open');
        var scrollY = document.documentElement.style.getPropertyValue('--scroll-y');
        document.body.style.position = 'fixed';
        document.body.style.overflowY = 'scroll';
        document.body.style.top = `-${scrollY}`;
        navMenu = true;
    }

    function closeNav() {
        menu.classList.remove('menu-open');
        hamburger.classList.remove('open');
        setTimeout(function() {
            closeAllSubmenuLevel2();
            closeAllSubmenuLevel3();
            removeSubmenuActive();
        }, 1000);
        const scrollY = document.body.style.top;
        document.body.style.position = '';
        document.body.style.top = '';
        window.scrollTo(0, parseInt(scrollY || '0') * -1);
        document.body.style.overflowY = 'auto';
        navMenu = false;
    }

    function toggleNav() {
        navMenu ? closeNav() : openNav();
    }

    hamburger.addEventListener('click', function () {
        toggleNav();
    });


    //Submenu
    var level1 = document.querySelectorAll('.level_1 > li.submenu');
    var level2 = document.querySelectorAll('.level_2 > li.submenu');
    var level3 = document.querySelectorAll('.level_3 > li');
    var backButtons = document.querySelectorAll('.level_2 > #back');

    level1.forEach(function (listElem) {
        linkElem = listElem.querySelector('a');

        linkElem.addEventListener('click', function (event) {
            event.preventDefault();

            listElem.querySelector('.level_2').classList.add('submenu-open');
            listElem.querySelector('.level_2 > .level_2').classList.add('submenu-open');
            document.querySelector('.mod_navigation').classList.add('overlap-header');


            // Back button
            backButtons.forEach(function (i) {
                i.addEventListener('click', function () {
                    closeAllSubmenuLevel2();
                    closeAllSubmenuLevel3();
                    removeSubmenuActive();
                })
            })
        });
    });


    var lvl2Background = document.querySelector('.level_2')



    // Level 3 opening
    level2.forEach(function (listElem) {

        linkElem = listElem.querySelector('a');

        linkElem.addEventListener('click', function (event) {
            event.preventDefault();

            // activate list item (icon animation etc.)
            level2.forEach(function (listElem) {
                listElem.classList.remove('submenu-active');
            })

            listElem.classList.add('submenu-active');

            // Change background on click
            listElem.classList.contains('sport') ?   lvl2Background.classList.add('sport') : lvl2Background.classList.remove('sport');
            listElem.classList.contains('industry') ?   lvl2Background.classList.add('industry') : lvl2Background.classList.remove('industry');
            listElem.classList.contains('health') ?   lvl2Background.classList.add('health') : lvl2Background.classList.remove('health');
            listElem.classList.contains('parking') ?   lvl2Background.classList.add('parking') : lvl2Background.classList.remove('parking');
            listElem.classList.contains('spaces') ?   lvl2Background.classList.add('spaces') : lvl2Background.classList.remove('spaces');


            // activate/open submenu
            closeAllSubmenuLevel3();
            listElem.querySelector('.level_3').classList.add('submenu-open');
            listElem.querySelector('.level_3 > .level_3').classList.add('submenu-open');

        });
    });


    // Close Main Nav when level 3 is a hash link
    level3.forEach(function (listElem) {
        linkElem = listElem.querySelector('a');

        linkElem.addEventListener('click', function (event) {
            //event.preventDefault();
            closeNav();
        });
    });


    // Close all Submenus functions
    function closeAllSubmenuLevel2() {
        document.querySelectorAll('.level_2').forEach(function (linkElem) {
            //linkElem.classList.remove('submenu-open');
            linkElem.classList.remove('submenu-open', 'sport', 'industry', 'health', 'parking', 'spaces');
        })
    }

    function closeAllSubmenuLevel3() {
        document.querySelectorAll('.level_3').forEach(function (linkElem) {
            linkElem.classList.remove('submenu-open');
        })
    }

    function removeSubmenuActive() {
        document.querySelectorAll('.level_2 li.submenu').forEach(function (activeItem) {
            activeItem.classList.remove('submenu-active');
            document.querySelector('.mod_navigation').classList.remove('overlap-header');
        });
    }

});
