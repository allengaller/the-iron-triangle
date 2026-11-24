/* 铁角指北 · 三书阅读器交互：字号、主题、目录、进度、章内导航、跨书搜索 */
(function () {
  "use strict";
  var ROOT = window.__ROOT__ || "";
  var $ = function (s) { return document.querySelector(s); };
  var on = function (el, ev, fn) { if (el) el.addEventListener(ev, fn); };
  var BOOKS = { tam: "TAM", sa: "SA", bte: "BTE" };

  /* ---------- 深 / 浅主题 ---------- */
  var root = document.documentElement;
  function applyTheme(t) {
    if (t === "dark") root.setAttribute("data-theme", "dark");
    else root.removeAttribute("data-theme");
    try { localStorage.setItem("it-theme", t); } catch (e) {}
  }
  on($("#btn-theme"), "click", function () {
    applyTheme(root.getAttribute("data-theme") === "dark" ? "light" : "dark");
  });

  /* ---------- 字号 ---------- */
  var STEPS = ["16px", "17px", "18.5px", "20px"];
  function curStep() {
    var v = getComputedStyle(root).getPropertyValue("--fs").trim();
    var i = STEPS.indexOf(v);
    return i < 0 ? 1 : i;
  }
  function setFs(i) {
    i = Math.max(0, Math.min(STEPS.length - 1, i));
    root.style.setProperty("--fs", STEPS[i]);
    try { localStorage.setItem("it-fs", STEPS[i]); } catch (e) {}
  }
  on($("#btn-fs-up"), "click", function () { setFs(curStep() + 1); });
  on($("#btn-fs-down"), "click", function () { setFs(curStep() - 1); });

  /* ---------- 侧栏（移动端） ---------- */
  var sidebar = $("#sidebar"), backdrop = $("#backdrop");
  function toggleToc(force) {
    if (!sidebar) return;
    var open = force !== undefined ? force : !sidebar.classList.contains("open");
    sidebar.classList.toggle("open", open);
    if (backdrop) backdrop.classList.toggle("open", open);
  }
  on($("#btn-toc"), "click", function () { toggleToc(); });
  on(backdrop, "click", function () { toggleToc(false); });
  on(sidebar, "click", function (e) {
    if (e.target.closest("a") && innerWidth <= 1080) toggleToc(false);
  });

  /* ---------- 滚动进度 ---------- */
  var bar = $("#progress"), ticking = false;
  function updateProgress() {
    if (!bar) return;
    var h = document.documentElement.scrollHeight - innerHeight;
    bar.style.width = (h > 0 ? (scrollY / h) * 100 : 0) + "%";
    ticking = false;
  }
  addEventListener("scroll", function () {
    if (!ticking) { requestAnimationFrame(updateProgress); ticking = true; }
  }, { passive: true });
  updateProgress();

  /* ---------- 侧栏当前项高亮 ---------- */
  var file = document.body.dataset.file;
  if (sidebar && file) {
    var active = sidebar.querySelector('a[data-file="' + CSS.escape(file) + '"]');
    if (active) {
      active.classList.add("active");
      var r = active.getBoundingClientRect(), s = sidebar.getBoundingClientRect();
      if (r.top < s.top + 80 || r.bottom > s.bottom) {
        sidebar.scrollTop += r.top - s.top - s.height / 2.4;
      }
    }
  }

  /* ---------- 本章小节（章内导航） ---------- */
  var outline = $("#outline");
  var heads = document.querySelectorAll("article h2[id]");
  if (outline && heads.length >= 3) {
    outline.hidden = false;
    var olinks = [], frag = document.createDocumentFragment();
    heads.forEach(function (h) {
      var a = document.createElement("a");
      a.href = "#" + h.id;
      a.textContent = h.textContent;
      frag.appendChild(a);
      olinks.push({ a: a, h: h });
    });
    outline.appendChild(frag);
    var spyTick = false;
    var spy = function () {
      var y = scrollY + 130, cur = 0;
      for (var i = 0; i < olinks.length; i++) {
        if (olinks[i].h.getBoundingClientRect().top + scrollY <= y) cur = i;
      }
      olinks.forEach(function (o, i) { o.a.classList.toggle("active", i === cur); });
      spyTick = false;
    };
    addEventListener("scroll", function () {
      if (!spyTick) { requestAnimationFrame(spy); spyTick = true; }
    }, { passive: true });
    spy();
  }

  /* ---------- 三书搜索 ---------- */
  var overlay = $("#search-overlay"), big = $("#search-big"),
      results = $("#search-results"), count = $("#search-count");
  var INDEX = null, loading = null, sel = 0, hits = [];

  function loadIndex() {
    if (INDEX) return Promise.resolve(INDEX);
    if (!loading) loading = fetch(ROOT + "search-index.json").then(function (r) { return r.json(); });
    return loading;
  }
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  /* 索引字段进 href 前白名单校验：文件路径与锚点 id 只允许安全字符 */
  function safePath(p) { return typeof p === "string" && /^[A-Za-z0-9_./-]+\.html$/.test(p) ? p : ""; }
  function safeId(i) { return typeof i === "string" && /^[A-Za-z0-9_-]+$/.test(i) ? i : ""; }
  function mark(s, q) {
    var i = s.toLowerCase().indexOf(q);
    if (i < 0) return esc(s.slice(0, 120));
    var a = Math.max(0, i - 34);
    return (a ? "…" : "") + esc(s.slice(a, i)) + "<mark>" + esc(s.slice(i, i + q.length)) + "</mark>" +
           esc(s.slice(i + q.length, i + q.length + 90)) + "…";
  }
  function search(q) {
    q = q.trim().toLowerCase();
    if (!q) { results.innerHTML = ""; count.textContent = ""; hits = []; return; }
    loadIndex().then(function (idx) {
      hits = [];
      for (var i = 0; i < idx.length && hits.length < 300; i++) {
        var e = idx[i], t = e.t.toLowerCase(), x = e.x.toLowerCase();
        var ti = t.indexOf(q), xi = x.indexOf(q);
        if (ti >= 0 || xi >= 0) hits.push({ e: e, w: (ti >= 0 ? 2 : 0) + (xi >= 0 ? 1 : 0) });
      }
      hits.sort(function (a, b) { return b.w - a.w; });
      // 三书同名：单本最多占 14 条，余下名额按权重回填。
      // 不这么分，「承诺」这类高频词会被 TAM 一口吃满，SA/BTE 永远不出现在首屏。
      var per = {}, kept = [], rest = [];
      hits.forEach(function (h) {
        var b = h.e.b || "";
        per[b] = (per[b] || 0) + 1;
        (per[b] <= 14 ? kept : rest).push(h);
      });
      hits = kept.concat(rest).slice(0, 40);
      // 按「书 → 页面」重排，同一页的命中挨在一起，分组头不会重复出现
      hits.sort(function (a, b) {
        var ka = (a.e.b || "") + "|" + a.e.f, kb = (b.e.b || "") + "|" + b.e.f;
        return ka < kb ? -1 : ka > kb ? 1 : 0;
      });
      sel = 0;
      if (!hits.length) { results.innerHTML = '<div id="search-empty">没有找到「' + esc(q) + '」</div>'; count.textContent = ""; return; }
      var html = "", lastFile = "";
      hits.forEach(function (h, i) {
        var e = h.e;
        if (e.f !== lastFile) {
          var label = (BOOKS[e.b] ? BOOKS[e.b] + " · " : "") + e.t;
          html += '<div class="part-head" style="padding-top:8px">' + esc(label) + '</div>';
          lastFile = e.f;
        }
        html += '<a class="sr-item' + (i === 0 ? " sel" : "") + '" data-i="' + i + '" href="' + ROOT + safePath(e.f) + (safeId(e.i) ? "#" + safeId(e.i) : "") + '">' +
                '<div class="sr-t">' + esc(e.h || e.t) + "</div>" +
                '<div class="sr-x">' + mark(e.x, q) + "</div></a>";
      });
      results.innerHTML = html;
      count.textContent = hits.length + " 条结果";
    });
  }
  function openSearch() {
    if (!overlay) return;
    overlay.classList.add("open");
    big.value = ""; results.innerHTML = ""; count.textContent = ""; hits = [];
    setTimeout(function () { big.focus(); }, 30);
    loadIndex();
  }
  function closeSearch() { if (overlay) overlay.classList.remove("open"); }
  function moveSel(d) {
    if (!hits.length) return;
    sel = Math.max(0, Math.min(hits.length - 1, sel + d));
    var items = results.querySelectorAll(".sr-item");
    items.forEach(function (el, i) { el.classList.toggle("sel", i === sel); });
    if (items[sel]) items[sel].scrollIntoView({ block: "nearest" });
  }

  on($("#btn-search"), "click", openSearch);
  on($("#search-input"), "focus", openSearch);
  on(big, "input", function () { search(big.value); });
  on(overlay, "click", function (e) { if (e.target === overlay) closeSearch(); });
  on(results, "click", function (e) { if (e.target.closest(".sr-item")) closeSearch(); });

  /* ---------- 键盘 ---------- */
  addEventListener("keydown", function (e) {
    var tag = document.activeElement && document.activeElement.tagName;
    var inInput = /INPUT|TEXTAREA/.test(tag || "");
    if (e.key === "Escape") { closeSearch(); toggleToc(false); return; }
    if (inInput) {
      if (e.key === "ArrowDown") { e.preventDefault(); moveSel(1); }
      if (e.key === "ArrowUp") { e.preventDefault(); moveSel(-1); }
      if (e.key === "Enter" && hits[sel]) {
        var el = results.querySelectorAll(".sr-item")[sel];
        if (el) { location.href = el.href; closeSearch(); }
      }
      return;
    }
    if (e.key === "/") { e.preventDefault(); openSearch(); return; }
    if (e.key === "ArrowLeft") {
      var p = document.querySelector(".pager .prev:not(.disabled)");
      if (p) location.href = p.href;
    }
    if (e.key === "ArrowRight") {
      var n = document.querySelector(".pager .next:not(.disabled)");
      if (n) location.href = n.href;
    }
  });
})();
