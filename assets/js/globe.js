/* НОВАТЕЛ — анимированный глобус из точек (vanilla canvas, без зависимостей) */
(function () {
  "use strict";
  var c = document.getElementById("hero-globe");
  if (!c || !c.getContext) return;
  var ctx = c.getContext("2d");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var w, h, dpr;
  function size() {
    var r = c.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    c.width = Math.max(1, r.width * dpr);
    c.height = Math.max(1, r.height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    w = r.width; h = r.height;
  }
  size();

  // Точки равномерно по сфере (спираль Фибоначчи)
  var N = 1000, pts = [];
  for (var i = 0; i < N; i++) {
    var y = 1 - (i / (N - 1)) * 2;
    var rad = Math.sqrt(Math.max(0, 1 - y * y));
    var th = i * 2.399963229728653;
    pts.push({ x: Math.cos(th) * rad, y: y, z: Math.sin(th) * rad, g: (i % 7 === 0) });
  }
  // Узлы связи (широта, долгота)
  function ll(lat, lon) {
    lat *= Math.PI / 180; lon *= Math.PI / 180;
    return { x: Math.cos(lat) * Math.cos(lon), y: Math.sin(lat), z: Math.cos(lat) * Math.sin(lon) };
  }
  var nodes = [ll(55, 37), ll(40, -74), ll(35, 139), ll(-23, -46), ll(51, 0), ll(1, 103)];

  var ang = 0, tilt = -0.34, ct = Math.cos(tilt), st = Math.sin(tilt);
  var running = false, raf = 0;

  function draw(t) {
    ctx.clearRect(0, 0, w, h);
    var cx = w / 2, cy = h * 0.47, R = Math.min(w, h) * 0.5;
    var ca = Math.cos(ang), sa = Math.sin(ang), k;
    for (k = 0; k < pts.length; k++) {
      var p = pts[k];
      var x = p.x * ca - p.z * sa, z = p.x * sa + p.z * ca, y = p.y;
      var y2 = y * ct - z * st, z2 = y * st + z * ct;
      var depth = (z2 + 1) / 2;
      var sx = cx + x * R, sy = cy + y2 * R;
      var a = 0.07 + depth * 0.6;
      ctx.beginPath();
      ctx.fillStyle = p.g ? "rgba(79,122,87," + (a * 0.95) + ")" : "rgba(31,78,140," + a + ")";
      ctx.arc(sx, sy, 0.55 + depth * 1.7, 0, 6.2832);
      ctx.fill();
    }
    for (k = 0; k < nodes.length; k++) {
      var n = nodes[k];
      var nx = n.x * ca - n.z * sa, nz = n.x * sa + n.z * ca, ny = n.y;
      var ny2 = ny * ct - nz * st, nz2 = ny * st + nz * ct;
      if (nz2 < 0.05) continue;
      var pxx = cx + nx * R, pyy = cy + ny2 * R;
      var ph = ((t / 1600) + k * 0.27) % 1;
      ctx.beginPath();
      ctx.strokeStyle = "rgba(31,78,140," + (0.45 * (1 - ph)) + ")";
      ctx.lineWidth = 1.2;
      ctx.arc(pxx, pyy, 2 + ph * 14, 0, 6.2832);
      ctx.stroke();
      ctx.beginPath();
      ctx.fillStyle = "#1F4E8C";
      ctx.arc(pxx, pyy, 2.6, 0, 6.2832);
      ctx.fill();
    }
  }

  function loop(t) {
    if (!running) return;
    draw(t || 0);
    ang += 0.0030;
    raf = requestAnimationFrame(loop);
  }
  function start() { if (running || reduce) return; running = true; raf = requestAnimationFrame(loop); }
  function stop() { running = false; cancelAnimationFrame(raf); }

  if (reduce) { draw(0); }
  else {
    // крутим только когда hero на экране и вкладка активна
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) { e.isIntersecting ? start() : stop(); });
      }, { threshold: 0.05 }).observe(c);
    } else { start(); }
    document.addEventListener("visibilitychange", function () { document.hidden ? stop() : start(); });
  }

  var to;
  window.addEventListener("resize", function () {
    clearTimeout(to);
    to = setTimeout(function () { size(); if (reduce || !running) draw(0); }, 120);
  });
})();
