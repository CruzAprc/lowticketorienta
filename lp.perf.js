(function () {
  var videos = document.querySelectorAll("video[data-src]");
  if (!videos.length) return;
  var arm = function (v) {
    if (v.dataset.armed) return;
    v.dataset.armed = "1";
    v.src = v.getAttribute("data-src");
    v.preload = "metadata";
    var play = function () { v.play().catch(function () {}); };
    if (v.readyState >= 2) play();
    else v.addEventListener("canplay", play, { once: true });
  };
  if (!("IntersectionObserver" in window)) {
    videos.forEach(arm);
    return;
  }
  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          arm(entry.target);
          io.unobserve(entry.target);
        }
      });
    },
    { rootMargin: "240px 0px" }
  );
  videos.forEach(function (v) { io.observe(v); });
})();
