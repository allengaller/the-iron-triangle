/* The TAM Book 阅读器交互 */
(function () {
  "use strict";
  var ROOT = window.__ROOT__ || "";
  var $ = function (s) { return document.querySelector(s); };

  /* ---------- 主题 ---------- */
  $("#btn-theme").addEventListener("click", function () {
    var cur = document.documentElement.dataset.theme;
    var next = cur === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem("tam-theme", next); } catch (e) {}
  });

  /* ---------- 字号 ---------- */
  var STEPS = ["16.5px", "17.5px", "19px", "20.5px"];
  function curStep() {
    var v = getComputedStyle(document.documentElement).getPropertyValue("--fs").trim();
    var i = STEPS.indexOf(v);
    return i < 0 ? 1 : i;
  }
  function setFs(i) {
    i = Math.max(0, Math.min(STEPS.length - 1, i));
    document.documentElement.style.setProperty("--fs", STEPS[i]);
    try { localStorage.setItem("tam-fs", STEPS[i]); } catch (e) {}
  }
  $("#btn-fs-up").addEventListener("click", function () { setFs(curStep() + 1); });
  $("#btn-fs-down").addEventListener("click", function () { setFs(curStep() - 1); });

  /* ---------- 侧栏（移动端） ---------- */
  var sidebar = $("#sidebar"), backdrop = $("#backdrop");
  function toggleToc(force) {
    var open = force !== undefined ? force : !sidebar.classList.contains("open");
    sidebar.classList.toggle("open", open);
    backdrop.classList.toggle("open", open);
  }
  $("#btn-toc").addEventListener("click", function () { toggleToc(); });
  backdrop.addEventListener("click", function () { toggleToc(false); });
  sidebar.addEventListener("click", function (e) {
    if (e.target.closest("a") && innerWidth <= 1080) toggleToc(false);
  });

  /* ---------- 滚动进度 ---------- */
  var bar = $("#progress"), ticking = false;
  function updateProgress() {
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
  var active = sidebar.querySelector('a[data-file="' + CSS.escape(file) + '"]');
  if (active) {
    active.classList.add("active");
    var r = active.getBoundingClientRect(), s = sidebar.getBoundingClientRect();
    if (r.top < s.top + 80 || r.bottom > s.bottom) {
      sidebar.scrollTop += r.top - s.top - s.height / 2.4;
    }
  }

  /* ---------- 全书搜索 ---------- */
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
      for (var i = 0; i < idx.length && hits.length < 60; i++) {
        var e = idx[i], t = e.t.toLowerCase(), x = e.x.toLowerCase();
        var ti = t.indexOf(q), xi = x.indexOf(q);
        if (ti >= 0 || xi >= 0) hits.push({ e: e, w: (ti >= 0 ? 2 : 0) + (xi >= 0 ? 1 : 0), xi: xi });
      }
      hits.sort(function (a, b) { return b.w - a.w; });
      hits = hits.slice(0, 30);
      sel = 0;
      if (!hits.length) { results.innerHTML = '<div id="search-empty">没有找到「' + esc(q) + '」</div>'; count.textContent = ""; return; }
      var html = "", lastFile = "";
      hits.forEach(function (h, i) {
        var e = h.e;
        if (e.f !== lastFile) {
          html += '<div class="part-head" style="padding-top:8px">' + esc(e.t) + '</div>';
          lastFile = e.f;
        }
        html += '<a class="sr-item' + (i === 0 ? " sel" : "") + '" data-i="' + i + '" href="' + ROOT + safePath(e.f) + (safeId(e.i) ? "#" + safeId(e.i) : "") + '">' +
                '<div class="sr-t">' + esc(e.t) + (e.h ? ' <span class="sr-sec">· ' + esc(e.h) + "</span>" : "") + "</div>" +
                '<div class="sr-x">' + mark(e.x, q) + "</div></a>";
      });
      results.innerHTML = html;
      count.textContent = hits.length + " 条结果";
    });
  }
  function openSearch() {
    overlay.classList.add("open");
    big.value = ""; results.innerHTML = ""; count.textContent = ""; hits = [];
    setTimeout(function () { big.focus(); }, 30);
    loadIndex();
  }
  function closeSearch() { overlay.classList.remove("open"); }
  function moveSel(d) {
    if (!hits.length) return;
    sel = Math.max(0, Math.min(hits.length - 1, sel + d));
    var items = results.querySelectorAll(".sr-item");
    items.forEach(function (el, i) { el.classList.toggle("sel", i === sel); });
    if (items[sel]) items[sel].scrollIntoView({ block: "nearest" });
  }

  $("#btn-search").addEventListener("click", openSearch);
  $("#search-input").addEventListener("focus", openSearch);
  big.addEventListener("input", function () { search(big.value); });
  overlay.addEventListener("click", function (e) { if (e.target === overlay) closeSearch(); });
  results.addEventListener("click", function (e) { if (e.target.closest(".sr-item")) closeSearch(); });

  /* ---------- 键盘 ---------- */
  addEventListener("keydown", function (e) {
    var inInput = /INPUT|TEXTAREA/.test(document.activeElement.tagName);
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
