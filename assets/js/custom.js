// Custom site JS (loaded after Swiper)
(function () {
  "use strict";

  // Open search modal on Ctrl+K / Cmd+K (like many modern sites)
  function initSearchHotkey() {
    document.addEventListener("keydown", function (e) {
      var isMac = navigator.platform && /mac/i.test(navigator.platform);
      var mod = isMac ? e.metaKey : e.ctrlKey;
      if (!mod) return;
      if ((e.key || "").toLowerCase() !== "k") return;
      e.preventDefault();
      var trigger = document.querySelector('[data-target="search-modal"]');
      if (trigger) trigger.click();
    });
  }

  function initActivitiesSlider() {
    if (typeof Swiper !== "function") return;
    var el = document.querySelector(".activities-slider");
    if (!el) return;

    // Avoid double-init
    if (el.classList.contains("swiper-initialized")) return;

    new Swiper(".activities-slider", {
      slidesPerView: 1,
      spaceBetween: 16,
      loop: true,
      autoplay: {
        delay: 3200,
        disableOnInteraction: false,
      },
      navigation: {
        nextEl: ".activities-slider-next",
        prevEl: ".activities-slider-prev",
      },
    });
  }

  // Publications-only search (filters the list on /publications)
  function initPublicationsSearch() {
    var input = document.querySelector(".pub-search-input");
    if (!input) return;

    var yearSections = Array.prototype.slice.call(
      document.querySelectorAll(".pub-year")
    );

    function applyFilter() {
      var q = (input.value || "").trim().toLowerCase();

      yearSections.forEach(function (sec) {
        var items = Array.prototype.slice.call(
          sec.querySelectorAll(".pub-item")
        );
        var anyVisible = false;

        items.forEach(function (it) {
          var hay = (it.getAttribute("data-search") || "").toLowerCase();
          var match = !q || hay.indexOf(q) !== -1;
          it.style.display = match ? "" : "none";
          if (match) anyVisible = true;
        });

        sec.style.display = anyVisible ? "" : "none";
      });
    }

    input.addEventListener("input", applyFilter);
    applyFilter();
  }

  // Project duration counters (days since a start date)
  function initProjectDurationCounters() {
    var nodes = document.querySelectorAll("[data-project-duration-start]");
    if (!nodes || !nodes.length) return;

    function daysSince(startISO) {
      // Expect "YYYY-MM-DD"
      var m = String(startISO || "").match(/^(\d{4})-(\d{2})-(\d{2})$/);
      if (!m) return null;
      var y = parseInt(m[1], 10);
      var mo = parseInt(m[2], 10) - 1;
      var d = parseInt(m[3], 10);
      var startUTC = Date.UTC(y, mo, d);
      var now = new Date();
      var nowUTC = Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate());
      var diffDays = Math.floor((nowUTC - startUTC) / 86400000);
      return diffDays < 0 ? 0 : diffDays;
    }

    nodes.forEach(function (el) {
      var start = el.getAttribute("data-project-duration-start");
      var n = daysSince(start);
      if (n === null) return;
      var numEl = el.querySelector(".project-panel-number");
      if (numEl) numEl.textContent = String(n);
    });
  }

  document.addEventListener("DOMContentLoaded", initActivitiesSlider);
  document.addEventListener("DOMContentLoaded", initSearchHotkey);
  document.addEventListener("DOMContentLoaded", initPublicationsSearch);
  document.addEventListener("DOMContentLoaded", initProjectDurationCounters);
})();


