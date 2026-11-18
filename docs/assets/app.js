/* 知识库站点交互 —— 主题切换 + 本地搜索，无依赖 */

(function () {
  "use strict";

  /* ---------- 主题 ---------- */
  var KEY = "kb-theme";
  var btn = document.getElementById("theme-toggle");

  function current() {
    var t = document.documentElement.getAttribute("data-theme");
    if (t) return t;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  if (btn) {
    btn.addEventListener("click", function () {
      var next = current() === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
    });
  }

  /* ---------- 吸顶栏高度（供 quicknav 定位与锚点偏移）---------- */
  var topBar = document.querySelector(".top");

  function syncTop() {
    if (topBar) {
      document.documentElement.style.setProperty("--top-h", topBar.offsetHeight + "px");
    }
  }

  syncTop();
  window.addEventListener("resize", syncTop);

  /* ---------- 分类下拉跳转 ---------- */
  var jump = document.getElementById("jump");
  if (jump) {
    jump.addEventListener("change", function () {
      var id = this.value;
      if (!id) return;
      var el = document.getElementById(id);
      if (el) {
        el.scrollIntoView({ behavior: "smooth", block: "start" });
        try { history.replaceState(null, "", "#" + id); } catch (e) {}
      }
      this.blur();
    });
  }

  /* ---------- 回到顶部 ---------- */
  var toTop = document.createElement("button");
  toTop.className = "totop";
  toTop.type = "button";
  toTop.setAttribute("aria-label", "回到顶部");
  toTop.textContent = "↑";
  toTop.addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
  document.body.appendChild(toTop);

  window.addEventListener("scroll", function () {
    toTop.classList.toggle("show", window.scrollY > 700);
  }, { passive: true });

  /* ---------- 搜索（只在首页有输入框时启用）---------- */
  var input = document.getElementById("q");
  var box = document.getElementById("results");
  if (!input || !box) return;

  var DATA = null;
  var FAILED = false;

  var script = document.currentScript;
  var base = "";
  if (script && script.src) {
    base = script.src.replace(/assets\/app\.js.*$/, "");
  }

  function load() {
    if (DATA) return Promise.resolve(DATA);
    if (FAILED) return Promise.resolve([]);
    return fetch(base + "search.json", { cache: "no-cache" })
      .then(function (r) { return r.json(); })
      .then(function (d) { DATA = d; return d; })
      .catch(function () { FAILED = true; return []; });
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function mark(text, q) {
    var safe = esc(text);
    if (!q) return safe;
    var idx = safe.toLowerCase().indexOf(q.toLowerCase());
    if (idx < 0) return safe;
    return safe.slice(0, idx) + "<mark>" + safe.slice(idx, idx + q.length) + "</mark>" +
      safe.slice(idx + q.length);
  }

  function score(it, q) {
    var t = it.t.toLowerCase();
    var s = 0;
    if (t === q) s += 200;
    else if (t.indexOf(q) === 0) s += 120;
    else if (t.indexOf(q) > 0) s += 70;
    for (var i = 0; i < (it.a || []).length; i++) {
      var a = it.a[i].toLowerCase();
      if (a === q) { s += 100; break; }
      if (a.indexOf(q) > -1) { s += 45; break; }
    }
    if ((it.d || "").toLowerCase().indexOf(q) > -1) s += 15;
    if ((it.x || "").toLowerCase().indexOf(q) > -1) s += 10;
    return s;
  }

  function render(hits, q) {
    if (!hits.length) {
      box.innerHTML = '<div class="empty">没有匹配「' + esc(q) + '」的概念</div>';
      box.hidden = false;
      return;
    }
    box.innerHTML = hits.map(function (h) {
      return '<a href="' + base + h.item.u + '">' +
        '<span class="rt">' + mark(h.item.t, q) + "</span>" +
        '<span class="rd">' + esc(h.item.d) + (h.item.s ? " · " + esc(h.item.s.slice(0, 46)) : "") + "</span>" +
        "</a>";
    }).join("");
    box.hidden = false;
  }

  var timer = null;

  input.addEventListener("input", function () {
    clearTimeout(timer);
    var q = input.value.trim();
    if (!q) { box.hidden = true; box.innerHTML = ""; return; }
    timer = setTimeout(function () {
      load().then(function (data) {
        var lq = q.toLowerCase();
        var hits = data
          .map(function (it) { return { item: it, s: score(it, lq) }; })
          .filter(function (x) { return x.s > 0; })
          .sort(function (a, b) { return b.s - a.s; })
          .slice(0, 12);
        render(hits, q);
      });
    }, 110);
  });

  input.addEventListener("focus", function () { load(); });

  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      var first = box.querySelector("a");
      if (first) window.location.href = first.getAttribute("href");
    } else if (e.key === "Escape") {
      box.hidden = true;
      input.blur();
    }
  });

  document.addEventListener("click", function (e) {
    if (!box.contains(e.target) && e.target !== input) box.hidden = true;
  });
})();
