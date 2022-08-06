
// detect IE 9,10,11, but not Edge
ua = navigator.userAgent.toLowerCase();
IEbrowser = /msie/.test(ua);
function startPrivacyMagic() {
    var buttonEnableAll = document.querySelector('button#enable-all');
    var buttonDisableAll = document.querySelector('button#disable-all');
    var buttonOpenPopup = document.querySelectorAll('button.open-privacy-settings');
    var buttonClosePopup = document.querySelectorAll('.close-settings');
    var inputAnalytics = document.querySelector('input[name="privacy-g-analytics"]');
    var inputAnalyticsMatomo = document.querySelector('input[name="privacy-matomo-analytics"]');
    var inputTagmanager = document.querySelector('input[name="privacy-g-tagmanager"]');
    var inputLeadLab = document.querySelector('input[name="privacy-leadlab"]');
    var inputGmaps = document.querySelector('input[name="privacy-g-maps"]');
    var inputMapbox = document.querySelector('input[name="privacy-mapbox"]');
    var inputYouTube = document.querySelector('input[name="privacy-youtube"]');
    var inputVimeo = document.querySelector('input[name="privacy-vimeo"]');
    var inputOpenStreetMap = document.querySelector('input[name="privacy-open-street-map"]');
    var buttonShowGmap = document.querySelectorAll('button#load-google-map');
    var buttonShowMapbox = document.querySelectorAll('button#load-mapbox');
    var buttonShowOpenStreetMap = document.querySelectorAll('button#load-open-street-map');
    var buttonShowVimeo = document.querySelectorAll('button#load-vimeo');
    var buttonShowYouTube = document.querySelectorAll('button#load-youtube');
    var contaoPrivacy = (function() {
        /**
         * Whether we show privacy bar or not
         * @return boolean
         */
        function toShowBar() {
            return !localStorage.getItem('contaoPrivacy.barUsed');
        }
        /**
         * Show privacy bar
         */
        function showBar() {
            document.querySelector('.privacy-bar').style.cssText = 'display: block; transform: translateY(0); opacity: 1';
        }
        /**
         * Set privacy bar used
         */
        function setBarUsed() {
            localStorage.setItem('contaoPrivacy.barUsed', '1');
        }
        /**
         * Close privacy bar
         */
        function closeBar() {
            document.querySelector('.privacy-bar').style.cssText = 'opacity: 0; transform: translateY(100%)';
            document.querySelector('#footer').style.paddingBottom = "0";
            setTimeout(function() {
                document.querySelector('.privacy-bar').style.cssText = 'height: 0; display: none';
            }, 600);
        }
        /**
         * Set all enabled
         */
        function enableAll() {
            setAnalytics(true, true);
            setAnalyticsMatomo(true, true);
            setTagmanager(true, true);
            setLeadLab(true, true);
            setGmap(true, true);
            setMapbox(true, true);
            setOpenStreetMap(true, true);
            setYouTube(true, true);
            setVimeo(true, true);
            addToHistory('all', true);
        }
        function disableAll() {
            setAnalytics(false, false);
            setAnalyticsMatomo(false, false);
            setTagmanager(false, false);
            setLeadLab(false, false);
            setGmap(false, false);
            setMapbox(false, false);
            setOpenStreetMap(false, false);
            setYouTube(false, false);
            setVimeo(false, false);
            addToHistory('all', false);
        }
        /**
         * @param bln {boolean}
         * @param skipHistory {boolean}
         */
        function setAnalytics(bln, skipHistory) {
            if (inputAnalytics) {
                localStorage.setItem('contaoPrivacy.enabledAnalytics', bln ? '1' : '');
                if (!skipHistory) {
                    addToHistory('analytics', bln);
                }
                // Switch checkbox correspondingly
                inputAnalytics.checked = bln;
                // Show right status message
                document.querySelector('.g-analytics .status-enabled').style.display = bln ? 'inline-block' : 'none';
                document.querySelector('.g-analytics .status-disabled').style.display = bln ? 'none' : 'inline-block';
            }
        }
        /**
         * @param bln {boolean}
         * @param skipHistory {boolean}
         */
        function setAnalyticsMatomo(bln, skipHistory) {
            if (inputAnalyticsMatomo) {
                localStorage.setItem('contaoPrivacy.enabledAnalyticsMatomo', bln ? '1' : '');
                if (!skipHistory) {
                    addToHistory('analyticsMatomo', bln);
                }
                // Switch checkbox correspondingly
                inputAnalyticsMatomo.checked = bln;
                // Show right status message
                document.querySelector('.matomo-analytics .status-enabled').style.display = bln ? 'inline-block' : 'none';
                document.querySelector('.matomo-analytics .status-disabled').style.display = bln ? 'none' : 'inline-block';
            }
        }
        /**
         * @param bln {boolean}
         * @param skipHistory {boolean}
         */
        function setTagmanager(bln, skipHistory) {
            if (inputTagmanager) {
                localStorage.setItem('contaoPrivacy.enabledTagManager', bln ? '1' : '');
                if (!skipHistory) {
                    addToHistory('tagManager', bln);
                }
                // Switch checkbox correspondingly
                inputTagmanager.checked = bln;
                // Show right status message
                document.querySelector('.g-tagmanager .status-enabled').style.display = bln ? 'inline-block' : 'none';
                document.querySelector('.g-tagmanager .status-disabled').style.display = bln ? 'none' : 'inline-block';
            }
        }
        /**
         * @param bln {boolean}
         * @param skipHistory {boolean}
         */
        function setLeadLab(bln, skipHistory) {
            if (inputLeadLab) {
                localStorage.setItem('contaoPrivacy.enabledLeadlab', bln ? '1' : '');
                if (!skipHistory) {
                    addToHistory('leadlab', bln);
                }
                // Switch checkbox correspondingly
                inputLeadLab.checked = bln;
                // Show right status message
                document.querySelector('.leadlab .status-enabled').style.display = bln ? 'inline-block' : 'none';
                document.querySelector('.leadlab .status-disabled').style.display = bln ? 'none' : 'inline-block';
            }
        }
        /**
         * @param bln {boolean}
         * @param skipHistory {boolean}
         */
        function setGmap(bln, skipHistory) {
            if (inputGmaps) {
                localStorage.setItem('contaoPrivacy.enabledGmap', bln ? '1' : '');
                if (!skipHistory) {
                    addToHistory('gmap', bln);
                }
                // Switch checkbox correspondingly
                inputGmaps.checked = bln;
                // Show right status message
                document.querySelector('.g-maps .status-enabled').style.display = bln ? 'inline-block' : 'none';
                document.querySelector('.g-maps .status-disabled').style.display = bln ? 'none' : 'inline-block';
                if (bln) {
                    return showGmap();
                }
                hideGmap();
            }
        }
        /**
         * Show google map if present
         */
        function showGmap() {
            var gMapContainer = document.querySelectorAll('.map-container');
            if (!gMapContainer) {
                return;
            }
            gMapContainer.forEach(function(elem) {
                var gMapBlock = elem.querySelector('.dlh_googlemap');
                var gMapQuestionBlock = elem.querySelector('.map-question-block');
                var gMapPrivacyBtn = elem.querySelector('.open-privacy-btn');
                elem.classList.add('active-gmap');
                gMapBlock.classList.remove('map-hidden');
                gMapQuestionBlock.style.display = 'none';
                gMapPrivacyBtn.style.display = 'block';
            });
            document.querySelector('#privacy-settings').classList.add('active-gmap');
        }
        /**
         * Hide google map if present
         */
        function hideGmap() {
            var gMapContainer = document.querySelectorAll('.map-container');
            if (!gMapContainer) {
                return;
            }
            gMapContainer.forEach(function(elem) {
                var gMapBlock = elem.querySelector('.dlh_googlemap');
                var gMapQuestionBlock = elem.querySelector('.map-question-block');
                var gMapPrivacyBtn = elem.querySelector('.open-privacy-btn');
                elem.classList.remove('active-gmap');
                gMapBlock.classList.add('map-hidden');
                gMapQuestionBlock.style.display = 'block';
                gMapPrivacyBtn.style.display = 'none';
            });
            document.querySelector('#privacy-settings').classList.remove('active-gmap');
        }
        /**
         * @param bln {boolean}
         * @param skipHistory {boolean}
         */
        function setMapbox(bln, skipHistory) {
            if (inputMapbox) {
                localStorage.setItem('contaoPrivacy.enabledMapbox', bln ? '1' : '');
                if (!skipHistory) {
                    addToHistory('mapbox', bln);
                }
                // Switch checkbox correspondingly
                inputMapbox.checked = bln;
                // Show right status message
                document.querySelector('.mapbox .status-enabled').style.display = bln ? 'inline-block' : 'none';
                document.querySelector('.mapbox .status-disabled').style.display = bln ? 'none' : 'inline-block';
                if (bln) {
                    return showMapbox();
                }
                hideMapbox();
            }
        }
        /**
         * Show mapbox if present
         */
        function showMapbox() {
            var mapboxContainer = document.querySelectorAll('.mapbox-container');
            if (!mapboxContainer) {
                return;
            }
            mapboxContainer.forEach(function(elem) {
                var mapboxBlock = elem.querySelector('.embeded-map');
                var mapboxQuestionBlock = elem.querySelector('.map-question-block');
                var mapboxPrivacyBtn = elem.nextElementSibling;
                elem.classList.add('active-mapbox');
                mapboxBlock.classList.remove('map-hidden');
                mapboxQuestionBlock.style.display = 'none';
                mapboxPrivacyBtn.style.display = 'block';
            });
            document.querySelector('#privacy-settings').classList.add('active-mapbox');
        }
        /**
         * Hide mapbox if present
         */
        function hideMapbox() {
            var mapboxContainer = document.querySelectorAll('.mapbox-container');
            if (!mapboxContainer) {
                return;
            }
            mapboxContainer.forEach(function(elem) {
                var mapboxBlock = elem.querySelector('.embeded-map');
                var mapboxQuestionBlock = elem.querySelector('.map-question-block');
                var mapboxPrivacyBtn = elem.nextElementSibling;
                elem.classList.remove('active-mapbox');
                mapboxBlock.classList.add('map-hidden');
                mapboxQuestionBlock.style.display = 'block';
                mapboxPrivacyBtn.style.display = 'none';
            });
            document.querySelector('#privacy-settings').classList.remove('active-mapbox');
        }
        /**
         * @param bln {boolean}
         * @param skipHistory {boolean}
         */
        function setOpenStreetMap(bln, skipHistory) {
            if (inputOpenStreetMap) {
                localStorage.setItem('contaoPrivacy.enabledOpenStreetMap', bln ? '1' : '');
                if (!skipHistory) {
                    addToHistory('openStreetMap', bln);
                }
                // Switch checkbox correspondingly
                inputOpenStreetMap.checked = bln;
                // Show right status message
                document.querySelector('.open-street-map .status-enabled').style.display = bln ? 'inline-block' : 'none';
                document.querySelector('.open-street-map .status-disabled').style.display = bln ? 'none' : 'inline-block';
                if (bln) {
                    return showOpenStreetMap();
                }
                hideOpenStreetMap();
            }
        }
        function showOpenStreetMap() {
            var openStreetMapContainer = document.querySelectorAll('.open-street-map-block');
            if (!openStreetMapContainer) {
                return;
            }
            openStreetMapContainer.forEach(function(elem) {
                var openStreetMapQuestionBlock = elem.nextElementSibling;
                var openStreetMapPrivacyBtn = elem.parentElement.nextElementSibling;
                elem.style.display = 'block';
                openStreetMapQuestionBlock.style.display = 'none';
                openStreetMapPrivacyBtn.style.display = 'block';
            });
        }
        function hideOpenStreetMap() {
            var openStreetMapContainer = document.querySelectorAll('.open-street-map-block');
            if (!openStreetMapContainer) {
                return;
            }
            openStreetMapContainer.forEach(function(elem) {
                var openStreetMapQuestionBlock = elem.nextElementSibling;
                var openStreetMapPrivacyBtn = elem.parentElement.nextElementSibling;
                elem.style.display = 'none';
                openStreetMapQuestionBlock.style.display = 'block';
                openStreetMapPrivacyBtn.style.display = 'none';
            });
        }
        /**
         * @param bln {boolean}
         * @param skipHistory {boolean}
         */
        function setYouTube(bln, skipHistory) {
            if (inputYouTube) {
                localStorage.setItem('contaoPrivacy.enabledYouTube', bln ? '1' : '');
                if (!skipHistory) {
                    addToHistory('youTube', bln);
                }
                // Switch checkbox correspondingly
                inputYouTube.checked = bln;
                // Show right status message
                document.querySelector('.youtube .status-enabled').style.display = bln ? 'inline-block' : 'none';
                document.querySelector('.youtube .status-disabled').style.display = bln ? 'none' : 'inline-block';
                if (bln) {
                    return showYouTube();
                }
                hideYouTube();
            }
        }
        function showYouTube() {
            var youTubeContainer = document.querySelectorAll('.youtube-video-block');
            youTubeContainer.forEach(function(elem) {
                var ytQuestionBlock = elem.nextElementSibling;
                var ytPrivacyBtn = ytQuestionBlock.nextElementSibling;
                elem.style.display = 'block';
                ytQuestionBlock.style.display = 'none';
                ytPrivacyBtn.style.display = 'block';
            });
            // show preview images (replace data-src with src)
            var previewImages = document.querySelectorAll('.youtube-preview img');
            if (previewImages) {
                for (var i = 0; i < previewImages.length; i += 1) {
                    previewImages[i].setAttribute('src', previewImages[i].getAttribute('data-src'));
                }
            }
        }
        function hideYouTube() {
            var youTubeContainer = document.querySelectorAll('.youtube-video-block');
            youTubeContainer.forEach(function(elem) {
                var ytQuestionBlock = elem.nextElementSibling;
                var ytPrivacyBtn = ytQuestionBlock.nextElementSibling;
                elem.style.display = 'none';
                ytQuestionBlock.style.display = 'block';
                ytPrivacyBtn.style.display = 'none';
            });
        }
        /**
         * @param bln {boolean}
         * @param skipHistory {boolean}
         */
        function setVimeo(bln, skipHistory) {
            if (inputVimeo) {
                localStorage.setItem('contaoPrivacy.enabledVimeo', bln ? '1' : '');
                if (!skipHistory) {
                    addToHistory('vimeo', bln);
                }
                // Switch checkbox correspondingly
                inputVimeo.checked = bln;
                // Show right status message
                document.querySelector('.vimeo .status-enabled').style.display = bln ? 'inline-block' : 'none';
                document.querySelector('.vimeo .status-disabled').style.display = bln ? 'none' : 'inline-block';
                if (bln) {
                    return showVimeo();
                }
                hideVimeo();
            }
        }
        function showVimeo() {
            var vimeoContainer = document.querySelectorAll('.vimeo-video-block');
            vimeoContainer.forEach(function(elem) {
                var vimeoQuestionBlock = elem.nextElementSibling;
                var vimeoPrivacyBtn = vimeoQuestionBlock.nextElementSibling;
                elem.style.display = 'block';
                vimeoQuestionBlock.style.display = 'none';
                vimeoPrivacyBtn.style.display = 'block';
            });
        }
        function hideVimeo() {
            var vimeoContainer = document.querySelectorAll('.vimeo-video-block');
            vimeoContainer.forEach(function(elem) {
                var vimeoQuestionBlock = elem.nextElementSibling;
                var vimeoPrivacyBtn = vimeoQuestionBlock.nextElementSibling;
                elem.style.display = 'none';
                vimeoQuestionBlock.style.display = 'block';
                vimeoPrivacyBtn.style.display = 'none';
            });
        }
        /**
         * Show privacy popup
         */
        function showPopup() {
            document.querySelector('#privacy-settings').style.display = 'block';
            document.querySelector('#footer').classList.remove('addSpace');
            setTimeout(function() {
                document.querySelector('#privacy-settings').style.opacity = '1';
            }, 200);
        }
        /**
         * Close privacy popup
         */
        function closePopup() {
            document.querySelector('#privacy-settings').style.opacity = '0';
            setTimeout(function() {
                document.querySelector('#privacy-settings').style.display = 'none';
                historyBackToMain(); // Close history preview on popup close;
            }, 1000);
        }
        /**
         * @return {object}
         */
        function getHistory() {
            return JSON.parse(localStorage.getItem('contaoPrivacy.history'));
        }
        /**
         *
         * @param type {string}
         * @param value {boolean}
         */
        function addToHistory(type, value) {
            var history = getHistory();
            history.push({
                type: type,
                value: value,
                time: Date.now()
            });
            localStorage.setItem('contaoPrivacy.history', JSON.stringify(history));
            updateHistory();
        }
        function historyShow() {
            document.querySelector('.privacy-settings-main').style.display = 'none';
            document.querySelector('.privacy-settings-history').style.display = 'flex';
        }
        function historyBackToMain() {
            document.querySelector('.privacy-settings-main').style.display = 'flex';
            document.querySelector('.privacy-settings-history').style.display = 'none';
        }
        function updateHistory() {
            var history = getHistory();
            var table = document.querySelector('#privacy-history-table');
            //table.empty();
            table.innerHTML = "";
            history.forEach(function(element) {
                var date = new Date(element.time);
                var germanDateFormat = (date.toLocaleDateString('de')) + ', ' + (date.toLocaleTimeString('de')) + ' Uhr';
                var englishDateFormat = (date.toLocaleDateString('en-GB')) + ' at ' + (date.toLocaleTimeString('en-GB'));
                var dateTimeFormatted = (document.documentElement.lang === "de") ? germanDateFormat : englishDateFormat;
                var label = document.querySelector('#privacy-history-labels #' + element.type + (element.value ? 1 : 0)).textContent;
                var row =
                    "<tr>" +
                    "<td>" + dateTimeFormatted + "</td>" +
                    "<td>" + label + "</td>" +
                    "</tr>";
                table.innerHTML += row;
            });
            if (!history.length) {
                document.querySelector('#privacy-popup-history-show').style.display = 'none';
            } else {
                document.querySelector('#privacy-popup-history-show').style.display = 'block';
            }
        }
        return {
            toShowBar: toShowBar,
            showBar: showBar,
            setBarUsed: setBarUsed,
            enableAll: enableAll,
            disableAll: disableAll,
            closeBar: closeBar,
            showPopup: showPopup,
            closePopup: closePopup,
            setAnalytics: setAnalytics,
            setAnalyticsMatomo: setAnalyticsMatomo,
            setTagmanager: setTagmanager,
            setLeadLab: setLeadLab,
            setGmap: setGmap,
            setMapbox: setMapbox,
            setYouTube: setYouTube,
            setVimeo: setVimeo,
            setOpenStreetMap: setOpenStreetMap,
            historyShow: historyShow,
            historyBackToMain: historyBackToMain,
            updateHistory: updateHistory
        };
    })();
    function runContaoPrivacy() {
        // Show privacy bar if not already shown previously
        if (contaoPrivacy.toShowBar()) {
            contaoPrivacy.showBar();
        }
        // Set history empty array if not in localStorage already
        if (!localStorage.getItem('contaoPrivacy.history')) {
            localStorage.setItem('contaoPrivacy.history', JSON.stringify([]))
        }
        contaoPrivacy.updateHistory();
        // Privacy bar position relative when the page is scrolled to the bottom
        var scrolling = false;
        document.addEventListener('scroll', function() {
            scrolling = true;
        });
        var globalFooter = document.querySelector('#footer');
        var privacyBar = document.querySelector(".privacy-bar");
        var privacyBarHeight = privacyBar.clientHeight + 30;
        setInterval(function() {
            if (scrolling && !localStorage.getItem('contaoPrivacy.barUsed') == '1') {
                scrolling = false;
                if (window.scrollY + window.innerHeight + privacyBarHeight > document.body.scrollHeight) {
                    privacyBar.style.borderTop = '1px solid #fff';
                    globalFooter.style.paddingBottom = privacyBar.clientHeight + 'px';
                } else {
                    privacyBar.style.borderTop = null;
                    globalFooter.style.paddingBottom = null;
                }
            }
        }, 20);
        // Set analytics initially
        if (inputAnalytics) {
            contaoPrivacy.setAnalytics(!!localStorage.getItem('contaoPrivacy.enabledAnalytics'), true);
        }
        // Set matomo analytics initially
        if (inputAnalyticsMatomo) {
            contaoPrivacy.setAnalyticsMatomo(!!localStorage.getItem('contaoPrivacy.enabledAnalyticsMatomo'), true);
        }
        // Set tagmanager initially
        if (inputTagmanager) {
            contaoPrivacy.setTagmanager(!!localStorage.getItem('contaoPrivacy.enabledTagManager'), true);
        }
        // Set leadlab initially
        if (inputLeadLab) {
            contaoPrivacy.setLeadLab(!!localStorage.getItem('contaoPrivacy.enabledLeadlab'), true);
        }
        // Set gmap initially
        if (inputGmaps) {
            contaoPrivacy.setGmap(!!localStorage.getItem('contaoPrivacy.enabledGmap'), true);
        }
        // Set mapbox initially
        if (inputMapbox) {
            contaoPrivacy.setMapbox(!!localStorage.getItem('contaoPrivacy.enabledMapbox'), true);
        }
        // Set youtube initially
        if (inputYouTube) {
            contaoPrivacy.setYouTube(!!localStorage.getItem('contaoPrivacy.enabledYouTube'), true);
        }
        // Set vimeo initially
        if (inputVimeo) {
            contaoPrivacy.setVimeo(!!localStorage.getItem('contaoPrivacy.enabledVimeo'), true);
        }
        // Set open street map initially
        if (inputOpenStreetMap) {
            contaoPrivacy.setOpenStreetMap(!!localStorage.getItem('contaoPrivacy.enabledOpenStreetMap'), true);
        }
        // Enable all
        buttonEnableAll.addEventListener('click', function() {
            contaoPrivacy.enableAll();
            contaoPrivacy.setBarUsed();
            contaoPrivacy.closeBar();
        });
        // Disable all
        buttonDisableAll.addEventListener('click', function() {
            contaoPrivacy.disableAll();
            contaoPrivacy.setBarUsed();
            contaoPrivacy.closeBar();
        });
        // Open privacy popup
        for (var i = 0; i < buttonOpenPopup.length; i++) {
            buttonOpenPopup[i].addEventListener('click', function() {
                contaoPrivacy.showPopup();
                contaoPrivacy.setBarUsed();
                contaoPrivacy.closeBar();
                var innerbox = document.querySelector("#privacy-settings > .innerbox")
                var innerboxHeight = innerbox.clientHeight;
                var windowHeight = window.innerHeight;
            });
        }
        // Close privacy popup
        for (var i = 0; i < buttonClosePopup.length; i++) {
            buttonClosePopup[i].addEventListener('click', function() {
                contaoPrivacy.closePopup();
            });
        }
        // Close privacy popup on click outside of it
        document.addEventListener('click', function(e) {
            // Exclude click on buttons that are opening the popup
            if (e.target.classList.contains('open-privacy-settings')) {
                return;
            }
            if (e.target.closest('.close-privacy')) {
                return contaoPrivacy.closePopup();
            }
            if (!e.target.closest('#privacy-settings .innerbox')) {
                contaoPrivacy.closePopup();
            }
        });
        // Toggle analytics
        if (inputAnalytics) {
            inputAnalytics.addEventListener('change', function() {
                contaoPrivacy.setAnalytics(inputAnalytics.checked);
            });
        }
        // Toggle analytics matomo
        if (inputAnalyticsMatomo) {
            inputAnalyticsMatomo.addEventListener('change', function() {
                contaoPrivacy.setAnalyticsMatomo(inputAnalyticsMatomo.checked);
            });
        }
        // Toggle tagmanager
        if (inputTagmanager) {
            inputTagmanager.addEventListener('change', function() {
                contaoPrivacy.setTagmanager(inputTagmanager.checked);
            });
        }
        // Toggle Leadlab
        if (inputLeadLab) {
            inputLeadLab.addEventListener('change', function() {
                contaoPrivacy.setLeadLab(inputLeadLab.checked);
            });
        }
        // Toggle gmap
        if (inputGmaps) {
            inputGmaps.addEventListener('change', function() {
                contaoPrivacy.setGmap(inputGmaps.checked);
            });
        }
        // Toggle mapbox
        if (inputMapbox) {
            inputMapbox.addEventListener('change', function() {
                contaoPrivacy.setMapbox(inputMapbox.checked);
            });
        }
        // Toggle open street map
        if (inputOpenStreetMap) {
            inputOpenStreetMap.addEventListener('change', function() {
                contaoPrivacy.setOpenStreetMap(inputOpenStreetMap.checked);
            });
        }
        // Toggle youtube
        if (inputYouTube) {
            inputYouTube.addEventListener('change', function() {
                contaoPrivacy.setYouTube(inputYouTube.checked);
            });
        }
        // Toggle vimeo
        if (inputVimeo) {
            inputVimeo.addEventListener('change', function() {
                contaoPrivacy.setVimeo(inputVimeo.checked);
            });
        }
        // Show gmap
        for (var i = 0; i < buttonShowGmap.length; i++) {
            buttonShowGmap[i].addEventListener('click', function() {
                contaoPrivacy.setGmap(true);
            });
        }
        // Show mapbox
        for (var i = 0; i < buttonShowMapbox.length; i++) {
            buttonShowMapbox[i].addEventListener('click', function() {
                contaoPrivacy.setMapbox(true);
            });
        }
        // Show open street map
        for (var i = 0; i < buttonShowOpenStreetMap.length; i++) {
            buttonShowOpenStreetMap[i].addEventListener('click', function() {
                contaoPrivacy.setOpenStreetMap(true);
            });
        }
        // Show youtube
        for (var i = 0; i < buttonShowYouTube.length; i++) {
            buttonShowYouTube[i].addEventListener('click', function() {
                contaoPrivacy.setYouTube(true);
            });
        }
        // Show vimeo
        for (var i = 0; i < buttonShowVimeo.length; i++) {
            buttonShowVimeo[i].addEventListener('click', function() {
                contaoPrivacy.setVimeo(true);
            });
        }
        // Show history
        document.querySelector('#privacy-popup-history-show').addEventListener('click', contaoPrivacy.historyShow);
        // Back to main (from history)
        document.querySelector('#privacy-popup-history-back-to-main').addEventListener('click', contaoPrivacy.historyBackToMain);
        // Accordion js logic
        var accTogglers = document.querySelectorAll('.accordion-item .acc-toggler');
        accTogglers.forEach(function(accordion) {
            var accHeading = accordion.parentElement;
            var accContent = accHeading.nextElementSibling;
            var otherHeadings = document.querySelectorAll('.accordion-item .acc-toggler');
            accordion.addEventListener('click', function() {
                if (accHeading.classList.contains('active')) {
                    accHeading.classList.remove('active');
                    accContent.style.maxHeight = null;
                } else {
                    for (var i = 0; i < otherHeadings.length; i++) {
                        otherHeadings[i].parentElement.classList.remove('active');
                        otherHeadings[i].parentElement.nextElementSibling.style.maxHeight = null;
                    }
                    accHeading.classList.add('active');
                    accContent.style.maxHeight = accContent.querySelector('.accordion-inner').clientHeight + 'px';
                }
            });
        });
    }
    runContaoPrivacy();
}
if (IEbrowser) {
    window.onload = function() {
        startPrivacyMagic();
    }
} else {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', startPrivacyMagic);
    } else {
        startPrivacyMagic();
    }
}