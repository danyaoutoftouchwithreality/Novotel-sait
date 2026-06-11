/* НОВАТЕЛ — точечная Земля в hero.
   Основной режим: библиотека cobe (WebGL, как у Cloudflare/Vercel).
   Если не загрузилась — запасной простой глобус из точек на 2D-canvas. */
(function () {
  "use strict";
  var canvas = document.getElementById("hero-globe");
  if (!canvas) return;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Города-маркеры (широта, долгота)
  var MARKERS = [
    { location: [55.75, 37.62], size: 0.08 }, // Москва
    { location: [59.94, 30.31], size: 0.05 }, // СПб
    { location: [40.71, -74.0], size: 0.05 }, // Нью-Йорк
    { location: [51.51, -0.13], size: 0.05 }, // Лондон
    { location: [35.68, 139.69], size: 0.05 }, // Токио
    { location: [25.2, 55.27], size: 0.05 },  // Дубай
    { location: [1.35, 103.82], size: 0.045 } // Сингапур
  ];

  import("https://cdn.jsdelivr.net/npm/cobe@0.6.4/+esm")
    .then(function (m) { initCobe(m.default); })
    .catch(function () { initFallback(); });

  /* ---------- cobe: точечная Земля ---------- */
  function initCobe(createGlobe) {
    var phi = 0, paused = reduce, size = 0, globe = null;
    function build() {
      if (globe) { globe.destroy(); globe = null; }
      size = canvas.offsetWidth || 600;
      globe = createGlobe(canvas, {
        devicePixelRatio: Math.min(window.devicePixelRatio || 1, 2),
        width: size * 2,
        height: size * 2,
        phi: 0,
        theta: 0.22,
        dark: 0,
        diffuse: 0.35,
        mapSamples: 17000,
        mapBrightness: 2.0,
        baseColor: [0.52, 0.66, 0.87],   // светлые сине-голубые точки суши
        markerColor: [0.12, 0.31, 0.55], // акцентные маркеры
        glowColor: [1, 1, 1],
        opacity: 0.62,
        markers: MARKERS,
        onRender: function (state) {
          if (!paused) phi += 0.0042;
          state.phi = phi;
          state.width = size * 2;
          state.height = size * 2;
        }
      });
    }
    build();
    var to;
    window.addEventListener("resize", function () {
      clearTimeout(to);
      to = setTimeout(function () { if ((canvas.offsetWidth || 0) !== size) build(); }, 180);
    });
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) { paused = reduce || !e.isIntersecting; });
      }, { threshold: 0.05 }).observe(canvas);
    }
    document.addEventListener("visibilitychange", function () {
      if (!reduce) paused = document.hidden;
    });
  }

  /* ---------- запасной глобус (2D точки) ---------- */
  function initFallback() {
    var ctx = canvas.getContext && canvas.getContext("2d");
    if (!ctx) return;
    var w, h, dpr;
    function size() {
      var r = canvas.getBoundingClientRect();
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.max(1, r.width * dpr);
      canvas.height = Math.max(1, r.height * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      w = r.width; h = r.height;
    }
    size();
    var N = 1000, pts = [];
    for (var i = 0; i < N; i++) {
      var y = 1 - (i / (N - 1)) * 2, rad = Math.sqrt(Math.max(0, 1 - y * y)), th = i * 2.399963229;
      pts.push({ x: Math.cos(th) * rad, y: y, z: Math.sin(th) * rad, g: (i % 7 === 0) });
    }
    var ang = 0, tilt = -0.34, ct = Math.cos(tilt), st = Math.sin(tilt), running = false, raf = 0;
    function draw() {
      ctx.clearRect(0, 0, w, h);
      var cx = w / 2, cy = h / 2, R = Math.min(w, h) * 0.46, ca = Math.cos(ang), sa = Math.sin(ang);
      for (var k = 0; k < pts.length; k++) {
        var p = pts[k], x = p.x * ca - p.z * sa, z = p.x * sa + p.z * ca, y = p.y;
        var y2 = y * ct - z * st, z2 = y * st + z * ct, d = (z2 + 1) / 2;
        var a = 0.07 + d * 0.6;
        ctx.beginPath();
        ctx.fillStyle = p.g ? "rgba(79,122,87," + (a * 0.95) + ")" : "rgba(31,78,140," + a + ")";
        ctx.arc(cx + x * R, cy + y2 * R, 0.55 + d * 1.7, 0, 6.2832); ctx.fill();
      }
    }
    function loop() { if (!running) return; draw(); ang += 0.003; raf = requestAnimationFrame(loop); }
    function start() { if (running || reduce) return; running = true; raf = requestAnimationFrame(loop); }
    function stop() { running = false; cancelAnimationFrame(raf); }
    reduce ? draw() : start();
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) { es.forEach(function (e) { e.isIntersecting ? start() : stop(); }); }, { threshold: 0.05 }).observe(canvas);
    }
    var to2; window.addEventListener("resize", function () { clearTimeout(to2); to2 = setTimeout(function () { size(); if (reduce || !running) draw(); }, 120); });
  }
})();
