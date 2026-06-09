/* НОВАТЕЛ — interactions */
(function () {
  "use strict";

  // Sticky nav background on scroll
  const nav = document.querySelector(".nav");
  const onScroll = () => {
    if (window.scrollY > 12) nav.classList.add("scrolled");
    else nav.classList.remove("scrolled");
  };
  if (nav) { onScroll(); window.addEventListener("scroll", onScroll, { passive: true }); }

  // Mobile menu
  const burger = document.querySelector(".burger");
  const menu = document.querySelector(".mobile-menu");
  if (burger && menu) {
    burger.addEventListener("click", () => {
      const open = menu.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    menu.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        menu.classList.remove("open");
        document.body.style.overflow = "";
      })
    );
  }

  // Reveal on scroll
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const reveals = document.querySelectorAll("[data-reveal]");
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach((el) => el.classList.add("in"));
  } else {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.14, rootMargin: "0px 0px -8% 0px" }
    );
    reveals.forEach((el) => io.observe(el));
  }

  // Lead form — compose mailto (no backend required; swap action for a real endpoint later)
  const form = document.getElementById("lead-form");
  if (form) {
    const status = document.getElementById("lf-status");
    const $ = (id) => document.getElementById(id);
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const name = $("lf-name").value.trim();
      const phone = $("lf-phone").value.trim();
      const email = $("lf-email").value.trim();
      const service = $("lf-service").value;
      const message = $("lf-msg").value.trim();
      if (!name || !phone) {
        (!name ? $("lf-name") : $("lf-phone")).focus();
        status.className = "form-status";
        status.style.display = "block";
        status.style.background = "rgba(255,128,64,.12)";
        status.style.color = "#c2410c";
        status.textContent = "Пожалуйста, укажите имя и телефон.";
        return;
      }
      const lines = [
        "Имя: " + name,
        "Телефон: " + phone,
        email ? "E-mail: " + email : null,
        service ? "Услуга: " + service : null,
        message ? "Сообщение: " + message : null,
      ].filter(Boolean);
      const href =
        "mailto:info@novatel.ru?subject=" +
        encodeURIComponent("Заявка с сайта — " + name) +
        "&body=" +
        encodeURIComponent(lines.join("\n"));
      window.location.href = href;
      status.className = "form-status ok";
      status.textContent = "Спасибо! Открываем почтовый клиент для отправки заявки. Если он не открылся — позвоните 8 800 775-12-87.";
      form.reset();
    });
  }

  // Count-up for stats
  const counters = document.querySelectorAll("[data-count]");
  if (counters.length && "IntersectionObserver" in window && !reduce) {
    const cio = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (!e.isIntersecting) return;
          const el = e.target;
          const target = parseFloat(el.dataset.count);
          const suffix = el.dataset.suffix || "";
          const dur = 1400;
          const start = performance.now();
          const tick = (now) => {
            const p = Math.min((now - start) / dur, 1);
            const eased = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.round(target * eased).toLocaleString("ru-RU") + suffix;
            if (p < 1) requestAnimationFrame(tick);
          };
          requestAnimationFrame(tick);
          cio.unobserve(el);
        });
      },
      { threshold: 0.5 }
    );
    counters.forEach((c) => cio.observe(c));
  }
})();
